"""
Extract FIASSE RFC section markdown from a single source file into a subdirectory.
Also, given the --combine switch, combines extracted sections into a single document from a directory of source files.

Splits on ## x[.x[.x[.x]]]. section headers (e.g. 1., 1.1., 2.3.1.) and writes each section
to S<section_id>.md in the destination directory using three numeric places (e.g., S1.0.0.md).
Use for turning multi-section
FIASSE source docs into one file per section under data/FIASSE/.
"""

import argparse
import re
from pathlib import Path
from typing import Dict, Tuple


MAX_SECTION_PARTS = 3
INITIAL_CONTENT_SECTION_ID = "0.0.0"


def log_status(level: str, message: str, **context):
    """Print structured status output with optional key=value context."""
    if context:
        context_str = " ".join(f"{key}={value}" for key, value in sorted(context.items()))
        print(f"[{level}] {message} | {context_str}")
        return
    print(f"[{level}] {message}")


def extract_section_id(header: str) -> str:
    """Extract full section ID from a heading line (e.g., '#### 6.4.1.2. X' -> '6.4.1.2')."""
    match = re.match(r'^#{2,6}\s+(\d+(?:\.\d+)*)\.', header)
    return match.group(1) if match else None


def normalize_section_id(section_id: str) -> str:
    """Normalize a section ID to the configured output depth."""
    return '.'.join(section_id.split('.')[:MAX_SECTION_PARTS])


def format_section_id_for_filename(section_id: str) -> str:
    """Format section IDs as exactly three numeric places for filenames."""
    parts = section_id.split('.')[:MAX_SECTION_PARTS]
    while len(parts) < MAX_SECTION_PARTS:
        parts.append('0')
    return '.'.join(parts)


def split_into_sections(content: str) -> Dict[str, str]:
    """
    Split markdown content into numbered headings up to three parts (e.g., 3.2.3).
    
    Returns a dictionary mapping section IDs to their content (including the header).
    """
    sections = {}
    lines = content.split('\n')
    current_section_id = None
    current_section_lines = []
    initial_content_lines = []
    non_matching_headers = 0
    grouped_deeper_headings = 0
    
    for line in lines:
        # Check if this line is a markdown heading where section ID may be present.
        if line.startswith('#'):
            section_id = extract_section_id(line)
            
            if section_id:
                normalized_section_id = normalize_section_id(section_id)
                if normalized_section_id != section_id:
                    grouped_deeper_headings += 1

                # Save previous section only when the normalized target section changes.
                if current_section_id and current_section_lines and normalized_section_id != current_section_id:
                    sections[current_section_id] = '\n'.join(current_section_lines).strip()

                # Start a new section bucket or continue appending within the same bucket.
                if normalized_section_id != current_section_id:
                    current_section_id = normalized_section_id
                    current_section_lines = [line]
                else:
                    current_section_lines.append(line)
            else:
                # Not a section header, add to current section
                if current_section_id:
                    non_matching_headers += 1
                    current_section_lines.append(line)
                else:
                    initial_content_lines.append(line)
        else:
            # Regular line, add to current section
            if current_section_id:
                current_section_lines.append(line)
            else:
                initial_content_lines.append(line)
    
    # Save the last section
    if current_section_id and current_section_lines:
        sections[current_section_id] = '\n'.join(current_section_lines).strip()

    # Preserve any content before the first numbered heading.
    if initial_content_lines:
        initial_content = '\n'.join(initial_content_lines).strip()
        if initial_content:
            sections[INITIAL_CONTENT_SECTION_ID] = initial_content
            log_status(
                "INFO",
                "Preserved initial content before first numbered section",
                section_id=INITIAL_CONTENT_SECTION_ID,
                chars=len(initial_content),
            )

    if non_matching_headers:
        log_status(
            "WARN",
            "Found markdown headings that did not match expected numbered section format",
            count=non_matching_headers,
        )
    if grouped_deeper_headings:
        log_status(
            "INFO",
            "Grouped deeper numbered headings into parent section files",
            count=grouped_deeper_headings,
            max_parts=MAX_SECTION_PARTS,
        )
    
    return sections


def extract_sections(input_file: Path, output_dir: Path):
    """Extract sections from a single FIASSE RFC markdown file into separate files."""
    log_status("INFO", "Starting section extraction", input=str(input_file), output=str(output_dir))
    
    if not input_file.exists():
        log_status("ERROR", "Input file does not exist", input=str(input_file))
        return
    if not input_file.is_file():
        log_status("ERROR", "Input path is not a file", input=str(input_file))
        return
    
    # Read the source file
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
    except OSError as exc:
        log_status("ERROR", "Failed to read input file", input=str(input_file), reason=str(exc))
        return

    log_status("INFO", "Source file loaded", bytes=len(content.encode('utf-8')), lines=content.count('\n') + 1)
    
    # Split into sections
    sections = split_into_sections(content)
    
    if not sections:
        log_status("WARN", "No extractable sections were found", input=str(input_file))
        return
    
    # Create output directory if it doesn't exist
    output_dir.mkdir(parents=True, exist_ok=True)
    log_status("INFO", "Output directory ready", output=str(output_dir))
    
    # Write each section to a separate file
    log_status("INFO", "Writing section files", section_count=len(sections))
    total_chars_written = 0
    for section_id, section_content in sorted(sections.items(), key=lambda item: section_id_sort_key(item[0])):
        output_section_id = format_section_id_for_filename(section_id)
        output_file = output_dir / f"S{output_section_id}.md"
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(section_content + '\n')
            total_chars_written += len(section_content) + 1
            log_status("INFO", "Wrote section file", file=output_file.name, chars=len(section_content))
        except OSError as exc:
            log_status("ERROR", "Failed to write section file", file=str(output_file), reason=str(exc))
            return
    
    log_status(
        "INFO",
        "Extraction complete",
        section_count=len(sections),
        total_chars=total_chars_written,
        output=str(output_dir),
    )


def natural_sort_key(filename: str) -> Tuple:
    """Generate a sort key for section filenames (e.g., S1.md, S1.1.md, S1.2.3.md)."""
    section_id = parse_section_id_from_filename(filename)
    if section_id:
        return section_id_sort_key(section_id)
    return (999, 999, 999, 999)  # Put non-matching files at the end


def section_id_sort_key(section_id: str) -> Tuple:
    """Generate natural sort order for section IDs (e.g., 1, 2, 10, 10.1)."""
    parts = [int(part) for part in section_id.split('.')]
    while len(parts) < MAX_SECTION_PARTS:
        parts.append(0)
    return tuple(parts)


def parse_section_id_from_filename(filename: str) -> str:
    """Extract section ID from filenames like S1.md, S1.2.md, S1.2.3.md, S1.0.0.md."""
    match = re.match(rf'^S(\d+(?:\.\d+){{0,{MAX_SECTION_PARTS - 1}}})\.md$', filename)
    return match.group(1) if match else None


def combine_sections(input_dir: Path, output_file: Path):
    """Combine section files from a directory into a single document."""
    log_status("INFO", "Starting section combine", input=str(input_dir), output=str(output_file))
    
    if not input_dir.exists() or not input_dir.is_dir():
        log_status("ERROR", "Input directory does not exist or is not a directory", input=str(input_dir))
        return
    
    # Get all .md files in the directory
    markdown_files = list(input_dir.glob('*.md'))
    section_files = sorted(
        [f for f in markdown_files if parse_section_id_from_filename(f.name)],
        key=lambda f: natural_sort_key(f.name)
    )
    ignored_files = sorted(f.name for f in markdown_files if f not in section_files)
    if ignored_files:
        log_status(
            "WARN",
            "Ignoring markdown files that do not match section filename pattern",
            count=len(ignored_files),
            files=",".join(ignored_files),
        )
    
    if not section_files:
        log_status("WARN", "No section files found to combine", input=str(input_dir))
        return
    
    # Combine all sections
    combined_content = []
    log_status("INFO", "Section files discovered", count=len(section_files))
    
    total_chars_read = 0
    for section_file in section_files:
        try:
            with open(section_file, 'r', encoding='utf-8') as f:
                content = f.read().strip()
                combined_content.append(content)
                total_chars_read += len(content)
                log_status("INFO", "Read section file", file=section_file.name, chars=len(content))
        except OSError as exc:
            log_status("ERROR", "Failed to read section file", file=str(section_file), reason=str(exc))
            return
    
    # Write combined output
    output_file.parent.mkdir(parents=True, exist_ok=True)
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write('\n\n'.join(combined_content) + '\n')
    except OSError as exc:
        log_status("ERROR", "Failed to write combined output", output=str(output_file), reason=str(exc))
        return
    
    log_status(
        "INFO",
        "Combine complete",
        section_count=len(section_files),
        total_chars=total_chars_read,
        output=str(output_file),
    )


def main():
    parser = argparse.ArgumentParser(
        description="Extract or combine FIASSE RFC section markdown files.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Extract sections from FIASSE-RFC.md into data/FIASSE/ directory
  python extract_fiasse_sections.py FIASSE-RFC.md data/FIASSE/
  
  # Combine sections from data/FIASSE/ into combined.md
  python extract_fiasse_sections.py --combine data/FIASSE/ combined.md
        """
    )
    
    parser.add_argument(
        'input',
        type=Path,
        help='Input file (for extract mode) or directory (for combine mode)'
    )
    
    parser.add_argument(
        'output',
        type=Path,
        help='Output directory (for extract mode) or file (for combine mode)'
    )
    
    parser.add_argument(
        '--combine',
        action='store_true',
        help='Combine mode: combine section files from input directory into output file'
    )
    
    args = parser.parse_args()
    
    try:
        if args.combine:
            combine_sections(args.input, args.output)
        else:
            extract_sections(args.input, args.output)
    except Exception as exc:  # Last-resort guardrail for actionable troubleshooting output.
        log_status("ERROR", "Unhandled exception", error_type=type(exc).__name__, reason=str(exc))
        raise


if __name__ == '__main__':
    main()
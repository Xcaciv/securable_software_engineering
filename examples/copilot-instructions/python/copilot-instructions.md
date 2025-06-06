# GitHub Copilot Instructions for Python Secure Application with FIASSE Framework


## Project Overview

This is a Python web application following the FAISE (Framework for Integrating Application Security into Software Engineering) principles and the Securable Software Engineering Model (SSEM). This document provides comprehensive guidance for working with GitHub Copilot to build secure, maintainable Python applications with heavy emphasis on security as defined by the FAISE framework.

## Python Secure Development Best Practices (FAISE-Aligned)

### 1. Configuration and Environment Management

- Use environment variables for sensitive configuration (database URLs, API keys, secrets)
- Implement secure configuration management with `python-decouple` or similar libraries
- Use separate configuration files for different environments (development, staging, production)
- Never commit secrets to version control; use `.env` files with `.gitignore`
- Validate configuration values at application startup

```python
# Example secure configuration pattern
import os
from decouple import config, Csv

DATABASE_URL = config('DATABASE_URL')
SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())
```

### 2. Dependency Management and Security

- Use `requirements.txt` with pinned versions and `pip-tools` for dependency management
- Regularly audit dependencies with `safety` and `pip-audit` tools
- Implement dependency scanning in CI/CD pipelines
- Use virtual environments for isolation
- Follow SSEM principles: analyze dependency trustworthiness, maintainability, and reliability

```python
# Example requirements.txt with pinned versions
Django==4.2.7
djangorestframework==3.14.0
python-decouple==3.8
cryptography==41.0.7
```

### 3. Input Validation and Sanitization (SSEM Trustworthiness)

- Validate all input at trust boundaries using proper validation libraries
- Use allowlist validation over blocklist when possible
- Implement type hints and runtime validation with `pydantic` or similar
- Sanitize user input to prevent injection attacks
- Use parameterized queries for database operations

```python
# Example secure input validation
from pydantic import BaseModel, EmailStr, validator
from typing import Optional
import re

class UserRegistration(BaseModel):
    username: str
    email: EmailStr
    password: str
    
    @validator('username')
    def validate_username(cls, v):
        if not re.match(r'^[a-zA-Z0-9_]{3,20}$', v):
            raise ValueError('Username must be 3-20 alphanumeric characters')
        return v
    
    @validator('password')
    def validate_password(cls, v):
        if len(v) < 8:
            raise ValueError('Password must be at least 8 characters')
        return v
```

### 4. Authentication and Authorization (SSEM Authenticity)

- Use established libraries like `django-allauth`, `flask-login`, or `fastapi-users`
- Implement proper password hashing with `bcrypt`, `scrypt`, or `argon2`
- Use secure session management with proper configuration
- Implement multi-factor authentication where appropriate
- Follow principle of least privilege for authorization

```python
# Example secure password hashing
from passlib.context import CryptContext
from passlib.hash import argon2

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)
```

### 5. Database Security (SSEM Integrity)

- Always use parameterized queries or ORM methods to prevent SQL injection
- Implement proper database connection security (SSL/TLS)
- Use database-specific security features (row-level security, encryption)
- Implement proper error handling to prevent information disclosure
- Use database migrations for schema changes

```python
# Example secure database operations with SQLAlchemy
from sqlalchemy.orm import Session
from sqlalchemy import text

# SECURE - Using ORM methods
def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

# SECURE - Using parameterized queries when raw SQL is needed
def get_user_notes(db: Session, user_id: int):
    result = db.execute(
        text("SELECT * FROM notes WHERE user_id = :user_id"),
        {"user_id": user_id}
    )
    return result.fetchall()
```

### 6. Output Encoding and XSS Prevention (SSEM Reliability)

- Use template engines with automatic escaping (Jinja2, Django templates)
- Properly encode output based on context (HTML, JavaScript, CSS, URL)
- Implement Content Security Policy (CSP) headers
- Validate and sanitize rich text content with libraries like `bleach`

```python
# Example secure output handling with bleach
import bleach
from markupsafe import Markup

ALLOWED_TAGS = ['p', 'br', 'strong', 'em', 'ul', 'ol', 'li']
ALLOWED_ATTRIBUTES = {}

def sanitize_html_content(content: str) -> str:
    return bleach.clean(content, tags=ALLOWED_TAGS, attributes=ALLOWED_ATTRIBUTES)

def safe_render_user_content(content: str) -> Markup:
    cleaned = sanitize_html_content(content)
    return Markup(cleaned)
```

### 7. Error Handling and Information Disclosure Prevention

- Implement comprehensive error handling that doesn't leak sensitive information
- Use proper logging with appropriate log levels
- Sanitize error messages shown to users
- Implement proper exception handling for security-critical operations

```python
# Example secure error handling
import logging
from typing import Dict, Any

logger = logging.getLogger(__name__)

def secure_error_response(error: Exception, user_message: str = "An error occurred") -> Dict[str, Any]:
    # Log detailed error for developers
    logger.error(f"Error occurred: {str(error)}", exc_info=True)
    
    # Return sanitized response to user
    return {
        "error": True,
        "message": user_message,
        # Never include stack traces or sensitive details in production
    }
```

### 8. Cryptography and Data Protection (SSEM Confidentiality)

- Use established cryptographic libraries like `cryptography` or `PyNaCl`
- Implement proper key management and rotation
- Use strong encryption algorithms (AES-256, RSA-2048+)
- Never implement custom cryptographic algorithms
- Protect sensitive data at rest and in transit

```python
# Example secure data encryption
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import os
import base64

def generate_key_from_password(password: bytes, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))
    return key

def encrypt_sensitive_data(data: str, key: bytes) -> bytes:
    f = Fernet(key)
    return f.encrypt(data.encode())

def decrypt_sensitive_data(encrypted_data: bytes, key: bytes) -> str:
    f = Fernet(key)
    return f.decrypt(encrypted_data).decode()
```

### 9. Session and Cookie Security

- Use secure session management with proper configuration
- Implement session timeout and invalidation
- Use secure cookie attributes (HttpOnly, Secure, SameSite)
- Implement CSRF protection for state-changing operations

```python
# Example Django secure session configuration
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SAMESITE = 'Strict'
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = True
```

### 10. File Upload Security

- Validate file types using allowlists
- Scan uploaded files for malware
- Store uploaded files outside web root
- Implement file size limits
- Use proper file name sanitization

```python
# Example secure file upload handling
import os
import magic
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
MAX_FILE_SIZE = 16 * 1024 * 1024  # 16MB

def allowed_file(filename: str) -> bool:
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def validate_file_content(file_path: str, expected_type: str) -> bool:
    mime = magic.Magic(mime=True)
    file_mime = mime.from_file(file_path)
    return file_mime.startswith(expected_type)

def secure_file_upload(file, upload_folder: str) -> str:
    if not allowed_file(file.filename):
        raise ValueError("File type not allowed")
    
    filename = secure_filename(file.filename)
    file_path = os.path.join(upload_folder, filename)
    file.save(file_path)
    
    # Validate file content matches extension
    if not validate_file_content(file_path, "image/"):
        os.remove(file_path)
        raise ValueError("File content doesn't match extension")
    
    return file_path
```

## FAISE Framework Integration

### Core SSEM Attributes for Python Development

When implementing features, always consider these SSEM attributes:

#### Maintainability
- **Analyzability**: Write clear, well-documented code with proper naming conventions
- **Modifiability**: Design modular code with low coupling and high cohesion
- **Testability**: Write code that is easily testable with clear interfaces

#### Trustworthiness
- **Confidentiality**: Protect sensitive data through proper encryption and access controls
- **Authenticity**: Implement robust authentication and authorization mechanisms
- **Accountability**: Ensure all actions can be traced and audited
- **Non-repudiation**: Implement logging and digital signatures where appropriate

#### Reliability
- **Availability**: Design systems that remain operational under various conditions
- **Integrity**: Ensure data accuracy and prevent unauthorized modifications
- **Fault Tolerance**: Handle errors gracefully and continue operation when possible
- **Resilience**: Build systems that can recover from failures and attacks

### Trust Boundaries in Python Applications

Identify and secure trust boundaries in your Python applications:

```python
# Example trust boundary validation
from typing import Any, Dict
import bleach

def validate_and_sanitize_input(user_input: str, input_type: str) -> str:
    """
    Validate and sanitize input at trust boundaries
    """
    # Input validation
    if input_type == "username":
        if not re.match(r'^[a-zA-Z0-9_]{3,20}$', user_input):
            raise ValueError("Invalid username format")
    elif input_type == "html_content":
        # Sanitize HTML content
        user_input = bleach.clean(user_input, tags=['p', 'br', 'strong', 'em'])
    
    return user_input

def secure_database_query(db_session, query_params: Dict[str, Any]):
    """
    Always use parameterized queries at database trust boundaries
    """
    # SECURE - Parameterized query
    result = db_session.execute(
        text("SELECT * FROM users WHERE id = :user_id AND active = :active"),
        {"user_id": query_params["user_id"], "active": True}
    )
    return result.fetchall()
```

### Python Framework Specific Guidelines

#### Django Security Best Practices
- Use Django's built-in security features (CSRF protection, XSS protection)
- Implement proper middleware configuration
- Use Django's ORM to prevent SQL injection
- Configure secure settings for production

```python
# Example Django security settings
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
X_FRAME_OPTIONS = 'DENY'
```

#### Flask Security Best Practices
- Use Flask-Security or similar extensions for authentication
- Implement proper CSRF protection with Flask-WTF
- Use Flask-Login for session management
- Configure secure cookie settings

```python
# Example Flask security configuration
from flask import Flask
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['SESSION_COOKIE_SECURE'] = True
app.config['SESSION_COOKIE_HTTPONLY'] = True
csrf = CSRFProtect(app)
```

#### FastAPI Security Best Practices
- Use FastAPI's built-in security utilities
- Implement OAuth2 with JWT tokens properly
- Use dependency injection for security validation
- Implement proper rate limiting

```python
# Example FastAPI security
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import jwt

security = HTTPBearer()

def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    try:
        payload = jwt.decode(credentials.credentials, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.PyJWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials"
        )
```

## Project-Specific Security Remediations

Based on the PRD document, when using Copilot to assist with this project, focus on fixing these security vulnerabilities:

1. Replace plaintext password storage with proper hashing (SEC-001)
2. Parameterize all database queries to prevent SQL injection (SEC-002)
3. Implement proper content sanitization to prevent XSS (SEC-003)
4. Add CSRF protection to all state-changing operations (SEC-004)
5. Implement proper authorization checks for resource access (SEC-005)
6. Validate and sanitize file paths to prevent path traversal (SEC-006)
7. Remove or properly secure command execution functionality (SEC-007)
8. Implement secure file upload validation and handling (SEC-008)
9. Improve session security mechanisms (SEC-009)
10. Implement proper error handling to prevent information disclosure (SEC-010)

## GitHub Copilot Usage Tips

1. **Comment-Driven Development**: When working with Copilot, write clear comments describing what you want to achieve before letting Copilot generate code.

```python
# Implement a secure password hashing method using Argon2
```

2. **Contextual Prompting**: Provide context in your comments to get better suggestions.

```python
# Create a validator for Note entities to prevent XSS attacks in content
```

3. **Iterate and Refine**: Don't accept the first suggestion - review, revise, and ask Copilot to improve.

```python
# Refactor this method to use async/await pattern with proper error handling
```

4. **Implementing Patterns**: Ask Copilot to implement specific patterns.

```python
# Implement repository pattern for NoteService with proper SQLAlchemy usage
```

5. **Fix Security Issues**: Specifically target security improvements.

```python
# Refactor this method to prevent SQL injection by using parameterized queries
```

## Testing Considerations

- Write unit tests for all service methods
- Implement integration tests for controllers
- Add security-focused tests to validate vulnerability fixes
- Use mock objects for external dependencies
- Follow AAA pattern (Arrange-Act-Assert) in test methods

## Modernization Recommendations

When working with legacy code, ask Copilot to help modernize patterns:

1. Replace older session management with modern authentication libraries
2. Upgrade from direct database connections to ORM patterns (SQLAlchemy, Django ORM)
3. Refactor synchronous code to use async/await patterns
4. Implement proper model validation with Pydantic or similar
5. Add API endpoints with OpenAPI documentation where appropriate

## Conclusion

This document serves as a guide for using GitHub Copilot effectively with Python web application projects. Following these Python best practices and security remediation guidelines will help ensure the application is developed according to modern standards and security requirements as defined by the FAISE framework.
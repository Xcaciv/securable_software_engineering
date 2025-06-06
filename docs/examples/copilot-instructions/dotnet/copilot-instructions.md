# GitHub Copilot Instructions - Secure .NET Development with FIASSE Framework

## Project Overview

This document provides comprehensive guidance for developing secure .NET applications using GitHub Copilot, integrating the **Framework for Integrating Application Security into Software Engineering (FIASSE)** and the **Securable Software Engineering Model (SSEM)**. The focus is on building inherently securable code that aligns with both software engineering excellence and cybersecurity objectives.

### FIASSE Core Principles

1. **Resiliently Add Computing Value**: Create software that withstands change, stress, and attack
2. **Reduce Material Impact**: Align security with business risk appetite
3. **Developer-Centric Security**: Empower developers without requiring penetration testing expertise
4. **Engineering-First Approach**: Use established software engineering terms for security concepts

## Securable Software Engineering Model (SSEM) Attributes

When prompting Copilot, emphasize these three core categories and their sub-attributes:

### Maintainability
- **Analyzability**: Code must be understandable to find and fix vulnerabilities
- **Modifiability**: Changes should not introduce new vulnerabilities or break existing security
- **Testability**: Security controls must be effectively testable

### Trustworthiness  
- **Confidentiality**: Protect sensitive data from unauthorized access
- **Non-repudiation**: Ensure actions can be proven and attributed
- **Accountability**: Enable unique tracing of system entity actions
- **Authenticity**: Verify entities are what they claim to be

### Reliability
- **Availability**: System accessible when needed by authorized entities
- **Integrity**: Data and system operations remain accurate and unimpaired
- **Fault Tolerance**: Continue operation despite component failures
- **Resilience**: Recover from failures and restore full operations

## ASP.NET Core Security-First Best Practices

### 1. Secure Configuration and Startup

- Use the `WebApplicationBuilder` pattern with security-first configuration
- Implement strongly-typed configuration with the options pattern and validate security settings
- **NEVER** store secrets in configuration files - use User Secrets, Azure Key Vault, or environment variables
- Implement defense-in-depth configuration validation

```csharp
// Security-focused builder configuration with validation
var builder = WebApplication.CreateBuilder(args);

// Validate critical security configuration at startup
builder.Services.AddOptions<SecuritySettings>()
    .Bind(builder.Configuration.GetSection("Security"))
    .ValidateDataAnnotations()
    .ValidateOnStart();

// Enable security headers by default
builder.Services.Configure<SecurityHeadersOptions>(options =>
{
    options.ContentSecurityPolicy = "default-src 'self'; script-src 'self'";
    options.XFrameOptions = "DENY";
    options.XContentTypeOptions = "nosniff";
});
```

### 2. Secure Dependency Injection

- Register services with **principle of least privilege** and appropriate lifetimes
- Use constructor injection exclusively for security-critical dependencies
- Implement secure service registration patterns that support SSEM attributes
- Always validate dependencies align with FIASSE principles

```csharp
// Secure service registration with explicit security considerations
builder.Services.AddScoped<IUserService, UserService>(provider =>
{
    var logger = provider.GetRequiredService<ILogger<UserService>>();
    var options = provider.GetRequiredService<IOptions<SecuritySettings>>();
    
    // Validate security configuration before creating service
    ValidateSecurityConfiguration(options.Value);
    return new UserService(logger, options);
});

// Security-focused repository pattern
builder.Services.AddScoped<ISecureRepository<Note>, SecureNoteRepository>();
```

### 3. Secure Entity Framework Core Implementation

- **ALWAYS** use parameterized queries - never string concatenation
- Implement repository pattern with built-in authorization checks
- Use async/await patterns with proper cancellation token handling
- Apply defense-in-depth data access patterns

```csharp
// Secure EF Core implementation with built-in authorization
public class SecureNoteRepository : ISecureRepository<Note>
{
    private readonly ApplicationDbContext _context;
    private readonly ICurrentUser _currentUser;
    private readonly ILogger<SecureNoteRepository> _logger;

    public async Task<Note?> GetByIdAsync(int id, CancellationToken cancellationToken = default)
    {
        // TRUSTWORTHINESS: Verify user authorization before data access
        var userId = _currentUser.GetUserId();
        
        var note = await _context.Notes
            .Where(n => n.Id == id && n.UserId == userId) // Authorization filter
            .FirstOrDefaultAsync(cancellationToken);
            
        // ACCOUNTABILITY: Log access attempts
        _logger.LogInformation("User {UserId} accessed note {NoteId}", userId, id);
        
        return note;
    }
}
```

### 4. Comprehensive Security Implementation

#### Authentication and Authorization (OWASP A01 - Broken Access Control)

- **MANDATORY**: Use ASP.NET Core Identity with secure configuration
- Implement proper password policies using PBKDF2 or Argon2
- Apply authorization at multiple layers (controller, action, resource level)
- Use security attributes consistently across all endpoints

```csharp
// Secure Identity configuration
builder.Services.Configure<IdentityOptions>(options =>
{
    // TRUSTWORTHINESS: Strong password requirements
    options.Password.RequireDigit = true;
    options.Password.RequiredLength = 12; // Stronger than OWASP minimum
    options.Password.RequireNonAlphanumeric = true;
    options.Password.RequireUppercase = true;
    options.Password.RequireLowercase = true;
    options.Password.RequiredUniqueChars = 8;

    // RELIABILITY: Account lockout protection
    options.Lockout.DefaultLockoutTimeSpan = TimeSpan.FromMinutes(30);
    options.Lockout.MaxFailedAccessAttempts = 3;
    
    // AUTHENTICITY: Email confirmation required
    options.SignIn.RequireConfirmedEmail = true;
    options.User.RequireUniqueEmail = true;
});

// ACCOUNTABILITY: Secure cookie configuration
builder.Services.ConfigureApplicationCookie(options =>
{
    options.Cookie.HttpOnly = true;
    options.Cookie.Secure = true; // HTTPS only
    options.Cookie.SameSite = SameSiteMode.Strict;
    options.ExpireTimeSpan = TimeSpan.FromMinutes(30);
    options.SlidingExpiration = false; // Fixed expiration for security
});
```

#### Cryptography (OWASP A02 - Cryptographic Failures)

- **NEVER** implement custom cryptographic functions
- Use modern .NET cryptography APIs (AES-GCM, PBKDF2, etc.)
- Implement proper key management and rotation
- Use HTTPS/TLS 1.2+ exclusively

```csharp
// Secure encryption implementation using AES-GCM
public class SecureDataProtector
{
    public byte[] Encrypt(string plaintext, byte[] key)
    {
        using var aes = new AesGcm(key);
        
        // INTEGRITY: Generate new nonce for each operation
        var nonce = new byte[AesGcm.NonceByteSizes.MaxSize];
        RandomNumberGenerator.Fill(nonce);
        
        var plaintextBytes = Encoding.UTF8.GetBytes(plaintext);
        var ciphertext = new byte[plaintextBytes.Length];
        var tag = new byte[AesGcm.TagByteSizes.MaxSize];
        
        aes.Encrypt(nonce, plaintextBytes, ciphertext, tag);
        
        // Return combined: nonce + ciphertext + tag
        return CombineArrays(nonce, ciphertext, tag);
    }
}
```

#### Input Validation and XSS Prevention (OWASP A03 - Injection)

- **ALWAYS** validate input at trust boundaries using allowlists
- Use parameterized queries exclusively for database operations
- Implement comprehensive output encoding
- Apply defense-in-depth validation strategies

```csharp
// Comprehensive input validation with FIASSE principles
public class SecureInputValidator
{
    public bool ValidateNoteContent(string content, out string sanitizedContent)
    {
        // ANALYZABILITY: Clear validation logic
        if (string.IsNullOrWhiteSpace(content))
        {
            sanitizedContent = string.Empty;
            return false;
        }
        
        // FAULT TOLERANCE: Length limits prevent DoS
        if (content.Length > 10000)
        {
            sanitizedContent = string.Empty;
            return false;
        }
        
        // INTEGRITY: HTML sanitization
        sanitizedContent = HtmlEncoder.Default.Encode(content);
        
        // TESTABILITY: Explicit return values
        return !string.IsNullOrEmpty(sanitizedContent);
    }
}

// Secure database query with parameterization
public async Task<Note> CreateNoteAsync(CreateNoteRequest request)
{
    // TRUSTWORTHINESS: Validate and sanitize input
    if (!_validator.ValidateNoteContent(request.Content, out string sanitizedContent))
    {
        throw new ValidationException("Invalid note content");
    }
    
    var note = new Note
    {
        Content = sanitizedContent,
        UserId = _currentUser.GetUserId(),
        CreatedAt = DateTime.UtcNow
    };
    
    // RELIABILITY: Parameterized query prevents SQL injection
    _context.Notes.Add(note);
    await _context.SaveChangesAsync();
    
    return note;
}
```

#### CSRF Protection (OWASP A05 - Security Misconfiguration)

- **MANDATORY**: Implement anti-forgery tokens on all state-changing operations
- Use automatic validation for enhanced security
- Properly handle token lifecycle and cleanup

```csharp
// Global CSRF protection
builder.Services.AddAntiforgery(options =>
{
    options.Cookie.Name = "__RequestVerificationToken";
    options.Cookie.HttpOnly = true;
    options.Cookie.SecurePolicy = CookieSecurePolicy.Always;
    options.Cookie.SameSite = SameSiteMode.Strict;
});

// Automatic validation for all non-GET requests
builder.Services.AddMvc(options =>
{
    options.Filters.Add(new AutoValidateAntiforgeryTokenAttribute());
});

// Secure controller implementation
[Authorize]
[AutoValidateAntiforgeryToken]
public class SecureNotesController : Controller
{
    [HttpPost]
    public async Task<IActionResult> Create([FromForm] CreateNoteViewModel model)
    {
        // CSRF token automatically validated
        // Additional authorization checks
        if (!await _authorizationService.AuthorizeAsync(User, "CreateNote"))
        {
            return Forbid();
        }
        
        // Proceed with secure implementation
        return View();
    }
}
```

#### Security Headers and HTTPS (Transport Security)

- **ALWAYS** enforce HTTPS in production
- Implement comprehensive security headers
- Use HSTS preload for maximum protection

```csharp
// Comprehensive security headers
app.Use(async (context, next) =>
{
    // CONFIDENTIALITY: Security headers
    context.Response.Headers.Append("X-Content-Type-Options", "nosniff");
    context.Response.Headers.Append("X-Frame-Options", "DENY");
    context.Response.Headers.Append("X-XSS-Protection", "0"); // Modern CSP replaces this
    context.Response.Headers.Append("Referrer-Policy", "strict-origin-when-cross-origin");
    context.Response.Headers.Append("Permissions-Policy", "geolocation=(), microphone=(), camera=()");
    
    // INTEGRITY: CSP for XSS protection
    context.Response.Headers.Append("Content-Security-Policy", 
        "default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline'; img-src 'self' data:;");
    
    await next();
});

// RELIABILITY: HTTPS redirection and HSTS
app.UseHttpsRedirection();
app.UseHsts();
```

### 5. Secure Minimal API Implementation

- Implement proper parameter validation and binding
- Use TypedResults for secure responses
- Apply authorization consistently across endpoints

```csharp
// Security-first minimal API
app.MapPost("/api/notes", async (
    CreateNoteRequest request,
    ISecureNoteService noteService,
    IValidator<CreateNoteRequest> validator,
    ClaimsPrincipal user) =>
{
    // TESTABILITY: Explicit validation
    var validationResult = await validator.ValidateAsync(request);
    if (!validationResult.IsValid)
    {
        return Results.ValidationProblem(validationResult.ToDictionary());
    }
    
    // ACCOUNTABILITY: User context validation
    if (!user.Identity?.IsAuthenticated == true)
    {
        return Results.Unauthorized();
    }
    
    try
    {
        var note = await noteService.CreateAsync(request, user.GetUserId());
        return Results.Created($"/api/notes/{note.Id}", note);
    }
    catch (UnauthorizedAccessException)
    {
        return Results.Forbid();
    }
    catch (ValidationException ex)
    {
        return Results.BadRequest(ex.Message);
    }
})
.RequireAuthorization()
.WithValidation<CreateNoteRequest>();
```

### 6. Security-Focused Performance and Monitoring

- Implement security-aware caching strategies
- Use structured logging for security events
- Monitor for security-relevant performance patterns
- Implement proper error handling that doesn't leak information

```csharp
// Security-aware response caching
[Authorize]
[ResponseCache(Duration = 60, Location = ResponseCacheLocation.Client, VaryByUser = true)]
public IActionResult GetUserNotes()
{
    // CONFIDENTIALITY: User-specific caching prevents data leakage
    var userId = User.GetUserId();
    var notes = _noteService.GetUserNotes(userId);
    return Json(notes);
}

// Comprehensive security logging
public class SecurityEventLogger
{
    private readonly ILogger<SecurityEventLogger> _logger;
    
    public void LogAuthenticationFailure(string username, string ipAddress, string reason)
    {
        // ACCOUNTABILITY: Structured security event logging
        _logger.LogWarning("Authentication failure for user {Username} from IP {IpAddress}. Reason: {Reason}",
            username, ipAddress, reason);
    }
    
    public void LogUnauthorizedAccess(string userId, string resource, string action)
    {
        // NON-REPUDIATION: Access attempt logging
        _logger.LogWarning("Unauthorized access attempt by user {UserId} to resource {Resource} for action {Action}",
            userId, resource, action);
    }
}

// Secure error handling
public class SecurityExceptionMiddleware
{
    public async Task InvokeAsync(HttpContext context, RequestDelegate next)
    {
        try
        {
            await next(context);
        }
        catch (SecurityException ex)
        {
            // AVAILABILITY: Don't leak internal details
            _logger.LogError(ex, "Security exception occurred");
            
            await WriteSecureErrorResponse(context, "Access denied");
        }
        catch (ValidationException ex)
        {
            // INTEGRITY: Safe validation error responses
            await WriteSecureErrorResponse(context, "Invalid input provided");
        }
    }
}
```

## Secure Dependency Management (FIASSE Principle)

When evaluating dependencies with Copilot, apply SSEM attributes:

### Dependency Security Checklist

```csharp
// Example of secure dependency evaluation
public class SecureDependencyManager
{
    public bool EvaluateDependency(PackageReference package)
    {
        // ANALYZABILITY: Can we understand this dependency's purpose and scope?
        if (!HasClearDocumentation(package)) return false;
        
        // MODIFIABILITY: Can we easily update or replace this dependency?
        if (!SupportsVersionUpdates(package)) return false;
        
        // TESTABILITY: Can we effectively test with this dependency?
        if (!SupportsMockingOrTesting(package)) return false;
        
        // TRUSTWORTHINESS: Is the source authentic and verified?
        if (!IsFromTrustedSource(package)) return false;
        
        // RELIABILITY: Does it have good security track record?
        if (HasKnownVulnerabilities(package)) return false;
        
        return true;
    }
}
```

### Regular Security Maintenance

```csharp
// Automated dependency security scanning
public class DependencySecurityScanner
{
    public async Task<SecurityScanResult> ScanProjectAsync(string projectPath)
    {
        // RESILIENCE: Regular vulnerability scanning
        var packages = await GetPackageReferences(projectPath);
        var vulnerabilities = new List<Vulnerability>();
        
        foreach (var package in packages)
        {
            var vulns = await _vulnerabilityDatabase.CheckAsync(package);
            vulnerabilities.AddRange(vulns);
        }
        
        return new SecurityScanResult
        {
            VulnerabilityCount = vulnerabilities.Count,
            HighSeverityCount = vulnerabilities.Count(v => v.Severity == Severity.High),
            Recommendations = GenerateSecurityRecommendations(vulnerabilities)
        };
    }
}
```

## FIASSE-Driven GitHub Copilot Usage

### 1. Security-First Comment-Driven Development

Write comments that explicitly request SSEM attributes and security considerations:

```csharp
// FIASSE: Create a user authentication method that demonstrates TRUSTWORTHINESS 
// through proper password hashing, ACCOUNTABILITY via login attempt logging,
// and RESILIENCE through rate limiting and account lockout protection
```

```csharp
// SSEM: Implement a note retrieval method with ANALYZABILITY (clear logic),
// TESTABILITY (mockable dependencies), and TRUSTWORTHINESS (authorization checks)
```

### 2. SSEM-Aware Contextual Prompting

Provide context that aligns with FIASSE principles:

```csharp
// Context: Building a secure multi-tenant note-taking application
// SSEM Focus: TRUSTWORTHINESS (data isolation) and ACCOUNTABILITY (audit trails)
// Create a service method that ensures users can only access their own notes
// with comprehensive logging of all access attempts
```

### 3. Security Pattern Implementation

Ask Copilot to implement specific security patterns aligned with OWASP Top 10:

```csharp
// OWASP A01 Prevention: Implement a resource-based authorization handler
// that checks user ownership before allowing note modifications
// Include SSEM TESTABILITY through dependency injection patterns
```

```csharp
// OWASP A03 Prevention: Create an input validation service that uses
// allowlist validation for note content, preventing XSS and injection attacks
// Focus on SSEM ANALYZABILITY through clear validation rules
```

### 4. Cryptography and Data Protection

```csharp
// FIASSE: Implement AES-GCM encryption for sensitive note content
// Requirements: CONFIDENTIALITY (strong encryption), INTEGRITY (authentication tags),
// and MODIFIABILITY (key rotation support)
// Use .NET's modern cryptography APIs exclusively
```

### 5. Secure API Development

```csharp
// SSEM-focused API endpoint: Create a note management API that demonstrates
// RELIABILITY (proper error handling), TRUSTWORTHINESS (authentication/authorization),
// and FAULT TOLERANCE (graceful degradation under high load)
// Include comprehensive input validation and rate limiting
```

### 6. Security Testing Integration

```csharp
// Generate comprehensive unit tests for the secure note service
// Focus on SSEM TESTABILITY: test authentication failures, authorization edge cases,
// input validation boundaries, and error handling scenarios
// Include tests for all OWASP Top 10 vulnerability categories
```

## OWASP Top 10 Remediation Strategies

When using Copilot to fix vulnerabilities, reference specific OWASP categories:

### A01: Broken Access Control
```csharp
// Fix: Implement proper authorization checks using ASP.NET Core policies
// SSEM Focus: TRUSTWORTHINESS and ACCOUNTABILITY
```

### A02: Cryptographic Failures  
```csharp
// Fix: Replace weak hashing with PBKDF2 or Argon2
// SSEM Focus: CONFIDENTIALITY and INTEGRITY
```

### A03: Injection
```csharp
// Fix: Use parameterized queries and input validation
// SSEM Focus: RELIABILITY and FAULT TOLERANCE
```

### A04: Insecure Design
```csharp
// Fix: Implement threat modeling and secure design patterns
// SSEM Focus: All attributes through architectural security
```

### A05: Security Misconfiguration
```csharp
// Fix: Secure default configurations and security headers
// SSEM Focus: AVAILABILITY and RESILIENCE
```

### A06: Vulnerable Components
```csharp
// Fix: Implement dependency scanning and update policies
// SSEM Focus: MODIFIABILITY and ANALYZABILITY
```

### A07: Authentication Failures
```csharp
// Fix: Implement proper session management and MFA
// SSEM Focus: AUTHENTICITY and NON-REPUDIATION
```

### A08: Software/Data Integrity Failures
```csharp
// Fix: Implement code signing and secure serialization
// SSEM Focus: INTEGRITY and TRUSTWORTHINESS
```

### A09: Logging and Monitoring Failures
```csharp
// Fix: Comprehensive security event logging
// SSEM Focus: ACCOUNTABILITY and ANALYZABILITY
```

### A10: Server-Side Request Forgery
```csharp
// Fix: Input validation and allowlist-based URL validation
// SSEM Focus: RELIABILITY and FAULT TOLERANCE
```

## Security Testing with FIASSE

### Unit Testing Security Controls

Focus on testing all SSEM attributes through comprehensive test coverage:

```csharp
// Test TRUSTWORTHINESS: Verify authorization controls
[Test]
public async Task GetNote_WithUnauthorizedUser_ShouldThrowUnauthorizedException()
{
    // Arrange: User attempting to access another user's note
    var unauthorizedUserId = "user123";
    var noteOwnerId = "user456";
    
    // Act & Assert: ACCOUNTABILITY - ensure unauthorized access is prevented
    await Assert.ThrowsAsync<UnauthorizedException>(
        () => _noteService.GetNoteAsync(noteId, unauthorizedUserId));
}

// Test RELIABILITY: Verify input validation boundary conditions
[Test]
public void ValidateNoteContent_WithMaliciousScript_ShouldReturnFalse()
{
    // Arrange: FAULT TOLERANCE - test against XSS attempts
    var maliciousInput = "<script>alert('xss')</script>";
    
    // Act: ANALYZABILITY - clear test logic
    var result = _validator.ValidateNoteContent(maliciousInput, out var sanitized);
    
    // Assert: INTEGRITY - ensure malicious content is rejected
    Assert.False(result);
    Assert.DoesNotContain("<script>", sanitized);
}
```

### Integration Testing for Security

```csharp
// Security-focused integration tests
[Test]
public async Task CreateNote_WithCSRFToken_ShouldSucceed()
{
    // TESTABILITY: Verify CSRF protection works correctly
    var client = _factory.CreateClient();
    var token = await GetAntiForgeryTokenAsync(client);
    
    var request = new HttpRequestMessage(HttpMethod.Post, "/notes")
    {
        Content = new FormUrlEncodedContent(new[]
        {
            new KeyValuePair<string, string>("Content", "Test note"),
            new KeyValuePair<string, string>("__RequestVerificationToken", token)
        })
    };
    
    var response = await client.SendAsync(request);
    Assert.Equal(HttpStatusCode.Created, response.StatusCode);
}
```

## AI-Driven Secure Development with FIASSE

### Prompt Engineering for Securable Code

When using Copilot or other AI tools, structure prompts to emphasize FIASSE principles:

```csharp
// FIASSE-compliant prompt example:
// "Generate a user registration endpoint that demonstrates SSEM TRUSTWORTHINESS 
// through secure password handling, RELIABILITY through proper error handling,
// and MAINTAINABILITY through clear, testable code structure. 
// Include OWASP A07 prevention measures."
```

### Security Requirements in AI Prompts

```csharp
// Include security requirements directly in prompts:
// "Create a file upload service with the following FIASSE requirements:
// - ANALYZABILITY: Clear validation logic for file types and sizes
// - TRUSTWORTHINESS: Virus scanning and secure file storage
// - RELIABILITY: Graceful handling of large files and upload failures
// - Prevent OWASP A08 issues through secure file handling"
```

## Threat Modeling Integration

### FIASSE-Based Threat Scenarios

When developing features, apply the "Four Question Framework" with SSEM context:

1. **What are we building?** A note-sharing feature with user collaboration
2. **What can go wrong?** (SSEM analysis)
   - CONFIDENTIALITY: Notes shared with unintended users
   - INTEGRITY: Note content modified by unauthorized users  
   - ACCOUNTABILITY: Actions cannot be traced to specific users
   - AVAILABILITY: System overwhelmed by malicious sharing requests

3. **What are we going to do about it?** (Security Requirements)
   - Implement explicit permission model for note sharing
   - Add digital signatures for note integrity verification
   - Comprehensive audit logging for all sharing actions
   - Rate limiting and input validation for DoS prevention

4. **Did we do a good job?** (Validation through SSEM)
   - TESTABILITY: Can we effectively test all security controls?
   - ANALYZABILITY: Is the security logic clear and maintainable?
   - MODIFIABILITY: Can we easily enhance security without breaking functionality?

### Trust Boundary Identification

```csharp
// Example of explicit trust boundary handling
public class NoteSharingService
{
    // TRUST BOUNDARY: External user input to internal system
    public async Task<ShareResult> ShareNoteAsync(ShareNoteRequest request)
    {
        // RESILIENCE: Validate at trust boundary
        var validation = await _validator.ValidateShareRequestAsync(request);
        if (!validation.IsValid)
        {
            // ACCOUNTABILITY: Log invalid sharing attempts
            _logger.LogWarning("Invalid share request from user {UserId}: {Errors}",
                request.UserId, validation.Errors);
            return ShareResult.Failed(validation.Errors);
        }
        
        // TRUSTWORTHINESS: Verify user authorization
        if (!await _authService.CanShareNoteAsync(request.NoteId, request.UserId))
        {
            _logger.LogWarning("Unauthorized share attempt for note {NoteId} by user {UserId}",
                request.NoteId, request.UserId);
            return ShareResult.Unauthorized();
        }
        
        // Proceed with controlled sharing logic...
    }
}
```

## Security-Driven Modernization with FIASSE

When working with legacy code, apply FIASSE principles for secure modernization:

### 1. Replace Insecure Patterns with SSEM-Compliant Alternatives

```csharp
// BEFORE: Insecure legacy pattern
string sql = "SELECT * FROM Users WHERE Username = '" + username + "'";
var users = context.Database.SqlQuery<User>(sql).ToList();

// AFTER: FIASSE-compliant secure pattern
// ANALYZABILITY: Clear parameterized query structure
// RELIABILITY: SQL injection prevention
// TESTABILITY: Easily mockable repository pattern
public async Task<User?> GetUserByUsernameAsync(string username)
{
    return await _context.Users
        .Where(u => u.Username == username)
        .FirstOrDefaultAsync();
}
```

### 2. Upgrade Authentication to Modern Standards

```csharp
// BEFORE: Insecure session-based authentication
Session["UserId"] = user.Id;

// AFTER: Secure ASP.NET Core Identity with FIASSE principles
// TRUSTWORTHINESS: Proper authentication with secure tokens
// ACCOUNTABILITY: Comprehensive login tracking
// RESILIENCE: Protection against session attacks
public async Task<SignInResult> SignInUserAsync(LoginViewModel model)
{
    var user = await _userManager.FindByEmailAsync(model.Email);
    if (user == null)
    {
        // FAULT TOLERANCE: Consistent timing to prevent user enumeration
        await Task.Delay(Random.Shared.Next(100, 300));
        return SignInResult.Failed;
    }
    
    var result = await _signInManager.PasswordSignInAsync(
        user, model.Password, model.RememberMe, lockoutOnFailure: true);
    
    // ACCOUNTABILITY: Log authentication attempts
    _logger.LogInformation("Sign-in attempt for user {Email}: {Result}",
        model.Email, result.Succeeded ? "Success" : "Failed");
    
    return result;
}
```

### 3. Implement Modern API Security

```csharp
// BEFORE: Unprotected API endpoint
[HttpGet]
public IActionResult GetUserData(int userId)
{
    var user = _context.Users.Find(userId);
    return Json(user);
}

// AFTER: Secure API with comprehensive protection
// TRUSTWORTHINESS: Authentication and authorization required
// RELIABILITY: Proper error handling and validation
// ANALYZABILITY: Clear security logic
[HttpGet("users/{userId}")]
[Authorize]
[ValidateAntiForgeryToken]
public async Task<ActionResult<UserDto>> GetUserData(
    int userId,
    [FromServices] IAuthorizationService authService)
{
    // TRUSTWORTHINESS: Verify user can access this data
    var authResult = await authService.AuthorizeAsync(
        User, userId, "CanAccessUserData");
    
    if (!authResult.Succeeded)
    {
        // ACCOUNTABILITY: Log unauthorized access attempts
        _logger.LogWarning("Unauthorized access attempt to user {UserId} by {CurrentUser}",
            userId, User.Identity?.Name);
        return Forbid();
    }
    
    try
    {
        var user = await _userService.GetUserAsync(userId);
        if (user == null)
        {
            return NotFound();
        }
        
        // CONFIDENTIALITY: Return only safe data via DTO
        return Ok(_mapper.Map<UserDto>(user));
    }
    catch (Exception ex)
    {
        // RESILIENCE: Secure error handling
        _logger.LogError(ex, "Error retrieving user data for {UserId}", userId);
        return StatusCode(500, "An error occurred processing your request");
    }
}
```

### 4. Secure File Handling Modernization

```csharp
// BEFORE: Insecure file upload
[HttpPost]
public async Task<IActionResult> UploadFile(IFormFile file)
{
    var path = Path.Combine("uploads", file.FileName);
    using var stream = new FileStream(path, FileMode.Create);
    await file.CopyToAsync(stream);
    return Ok();
}

// AFTER: Secure file upload with FIASSE principles
[HttpPost("upload")]
[Authorize]
[RequestSizeLimit(10 * 1024 * 1024)] // 10MB limit
public async Task<IActionResult> UploadFile(
    IFormFile file,
    [FromServices] IFileValidationService validator,
    [FromServices] IVirusScanService virusScanner)
{
    // ANALYZABILITY: Clear validation steps
    var validationResult = await validator.ValidateFileAsync(file);
    if (!validationResult.IsValid)
    {
        return BadRequest(validationResult.Errors);
    }
    
    // INTEGRITY: Virus scanning
    var scanResult = await virusScanner.ScanAsync(file);
    if (!scanResult.IsClean)
    {
        _logger.LogWarning("Malicious file upload attempt by user {UserId}: {FileName}",
            User.GetUserId(), file.FileName);
        return BadRequest("File failed security scan");
    }
    
    // CONFIDENTIALITY: Secure file storage with generated names
    var secureFileName = $"{Guid.NewGuid()}{Path.GetExtension(file.FileName)}";
    var securePath = Path.Combine(_secureUploadPath, secureFileName);
    
    using var stream = new FileStream(securePath, FileMode.Create);
    await file.CopyToAsync(stream);
    
    // ACCOUNTABILITY: Log successful uploads
    _logger.LogInformation("File uploaded successfully by user {UserId}: {OriginalName} -> {SecureName}",
        User.GetUserId(), file.FileName, secureFileName);
    
    return Ok(new { Message = "File uploaded successfully", FileId = secureFileName });
}
```

## Cloud-Native Security Considerations

### Secure Configuration for Cloud Deployment

```csharp
// Azure App Service security configuration
public void ConfigureServices(IServiceCollection services)
{
    // CONFIDENTIALITY: Use Azure Key Vault for secrets
    if (!_environment.IsDevelopment())
    {
        var keyVaultUrl = Configuration["KeyVault:VaultUrl"];
        var configBuilder = new ConfigurationBuilder()
            .AddAzureKeyVault(keyVaultUrl, new DefaultAzureCredential());
        Configuration = configBuilder.Build();
    }
    
    // RELIABILITY: Health checks for dependencies
    services.AddHealthChecks()
        .AddDbContext<ApplicationDbContext>()
        .AddAzureKeyVault(options => {
            options.VaultUri = Configuration["KeyVault:VaultUrl"];
        });
    
    // RESILIENCE: Circuit breaker for external services
    services.AddHttpClient<ExternalApiService>()
        .AddPolicyHandler(GetRetryPolicy())
        .AddPolicyHandler(GetCircuitBreakerPolicy());
}

// FAULT TOLERANCE: Resilience policies
private static IAsyncPolicy<HttpResponseMessage> GetRetryPolicy()
{
    return HttpPolicyExtensions
        .HandleTransientHttpError()
        .WaitAndRetryAsync(
            retryCount: 3,
            sleepDurationProvider: retryAttempt => 
                TimeSpan.FromSeconds(Math.Pow(2, retryAttempt)));
}
```

## Conclusion

This document provides comprehensive guidance for using GitHub Copilot to develop secure .NET applications aligned with the FIASSE framework and SSEM principles. By integrating security considerations into every aspect of development—from initial design through deployment—we can build software that is inherently resilient against threats while maintaining engineering excellence.

### Key Takeaways

1. **Security is Engineering**: Use SSEM attributes to make security discussions native to software engineering
2. **Defense in Depth**: Apply multiple layers of security controls across all OWASP Top 10 categories
3. **FIASSE Integration**: Embed security into existing development workflows rather than treating it as separate
4. **AI-Powered Security**: Leverage Copilot with security-focused prompts to generate inherently securable code
5. **Continuous Improvement**: Regularly assess and modernize security controls using FIASSE principles

### Next Steps

- Integrate these guidelines into your team's development workflow
- Train developers on FIASSE principles and SSEM terminology
- Establish security requirements and acceptance criteria for all new features
- Implement automated security testing aligned with OWASP Top 10
- Regular security reviews using SSEM attributes as evaluation criteria

By following these practices, development teams can confidently build secure .NET applications that protect against evolving threats while delivering business value effectively.
# GitHub Copilot Instructions for Securable .NET Development with FIASSE Framework

## Project Context
Integrating the **Framework for Integrating Application Security into Software Engineering (FIASSE)** and the **Securable Software Engineering Model (SSEM)** to build inherently securable .NET applications.
**Core Principle**: Resiliently Add Computing Value – create software that withstands change, stress, and attack.

## Securable Software Engineering Model (SSEM) Attributes
Focus on these core categories and their sub-attributes when generating or refactoring code:

### Maintainability
- **Analyzability**: Code must be understandable to find and fix vulnerabilities.
- **Modifiability**: Changes should not introduce new vulnerabilities or break existing security.
- **Testability**: Security controls must be effectively testable.

### Trustworthiness
- **Confidentiality**: Protect sensitive data from unauthorized access.
- **Accountability**: Enable unique tracing of system entity actions.
- **Authenticity**: Verify entities are what they claim to be.

### Reliability
- **Availability**: System accessible when needed by authorized entities.
- **Integrity**: Data and system operations remain accurate and unimpaired.
- **Fault Tolerance**: Continue operation despite component failures.
- **Resilience**: Recover from failures and restore full operations.

## Securable .NET Development Practices

### 1. Unified Security Configuration & Implementation
This section consolidates guidance for establishing a secure foundation in ASP.NET Core applications, emphasizing SSEM attributes.

#### 1.1. Application Setup and Configuration
- Utilize `WebApplicationBuilder` for configuring applications with securable software engineering principles.
- Implement strongly-typed configuration using the options pattern; validate all security-critical settings at startup.
- **Secret Management**: NEVER store secrets in configuration files. Employ User Secrets, Azure Key Vault, or environment variables.
- Implement defense-in-depth configuration validation.
```csharp
// Securable builder configuration with validation
var builder = WebApplication.CreateBuilder(args);

// Validate critical security configuration at startup
builder.Services.AddOptions<SecuritySettings>()
    .ValidateDataAnnotations() // Example validation using data annotations on SecuritySettings class
    .ValidateOnStart(); // Ensure validation runs at startup

// Enable security headers by default (example)
builder.Services.Configure<SecurityHeadersOptions>(options =>
{
    options.XContentTypeOptions = "nosniff";
    // Add other headers like CSP, Strict-Transport-Security, etc., as per section 1.8
});
```

#### 1.2. Dependency Injection (DI)
- Register services adhering to the **principle of least privilege** and select appropriate lifetimes (Scoped, Singleton, Transient).
- Use constructor injection for dependencies, especially those critical to security.
- Ensure service registration patterns support SSEM attributes (e.g., testability through mockable dependencies).
- Validate that dependencies align with FIASSE principles.
```csharp
// Secure service registration
builder.Services.AddScoped<IUserService, UserService>(); // Assuming UserService handles its dependencies securely

// Example: Registering a repository with security considerations
// ISecureRepository<T> might enforce authorization checks within its implementation
builder.Services.AddScoped<ISecureRepository<Note>, SecureNoteRepository>();
```

#### 1.3. Data Access (Entity Framework Core)
- **Query Security**: ALWAYS use parameterized queries. Avoid string concatenation to prevent SQL injection. EF Core LINQ queries are parameterized by default.
- Implement the repository pattern with authorization checks integrated into data access logic where appropriate.
- Utilize async/await patterns correctly, including cancellation token propagation for long-running queries.
- Apply defense-in-depth data access strategies (e.g., validating data before persistence and after retrieval if necessary).
```csharp
// Secure EF Core usage (conceptual example within a repository)
public class SecureNoteRepository : ISecureRepository<Note>
{
    private readonly ApplicationDbContext _context;
    private readonly IAuthorizationService _authorizationService; // For resource-based authorization

    public SecureNoteRepository(ApplicationDbContext context, IAuthorizationService authorizationService)
    {
        _context = context;
        _authorizationService = authorizationService;
    }

    public async Task<Note?> GetByIdAsync(int id, ClaimsPrincipal user)
    {
        var note = await _context.Notes.FindAsync(id);
        if (note == null) return null;

        // TRUSTWORTHINESS: Authorization check before returning data
        var authorizationResult = await _authorizationService.AuthorizeAsync(user, note, "ReadPolicy"); // Example policy
        if (!authorizationResult.Succeeded)
        {
            // Log authorization failure (ACCOUNTABILITY)
            // throw new UnauthorizedAccessException("User cannot access this note."); // Or return null/handle as per policy
            return null;
        }
        return note;
    }
    // ... other methods using parameterized queries (via LINQ) and authorization
}
```

#### 1.4. Authentication and Authorization (OWASP A01 - Broken Access Control)
- **Authentication**: Implement ASP.NET Core Identity with secure configurations (e.g., strong password policies, Multi-Factor Authentication (MFA)).
- **Password Hashing**: Use PBKDF2 (default in ASP.NET Core Identity) or Argon2 for password storage.
- **Authorization**: Apply authorization at multiple layers (e.g., controller attributes, action attributes, resource-based policies). Use security attributes (`[Authorize]`) and policies consistently.
- **ACCOUNTABILITY**: Configure secure cookie settings (e.g., `HttpOnly`, `Secure`, `SameSite=Strict`, fixed expiration).
```csharp
// Secure Identity configuration
builder.Services.AddIdentity<ApplicationUser, IdentityRole>(options =>
{
    options.Password.RequireDigit = true;
    options.Password.RequiredLength = 12;
    options.Password.RequireNonAlphanumeric = true;
    options.Password.RequireUppercase = true;
    options.Password.RequireLowercase = true;
    options.User.RequireUniqueEmail = true;
    options.SignIn.RequireConfirmedAccount = true; // Recommended
    options.Lockout.DefaultLockoutTimeSpan = TimeSpan.FromMinutes(5);
    options.Lockout.MaxFailedAccessAttempts = 5;
})
.AddEntityFrameworkStores<ApplicationDbContext>()
.AddDefaultTokenProviders();

// ACCOUNTABILITY: Secure cookie configuration
builder.Services.ConfigureApplicationCookie(options =>
{
    options.Cookie.HttpOnly = true;
    options.Cookie.SecurePolicy = CookieSecurePolicy.Always; // Enforce HTTPS for the cookie
    options.Cookie.SameSite = SameSiteMode.Strict;
    options.SlidingExpiration = false; // Fixed expiration for better security posture
    options.ExpireTimeSpan = TimeSpan.FromHours(1); // Example fixed expiration
});

// Example: Resource-based authorization policy in ConfigureServices
// services.AddAuthorization(options =>
// {
//     options.AddPolicy("EditPolicy", policy =>
//         policy.Requirements.Add(new SameAuthorRequirement())); // Custom requirement
// });
```

#### 1.5. Cryptography (OWASP A02 - Cryptographic Failures)
- **Guideline**: NEVER implement custom cryptographic functions.
- Utilize modern .NET cryptography APIs (e.g., `System.Security.Cryptography` for AES-GCM, `IDataProtector` from ASP.NET Core Data Protection).
- Implement robust key management and rotation strategies (ASP.NET Core Data Protection APIs can help manage this).
- **Transport Security**: Enforce HTTPS/TLS 1.2+ for all communications (see [Security Headers and HTTPS](#18-security-headers-and-https)).
```csharp
// Example: Secure data protection using .NET's Data Protection APIs
// (Assumes Data Protection is configured, e.g., with key storage and rotation in Program.cs)
public class UserProfileDataProtector
{
    private readonly IDataProtector _protector;

    // Purpose string should be unique for the type of data being protected
    public UserProfileDataProtector(IDataProtectionProvider provider)
    {
        _protector = provider.CreateProtector("UserProfile.SensitiveData.v1");
    }

    public string Protect(string plaintext) => _protector.Protect(plaintext);
    public string Unprotect(string protectedData) => _protector.Unprotect(protectedData);
}
// builder.Services.AddDataProtection(); // Basic setup in Program.cs
```

#### 1.6. Input Validation and Output Encoding (OWASP A03 - Injection)
- **Input Validation**:
    - Validate ALL input at trust boundaries (e.g., API endpoints, service method entries from external calls).
    - Use strong typing, data annotations, FluentValidation, or custom validation logic. Prefer allowlists over denylists.
    - For database operations, rely on parameterized queries (see [Data Access](#13-data-access-entity-framework-core)).
- **Output Encoding**:
    - Implement comprehensive output encoding appropriate for the context (HTML, JavaScript, URL, CSS).
    - Razor views automatically HTML-encode content. For other contexts, use appropriate encoders (e.g., `HttpUtility.JavaScriptStringEncode`, `UrlEncoder`).
- Apply defense-in-depth: validate input, use parameterized queries, encode output, and use secure APIs.
```csharp
// Input Validation Example (using FluentValidation)
// public class CreateNoteRequestValidator : AbstractValidator<CreateNoteRequest>
// {
//     public CreateNoteRequestValidator()
//     {
//         RuleFor(x => x.Title).NotEmpty().MaximumLength(100);
//         RuleFor(x => x.Content).NotEmpty().Must(BeSafeHtml) // Custom rule for HTML sanitization
//             .WithMessage("Content contains potentially unsafe HTML.");
//     }
//     private bool BeSafeHtml(string content) { /* Implement HTML sanitization */ return true; }
// }
// Register in Program.cs: builder.Services.AddValidatorsFromAssemblyContaining<CreateNoteRequestValidator>();

// Output Encoding: Razor views handle HTML encoding by default.
// In APIs, if returning HTML or script, ensure it's properly sanitized/encoded.
// For JavaScript contexts in Razor:
// <script>
//   var untrustedData = @Json.Serialize(Model.SomeData); // Correctly encodes for JS string literal
// </script>
```

#### 1.7. Cross-Site Request Forgery (CSRF) Protection
- **MANDATORY**: Implement anti-forgery tokens on all state-changing operations (POST, PUT, DELETE) in web applications with cookie-based authentication.
- Utilize ASP.NET Core's built-in anti-CSRF features (e.g., `AutoValidateAntiforgeryTokenAttribute` for MVC/Razor Pages).
- Configure anti-forgery cookies with `SameSite=Strict`, `HttpOnly=true`, `SecurePolicy=Always`.
```csharp
// Global CSRF protection configuration in Program.cs
builder.Services.AddAntiforgery(options =>
{
    options.HeaderName = "X-CSRF-TOKEN"; // For SPAs that might send token in header
    options.Cookie.SameSite = SameSiteMode.Strict;
    options.Cookie.HttpOnly = true;
    options.Cookie.SecurePolicy = CookieSecurePolicy.Always;
});

// Automatic validation for non-GET requests in MVC/Razor Pages
// builder.Services.AddControllersWithViews(options =>
{
//     options.Filters.Add(new AutoValidateAntiforgeryTokenAttribute());
// });
// For Minimal APIs, CSRF protection needs to be handled explicitly if using cookies for auth.
```

#### 1.8. Security Headers and HTTPS
- **HTTPS**: Enforce HTTPS in all environments. Use HTTP Strict Transport Security (HSTS).
- **Security Headers**: Implement headers like Content Security Policy (CSP), X-Content-Type-Options, X-Frame-Options, Referrer-Policy to mitigate various attacks.
```csharp
// In Program.cs (after routing, before endpoints/MVC)
app.UseHttpsRedirection(); // Redirect HTTP to HTTPS
app.UseHsts(); // Adds Strict-Transport-Security header

// Example: Adding other security headers (can be done via middleware or dedicated packages)
app.Use(async (context, next) =>
{
    context.Response.Headers.Append("X-Content-Type-Options", "nosniff");
    context.Response.Headers.Append("X-Frame-Options", "DENY"); // Or SAMEORIGIN
    // A restrictive CSP. Customize heavily based on application needs.
    context.Response.Headers.Append("Content-Security-Policy", "default-src 'self'; script-src 'self'; style-src 'self'; img-src 'self'; font-src 'self'; connect-src 'self'; frame-ancestors 'none'; form-action 'self';");
    context.Response.Headers.Append("Referrer-Policy", "strict-origin-when-cross-origin");
    await next();
});
```

#### 1.9. Secure Minimal API Design
- Implement parameter validation robustly (e.g., using `IValidator<T>` with FluentValidation and endpoint filters, or `BindAsync` with custom validation).
- Use `TypedResults` for clear, type-safe, and secure response types.
- Apply authorization consistently using `.RequireAuthorization()` and policies.
```csharp
// Securable Minimal API endpoint example
// app.MapPost("/api/items", async (
//     CreateItemRequest request,
//     IValidator<CreateItemRequest> validator, // Injected validator
//     ClaimsPrincipal user,
//     IItemService itemService) =>
{
    var validationResult = await validator.ValidateAsync(request);
    if (!validationResult.IsValid)
    {
        return TypedResults.ValidationProblem(validationResult.ToDictionary());
    }
    var item = await itemService.CreateItemAsync(request, user);
    return TypedResults.Created($"/api/items/{item.Id}", item);
})
.RequireAuthorization("CreateItemPolicy") // Example policy
.AddEndpointFilter<ValidationFilter<CreateItemRequest>>(); // Endpoint filter for validation
.WithName("CreateItem") // Good for discoverability and testing
.WithTags("Items"); // OpenAPI grouping
```

#### 1.10. Logging, Monitoring, and Error Handling
- **Logging**: Implement structured logging for security events (e.g., authentication attempts, authorization failures, input validation failures, significant errors).
    - **ACCOUNTABILITY**: Ensure logs provide audit trails without logging sensitive data (PII, secrets, session tokens).
- **Monitoring**: Monitor logs and application performance for security-relevant patterns (e.g., repeated failed logins, spikes in 4xx/5xx errors, unusual traffic).
- **Error Handling**: Implement global error handling that does not leak sensitive information or internal system details to the client. Provide generic error messages.
```csharp
// Structured logging (e.g., Serilog, configured in Program.cs)
// builder.Host.UseSerilog(...);

// Secure error handling middleware (conceptual, register in Program.cs)
// public class SecureExceptionMiddleware
// {
//     private readonly RequestDelegate _next;
//     private readonly ILogger<SecureExceptionMiddleware> _logger;
//     public SecureExceptionMiddleware(RequestDelegate next, ILogger<SecureExceptionMiddleware> logger) { /* ... */ }
//     public async Task InvokeAsync(HttpContext context)
//     {
//         try { await _next(context); }
//         catch (Exception ex)
//         {
//             _logger.LogError(ex, "Unhandled exception. RequestId: {RequestId}", context.TraceIdentifier);
//             context.Response.StatusCode = StatusCodes.Status500InternalServerError;
//             await context.Response.WriteAsJsonAsync(new { error = "An unexpected error occurred." });
//         }
//     }
// }
// app.UseMiddleware<SecureExceptionMiddleware>(); // Register early in pipeline
```

### 2. Secure Dependency Management (FIASSE Principle)
- **Evaluation**: Assess dependencies for security vulnerabilities before integration. Check for known CVEs, maintenance status, and community trust.
- **Regular Maintenance**:
    - Keep dependencies updated to their latest secure versions.
    - Use automated tools for dependency scanning (e.g., `dotnet list package --vulnerable`, GitHub Dependabot, Snyk).
- **Principle of Least Privilege**: Only include dependencies that are necessary.
```csharp
// Example: Using dotnet CLI to check for vulnerable packages
// In terminal: dotnet list package --vulnerable

// Conceptual process for dependency evaluation:
// 1. Identify need for a dependency.
// 2. Research: Check vulnerability databases (NVD, GitHub Advisories), project activity, open issues.
// 3. Assess: Popularity, maintenance frequency, license compatibility.
// 4. Test: Integrate in a sandbox/dev environment; run security scans.
// 5. Monitor: Continuously scan after integration using automated tools.
```

## FIASSE-Driven GitHub Copilot Usage
Guide Copilot by explicitly requesting SSEM attributes and security considerations in comments and prompts.

### 1. SSEM-Focused Comment-Driven Development
```csharp
// FIASSE: Implement user authentication method.
// SSEM Attributes:
// - TRUSTWORTHINESS (Authenticity, Confidentiality): Secure password hashing (PBKDF2/Argon2), consider MFA support.
// - ACCOUNTABILITY: Log login attempts (success/failure with anonymized identifiers), track session creation.
// - RESILIENCE: Implement rate limiting and account lockout for failed login attempts.
```
```csharp
// SSEM: Develop a data retrieval method for 'Order' records.
// SSEM Attributes:
// - ANALYZABILITY: Ensure clear, understandable logic for data access and authorization checks.
// - TESTABILITY: Design with mockable dependencies for testing security controls (e.g., authorization).
// - TRUSTWORTHINESS (Confidentiality, Integrity): Enforce strict authorization checks (e.g., user can only access their own orders).
```

### 2. Contextual Prompting with SSEM and FIASSE
Provide context that aligns with FIASSE principles and desired SSEM attributes.
```csharp
// Context: Building a secure multi-tenant SaaS application.
// FIASSE Principle: Ensure strict isolation of tenant data and operations.
// SSEM Focus:
// - TRUSTWORTHINESS (Confidentiality, Integrity): Guarantee data isolation between tenants.
// - ACCOUNTABILITY: Implement comprehensive audit trails for all tenant-specific administrative actions.
// Task: Create a service method that retrieves tenant-specific configuration settings. Ensure that a user/administrator from one tenant cannot access settings from another. Log all access attempts, including unauthorized ones, with tenant context.
```

### 3. Implementing Security Patterns (OWASP Alignment)
Request Copilot to implement specific security patterns, referencing OWASP Top 10 categories and SSEM attributes.
```csharp
// OWASP A01 (Broken Access Control) Prevention:
// Implement a resource-based authorization handler for 'Invoice' entities in ASP.NET Core.
// The handler should verify that the current user is either the creator of the invoice or has a 'FinanceManager' role.
// SSEM Focus:
// - TESTABILITY: Ensure the handler can be unit-tested with mock user principals and invoice resources.
// - TRUSTWORTHINESS (Authenticity): Correctly enforce access rules based on user identity and roles/claims.
```
```csharp
// OWASP A03 (Injection) Prevention:
// Create an input validation routine for a 'ProductSearch' feature.
// The search term should be validated against a restrictive allowlist of characters and length constraints.
// Sanitize the search term to prevent XSS if it's reflected directly in the UI (though ideally avoid reflection).
// SSEM Focus:
// - ANALYZABILITY: Validation rules should be clear, explicit, and maintainable.
// - RELIABILITY: Effectively block or neutralize potentially malicious inputs.
```

### 4. Cryptography and Data Protection
```csharp
// FIASSE: Implement encryption for 'APISetting.SecretValue' stored at rest using ASP.NET Core Data Protection APIs.
// Requirements:
// - SSEM CONFIDENTIALITY: Use strong, authenticated encryption (AEAD).
// - SSEM INTEGRITY: Ensure data cannot be tampered with undetected.
// - SSEM MODIFIABILITY: Leverage Data Protection API's key management for key rotation.
// Constraints: Use .NET's built-in Data Protection APIs. Do not implement custom cryptographic algorithms.
```

### 5. Secure API Development
```csharp
// SSEM-focused API endpoint design:
// Create a 'UserPreferences' API (GET, PUT operations).
// SSEM Attributes:
// - RELIABILITY: Implement robust error handling using TypedResults; return appropriate HTTP status codes.
// - TRUSTWORTHINESS (Authenticity, Confidentiality): Enforce authentication (e.g., JWT Bearer) and authorization (user can only access/modify their own preferences).
```
# Security Policy

## Supported Versions

We actively support the following versions of the Image Editor:

| Version | Supported          |
| ------- | ------------------ |
| 2.0.x   | :white_check_mark: |
| 1.0.x   | :x:                |

## Reporting a Vulnerability

We take security vulnerabilities seriously. If you discover a security vulnerability in the Image Editor, please follow these steps:

### 1. **Do Not** Create Public Issues

Please **do not** report security vulnerabilities through public GitHub issues, discussions, or pull requests.

### 2. Report Privately

Instead, please report security vulnerabilities by:

- **Email**: Send details to [yyyabed123@gmail.com]
- **GitHub Security**: Use GitHub's private vulnerability reporting feature
- **Direct Message**: Contact the maintainers directly

### 3. Include Details

When reporting a vulnerability, please include:

- **Description** of the vulnerability
- **Steps to reproduce** the issue
- **Potential impact** of the vulnerability
- **Suggested fix** (if you have one)
- **Your contact information** for follow-up

### 4. Response Timeline

We aim to respond to security reports within:

- **24 hours**: Initial acknowledgment
- **72 hours**: Preliminary assessment
- **1 week**: Detailed investigation results
- **2 weeks**: Fix implementation (if applicable)

### 5. Disclosure Policy

- We will work with you to understand and resolve the issue
- We will not take legal action against researchers who report vulnerabilities responsibly
- We will credit you in our security advisories (unless you prefer to remain anonymous)
- We will coordinate public disclosure timing with you

## Security Best Practices

When using the Image Editor:

### For Users
- **Keep Updated**: Always use the latest version
- **Trusted Sources**: Only download from official repositories
- **File Safety**: Be cautious when opening images from untrusted sources
- **System Updates**: Keep your Python and system libraries updated

### For Developers
- **Code Review**: All contributions go through code review
- **Dependencies**: We regularly audit and update dependencies
- **Input Validation**: All user inputs are validated and sanitized
- **Error Handling**: Sensitive information is not exposed in error messages

## Known Security Considerations

### Image Processing
- **File Parsing**: We use PIL/Pillow which is actively maintained and secure
- **Memory Usage**: Large images are automatically resized to prevent memory exhaustion
- **File Types**: Only common, well-supported image formats are allowed

### User Interface
- **File Dialogs**: Standard OS file dialogs are used for security
- **Input Validation**: All user inputs are validated before processing
- **Error Messages**: No sensitive system information is displayed

## Dependencies Security

We monitor our dependencies for security vulnerabilities:

- **Pillow**: Regularly updated for security patches
- **CustomTkinter**: Modern, actively maintained UI framework
- **ScreenInfo**: Minimal, well-reviewed library

## Contact

For security-related questions or concerns:

- **Security Team**: [yyyabed123@gmail.com]
- **Maintainers**: See [CONTRIBUTING.md](CONTRIBUTING.md) for contact information

Thank you for helping keep the Image Editor secure! 🔒

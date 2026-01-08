# Contributing to AJNETWORKS Website

Thank you for your interest in contributing to the AJNETWORKS website! This document provides guidelines for authorized team members and contributors.

## 🔐 Access Requirements

This is a **private corporate website**. Contributions are limited to:

- Authorized AJNETWORKS team members
- Approved contractors with signed agreements
- Strategic partners with explicit permissions

## 📋 Before You Start

1. **Read the Master Blueprint**: Review `data.md` for complete brand guidelines
2. **Understand Brand Positioning**: AJNETWORKS is a consulting-first firm
3. **Review Existing Code**: Familiarize yourself with the codebase structure
4. **Check Open Issues**: See if your contribution is already being addressed

## 🚀 Getting Started

### 1. Set Up Your Development Environment

```bash
# Clone the repository
git clone https://github.com/AJ-NETWORKS-KENYA/Ajnets.git
cd Ajnets

# Create a new branch for your feature
git checkout -b feature/your-feature-name
```

### 2. Start Local Server

```bash
# Using Python
python -m http.server 8000

# Using PHP
php -S localhost:8000

# Using Node.js
npx http-server -p 8000
```

Visit `http://localhost:8000/index.html`

## 📝 Contribution Guidelines

### Code Style

#### HTML

- Use semantic HTML5 elements
- Maintain consistent indentation (2 spaces)
- Add comments for complex sections
- Follow existing naming conventions
- Ensure accessibility (alt text, ARIA labels)

#### CSS

- Follow existing class naming patterns
- Keep styles modular and reusable
- Use consistent spacing and formatting
- Comment complex selectors
- Test responsive breakpoints

#### JavaScript

- Use ES6+ syntax where appropriate
- Follow existing jQuery patterns
- Add JSDoc comments for functions
- Handle errors gracefully
- Test across browsers

### Branding Consistency

**CRITICAL:** All content must align with AJNETWORKS brand guidelines:

- **Contact Email**: jabrahamjohns@gmail.com
- **Phone**: +254 758 238 617
- **Locations**: Nairobi & Mombasa, Kenya
- **Social Links**:
  - Twitter: https://twitter.com/ajnetworks
  - Facebook: https://facebook.com/ajnetworks
  - LinkedIn: https://linkedin.com/company/ajnetworks
  - Instagram: https://instagram.com/ajnetworks

### Service Structure

Always reference the **5 Core Practices**:

1. Technology & Digital Strategy
2. Software Engineering
3. Cybersecurity & Assurance
4. Networking & Infrastructure
5. Performance & SEO

## 🔄 Workflow

### 1. Create a Feature Branch

```bash
git checkout -b feature/description
# Examples:
# feature/update-portfolio
# fix/contact-form-validation
# content/update-about-page
```

### 2. Make Your Changes

- Keep commits focused and atomic
- Write clear, descriptive commit messages
- Test thoroughly before committing

### 3. Commit Your Changes

```bash
git add .
git commit -m "feat: Add new portfolio case study"

# Commit message format:
# feat: New feature
# fix: Bug fix
# docs: Documentation changes
# style: Formatting, missing semicolons, etc.
# refactor: Code restructuring
# test: Adding tests
# chore: Maintenance tasks
```

### 4. Push to Remote

```bash
git push origin feature/your-feature-name
```

### 5. Create Pull Request

- Provide clear description of changes
- Reference any related issues
- Add screenshots for UI changes
- Request review from team lead

## 🧪 Testing Checklist

Before submitting your PR, verify:

- [ ] All pages load without errors
- [ ] Responsive design works on mobile, tablet, desktop
- [ ] Forms validate correctly
- [ ] Links are working (no 404s)
- [ ] Images display properly
- [ ] Contact information is correct
- [ ] Navigation menus function properly
- [ ] Cross-browser compatibility (Chrome, Firefox, Safari, Edge)
- [ ] Performance is acceptable (page load times)
- [ ] No console errors or warnings

## 📂 File Organization

### Adding New Pages

1. Copy an appropriate template page
2. Update meta tags (title, description, keywords)
3. Update header navigation
4. Update footer information
5. Follow content structure from `data.md`
6. Test all links and functionality

### Modifying Existing Pages

1. Read current content carefully
2. Maintain existing structure
3. Update only necessary sections
4. Preserve branding consistency
5. Test before and after changes

## 🎨 Design Guidelines

### Colors

Primary colors as defined in `style.css`:

- Primary Blue: #43BAFF
- Dark Blue: #0160E7
- Accent Orange: #FFB524

### Typography

- Headings: Montserrat
- Body Text: Nunito Sans
- Maintain hierarchy (h1 > h2 > h3)

### Images

- Optimize images before adding (compress, resize)
- Use appropriate formats (JPG for photos, PNG for graphics, SVG for logos)
- Include descriptive alt text
- Store in `/images/` directory

## 🚫 What NOT to Do

- ❌ Don't commit directly to `main` branch
- ❌ Don't change core branding elements without approval
- ❌ Don't remove or modify LICENSE file
- ❌ Don't commit sensitive data (passwords, API keys)
- ❌ Don't break existing functionality
- ❌ Don't ignore lint errors
- ❌ Don't skip testing

## 🔧 Using Maintenance Scripts

The repository includes PowerShell scripts for bulk updates:

```powershell
# Update branding across pages
.\update-remaining-pages.ps1

# Update navigation menus
.\update-navigation.ps1

# Verify updates
.\verify-updates.ps1
```

**Note**: Always review script changes before committing.

## 📞 Getting Help

### Questions?

Contact the development team:

- **Email**: jabrahamjohns@gmail.com
- **Team Channel**: [Internal communication channel]

### Issues

Found a bug or have a suggestion?

1. Check existing issues first
2. Create a new issue with detailed description
3. Include screenshots if relevant
4. Tag appropriately (bug, enhancement, question)

## 📄 Documentation

When adding new features:

- Update `README.md` if necessary
- Add comments in code
- Update `data.md` for content changes
- Document any new dependencies

## 🔒 Security

### Reporting Security Issues

**DO NOT** open public issues for security vulnerabilities.

Contact directly:

- Email: jabrahamjohns@gmail.com
- Subject: [SECURITY] Description

### Best Practices

- Keep dependencies updated
- Validate all user inputs
- Use HTTPS for all external links
- Don't expose sensitive data in code
- Follow OWASP guidelines

## ✅ Pull Request Checklist

Before submitting, ensure:

- [ ] Code follows style guidelines
- [ ] All tests pass
- [ ] Documentation is updated
- [ ] Commit messages are clear
- [ ] Branch is up to date with main
- [ ] No merge conflicts
- [ ] Changes are tested locally
- [ ] Screenshots added (for UI changes)
- [ ] Reviewer assigned

## 🎯 Review Process

1. **Automated Checks**: Linting, basic validation
2. **Peer Review**: Code quality, best practices
3. **Team Lead Approval**: Final sign-off
4. **Merge**: Squash and merge to main

## 📊 Versioning

We use [Semantic Versioning](https://semver.org/):

- MAJOR.MINOR.PATCH
- Example: 2.1.3

## 🙏 Thank You

Your contributions help make AJNETWORKS better! We appreciate your:

- Attention to detail
- Commitment to quality
- Respect for guidelines
- Collaborative spirit

---

**Questions or concerns? Reach out to the team lead.**

**Happy coding! 🚀**

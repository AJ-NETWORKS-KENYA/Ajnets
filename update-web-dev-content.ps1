# Comprehensive content update for web-development.html
$ErrorActionPreference = "Stop"

$file = "web-development.html"
Write-Host "Updating $file content..." -ForegroundColor Cyan

$content = Get-Content $file -Raw -Encoding UTF8

# Update page title
$content = $content -replace '<h1 class="page-title">Web Development</h1>', '<h1 class="page-title">Web & Platform Engineering</h1>'
$content = $content -replace '<li class="active">Web Development</li>', '<li class="active">Web & Platform Engineering</li>'
$content = $content -replace '<li><a href="web-development\.html">IT Services</a></li>', '<li><a href="services.html">Services</a></li>'

# Update main heading
$content = $content -replace '// about service', '// software engineering'
$content = $content -replace 'We Provide Best <br />Web Development', 'Engineering Reliable Systems <br />That Scale With Your Business'

# Update service boxes
$content = $content -replace '<h6 class="mb-0">Java Development</h6>', '<h6 class="mb-0">Corporate Websites</h6>'
$content = $content -replace '<h6 class="mb-0">PHP Development</h6>', '<h6 class="mb-0">Enterprise Portals</h6>'
$content = $content -replace '<h6 class="mb-0">C\+\+ Development</h6>', '<h6 class="mb-0">Custom Business Systems</h6>'
$content = $content -replace '<h6 class="mb-0">\.NET Development</h6>', '<h6 class="mb-0">API & Integrations</h6>'

# Update descriptions
$content = $content -replace "We're committed to building sustainable and\s+high-quality Java solutions\.", 'Professional web presence with content management and SEO optimization.'

# Update secondary service boxes
$content = $content -replace '<h5>Machine Learning</h5>\s*<p>Support and Evolution</p>', '<h5>Secure by Design</h5><p>Security embedded into every solution</p>'
$content = $content -replace '<h5>Artificial Intelligence</h5>\s*<p>Support and Evolution</p>', '<h5>Scalable Architecture</h5><p>Built to grow with your business</p>'
$content = $content -replace '<h5>Augmented Reality</h5>\s*<p>Support and Evolution</p>', '<h5>Performance Optimized</h5><p>Fast, efficient, and reliable systems</p>'

# Update process section
$content = $content -replace 'We Organize Our <br />Production Process', 'Our Engineering <br />Approach'

# Update pricing section
$content = $content -replace '// choose your plan', '// transparent pricing'
$content = $content -replace 'Flexible Pricing Plans', 'Web & Platform Engineering Investment'
$content = $content -replace 'We help businesses elevate their value through custom software development, product design, QA and consultancy services\.', 'All pricing shown in USD for international reference. Local billing may be converted to KES at prevailing exchange rates. Every engagement begins with a complimentary strategy call.'

# Update pricing tiers
$content = $content -replace 'Basic Plan', 'Corporate Website'
$content = $content -replace '\$\s*129\.99', '1,700+'
$content = $content -replace 'Economy Plan', 'Enterprise Portal'
$content = $content -replace '\$\s*159\.99', '3,500+'
$content = $content -replace 'Premium Plan', 'Custom Platform'
$content = $content -replace '\$\s*189\.99', '10,000+'
$content = $content -replace 'Monthly Package', 'Starting From (USD)'

# Update testimonials section
$content = $content -replace 'We are Trusted <br />15\+ Countries Worldwide', 'Trusted Technology <br />Partner Across Kenya & Beyond'

Write-Host "Writing updated content..." -ForegroundColor Yellow
Set-Content -Path $file -Value $content -Encoding UTF8 -NoNewline
Write-Host "Successfully updated $file!" -ForegroundColor Green

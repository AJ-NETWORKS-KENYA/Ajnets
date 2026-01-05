# Update web-development.html and mobile-development.html for AJNETWORKS
$ErrorActionPreference = "Stop"

# Files to update
$files = @("web-development.html", "mobile-development.html")

foreach ($file in $files) {
    Write-Host "Updating $file..." -ForegroundColor Cyan
    
    $content = Get-Content $file -Raw -Encoding UTF8
    
    # Update title and branding
    $content = $content -replace '<title>Engitech</title>', '<title>AJNETWORKS - Technology Consulting & Engineering</title>'
    $content = $content -replace 'alt="Engitech"', 'alt="AJNETWORKS"'
    
    # Remove royal_preloader class
    $content = $content -replace '<body class="royal_preloader">', '<body>'
    
    # Update contact information
    $content = $content -replace 'engitech@mail\.net', 'jabrahamjohns@gmail.com'
    $content = $content -replace 'contact@mail\.net', 'jabrahamjohns@gmail.com'
    $content = $content -replace '\+1 -800-456-478-23', '+254 758 238 617'
    $content = $content -replace '411 University St, Seattle, USA', 'Nairobi & Mombasa, Kenya'
    
    # Update social media links
    $content = $content -replace 'href="http://twitter\.com/" target="_self"', 'href="https://twitter.com/ajnetworks" target="_blank" rel="noopener"'
    $content = $content -replace 'href="http://facebook\.com/" target="_self"', 'href="https://facebook.com/ajnetworks" target="_blank" rel="noopener"'
    $content = $content -replace 'href="http://linkedin\.com/" target="_self"', 'href="https://linkedin.com/company/ajnetworks" target="_blank" rel="noopener"'
    $content = $content -replace 'href="http://instagram/" target="_self"', 'href="https://instagram.com/ajnetworks" target="_blank" rel="noopener"'
    
    # Update footer social links
    $content = $content -replace 'href="twitter\.html"', 'href="https://twitter.com/ajnetworks" target="_blank" rel="noopener"'
    $content = $content -replace 'href="facebook\.html"', 'href="https://facebook.com/ajnetworks" target="_blank" rel="noopener"'
    $content = $content -replace 'href="linkedin\.html"', 'href="https://linkedin.com/company/ajnetworks" target="_blank" rel="noopener"'
    $content = $content -replace 'href="instagram\.html"', 'href="https://instagram.com/ajnetworks" target="_blank" rel="noopener"'
    
    # Update copyright
    $content = $content -replace 'Copyright © 2020 Engitech by ThemeModern\. All Rights Reserved\.', 'Copyright © 2026 AJNETWORKS. All Rights Reserved.'
    
    # Update company references
    $content = $content -replace 'Engitech is the partner of choice', 'AJNETWORKS is the partner of choice'
    $content = $content -replace '>Engitech<', '>AJNETWORKS<'
    
    # Update navigation structure for Services
    $content = $content -replace '<li><a href="it-services\.html">It Services</a></li>\s*<li class="current-menu-item"><a href="web-development\.html">Web Development</a></li>\s*<li><a href="mobile-development\.html">Mobile Development</a></li>', @'
<li><a href="technology-strategy.html">Technology & Digital Strategy</a></li>
                                                    <li><a href="software-engineering.html">Software Engineering</a></li>
                                                    <li><a href="cybersecurity.html">Cybersecurity & Assurance</a></li>
                                                    <li><a href="networking.html">Networking & Infrastructure</a></li>
                                                    <li><a href="performance-seo.html">Performance & SEO</a></li>
'@
    
    # Write updated content
    Set-Content -Path $file -Value $content -Encoding UTF8 -NoNewline
    Write-Host "Successfully updated $file" -ForegroundColor Green
}

Write-Host ""
Write-Host "All files updated successfully!" -ForegroundColor Green

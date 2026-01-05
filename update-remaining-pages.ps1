# PowerShell script to update remaining pages with AJNETWORKS branding
$files = @(
    "blog.html",
    "faq.html",
    "portfolio-details-1.html",
    "portfolio-details-2.html"
)

foreach ($file in $files) {
    $content = Get-Content $file -Raw -Encoding UTF8
    
    # Update page title
    $content = $content -replace '<title>Engitech</title>', '<title>AJNETWORKS - Technology Consulting & Engineering</title>'
    $content = $content -replace '<title>AJNETWORKS</title>', '<title>AJNETWORKS - Technology Consulting & Engineering</title>'
    
    # Update logo alt text
    $content = $content -replace 'alt="Engitech"', 'alt="AJNETWORKS"'
    
    # Update email in header
    $content = $content -replace '<li><i class="fas fa-envelope"></i><a href="mailto:[^"]+">.*?</a></li>', '<li><i class="fas fa-envelope"></i><a href="mailto:jabrahamjohns@gmail.com"> jabrahamjohns@gmail.com</a></li>'
    
    # Update topbar CTA
    $content = $content -replace 'We hire and build your own remote dedicated development teams tailored to your specific needs\.', 'We are creative, ambitious and ready for challenges! <a href="contact.html">Hire Us</a>'
    
    # Update social media links - Twitter
    $content = $content -replace '<a class="twitter" href="twitter\.html">', '<a class="twitter" href="https://twitter.com/ajnetworks" target="_blank" rel="noopener">'
    
    # Update social media links - Facebook
    $content = $content -replace '<a class="facebook" href="facebook\.html">', '<a class="facebook" href="https://facebook.com/ajnetworks" target="_blank" rel="noopener">'
    
    # Update social media links - LinkedIn
    $content = $content -replace '<a class="linkedin" href="linkedin\.html">', '<a class="linkedin" href="https://linkedin.com/company/ajnetworks" target="_blank" rel="noopener">'
    
    # Update social media links - Instagram
    $content = $content -replace '<a class="instagram" href="instagram\.html">', '<a class="instagram" href="https://instagram.com/ajnetworks" target="_blank" rel="noopener">'
    
    # Update footer address
    $content = $content -replace '411 University St, Seattle, USA', 'Nairobi & Mombasa, Kenya'
    $content = $content -replace '<h6>Our Address</h6>', '<h6>Our Locations</h6>'
    
    # Update footer email
    $content = $content -replace '<p>contact@mail\.net</p>', '<p>jabrahamjohns@gmail.com</p>'
    
    # Update footer phone
    $content = $content -replace '<p>\+1 -800-456-478-23</p>', '<p>+254 758 238 617</p>'
    
    # Update copyright
    $content = $content -replace 'Copyright © 2020 Engitech by ThemeModern\. All Rights Reserved\.', 'Copyright © 2026 AJNETWORKS. All Rights Reserved.'
    $content = $content -replace 'Copyright © 2020 AJNETWORKS by ThemeModern\. All Rights Reserved\.', 'Copyright © 2026 AJNETWORKS. All Rights Reserved.'
    
    # Update phone in header
    $content = $content -replace '<span class="main-text"><a href="tel:[^"]+">.*?</a></span>', '<span class="main-text"><a href="tel:+254 758 238 617">+254 758 238 617</a></span>'
    
    Set-Content -Path $file -Value $content -Encoding UTF8 -NoNewline
    Write-Host "Updated $file"
}

Write-Host "`nAll pages updated successfully!"

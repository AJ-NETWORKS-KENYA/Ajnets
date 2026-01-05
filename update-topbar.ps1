# PowerShell script to update topbar section with proper social links
$files = @(
    "blog.html",
    "faq.html",
    "portfolio-details-1.html",
    "portfolio-details-2.html"
)

foreach ($file in $files) {
    $content = Get-Content $file -Raw -Encoding UTF8
    
    # Update topbar social links section
    $oldTopbarSocial = @'
                                    <ul class="social-list">
                                        <li><a href="twitter.html"><i class="fab fa-twitter"></i></a></li>
                                        <li><a href="facebook.html"><i class="fab fa-facebook-f"></i></a></li>
                                        <li><a href="linkedin.html"><i class="fab fa-linkedin-in"></i></a></li>
                                        <li><a href="instagram.html"><i class="fab fa-instagram"></i></a></li>
                                    </ul>
'@

    $newTopbarSocial = @'
                                    <ul class="social-list">
                                        <li><a href="https://twitter.com/ajnetworks" target="_blank" rel="noopener"><i class="fab fa-twitter"></i></a></li>
                                        <li><a href="https://facebook.com/ajnetworks" target="_blank" rel="noopener"><i class="fab fa-facebook-f"></i></a></li>
                                        <li><a href="https://linkedin.com/company/ajnetworks" target="_blank" rel="noopener"><i class="fab fa-linkedin-in"></i></a></li>
                                        <li><a href="https://instagram.com/ajnetworks" target="_blank" rel="noopener"><i class="fab fa-instagram"></i></a></li>
                                    </ul>
'@

    if ($content -match [regex]::Escape($oldTopbarSocial)) {
        $content = $content -replace [regex]::Escape($oldTopbarSocial), $newTopbarSocial
    }
    
    # Update topbar extra text
    $oldExtraText = '<li>We hire and build your own remote dedicated development teams tailored to your specific needs.</li>'
    $newExtraText = '<li>We are creative, ambitious and ready for challenges! <a href="contact.html">Hire Us</a></li>'
    
    $content = $content -replace [regex]::Escape($oldExtraText), $newExtraText
    
    Set-Content -Path $file -Value $content -Encoding UTF8 -NoNewline
    Write-Host "Updated topbar in $file"
}

Write-Host "`nTopbar sections updated successfully!"

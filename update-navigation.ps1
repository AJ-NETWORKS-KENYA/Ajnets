# PowerShell script to update navigation menus on remaining pages
$files = @(
    "blog.html",
    "faq.html",
    "portfolio-details-1.html",
    "portfolio-details-2.html"
)

foreach ($file in $files) {
    $content = Get-Content $file -Raw -Encoding UTF8
    
    # Update desktop navigation - Services submenu
    $oldServicesMenu = @'
                                <li class="menu-item-has-children"><a href="#">Services</a>
                                    <ul class="sub-menu">
                                        <li><a href="it-services.html">IT Services</a></li>
                                        <li><a href="web-development.html">Web Development</a></li>
                                        <li><a href="mobile-development.html">Mobile Development</a></li>
                                    </ul>
                                </li>
'@

    $newServicesMenu = @'
                                <li class="menu-item-has-children"><a href="services.html">Services</a>
                                    <ul class="sub-menu">
                                        <li><a href="technology-strategy.html">Technology & Digital Strategy</a></li>
                                        <li><a href="software-engineering.html">Software Engineering</a></li>
                                        <li><a href="cybersecurity.html">Cybersecurity & Assurance</a></li>
                                        <li><a href="networking.html">Networking & Infrastructure</a></li>
                                        <li><a href="performance-seo.html">Performance & SEO</a></li>
                                    </ul>
                                </li>
'@

    if ($content -match [regex]::Escape($oldServicesMenu)) {
        $content = $content -replace [regex]::Escape($oldServicesMenu), $newServicesMenu
    }
    
    # Update mobile navigation - Services submenu
    $oldMobileServices = @'
                                <li class="menu-item-has-children"><a href="#">Services</a>
                                    <ul class="sub-menu">
                                        <li><a href="it-services.html">IT Services</a></li>
                                        <li><a href="web-development.html">Web Development</a></li>
                                        <li><a href="mobile-development.html">Mobile Development</a></li>
                                    </ul>
                                </li>
'@

    $newMobileServices = @'
                                <li class="menu-item-has-children"><a href="services.html">Services</a>
                                    <ul class="sub-menu">
                                        <li><a href="technology-strategy.html">Technology & Digital Strategy</a></li>
                                        <li><a href="software-engineering.html">Software Engineering</a></li>
                                        <li><a href="cybersecurity.html">Cybersecurity & Assurance</a></li>
                                        <li><a href="networking.html">Networking & Infrastructure</a></li>
                                        <li><a href="performance-seo.html">Performance & SEO</a></li>
                                    </ul>
                                </li>
'@

    if ($content -match [regex]::Escape($oldMobileServices)) {
        $content = $content -replace [regex]::Escape($oldMobileServices), $newMobileServices
    }
    
    Set-Content -Path $file -Value $content -Encoding UTF8 -NoNewline
    Write-Host "Updated navigation in $file"
}

Write-Host "`nNavigation menus updated successfully!"

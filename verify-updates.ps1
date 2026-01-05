# Verification script for updated pages
Write-Host "=== VERIFICATION SUMMARY ===" -ForegroundColor Green
Write-Host ""
Write-Host "Checking updated files..." -ForegroundColor Yellow

$files = @("blog.html", "faq.html", "portfolio-details-1.html", "portfolio-details-2.html")

foreach ($file in $files) {
    if (Test-Path $file) {
        $content = Get-Content $file -Raw
        $hasAJNETWORKS = $content -match "AJNETWORKS"
        $hasCorrectEmail = $content -match "jabrahamjohns@gmail.com"
        $hasCorrectPhone = $content -match "\+254 758 238 617"
        $hasCorrectLocation = $content -match "Nairobi & Mombasa, Kenya"
        $hasSocialLinks = $content -match "twitter.com/ajnetworks"
        
        Write-Host ""
        Write-Host "$file" -ForegroundColor Cyan
        Write-Host "  AJNETWORKS branding: $(if($hasAJNETWORKS){'✓'}else{'✗'})" -ForegroundColor $(if($hasAJNETWORKS){'Green'}else{'Red'})
        Write-Host "  Correct email: $(if($hasCorrectEmail){'✓'}else{'✗'})" -ForegroundColor $(if($hasCorrectEmail){'Green'}else{'Red'})
        Write-Host "  Correct phone: $(if($hasCorrectPhone){'✓'}else{'✗'})" -ForegroundColor $(if($hasCorrectPhone){'Green'}else{'Red'})
        Write-Host "  Correct location: $(if($hasCorrectLocation){'✓'}else{'✗'})" -ForegroundColor $(if($hasCorrectLocation){'Green'}else{'Red'})
        Write-Host "  Social links updated: $(if($hasSocialLinks){'✓'}else{'✗'})" -ForegroundColor $(if($hasSocialLinks){'Green'}else{'Red'})
    }
}

Write-Host ""
Write-Host "=== UPDATE COMPLETE ===" -ForegroundColor Green

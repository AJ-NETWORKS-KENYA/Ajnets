# AJNETWORKS Logo Replacement Guide

## ✅ What I've Done

Created `css/logo-ajnetworks.css` - A CSS file that will properly size your 500x500px logo to fit in:

- Header: 160x75px (max)
- Footer: 180x80px (max)
- Mobile: Responsive scaling
- All pages automatically

## 📋 Steps to Complete Logo Replacement

### Step 1: Prepare Your Logo Files

You mentioned you have:

- `c:\Users\lenovo\Downloads\AJ\ajnets\Ajnets-removebg-preview.png` (500x500px)
- SVG version (coming)

**Action needed:**

1. Copy your PNG file to: `c:\My Web Sites\ajnets\images\logo.png`
2. When you get the SVG, copy it to: `c:\My Web Sites\ajnets\images\logo.svg`

**Commands to run:**

```powershell
# Copy PNG logo
Copy-Item "c:\Users\lenovo\Downloads\AJ\ajnets\Ajnets-removebg-preview.png" "c:\My Web Sites\ajnets\images\logo.png" -Force

# When you have SVG, copy it:
# Copy-Item "path\to\your\logo.svg" "c:\My Web Sites\ajnets\images\logo.svg" -Force
```

### Step 2: Add CSS to All Pages

The new CSS file needs to be included in every HTML page.

**Pages that need updating:**

- index.html
- index-2.html
- contact.html
- about-us.html
- blog.html
- faq.html
- mobile-development.html
- networking.html
- All other HTML files

**What to add:**
In the `<head>` section of each file, after other CSS includes, add:

```html
<link rel="stylesheet" href="css/logo-ajnetworks.css" />
```

**Example location in file:**

```html
<link rel="stylesheet" href="css/magnific-popup.css" />
<link rel="stylesheet" href="style.css" />
<link rel="stylesheet" href="css/logo-ajnetworks.css" />
<link rel="stylesheet" href="css/royal-preload.css" />
```

### Step 3: Verify Logo Sizing

After copying the logo files and adding the CSS:

1. Start your server:

```powershell
cd "c:\My Web Sites\ajnets"
python -m http.server 8000
```

2. Visit: http://localhost:8000/

3. Check:
   - ✅ Logo displays in header (should be ~160px wide)
   - ✅ Logo displays in footer
   - ✅ Logo looks good on mobile (resize browser)
   - ✅ No "Engitech" text visible

## 🔧 Quick Fix Script

Run this PowerShell script to add the CSS to main pages automatically:

```powershell
cd "c:\My Web Sites\ajnets"

# List of main pages to update
$pages = @(
    "index.html",
    "index-2.html",
    "contact.html",
    "about-us.html",
    "blog.html",
    "faq.html",
    "mobile-development.html",
    "networking.html"
)

foreach ($page in $pages) {
    if (Test-Path $page) {
        $content = Get-Content $page -Raw
        if ($content -notmatch "logo-ajnetworks.css") {
            $content = $content -replace '(<link rel="stylesheet" href="style\.css" />)', '$1`n    <link rel="stylesheet" href="css/logo-ajnetworks.css" />'
            Set-Content $page $content -NoNewline
            Write-Host "✓ Updated: $page" -ForegroundColor Green
        } else {
            Write-Host "- Already updated: $page" -ForegroundColor Gray
        }
    }
}

Write-Host "`nDone! CSS added to all main pages." -ForegroundColor Green
```

## 📐 Logo Specifications

### Current Setup:

- **Your logo:** 500x500px (square)
- **Needs to fit:** 160x75px header space

### CSS Handles:

- ✅ Automatic scaling to fit
- ✅ Maintains aspect ratio
- ✅ Responsive on mobile
- ✅ Works with PNG and SVG
- ✅ No distortion

### Sizing Reference:

| Location       | Max Width | Max Height |
| -------------- | --------- | ---------- |
| Header Desktop | 160px     | 75px       |
| Header Mobile  | 100px     | 45px       |
| Footer         | 180px     | 80px       |
| Sticky Header  | 140px     | 60px       |

## 🎨 Logo Formats

### PNG (Current):

- ✅ Works immediately
- ✅ Transparent background
- File: `images/logo.png`

### SVG (Recommended):

- ✅ Perfect at any size
- ✅ Smaller file size
- ✅ Crisp on retina displays
- File: `images/logo.svg`

**Recommendation:** Once you have the SVG, replace the PNG references with SVG for best quality.

## 🔍 Finding Old "Engitech" Logos

If you still see "Engitech" anywhere:

### Search for remaining instances:

```powershell
cd "c:\My Web Sites\ajnets"
Get-ChildItem -Filter "*.html" -Recurse | Select-String -Pattern "engitech|Engitech" -List
```

### Check for old logo files:

```powershell
Get-ChildItem images\* -Include "*engi*","*logo-*" | Select-Object Name
```

## ✅ Verification Checklist

After completing all steps:

- [ ] PNG logo copied to `images/logo.png`
- [ ] SVG logo copied to `images/logo.svg` (when available)
- [ ] CSS file exists at `css/logo-ajnetworks.css`
- [ ] CSS added to all main HTML pages
- [ ] Logo displays correctly in header
- [ ] Logo displays correctly in footer
- [ ] Logo responsive on mobile
- [ ] No "Engitech" text visible
- [ ] Logo not too big or too small

## 🚀 Next Steps

1. **Copy your logo files** (see Step 1)
2. **Run the PowerShell script** (see Quick Fix Script)
3. **Test in browser** (python -m http.server 8000)
4. **Check all pages** to ensure logo looks good

## 📞 Need Help?

If logo still looks wrong:

- Check browser console for errors (F12)
- Clear browser cache (Ctrl+Shift+R)
- Verify file paths are correct
- Make sure CSS file is loaded (check Network tab in F12)

---

**Created:** January 7, 2026  
**Purpose:** Replace Engitech logo with AJNETWORKS logo  
**Status:** CSS ready, awaiting logo file copy

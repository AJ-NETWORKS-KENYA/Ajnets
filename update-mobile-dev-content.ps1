# Comprehensive content update for mobile-development.html
$ErrorActionPreference = "Stop"

$file = "mobile-development.html"
Write-Host "Updating $file content..." -ForegroundColor Cyan

$content = Get-Content $file -Raw -Encoding UTF8

# Update page title
$content = $content -replace '<h1 class="page-title">Mobile Development</h1>', '<h1 class="page-title">Mobile App Development</h1>'
$content = $content -replace '<li class="active">Mobile Development</li>', '<li class="active">Mobile App Development</li>'
$content = $content -replace '<li><a href="web-development\.html">IT Services</a></li>', '<li><a href="services.html">Services</a></li>'

# Update main headings
$content = $content -replace '// business benefits', '// mobile solutions'
$content = $content -replace 'Mobile Apps Benefits', 'Mobile Applications That Drive Business Value'

# Update mobile benefits - left side
$content = $content -replace '<h5>Software as a Service</h5>\s*<p>51% of smartphone users have discovered a new company or product\.</p>', '<h5>Customer Engagement</h5><p>Reach customers directly on their most-used devices with push notifications and personalized experiences.</p>'
$content = $content -replace '<h5>Internet of Things</h5>\s*<p>Move your SaaS products to mobile, Companies with a professional mobile\.</p>', '<h5>Operational Efficiency</h5><p>Streamline workflows and enable teams to work effectively from anywhere with mobile-first tools.</p>'
$content = $content -replace '<h5>Gambling &amp; Betting</h5>\s*<p>Develop a custom mobile app to thrive in a mobile market worth over \$100\.</p>', '<h5>Competitive Advantage</h5><p>Stay ahead with innovative mobile solutions that differentiate your business in the market.</p>'

# Update mobile benefits - right side
$content = $content -replace '<h5>Social Media </h5>\s*<p>80% of time users spend in social mediafrom their mobile devices\.</p>', '<h5>Data & Insights</h5><p>Gather valuable user behavior data to make informed business decisions and improve services.</p>'
$content = $content -replace '<h5>Business Management</h5>\s*<p>65% of sales representatives have achieved their quotas by adopting\.</p>', '<h5>Revenue Growth</h5><p>Open new revenue streams through in-app purchases, subscriptions, or enhanced service delivery.</p>'
$content = $content -replace '<h5>Trading Systems</h5>\s*<p>We provide top-tier mobile app development services for brokers\.</p>', '<h5>Brand Visibility</h5><p>Increase brand presence and accessibility with a professionally designed mobile application.</p>'

# Update about section
$content = $content -replace '// about company', '// our approach'
$content = $content -replace 'Your Partner for <br>Software Innovation', 'Strategic Mobile <br>Development'
$content = $content -replace 'We help businesses elevate their value through custom software development, product design, QA and consultancy services\.', 'We develop native and cross-platform mobile applications for iOS and Android that are secure, performant, and aligned with your business objectives. Every app is built with user experience and scalability in mind.'
$content = $content -replace 'We can help to maintain and modernize your IT infrastructure and solve various infrastructure-specific issues a business may face\.', 'From concept to launch and beyond, we provide end-to-end mobile development services including strategy, design, development, testing, and ongoing support.'

# Update case studies section
$content = $content -replace '// latest case studies', '// our work'
$content = $content -replace 'Introduce Our Projects', 'Featured Mobile Solutions'
$content = $content -replace 'Software development outsourcing is just a tool to achieve business goals\. But there is no way to get worthwhile results without cooperation and trust between a client company\.', 'Our mobile applications are designed to solve real business problems and deliver measurable results. We work closely with clients to ensure every solution aligns with strategic objectives.'

# Update business industries section
$content = $content -replace 'BUSINESS INDUSTRIES', 'INDUSTRIES WE SERVE'
$content = $content -replace 'Business Industries <br>What We Serve', 'Mobile Solutions <br>Across Industries'

# Update mobile navigation
$content = $content -replace '<li><a href="it-services\.html">It Services</a></li>\s*<li class="current-menu-item">\s*<a href="mobile-development\.html">Mobile Development</a>\s*</li>\s*<li>\s*<a href="web-development\.html">Web Development</a>\s*</li>', @'
<li><a href="technology-strategy.html">Technology & Digital Strategy</a></li>
                      <li><a href="software-engineering.html">Software Engineering</a></li>
                      <li><a href="cybersecurity.html">Cybersecurity & Assurance</a></li>
                      <li><a href="networking.html">Networking & Infrastructure</a></li>
                      <li><a href="performance-seo.html">Performance & SEO</a></li>
'@

Write-Host "Writing updated content..." -ForegroundColor Yellow
Set-Content -Path $file -Value $content -Encoding UTF8 -NoNewline
Write-Host "Successfully updated $file!" -ForegroundColor Green

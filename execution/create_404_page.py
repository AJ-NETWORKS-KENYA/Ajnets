import os
import re

def create_404_page(source_path, target_path):
    with open(source_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Change title
    content = re.sub(r'<title>.*?</title>', '<title>Page Not Found | AJNETWORKS</title>', content)
    
    # Empty the main content area (slider/hero area in index.html)
    # We'll use a regex to replace everything between <main> and </main> if it existed, or we can just replace the main slider
    # It's safer to use faq.html as a base since we know its structure
    content = re.sub(r'<li class="breadcrumb-item active" aria-current="page">.*?</li>', '<li class="breadcrumb-item active" aria-current="page">404 Error</li>', content)
    content = re.sub(r'<h2 class="title text-white">.*?</h2>', '<h2 class="title text-white">Page Not Found</h2>', content)
    content = re.sub(r'<h2 class="title">.*?</h2>', '<h2 class="title">404 Error</h2>', content)

    # Empty the accordion content
    accordion_pattern = re.compile(r'<div class="accordion" id="accordion1">.*?</div>\s*</div>\s*</div>\s*</div>', re.DOTALL)
    
    placeholder = '''
    <div class="col-lg-12 text-center">
        <div class="content-box py-5">
            <h1 class="display-1 fw-bold text-primary mb-4">404</h1>
            <h3 class="mb-4">Oops! The page you are looking for does not exist.</h3>
            <p class="mb-5">It might have been moved, deleted, or perhaps you mistyped the URL.</p>
            <a href="/" class="sl-button">Return to Homepage</a>
        </div>
    </div>
    </div>
    </div>
    </div>
    '''
    
    content = accordion_pattern.sub(placeholder, content)

    # Make sure links to CSS/JS are absolute since 404 can trigger on deep paths (e.g., /services/foo/bar)
    # Vercel handles this well if we use root-relative paths like /css/style.css, which this site already uses (hopefully).
    # We already checked HTML paths and they use /css, /js, /images.

    with open(target_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Created: {target_path}")

def main():
    faq_path = r"c:\My Web Sites\ajnets\company\faq.html"
    target_path = r"c:\My Web Sites\ajnets\404.html"
    
    create_404_page(faq_path, target_path)

if __name__ == "__main__":
    main()

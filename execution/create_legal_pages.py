import os
import re
import shutil

def create_legal_page(source_path, target_path, new_title, new_slug, new_heading):
    with open(source_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Change title
    content = re.sub(r'<title>.*?</title>', f'<title>{new_title} | AJNETWORKS</title>', content)
    
    # Change canonical and og:url
    content = re.sub(r'href="https://ajnetworks.co/faq"', f'href="https://ajnetworks.co/{new_slug}"', content)
    content = re.sub(r'content="https://ajnetworks.co/faq"', f'content="https://ajnetworks.co/{new_slug}"', content)
    
    # Change breadcrumb active item
    content = re.sub(r'<li class="breadcrumb-item active" aria-current="page">FAQ\'S</li>', f'<li class="breadcrumb-item active" aria-current="page">{new_title}</li>', content)

    # Change the heading
    content = re.sub(r'<h2 class="title text-white">Frequently Asked Questions</h2>', f'<h2 class="title text-white">{new_heading}</h2>', content)
    content = re.sub(r'<h2 class="title">General Questions</h2>', f'<h2 class="title">{new_heading}</h2>', content)

    # Empty the accordion content (which has id="accordion1")
    # A bit hacky but we'll regex out everything between <div class="accordion" id="accordion1"> and its closing </div>
    accordion_pattern = re.compile(r'<div class="accordion" id="accordion1">.*?</div>\s*</div>\s*</div>\s*</div>', re.DOTALL)
    
    placeholder = f'''
    <div class="col-lg-12">
        <div class="content-box">
            <p>This page is currently being updated. Please check back later for the full {new_title}.</p>
        </div>
    </div>
    </div>
    </div>
    </div>
    '''
    
    content = accordion_pattern.sub(placeholder, content)

    with open(target_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Created: {target_path}")

def main():
    faq_path = r"c:\My Web Sites\ajnets\company\faq.html"
    company_dir = r"c:\My Web Sites\ajnets\company"
    
    create_legal_page(faq_path, os.path.join(company_dir, 'privacy.html'), "Privacy Policy", "privacy", "Privacy Policy")
    create_legal_page(faq_path, os.path.join(company_dir, 'terms.html'), "Terms of Service", "terms", "Terms of Service")
    create_legal_page(faq_path, os.path.join(company_dir, 'responsible-disclosure.html'), "Responsible Disclosure", "responsible-disclosure", "Responsible Disclosure")

if __name__ == "__main__":
    main()

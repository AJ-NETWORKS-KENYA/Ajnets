import os
import re
import shutil

target_folders = {
    'company': ['about-us.html', 'book-consultation.html', 'faq.html'],
    'services': [
        'services.html', 'technology-strategy.html', 'software-engineering.html',
        'cybersecurity.html', 'networking.html', 'performance-seo.html',
        'mobile-development.html', 'web-development.html', 'solutions.html'
    ],
    'portfolio': [
        'client-success.html', 'case-study-audiophile.html', 'case-study-bada.html',
        'case-study-crappo.html', 'case-study-greenremedies.html', 'case-study-racnyali.html',
        'case-study-sgss.html', 'case-study-transitflow.html', 'portfolio-details-1.html',
        'portfolio-details-2.html'
    ],
    'insights': ['insights.html', 'post.html'],
    'elements': ['elements.html']
}

# Reverse mapping to get destination route for replacing cross-page links
link_mapping = {}
for folder, files in target_folders.items():
    for file in files:
        # e.g. "about-us.html" -> "/company/about-us"
        link_mapping[file] = f"/{folder}/{file.replace('.html', '')}"

# We also know index.html -> "/"
link_mapping['index.html'] = '/'

# Files we will process
all_html = []
for folder, files in target_folders.items():
    all_html.extend(files)
all_html.append('index.html')

def update_html_content(content):
    # 1. Update relative asset paths to root-relative paths
    content = re.sub(r'href="(css/)', r'href="/\1', content)
    content = re.sub(r'href="(images/)', r'href="/\1', content)
    content = re.sub(r'href="(fonts/)', r'href="/\1', content)
    content = re.sub(r'href="(plugins/)', r'href="/\1', content)
    content = re.sub(r'src="(images/)', r'src="/\1', content)
    content = re.sub(r'src="(js/)', r'src="/\1', content)
    content = re.sub(r'src="(plugins/)', r'src="/\1', content)

    # Note: avoid double replacement (if they already had /css/)
    content = content.replace('href="//css/', 'href="/css/')
    content = content.replace('href="//images/', 'href="/images/')
    content = content.replace('href="//fonts/', 'href="/fonts/')
    content = content.replace('href="//plugins/', 'href="/plugins/')
    content = content.replace('src="//images/', 'src="/images/')
    content = content.replace('src="//js/', 'src="/js/')
    content = content.replace('src="//plugins/', 'src="/plugins/')

    # 2. Update page-to-page links based on link_mapping
    for old_file, new_link in link_mapping.items():
        # Match exactly href="file.html" or href="file.html#..."
        # using a simple replace for exactly href="filename"
        # We need to handle possible hash fragments, e.g. href="index.html#about" -> href="/#about"
        # A regex works better
        pattern = r'href="' + re.escape(old_file) + r'([#?][^"]*)?"'
        replacement = r'href="' + new_link + r'\1"'
        content = re.sub(pattern, replacement, content)

    return content


def run():
    print("Creating folders...")
    for folder in target_folders.keys():
        os.makedirs(folder, exist_ok=True)

    print("Updating contents and moving files...")
    for html_file in all_html:
        if not os.path.exists(html_file):
            print(f"Skipping {html_file}, file not found in root.")
            continue
            
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()

        new_content = update_html_content(content)

        # Determine target path
        target_path = html_file
        for folder, files in target_folders.items():
            if html_file in files:
                target_path = os.path.join(folder, html_file)
                break
        
        # We write directly to the target_path. If target_path != html_file, 
        # it means we moved it. Once we write the new one, we can delete the old one.
        with open(target_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        if target_path != html_file:
            os.remove(html_file)
            print(f"Moved and updated {html_file} -> {target_path}")
        else:
            print(f"Updated {html_file} in place")

if __name__ == '__main__':
    run()
    print("Done!")

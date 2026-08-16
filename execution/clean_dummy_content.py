import os
import re

def clean_about_us(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove the dummy video popup
    pattern = re.compile(r'<div class="video-popup style-2">.*?</div>\s*</div>', re.DOTALL)
    new_content = pattern.sub('', content)

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Cleaned dummy video in: {filepath}")

def clean_post(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove dummy share and author socials
    content = re.sub(r'<div class="share-post">.*?</div>', '', content, flags=re.DOTALL)
    content = re.sub(r'<div class="author-socials">.*?</div>', '', content, flags=re.DOTALL)

    # Replace dead href="#" with "/insights" to keep them valid but not dead
    # Some might be for comment replies, replace those too
    content = content.replace('href="#"', 'href="/insights"')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Cleaned dummy content in: {filepath}")

def main():
    about_us = r"c:\My Web Sites\ajnets\company\about-us.html"
    post = r"c:\My Web Sites\ajnets\insights\post.html"
    
    if os.path.exists(about_us):
        clean_about_us(about_us)
    if os.path.exists(post):
        clean_post(post)

if __name__ == "__main__":
    main()

import os
import glob

directory = "."
extensions = ["*.html", "*.md", "LICENSE"]

def html_encode(text):
    return "".join(f"&#{ord(c)};" for c in text)

files_to_process = []
# recursively add files in subdirectories
for root, dirs, files in os.walk(directory):
    if 'execution' in dirs:
        dirs.remove('execution')
    if '.git' in dirs:
        dirs.remove('.git')
    if 'node_modules' in dirs:
        dirs.remove('node_modules')

    for file in files:
        if any(file.endswith(e.replace('*', '')) for e in extensions) or file == 'LICENSE':
            files_to_process.append(os.path.join(root, file))

# Remove duplicates
files_to_process = list(set(files_to_process))

email = "hello@ajnetworkskenya.it.com"
encoded_email = html_encode(email)
mailto_link = f"mailto:{email}"
encoded_mailto_link = html_encode(mailto_link)

for file_path in files_to_process:
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    
    # Replace mailto links directly
    new_content = content.replace("mailto:jabrahamjohns@gmail.com", encoded_mailto_link)
    
    # Replace visual text with HTML-encoded spam protection
    # Note: mailto link replacements are done, so any remaining "jabrahamjohns@gmail.com" are text content
    new_content = new_content.replace("jabrahamjohns@gmail.com", encoded_email)

    # Also replace any already semi-encoded versions just in case
    new_content = new_content.replace("mailto:hello@ajnetworkskenya.it.com", encoded_mailto_link)
    new_content = new_content.replace("hello&#64;ajnetworkskenya.it.com", encoded_email)
    new_content = new_content.replace("hello@ajnetworkskenya.it.com", encoded_email)

    
    if content != new_content:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated {os.path.basename(file_path)}")

print("Global email replacement completed successfully.")

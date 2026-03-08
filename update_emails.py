import os
import glob

directory = r"c:\My Web Sites\ajnets"
extensions = ["*.html", "*.md", "LICENSE"]

files_to_process = []
for ext in extensions:
    files_to_process.extend(glob.glob(os.path.join(directory, ext)))

for file_path in files_to_process:
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    
    # Replace mailto links directly
    new_content = content.replace("mailto:jabrahamjohns@gmail.com", "mailto:hello@ajnetworkskenya.it.com")
    
    # Replace visual text with HTML-encoded spam protection
    # Note: mailto link replacements are done, so any remaining "jabrahamjohns@gmail.com" are text content
    new_content = new_content.replace("jabrahamjohns@gmail.com", "hello&#64;ajnetworkskenya.it.com")
    
    if content != new_content:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated {os.path.basename(file_path)}")

print("Global email replacement completed successfully.")

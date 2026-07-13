import os

ROOT = r"c:\My Web Sites\ajnets"

REPLACEMENTS = {
    "ajnetworkskenya.it.com": "ajnetworks.co",
    "hello@ajnetworkskenya.it.com": "hello@ajnetworks.co",
    "hello&#64;ajnetworkskenya.it.com": "hello&#64;ajnetworks.co"
}

def process_file(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        return False

    new_content = content
    for old, new in REPLACEMENTS.items():
        new_content = new_content.replace(old, new)

    if new_content != content:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        return True

    return False

def main():
    fixed = 0
    for dirpath, dirnames, filenames in os.walk(ROOT):
        # Skip certain directories
        dirnames[:] = [d for d in dirnames if d not in (".git", "node_modules", "execution", ".tmp")]
        for fname in filenames:
            if fname.endswith((".html", ".xml", ".txt", ".json", ".md")):
                fpath = os.path.join(dirpath, fname)
                if process_file(fpath):
                    print(f"  [UPDATED] {os.path.relpath(fpath, ROOT)}")
                    fixed += 1

    print(f"\nDone - {fixed} files updated.")

if __name__ == "__main__":
    main()

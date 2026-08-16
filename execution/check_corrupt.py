from pathlib import Path

root = Path(r"C:\My Web Sites\ajnets")
html_files = [f for f in root.rglob("*.html") if not any(p in f.parts for p in ["node_modules", ".tmp", ".agent", ".agents"])]

for hf in sorted(html_files):
    rel = str(hf.relative_to(root)).replace("\\", "/")
    with open(hf, "r", encoding="utf-8", errors="replace") as f:
        content = f.read()
    if "\ufffd" in content:
        print(f"{rel} has {content.count(chr(0xFFFD))} corrupt characters (\\ufffd)")
        # Find snippets around \ufffd
        for i, line in enumerate(content.splitlines()):
            if "\ufffd" in line:
                print(f"   Line {i+1}: {line.strip()[:100]}")

import os
import re

def fix_cards_and_nav():
    root_dir = r"c:\My Web Sites\ajnets"
    count_nav = 0
    count_cards = 0

    # Patterns to match the Book Consultation LI
    # Desktop nav
    nav_pattern_1 = re.compile(
        r'<li>\s*<a href="/company/book-consultation(?:\.html)?">Book Consultation</a>\s*</li>',
        re.IGNORECASE
    )
    
    # We will just read all HTML files and apply fixes
    for dirpath, dirnames, filenames in os.walk(root_dir):
        dirnames[:] = [d for d in dirnames if d not in (".git", "node_modules", "execution", ".tmp")]
        for fname in filenames:
            if fname.endswith(".html"):
                fpath = os.path.join(dirpath, fname)
                with open(fpath, "r", encoding="utf-8") as f:
                    content = f.read()
                
                original_content = content
                
                # 1. Remove Book Consultation from menu
                content, num_subs = nav_pattern_1.subn("", content)
                if num_subs > 0:
                    count_nav += 1
                
                # 2. Fix the card headings in support-box content-box
                # If it's about-us.html (or any other file with support-box)
                # change <h4>Our Mission</h4> to <h3>Our Mission</h3> inside content-box
                if '<div class="content-box">' in content and '<h4>' in content:
                    # We only want to target Our Mission, Our Vision, Our Philosophy, Our Strategy
                    content = content.replace("<h4>Our Mission</h4>", "<h3>Our Mission</h3>")
                    content = content.replace("<h4>Our Vision</h4>", "<h3>Our Vision</h3>")
                    content = content.replace("<h4>Our Philosophy</h4>", "<h3>Our Philosophy</h3>")
                    content = content.replace("<h4>Our Strategy</h4>", "<h3>Our Strategy</h3>")
                    
                    if content != original_content:
                        count_cards += 1

                if content != original_content:
                    with open(fpath, "w", encoding="utf-8") as f:
                        f.write(content)

    print(f"Fixed navigation in {count_nav} files.")
    print(f"Fixed card headings in {count_cards} files.")

if __name__ == "__main__":
    fix_cards_and_nav()

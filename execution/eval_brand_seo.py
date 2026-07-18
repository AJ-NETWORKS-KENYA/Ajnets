import os
import re
import json

ROOT_DIR = r"c:\My Web Sites\ajnets"

def run_eval():
    print("Evaluating SEO and Brand Alignment Metrics...")
    total_pages = 0
    passed_pages = 0
    json_ld_count = 0
    canonical_match_count = 0
    og_match_count = 0

    for dirpath, _, filenames in os.walk(ROOT_DIR):
        if "node_modules" in dirpath or ".git" in dirpath or ".tmp" in dirpath:
            continue
        for f in filenames:
            if f.endswith(".html"):
                total_pages += 1
                filepath = os.path.join(dirpath, f)
                with open(filepath, "r", encoding="utf-8") as file:
                    content = file.read()

                # Check JSON-LD
                if '<script type="application/ld+json">' in content:
                    json_ld_count += 1

                # Check Canonical
                if 'rel="canonical"' in content and 'https://ajnetworks.co' in content:
                    canonical_match_count += 1

                # Check Open Graph
                if 'property="og:url"' in content and 'https://ajnetworks.co' in content:
                    og_match_count += 1

                # Full check
                if (all(l in content for l in [
                    "https://facebook.com/ajnetworks",
                    "https://linkedin.com/company/ajnetworks",
                    "https://www.youtube.com/@ajnets",
                    "https://pinterest.com/ajnetworks"
                ]) and '<script type="application/ld+json">' in content):
                    passed_pages += 1

    score = (passed_pages / total_pages * 100) if total_pages > 0 else 0
    print(f"Total Pages Analyzed: {total_pages}")
    print(f"JSON-LD Schema Coverage: {json_ld_count}/{total_pages} ({json_ld_count/total_pages*100:.1f}%)")
    print(f"Canonical URL Consistency: {canonical_match_count}/{total_pages} ({canonical_match_count/total_pages*100:.1f}%)")
    print(f"Open Graph URL Consistency: {og_match_count}/{total_pages} ({og_match_count/total_pages*100:.1f}%)")
    print(f"Overall Brand & SEO Compliance Score: {score:.1f}%")

    assert score == 100.0, f"Evaluation score {score}% is below 100.0% threshold!"
    print("SEO & Brand Alignment Evaluation PASSED.")

if __name__ == "__main__":
    run_eval()

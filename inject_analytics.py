import os
import glob
import re

# GA4 Placeholder ID
MEASUREMENT_ID = "G-2E6LLT0TT7"

DIRECTORY = r"c:\My Web Sites\ajnets"

GA4_SNIPPET = f"""
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id={MEASUREMENT_ID}"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){{dataLayer.push(arguments);}}
      gtag('js', new Date());

      gtag('config', '{MEASUREMENT_ID}');
    </script>"""

def inject_analytics():
    files = glob.glob(os.path.join(DIRECTORY, "*.html"))
    count = 0
    
    for filepath in files:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        # Check if already injected
        if "googletagmanager.com/gtag/js" in content:
            print(f"Skipping {os.path.basename(filepath)} - Analytics already present.")
            continue
            
        # Inject before closing </head>
        if "</head>" in content:
            new_content = content.replace("</head>", f"{GA4_SNIPPET}\n  </head>")
            
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(new_content)
            count += 1
            print(f"Injected analytics into {os.path.basename(filepath)}")
        else:
            print(f"Warning: No </head> tag found in {os.path.basename(filepath)}")

    print(f"Batch injection completed. Updated {count} files.")

if __name__ == "__main__":
    inject_analytics()

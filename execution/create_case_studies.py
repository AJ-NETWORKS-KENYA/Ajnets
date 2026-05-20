import shutil
import os

source = r"c:\My Web Sites\ajnets\portfolio-details-1.html"
targets = [
    r"c:\My Web Sites\ajnets\case-study-bada.html",
    r"c:\My Web Sites\ajnets\case-study-sgss.html",
    r"c:\My Web Sites\ajnets\case-study-racnyali.html",
    r"c:\My Web Sites\ajnets\case-study-transitflow.html",
    r"c:\My Web Sites\ajnets\case-study-audiophile.html",
    r"c:\My Web Sites\ajnets\case-study-greenremedies.html"
]

for target in targets:
    shutil.copy2(source, target)
    print(f"Created {target}")

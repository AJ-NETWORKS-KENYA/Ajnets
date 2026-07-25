import timeit
import re

content = """<html>
<body>
<nav id="site-navigation" class="main-navigation">
    <ul><li>Test</li></ul>
</nav>
<ul id="menu-main-menu" class="mobile_mainmenu">
    <li>Test Mobile</li>
</ul>
</body>
</html>""" * 1000

desktop_nav_replacement = "NAV"
mobile_nav_replacement = "MOBILE"

def inside_loop():
    c = content
    for _ in range(100):
        pattern_desktop = re.compile(r'<nav id="site-navigation" class="main-navigation">.*?</nav>', re.DOTALL)
        c = re.sub(pattern_desktop, desktop_nav_replacement, c)
        pattern_mobile = re.compile(r'<ul id="menu-main-menu" class="mobile_mainmenu">.*?</ul>', re.DOTALL)
        c = re.sub(pattern_mobile, mobile_nav_replacement, c)

pattern_desktop = re.compile(r'<nav id="site-navigation" class="main-navigation">.*?</nav>', re.DOTALL)
pattern_mobile = re.compile(r'<ul id="menu-main-menu" class="mobile_mainmenu">.*?</ul>', re.DOTALL)

def outside_loop():
    c = content
    for _ in range(100):
        c = re.sub(pattern_desktop, desktop_nav_replacement, c)
        c = re.sub(pattern_mobile, mobile_nav_replacement, c)

if __name__ == "__main__":
    t_inside = timeit.timeit(inside_loop, number=10)
    t_outside = timeit.timeit(outside_loop, number=10)
    print(f"Inside loop: {t_inside:.4f}s")
    print(f"Outside loop: {t_outside:.4f}s")

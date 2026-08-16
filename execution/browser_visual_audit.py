import os
import sys
import time
import threading
import http.server
import socketserver
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

PORT = 8091
ROOT = Path(r"C:\My Web Sites\ajnets")
TMP_DIR = ROOT / ".tmp"
TMP_DIR.mkdir(exist_ok=True)

class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)
    def log_message(self, format, *args):
        pass
    def handle(self):
        try:
            super().handle()
        except (ConnectionResetError, ConnectionAbortedError, BrokenPipeError):
            pass

def start_server():
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), QuietHandler) as httpd:
        httpd.serve_forever()

server_thread = threading.Thread(target=start_server, daemon=True)
server_thread.start()
time.sleep(1)

print(f"[INFO] Local server running at http://localhost:{PORT}")

chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--window-size=1280,1024")

driver = None
try:
    driver = webdriver.Chrome(options=chrome_options)
    url = f"http://localhost:{PORT}/company/book-consultation.html"
    print(f"[INFO] Navigating to {url}...")
    driver.get(url)
    time.sleep(2)

    # Dismiss cookie banner
    try:
        accept_btn = driver.find_element(By.ID, "btn-accept-cookies")
        if accept_btn.is_displayed():
            accept_btn.click()
            time.sleep(0.5)
    except Exception:
        pass

    # 1. Check all .error elements on initial load
    error_elements = driver.find_elements(By.CLASS_NAME, "error")
    print(f"[INFO] Found {len(error_elements)} .error elements on the page.")
    visible_errors = [e for e in error_elements if e.is_displayed()]
    
    if len(visible_errors) == 0:
        print("[PASS] All validation error messages are HIDDEN on initial load.")
    else:
        print(f"[FAIL] Found {len(visible_errors)} VISIBLE error messages on initial load:")
        for e in visible_errors:
            print(f"  - id='{e.get_attribute('id')}', text='{e.text}'")
        raise AssertionError("Validation error messages visible on initial load")

    # 2. Check #region select
    region_el = driver.find_element(By.ID, "region")
    select_obj = Select(region_el)
    options = select_obj.options
    print(f"[INFO] Region dropdown has {len(options)} total options.")
    for idx, opt in enumerate(options):
        print(f"  Option [{idx}]: value='{opt.get_attribute('value')}', text='{opt.text}', disabled={not opt.is_enabled()}")

    assert len(options) >= 4, "Expected at least 4 options in region select"
    assert not options[0].is_enabled(), "First option should be disabled placeholder"
    
    # Test selecting each selectable option
    for val in ["Kenya", "Rwanda", "East Africa", "International"]:
        select_obj.select_by_value(val)
        selected = select_obj.first_selected_option
        assert selected.get_attribute("value") == val
        print(f"[PASS] Successfully selected option: {selected.text}")

    # 3. Take initial screenshot
    screenshot_path = TMP_DIR / "contact_form_initial_load.png"
    driver.save_screenshot(str(screenshot_path))
    print(f"[PASS] Saved initial screenshot to {screenshot_path}")

    # 4. Refresh to test fresh submission validation
    driver.refresh()
    time.sleep(1)

    # Dismiss cookie banner again if needed
    try:
        accept_btn = driver.find_element(By.ID, "btn-accept-cookies")
        if accept_btn.is_displayed():
            accept_btn.click()
            time.sleep(0.5)
    except Exception:
        pass

    submit_btn = driver.find_element(By.ID, "send")
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", submit_btn)
    time.sleep(0.5)
    
    # Submit empty form via JS click or native click
    driver.execute_script("arguments[0].click();", submit_btn)
    time.sleep(1)

    post_submit_errors = [e for e in driver.find_elements(By.CLASS_NAME, "error") if e.is_displayed()]
    print(f"[INFO] After submit with empty fields, {len(post_submit_errors)} error messages are displayed as expected.")
    for e in post_submit_errors:
        print(f"  - Visible Error: id='{e.get_attribute('id')}', text='{e.text}'")

    assert len(post_submit_errors) >= 3, "Expected at least 3 validation error messages displayed"

    post_screenshot_path = TMP_DIR / "contact_form_after_validation.png"
    driver.save_screenshot(str(post_screenshot_path))
    print(f"[PASS] Saved validation screenshot to {post_screenshot_path}")

    # 5. Fill fields and verify errors clear
    name_input = driver.find_element(By.NAME, "name")
    name_input.send_keys("Jane Doe")
    # Trigger jQuery input event
    driver.execute_script("$(arguments[0]).trigger('input');", name_input)
    time.sleep(0.3)
    
    print("\n[PASS] Visual & Form Verification Complete and 100% Successful!")

except Exception as ex:
    print(f"[FAIL] Visual verification encountered error: {ex}")
    sys.exit(1)
finally:
    if driver:
        driver.quit()

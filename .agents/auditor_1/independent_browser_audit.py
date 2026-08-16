import os
import sys
import time
import socket
import threading
import http.server
import socketserver
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

ROOT = Path(r"C:\My Web Sites\ajnets")
AUDITOR_DIR = ROOT / ".agents" / "auditor_1"
AUDITOR_DIR.mkdir(parents=True, exist_ok=True)

def find_free_port():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("", 0))
        return s.getsockname()[1]

PORT = find_free_port()

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

class ThreadingHTTPServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
    daemon_threads = True

def start_server():
    httpd = ThreadingHTTPServer(("", PORT), QuietHandler)
    httpd.serve_forever()

def main():
    print("=" * 70)
    print("AJNETWORKS VICTORY AUDITOR — INDEPENDENT BROWSER VISUAL VERIFICATION")
    print("=" * 70)
    
    server_thread = threading.Thread(target=start_server, daemon=True)
    server_thread.start()
    time.sleep(1)
    print(f"[INFO] Audit HTTP server running on http://127.0.0.1:{PORT}")
    
    chrome_opts = Options()
    chrome_opts.add_argument("--headless=new")
    chrome_opts.add_argument("--disable-gpu")
    chrome_opts.add_argument("--no-sandbox")
    chrome_opts.add_argument("--window-size=1280,1024")
    
    driver = None
    try:
        driver = webdriver.Chrome(options=chrome_opts)
        target_url = f"http://127.0.0.1:{PORT}/company/book-consultation.html"
        print(f"[INFO] Navigating to {target_url}...")
        driver.get(target_url)
        time.sleep(2)
        
        # 1. Check cookie banner
        try:
            cookie_btn = driver.find_element(By.ID, "btn-accept-cookies")
            if cookie_btn.is_displayed():
                cookie_btn.click()
                time.sleep(0.5)
        except Exception:
            pass
            
        # 2. Check all .error elements on initial load
        print("\n>>> 1. AUDITING VALIDATION ERRORS ON INITIAL LOAD...")
        error_elements = driver.find_elements(By.CLASS_NAME, "error")
        print(f"    Found {len(error_elements)} .error elements on page.")
        
        visible_errors = []
        for e in error_elements:
            if e.is_displayed():
                visible_errors.append((e.get_attribute("id"), e.text))
                
        if len(visible_errors) == 0:
            print("    [PASS] All validation error elements are strictly HIDDEN on initial load.")
        else:
            print(f"    [FAIL] Detected {len(visible_errors)} VISIBLE error elements on initial load: {visible_errors}")
            raise AssertionError(f"Visible errors on initial load: {visible_errors}")

        # 3. Take initial screenshot
        init_ss = AUDITOR_DIR / "screenshot_initial_load.png"
        driver.save_screenshot(str(init_ss))
        print(f"    [PASS] Captured initial load screenshot -> {init_ss}")

        # 4. Check #region select
        print("\n>>> 2. AUDITING REGION DROPDOWN...")
        region_el = driver.find_element(By.ID, "region")
        select_obj = Select(region_el)
        options = select_obj.options
        print(f"    Region dropdown has {len(options)} options.")
        
        for idx, opt in enumerate(options):
            print(f"      Option [{idx}]: value='{opt.get_attribute('value')}', text='{opt.text}', enabled={opt.is_enabled()}")
            
        assert len(options) >= 4, f"Expected at least 4 options, got {len(options)}"
        assert not options[0].is_enabled() or options[0].get_attribute("disabled"), "Placeholder should be disabled"
        
        # Test selecting options
        for val in ["Kenya", "Rwanda", "East Africa", "International"]:
            select_obj.select_by_value(val)
            chosen = select_obj.first_selected_option
            assert chosen.get_attribute("value") == val, f"Selection failed for {val}"
            print(f"    [PASS] Successfully selected: '{chosen.text}'")
            
        print("    [PASS] Region dropdown is fully populated, correctly disabled on placeholder, and functional.")

        # 5. Form submission validation
        print("\n>>> 3. AUDITING FORM VALIDATION ON EMPTY SUBMIT...")
        submit_btn = driver.find_element(By.ID, "send")
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", submit_btn)
        time.sleep(0.5)
        driver.execute_script("arguments[0].click();", submit_btn)
        time.sleep(1)
        
        post_errors = [e for e in driver.find_elements(By.CLASS_NAME, "error") if e.is_displayed()]
        print(f"    After submit, {len(post_errors)} validation errors are visible.")
        for e in post_errors:
            print(f"      Visible error: id='{e.get_attribute('id')}', text='{e.text}'")
            
        assert len(post_errors) >= 3, "Expected validation errors to appear upon empty submission"
        
        err_ss = AUDITOR_DIR / "screenshot_validation_errors.png"
        driver.save_screenshot(str(err_ss))
        print(f"    [PASS] Captured validation error screenshot -> {err_ss}")

        print("\n" + "=" * 70)
        print("BROWSER VISUAL AUDIT VERDICT: 100% PASS (ALL CRITERIA VERIFIED)")
        print("=" * 70)
        return True
        
    except Exception as ex:
        print(f"\n[FAIL] Browser visual audit error: {ex}")
        return False
    finally:
        if driver:
            driver.quit()

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)

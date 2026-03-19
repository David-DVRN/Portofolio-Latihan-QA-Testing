import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Buat folder screenshots kalau belum ada
def create_screenshot_folders():
    folders = ["screenshots/pass", "screenshots/fail"]
    for folder in folders:
        if not os.path.exists(folder):
            os.makedirs(folder)

@pytest.fixture
def driver():
    create_screenshot_folders()
    print("\n🚀 Membuka browser...")
    
    # Chrome Options — matikan Password Manager
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-save-password-bubble")
    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False
    })
    
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    driver.maximize_window()
    driver.implicitly_wait(15)

    yield driver

    print("\n🔒 Menutup browser...")
    driver.quit()

# Otomatis screenshot setiap test selesai
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":
        driver = item.funcargs.get("driver")
        if driver:
            test_name = item.name
            if report.passed:
                path = f"screenshots/pass/{test_name}.png"
                driver.save_screenshot(path)
                print(f"\n📸 Screenshot PASS disimpan: {path}")
            elif report.failed:
                path = f"screenshots/fail/{test_name}.png"
                driver.save_screenshot(path)
                print(f"\n📸 Screenshot FAIL disimpan: {path}")
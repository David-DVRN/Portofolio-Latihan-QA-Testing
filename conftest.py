import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    # SETUP — dijalankan sebelum setiap test
    print("\n🚀 Membuka browser...")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(10)  # tunggu elemen maksimal 10 detik
    
    yield driver  # titik dimana test berjalan
    
    # TEARDOWN — dijalankan setelah setiap test
    print("\n🔒 Menutup browser...")
    driver.quit()
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# URL website yang di-test
BASE_URL = "https://www.saucedemo.com"

class TestLogin:

    # =============================================
    # TC_AUTO_001 - Login dengan kredensial valid
    # =============================================
    def test_login_valid(self, driver):
        print("\n📋 TC_AUTO_001 - Login dengan kredensial valid")
        
        # Buka website
        driver.get(BASE_URL)
        
        # Isi username
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        
        # Isi password
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        
        # Klik tombol login
        driver.find_element(By.ID, "login-button").click()
        
        # Verifikasi login berhasil
        assert "/inventory" in driver.current_url
        print("✅ PASS - Login berhasil, diarahkan ke halaman inventory")

    # =============================================
    # TC_AUTO_002 - Login dengan password salah
    # =============================================
    def test_login_password_salah(self, driver):
        print("\n📋 TC_AUTO_002 - Login dengan password salah")
        
        # Buka website
        driver.get(BASE_URL)
        
        # Isi username
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        
        # Isi password yang salah
        driver.find_element(By.ID, "password").send_keys("passwordsalah")
        
        # Klik tombol login
        driver.find_element(By.ID, "login-button").click()
        
        # Verifikasi muncul pesan error
        error_message = driver.find_element(By.CLASS_NAME, "error-message-container")
        assert error_message.is_displayed()
        print("✅ PASS - Muncul pesan error saat password salah")

    # =============================================
    # TC_AUTO_003 - Login dengan username kosong
    # =============================================
    def test_login_username_kosong(self, driver):
        print("\n📋 TC_AUTO_003 - Login dengan username kosong")
        
        # Buka website
        driver.get(BASE_URL)
        
        # Langsung isi password tanpa username
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        
        # Klik tombol login
        driver.find_element(By.ID, "login-button").click()
        
        # Verifikasi muncul pesan error
        error_message = driver.find_element(By.CLASS_NAME, "error-message-container")
        assert error_message.is_displayed()
        print("✅ PASS - Muncul pesan error saat username kosong")

    # =============================================
    # TC_AUTO_004 - Login dengan password kosong
    # =============================================
    def test_login_password_kosong(self, driver):
        print("\n📋 TC_AUTO_004 - Login dengan password kosong")
        
        # Buka website
        driver.get(BASE_URL)
        
        # Isi username tanpa password
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        
        # Klik tombol login
        driver.find_element(By.ID, "login-button").click()
        
        # Verifikasi muncul pesan error
        error_message = driver.find_element(By.CLASS_NAME, "error-message-container")
        assert error_message.is_displayed()
        print("✅ PASS - Muncul pesan error saat password kosong")

    # =============================================
    # TC_AUTO_005 - Login lalu logout
    # =============================================
    def test_login_lalu_logout(self, driver):
        print("\n📋 TC_AUTO_005 - Login lalu logout")
        
        # Buka website
        driver.get(BASE_URL)
        
        # Login dulu
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        
        # Verifikasi sudah login
        assert "/inventory" in driver.current_url
        
        # Klik menu burger (3 garis)
        driver.find_element(By.ID, "react-burger-menu-btn").click()
        time.sleep(1)

        # Tunggu tombol logout benar-benar muncul dan bisa diklik
        wait = WebDriverWait(driver, 10)
        logout_btn = wait.until(
            EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))
        )
        logout_btn.click()

        # Tunggu sampai URL berubah ke halaman login
        wait.until(EC.url_to_be(BASE_URL + "/"))
                
        # Verifikasi kembali ke halaman login
        assert driver.current_url == BASE_URL + "/"
        print("✅ PASS - Berhasil logout, kembali ke halaman login")
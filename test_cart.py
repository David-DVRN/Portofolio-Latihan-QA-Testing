import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

BASE_URL = "https://www.saucedemo.com"

class TestCart:

    # Helper: login dulu sebelum test cart
    def login(self, driver):
        driver.get(BASE_URL)
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

    # =============================================
    # TC_AUTO_006 - Add to Cart produk pertama
    # =============================================
    def test_add_to_cart(self, driver):
        print("\n📋 TC_AUTO_006 - Add to Cart produk pertama")

        # Login dulu
        self.login(driver)

        # Klik tombol Add to Cart produk pertama
        driver.find_element(
            By.XPATH, "(//button[text()='Add to cart'])[1]"
        ).click()

        # Cek badge keranjang berubah jadi 1
        badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        assert badge.text == "1"
        print("✅ PASS - Produk berhasil ditambahkan ke keranjang")

    # =============================================
    # TC_AUTO_007 - Add to Cart lalu Remove
    # =============================================
    def test_add_lalu_remove(self, driver):
        print("\n📋 TC_AUTO_007 - Add to Cart lalu Remove")

        # Login dulu
        self.login(driver)

        # Add to cart
        driver.find_element(
            By.XPATH, "(//button[text()='Add to cart'])[1]"
        ).click()

        # Verifikasi badge muncul
        badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        assert badge.text == "1"

        # Klik Remove
        driver.find_element(
            By.XPATH, "(//button[text()='Remove'])[1]"
        ).click()

        # Verifikasi badge hilang
        badges = driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
        assert len(badges) == 0
        print("✅ PASS - Produk berhasil di-remove dari keranjang")

    # =============================================
    # TC_AUTO_008 - Checkout sampai selesai
    # =============================================
    def test_checkout(self, driver):
        print("\n📋 TC_AUTO_008 - Checkout sampai selesai")

        # Login dulu
        self.login(driver)

        # Add to cart
        driver.find_element(
            By.XPATH, "(//button[text()='Add to cart'])[1]"
        ).click()

        # Buka keranjang
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        # Verifikasi di halaman cart
        assert "/cart" in driver.current_url

        # Klik Checkout
        driver.find_element(By.ID, "checkout").click()

        # Isi form checkout
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.ID, "first-name")))

        driver.find_element(By.ID, "first-name").send_keys("David")
        driver.find_element(By.ID, "last-name").send_keys("Darmawan")
        driver.find_element(By.ID, "postal-code").send_keys("12345")

        # Klik Continue
        driver.find_element(By.ID, "continue").click()

        # Verifikasi di halaman overview
        wait.until(EC.url_contains("/checkout-step-two"))
        assert "/checkout-step-two" in driver.current_url

        # Klik Finish
        driver.find_element(By.ID, "finish").click()

        # Verifikasi order berhasil
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "complete-header")))
        success_msg = driver.find_element(By.CLASS_NAME, "complete-header")
        assert "Thank you" in success_msg.text
        print("✅ PASS - Checkout berhasil, muncul pesan Thank you!")
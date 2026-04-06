from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pytest


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()


def test_login_y_compra(driver):
    # 🌐 abrir página
    driver.get("https://www.saucedemo.com/")

    # 🔐 login
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # ✅ validación login (ASSERT real)
    title = driver.find_element(By.CLASS_NAME, "title").text
    assert title == "Products", "❌ El login falló"

    # 🛒 agregar producto
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # 📦 validación carrito
    producto = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    assert producto == "Sauce Labs Backpack", "❌ El producto no es el esperado"

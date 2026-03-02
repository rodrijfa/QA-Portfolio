from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#driver = webdriver.Chrome()

from selenium.webdriver.chrome.options import Options
import os
from datetime import datetime

chrome_options = Options()
chrome_options.add_argument("--guest")
chrome_options.add_argument("--disable-features=PasswordLeakDetection")
chrome_options.add_experimental_option("prefs", {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False
})

driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 10)
driver.get("https://www.saucedemo.com")

passed = 0
failed = 0

def login(username, password):
    #Función para hacer login

    # Esperar que el campo username esté presente antes de interactuar
    wait.until(EC.presence_of_element_located((By.ID, "user-name")))

    # Limpiar campos antes de escribir
    driver.find_element(By.ID, "user-name").clear()
    driver.find_element(By.ID, "password").clear()

    # Ingresar credenciales
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)

    # Click en login
    driver.find_element(By.ID, "login-button").click()


def get_error_message():
    ##Espera explícitamente el mensaje de error y devuelve su texto
    error_element = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='error']"))
    )
    return error_element.text


def close_error_message():
    #Cierra el mensaje de error (botón X)
    driver.find_element(By.CSS_SELECTOR, "[data-test='error-button']").click()

# TC-001: Login exitoso
login("standard_user", "secret_sauce")
# Verificar que redirige correctamente al inventario
try:
    assert "/inventory.html" in driver.current_url
    print("TC-001 PASSED: Login exitoso con standard_user")
    passed += 1
except AssertionError:
    print("TC-001 FAILED")
    failed += 1

# Abrir menú lateral
wait.until(EC.element_to_be_clickable((By.ID, "react-burger-menu-btn"))).click()
# Esperar que aparezca el botón logout
wait.until(EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))).click()
# Esperar volver a la pantalla de login
wait.until(EC.presence_of_element_located((By.ID, "user-name")))


# TC-002: Usuario bloqueado
login("locked_out_user", "secret_sauce")
error_message = get_error_message()
print("TC-002 Error message:", error_message)

try:
    assert "Epic sadface: Sorry, this user has been locked out." in error_message
    print("TC-002 PASSED: Usuario bloqueado muestra mensaje correcto")
    passed += 1
except AssertionError:
    print("TC-002 FAILED")
    failed += 1

close_error_message()


# TC-003: Contraseña incorrecta
login("standard_user", "wrongpass")
error_message = get_error_message()

try:
    assert "Username and password do not match" in error_message
    print("TC-003 PASSED: Login con contraseña incorrecta")
    passed += 1
except AssertionError:
    print("TC-003 FAILED")
    failed += 1

close_error_message()


# TC-004: Campos vacíos
driver.refresh()
wait.until(EC.presence_of_element_located((By.ID, "user-name")))
# Verificar que los campos estén vacíos
print("Username antes:", driver.find_element(By.ID, "user-name").get_attribute("value"))
print("Password antes:", driver.find_element(By.ID, "password").get_attribute("value"))
# Click sin ingresar nada
driver.find_element(By.ID, "login-button").click()
error_message = get_error_message()
print("TC-004 Error message:", error_message)

try:
    assert "Username is required" in error_message
    print("TC-004 PASSED: Login con campos vacíos")
    passed += 1
except AssertionError:
    print("TC-004 FAILED")
    failed += 1


# TC-005: Solo usuario, sin contraseña
driver.refresh()
wait.until(EC.presence_of_element_located((By.ID, "user-name")))

login("standard_user", "")

error_message = get_error_message()
print("TC-005 Error message:", error_message)

try:
    assert "Password is required" in error_message
    print("TC-005 PASSED: Login solo con usuario sin contraseña")
    passed += 1
except AssertionError:
    print("TC-005 FAILED")
    failed += 1

close_error_message()


# TC-006: performance_glitch_user
import time

driver.refresh()
wait.until(EC.presence_of_element_located((By.ID, "user-name")))

start_time = time.time()

login("performance_glitch_user", "secret_sauce")
wait.until(EC.url_contains("inventory.html"))

end_time = time.time()
duration = end_time - start_time
print("TC-006 Tiempo de login:", duration)

try:
    assert duration < 6   # Ajusta si es necesario
    print("TC-006 PASSED: Login exitoso con performance_glitch_user")
    passed += 1
except AssertionError:
    print("TC-006 FAILED: Tiempo de login alto")
    failed += 1

wait.until(EC.element_to_be_clickable((By.ID, "react-burger-menu-btn"))).click()
wait.until(EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))).click()


# TC-007: Login con caracteres especiales
driver.refresh()
wait.until(EC.presence_of_element_located((By.ID, "user-name")))

login("!@#$%^&*()", "secret_sauce")

error_message = get_error_message()
print("TC-007 Error message:", error_message)

try:
    assert "Username and password do not match" in error_message
    print("TC-007 PASSED: Login con caracteres especiales muestra error")
    passed += 1
except AssertionError:
    print("TC-007 FAILED")
    failed += 1

close_error_message()


# TC-008: Validación imagen correcta del Backpack
driver.refresh()
wait.until(EC.presence_of_element_located((By.ID, "user-name")))
login("visual_user", "secret_sauce")
wait.until(EC.url_contains("inventory.html"))

# Buscar todos los productos
items = driver.find_elements(By.CLASS_NAME, "inventory_item")

backpack_image_src = None

for item in items:
    name = item.find_element(By.CLASS_NAME, "inventory_item_name").text
    
    if name == "Sauce Labs Backpack":
        backpack_image_src = item.find_element(By.TAG_NAME, "img").get_attribute("src")
        break

# Imagen esperada
#expected_image = "https://www.saucedemo.com/static/media/sl-404.168b1cce10384b857a6f.jpg" #INCORRECTA (perrito)
expected_image = "https://www.saucedemo.com/static/media/sauce-backpack-1200x1500.0a0b85a385945026062b.jpg" #CORRECTA (mochila)

if backpack_image_src is None:
    print("TC-008 FAILED: No se encontró el producto 'Sauce Labs Backpack'")
    failed += 1
    

elif expected_image in backpack_image_src:
    print("TC-008 PASSED: Imagen correcta del Backpack")
    passed += 1

else:
    print("TC-008 FAILED: Imagen incorrecta detectada")
    print("Obtenida:", backpack_image_src)

    #Screenshot error
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    # Crear carpeta
    if not os.path.exists("screenshots"):
        os.makedirs("screenshots")
    
    screenshot_path = f"screenshots/TC008_FAIL_{timestamp}.png"
    driver.save_screenshot(screenshot_path)
    print(f"Screenshot guardado en: {screenshot_path}")
    
    failed += 1


#CONTADOR FINAL DE PASSED/FAILED
print("\n==============================")
print("RESUMEN FINAL")
print("Tests PASSED:", passed)
print("Tests FAILED:", failed)
print("==============================")


# GENERAR REPORTE HTML
html_content = f"""
<html>
<head>
    <title>Test Report - SauceDemo</title>
    <style>
        body {{ font-family: Arial; background-color: #f4f4f4; }}
        h1 {{ color: #333; }}
        .passed {{ color: green; }}
        .failed {{ color: red; }}
        .box {{
            background: white;
            padding: 20px;
            border-radius: 8px;
            width: 400px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }}
    </style>
</head>
<body>
    <h1>Reporte de Tests - SauceDemo LOGIN</h1>
    <div class="box">
        <p class="passed"><strong>Tests PASSED:</strong> {passed}</p>
        <p class="failed"><strong>Tests FAILED:</strong> {failed}</p>
        <p><strong>Total:</strong> {passed + failed}</p>
    </div>
</body>
</html>
"""

with open("reporte_saucedemo.html", "w", encoding="utf-8") as file:
    file.write(html_content)

print("\nReporte HTML generado: reporte_saucedemo.html")

# FIN
input("Presiona Enter para cerrar el navegador...")
driver.quit()

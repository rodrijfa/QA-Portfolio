# Test Cases — Login | SauceDemo

| ID | Título | Precondición | Pasos | Resultado Esperado | Resultado Obtenido | Estado |
|----|--------|--------------|-------|-------------------|-------------------|--------|
| TC-001 | Login exitoso con usuario estándar | App abierta | 1. Ingresar "standard_user" en usuario 2. Ingresar "secret_sauce" en contraseña 3. Click en "Login" | Redirige a /inventory.html |Redirige correctamente a /inventory.html y muestra el catálogo de productos |Pass |
| TC-002 | Login con usuario bloqueado | App abierta | 1. Ingresar "locked_out_user" 2. Ingresar "secret_sauce" 3. Click en "Login" | Muestra error: "Epic sadface: Sorry, this user has been locked out." |Muestra mensaje: "Epic sadface: Sorry, this user has been locked out." |Pass |
| TC-003 | Login con contraseña incorrecta | App abierta | 1. Ingresar "standard_user" 2. Ingresar "wrongpass" 3. Click en "Login" | Muestra error de credenciales inválidas | Muestra mensaje: "Epic sadface: Username and password do not match any user in this service" |Pass |
| TC-004 | Login con campos vacíos | App abierta | 1. No ingresar nada 2. Click en "Login" | Muestra error indicando que usuario es requerido | Muestra mensaje: "Epic sadface: Username is required" | Pass |
| TC-005 | Login solo con usuario, sin contraseña | App abierta | 1. Ingresar "standard_user" 2. Dejar contraseña vacía 3. Click en "Login" | Muestra error indicando que contraseña es requerida |Muestra mensjae: "Epic sadface: Password is required" | Pass |
| TC-006 | Login con performance_glitch_user | App abierta | 1. Ingresar "performance_glitch_user" 2. Ingresar "secret_sauce" 3. Click en "Login" | Login exitoso. Se observa una demora de aproximadamente 3-5 segundos antes de redirigir a /inventory.html. El botón no da feedback visual durante la espera. | Redirige a /inventory.html con una demora notable | Pass |
| TC-007 | Login con caracteres especiales en usuario | App abierta | 1. Ingresar "!@#$%^&*()" en usuario 2. Ingresar "secret_sauce" 3. Click en "Login" | Muestra error de credenciales inválidas | Muestra mensaje: "Epic sadface: Username and password do not match any user in this service"| Pass|
| TC-008 | Login con visual_user | App abierta | 1. Ingresar "visual_user" en usuario 2. Ingresar "secret_sauce" 3. Click en "Login" | Muestra error visual | Muestra ítem "Sauce Labs Backpack" con imagen incorrecta| Pass|

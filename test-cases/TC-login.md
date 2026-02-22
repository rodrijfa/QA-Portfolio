# Test Cases — Login | SauceDemo

| ID     | Título                                     | Precondición | Pasos                                         | Resultado Esperado                                  | Resultado Obtenido | Estado |
|--------|--------------------------------------------|--------------|-----------------------------------------------|-----------------------------------------------------|--------------------|--------|
| TC-001 | Login exitoso con usuario estándar         | App abierta  | 1. Ingresar "standard_user" en usuario 
                                                                       2. Ingresar "secret_sauce" en contraseña 
                                                                       3. Click en "Login"                           | Redirige a /inventory.html                          |                   | |
| TC-002 | Login con usuario bloqueado                | App abierta  | 1. Ingresar "locked_out_user" 
                                                                       2. Ingresar "secret_sauce" 
                                                                       3. Click en "Login"                           | Muestra error: "Epic sadface: Sorry, this user 
                                                                                                                      has been locked out."                                |                   | |
| TC-003 | Login con contraseña incorrecta            | App abierta  | 1. Ingresar "standard_user" 
                                                                       2. Ingresar "wrongpass" 
                                                                       3. Click en "Login"                           | Muestra error de credenciales inválidas             |                   | |
| TC-004 | Login con campos vacíos                    | App abierta  | 1. No ingresar nada 
                                                                       2. Click en "Login"                           | Muestra error indicando que usuario es requerido    |                   | |
| TC-005 | Login solo con usuario, sin contraseña     | App abierta  | 1. Ingresar "standard_user" 
                                                                       2. Dejar contraseña vacía 
                                                                       3. Click en "Login"                           | Muestra error indicando que contraseña es requerida |                    | |
| TC-006 | Login con performance_glitch_user          | App abierta  | 1. Ingresar "performance_glitch_user" 
                                                                       2. Ingresar "secret_sauce" 
                                                                       3. Click en "Login"                           | Login exitoso pero con demora notable               |                     | |
| TC-007 | Login con caracteres especiales en usuario | App abierta  | 1. Ingresar "!@#$%^&*()" en usuario 
                                                                       2. Ingresar "secret_sauce" 
                                                                       3. Click en "Login"                           | Muestra error de credenciales inválidas             |                     | |

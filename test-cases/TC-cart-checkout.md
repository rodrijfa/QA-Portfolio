# Test Cases — Cart & Checkout | SauceDemo

## Módulo: Carrito

| ID | Título | Precondición | Pasos | Resultado Esperado | Resultado Obtenido | Estado |
|----|--------|--------------|-------|-------------------|-------------------|--------|
| TC-009 | Agregar producto al carrito desde inventario | Login con standard_user | 1. Click en "Add to cart" de cualquier producto | Producto agregado, contador del carrito muestra 1 | | |
| TC-010 | Agregar todos los productos al carrito | Login con standard_user | 1. Click en "Add to cart" de los 6 productos | Contador muestra 6, todos los productos en carrito | | |
| TC-011 | Eliminar producto desde inventario | Login con standard_user | 1. Agregar producto 2. Click en "Remove" desde inventario | Producto eliminado, contador se actualiza | | |
| TC-012 | Eliminar producto desde página individual | Login con standard_user | 1. Agregar producto 2. Entrar a página del producto 3. Click en "Remove" | Producto eliminado, contador se actualiza | | |
| TC-013 | Eliminar producto desde carrito | Login con standard_user | 1. Agregar producto 2. Ir al carrito 3. Click en "Remove" | Producto eliminado del carrito | | |
| TC-014 | Agregar producto al carrito desde inventario con error_user | Login con error_user | 1. Intentar click en "Add to cart" de los 6 productos | Todos los productos se agregan correctamente | | |
| TC-015 | Eliminar producto desde inventario con error_user | Login con error_user | 1. Agregar producto 2. Click en "Remove" desde inventario | Producto eliminado, contador se actualiza | | |
| TC-016 | Eliminar producto desde página individual con error_user | Login con error_user | 1. Agregar producto 2. Entrar a página del producto 3. Click en "Remove" | Producto eliminado, contador se actualiza | | |

## Módulo: Checkout

| ID | Título | Precondición | Pasos | Resultado Esperado | Resultado Obtenido | Estado |
|----|--------|--------------|-------|-------------------|-------------------|--------|
| TC-017 | Checkout completo con standard_user | Login con standard_user, al menos 1 producto en carrito | 1. Ir al carrito 2. Click "Checkout" 3. Completar First Name, Last Name, Postal Code 4. Click "Continue" 5. Click "Finish" | Compra finalizada correctamente | | |
| TC-018 | Checkout con campos vacíos | Login con standard_user, al menos 1 producto en carrito | 1. Ir al carrito 2. Click "Checkout" 3. No completar ningún campo 4. Click "Continue" | Muestra error indicando campos requeridos | | |
| TC-019 | Checkout con postal code no numérico | Login con standard_user, al menos 1 producto en carrito | 1. Completar First Name y Last Name 2. Ingresar texto en Postal Code 3. Click "Continue" | Muestra error indicando que Postal Code debe ser numérico | | |
| TC-020 | Checkout completo con error_user | Login con error_user, productos en carrito | 1. Ir al carrito 2. Click "Checkout" 3. Intentar completar los 3 campos 4. Click "Continue" 5. Click "Finish" | Compra finalizada correctamente | | |
| TC-021 | Campo Last Name con error_user | Login con error_user | 1. Ir a checkout 2. Intentar escribir en campo Last Name | Campo acepta input correctamente | | |

# Test Cases — Cart & Checkout | SauceDemo

## Módulo: Carrito

| ID | Título | Precondición | Pasos | Resultado Esperado | Resultado Obtenido | Estado |
|----|--------|--------------|-------|-------------------|-------------------|--------|
| TC-009 | Agregar producto al carrito desde inventario | Login con standard_user | 1. Click en "Add to cart" de cualquier producto | Producto agregado, contador del carrito muestra 1 | Producto agregado correctamente, contador del carrito muestra 1 | Pass |
| TC-010 | Agregar todos los productos al carrito | Login con standard_user | 1. Click en "Add to cart" de los 6 productos | Contador muestra 6, todos los productos en carrito | Todos los productos agregados al carrito, contador muestra 6 | Pass |
| TC-011 | Eliminar producto desde inventario | Login con standard_user | 1. Agregar producto 2. Click en "Remove" desde inventario | Producto eliminado, contador se actualiza | Producto(s) eliminado(s), contador se actualiza | Pass |
| TC-012 | Eliminar producto desde página individual | Login con standard_user | 1. Agregar producto 2. Entrar a página del producto 3. Click en "Remove" | Producto eliminado, contador se actualiza |Producto eliminado correctamente, contador actualizado correctamente | Pass |
| TC-013 | Eliminar producto desde carrito | Login con standard_user | 1. Agregar producto 2. Ir al carrito 3. Click en "Remove" | Producto eliminado del carrito |Producto(s) eliminado(s) correctamente del carrito | Pass |
| TC-014 | Agregar producto al carrito desde inventario con error_user | Login con error_user | 1. Intentar click en "Add to cart" de los 6 productos | Todos los productos se agregan correctamente | Solo se pueden agregar los ítems 1, 2 y 5. Los ítems 3, 4 y 6 no responden al click en "Add to cart" | FAIL |
| TC-015 | Eliminar producto desde inventario con error_user | Login con error_user | 1. Agregar producto 2. Click en "Remove" desde inventario | Producto eliminado, contador se actualiza | Producto(s) no se eliminan desde el inventario | Fail |
| TC-016 | Eliminar producto desde página individual con error_user | Login con error_user | 1. Agregar producto 2. Entrar a página del producto 3. Click en "Remove" | Producto eliminado, contador se actualiza | Producto no se elimina, contador no se actualiza | FAIL |

## Módulo: Checkout

| ID | Título | Precondición | Pasos | Resultado Esperado | Resultado Obtenido | Estado |
|----|--------|--------------|-------|-------------------|-------------------|--------|
| TC-017 | Checkout completo con standard_user | Login con standard_user, al menos 1 producto en carrito | 1. Ir al carrito 2. Click "Checkout" 3. Completar First Name, Last Name, Postal Code 4. Click "Continue" 5. Click "Finish" | Compra finalizada correctamente | Compra finalizada correctamente, independientemente del numero de productos. | Pass |
| TC-018 | Checkout con campos vacíos | Login con standard_user, al menos 1 producto en carrito | 1. Ir al carrito 2. Click "Checkout" 3. No completar ningún campo 4. Click "Continue" | Muestra error indicando campos requeridos | Muestra error: "Error: First Name is required" | Pass |
| TC-019 | Checkout con postal code no numérico | Login con standard_user, al menos 1 producto en carrito | 1. Completar First Name y Last Name 2. Ingresar texto en Postal Code 3. Click "Continue" | Muestra error indicando que Postal Code debe ser numérico | Compra completada exitosamente | FAIL |
| TC-020 | Checkout completo con error_user | Login con error_user, productos en carrito | 1. Ir al carrito 2. Click "Checkout" 3. Intentar completar los 3 campos 4. Click "Continue" 5. Click "Finish" | Compra finalizada correctamente | No permite finalizar la compra. Boton "Finish" sin respuesta | FAIL |
| TC-021 | Campo Last Name con error_user | Login con error_user | 1. Ir a checkout 2. Intentar escribir en campo Last Name | Campo acepta input correctamente | No se permite introducir ningún valor en Last Name, pero se acepta y avanza con los campos así. No se puede finalizar la compra | FAIL |

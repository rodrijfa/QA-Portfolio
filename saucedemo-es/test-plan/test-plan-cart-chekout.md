# Test Plan — Cart & Checkout Module | SauceDemo

## 1. Objetivo
Validar el comportamiento del módulo de carrito y checkout de SauceDemo,
verificando el flujo completo de compra bajo distintos usuarios y escenarios,
incluyendo casos positivos, negativos y usuarios con comportamiento especial.

## 2. Alcance
**Incluye:**
- Agregar productos al carrito desde inventario y página individual de cada producto
- Eliminar productos desde inventario, página individual del producto y carrito
- Contador del carrito
- Formulario de checkout (validaciones de campos)
- Flujo completo de compra hasta finalización

**Excluye:**
- Módulo de login (cubierto en test-plan-login.md)
- Ordenamiento y filtrado de productos

## 3. App bajo prueba
- **URL:** https://www.saucedemo.com
- **Usuarios utilizados:**
  - standard_user / secret_sauce (referencia de comportamiento correcto)
  - error_user / secret_sauce (usuario con comportamiento especial)

## 4. Criterios de entrada
- Login exitoso con el usuario correspondiente
- App disponible y accesible

## 5. Criterios de salida
- Todos los casos de prueba fueron ejecutados
- Los bugs encontrados fueron reportados con evidencia

## 6. Tipos de prueba
- Pruebas funcionales manuales
- Pruebas exploratorias con usuario especial

## 7. Entorno
- Navegador: Edge
- SO: Windows 10

## 8. Riesgos identificados
- El comportamiento de error_user es inestable e impredecible,
  por lo que pueden existir bugs adicionales no cubiertos en este plan

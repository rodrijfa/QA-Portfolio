# Test Plan — Login Module | SauceDemo

## 1. Objetivo
Validar el comportamiento del módulo de login de SauceDemo bajo distintos escenarios de autenticación, incluyendo casos positivos, negativos y usuarios con comportamiento especial.

## 2. Alcance
**Incluye:**
- Formulario de login (usuario, contraseña, botón de acceso)
- Mensajes de error
- Redirección exitosa al inventario
- Comportamiento con usuarios especiales

**Excluye:**
- Módulos de carrito, checkout, inventario (se cubren en otro plan)

## 3. App bajo prueba
- **URL:** https://www.saucedemo.com
- **Usuarios de prueba disponibles:**
  - standard_user / secret_sauce
  - locked_out_user / secret_sauce
  - problem_user / secret_sauce
  - performance_glitch_user / secret_sauce
  - visual_user/ secret_sauce

## 4. Criterios de entrada
- La app está disponible y accesible
- Se conocen los datos de prueba

## 5. Criterios de salida
- Todos los casos de prueba fueron ejecutados
- Los bugs encontrados fueron reportados

## 6. Tipos de prueba
- Pruebas funcionales manuales

## 7. Entorno
- Navegador: Edge (última versión)
- SO: Windows 10

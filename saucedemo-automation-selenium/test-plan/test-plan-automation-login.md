# Test Plan — Login Automation | SauceDemo

## 1. Objetivo

Validar de manera automatizada el comportamiento del módulo de Login y verificar defectos visuales en el inventario.

---

## 2. Alcance

Incluye:

- Validación de autenticación
- Validación de mensajes de error
- Medición básica de tiempo de respuesta
- Validación visual de imágenes
- Generación automática de evidencia en fallos

Excluye:

- Carrito
- Checkout
- Pruebas de integración

---

## 3. Tipo de pruebas

- Pruebas funcionales automatizadas
- Validación visual básica
- Medición simple de rendimiento

---

## 4. Entorno

| Campo | Detalle |
|-------|---------|
| Navegador | Chrome |
| Driver | ChromeDriver |
| Lenguaje | Python |
| Librería | Selenium |
| SO | Windows 10 |

---

## 5. Criterios de entrada

- Chrome instalado
- ChromeDriver compatible
- Python configurado
- Dependencias instaladas

---

## 6. Criterios de salida

- Todos los tests ejecutados
- Resumen PASS/FAIL generado
- Reporte HTML generado
- Screenshots capturados en fallos

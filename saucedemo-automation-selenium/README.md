  # QA Automation Portfolio — SauceDemo

Automatización de pruebas funcionales sobre la aplicación SauceDemo  
https://www.saucedemo.com

Este proyecto complementa el testing manual previamente documentado, incorporando automatización con Selenium y Python.

---

## 🎯 Objetivo

Automatizar escenarios críticos del módulo de Login y validaciones visuales del inventario para:

- Validar autenticación
- Detectar errores funcionales
- Verificar tiempos de respuesta
- Identificar defectos visuales
- Generar evidencia automática en caso de fallo

---

## 🧪 Alcance

Se automatizaron 8 casos de prueba correspondientes al módulo de Login:

| ID | Descripción | Tipo |
|----|------------|------|
| TC-001 | Login exitoso | Positivo |
| TC-002 | Usuario bloqueado | Negativo |
| TC-003 | Contraseña incorrecta | Negativo |
| TC-004 | Campos vacíos | Validación |
| TC-005 | Usuario sin contraseña | Validación |
| TC-006 | Usuario con glitch de performance | Performance básica |
| TC-007 | Caracteres especiales | Validación |
| TC-008 | Validación visual de imágenes | Visual / Defecto |

---

## 🛠️ Tecnologías utilizadas

- Python
- Selenium WebDriver
- ChromeDriver
- WebDriverWait (esperas explícitas)
- Manejo de excepciones controladas
- Generación de reporte HTML
- Captura automática de screenshots

---

## 📂 Estructura del proyecto

- `src/` — Código fuente de automatización
- `test-plan/` — Plan de pruebas automatizadas
- `test-cases/` — Casos automatizados documentados
- `test-reports/` — Reportes HTML generados
- `screenshots/` — Evidencia automática en fallos

---

## 🐞 Defecto detectado automáticamente

Durante la automatización se validó el defecto documentado en el testing manual:

Usuario `visual_user` muestra imagen incorrecta para el producto *Sauce Labs Backpack*.

El sistema genera screenshot automático cuando el test falla.

---

## 👨‍💻 Autor

Rodrigo Flores Agreda  
LinkedIn | GitHub: rodrijfa

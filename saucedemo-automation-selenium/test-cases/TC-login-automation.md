# Test Cases — Login Automation | SauceDemo

| ID | Título | Tipo | Validación automatizada | Resultado esperado |
|----|--------|------|------------------------|-------------------|
| TC-001 | Login exitoso | Positivo | Verificación de URL contiene /inventory.html | Redirección correcta |
| TC-002 | Usuario bloqueado | Negativo | Validación de mensaje de error exacto | Mensaje correcto mostrado |
| TC-003 | Contraseña incorrecta | Negativo | Validación de mensaje parcial | Error mostrado |
| TC-004 | Campos vacíos | Validación | Validación de error requerido | Error mostrado |
| TC-005 | Usuario sin contraseña | Validación | Validación de error requerido | Error mostrado |
| TC-006 | Performance glitch user | Performance | Medición de tiempo < 6 segundos | Login dentro del umbral |
| TC-007 | Caracteres especiales | Negativo | Validación de error credenciales inválidas | Error mostrado |
| TC-008 | Validación visual Backpack | Visual | Comparación de atributo src de imagen | Imagen correcta |

---

## Evidencia automática

Cuando TC-008 falla, el sistema:

- Guarda screenshot en `/screenshots`
- Muestra ubicación en consola
- Registra FAIL en resumen final

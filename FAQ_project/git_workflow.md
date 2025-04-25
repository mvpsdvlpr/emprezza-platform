
# 🧠 Git Workflow - Emprezza One

Este documento describe el flujo de trabajo en Git que se usará en el proyecto **Emprezza One**, siguiendo buenas prácticas y una estructura profesional basada en GitHub Flow.

---

## 📂 Estructura de Ramas

- `main` → código estable (producción o versión lista para entrega).
- `dev` → rama de integración y pruebas (última versión funcional).
- `feat/*` → desarrollo de nuevas funcionalidades.
- `fix/*` → correcciones de errores o bugs.
- `test/*` → pruebas o experimentación.
- `ref/*` → refactorizaciones (limpieza/mejora de código).

---

## 🔄 Flujo de trabajo recomendado

1. **Crea una nueva rama a partir de `dev`**
   ```bash
   git checkout dev
   git pull origin dev
   git checkout -b feat/nombre-funcionalidad
   ```

2. **Desarrolla tu funcionalidad**
   - Haz commits pequeños, claros y enfocados:
     ```
     feat(user): add registration endpoint
     fix(auth): handle invalid token error
     ```

3. **Haz push de la rama**
   ```bash
   git push origin feat/nombre-funcionalidad
   ```

4. **Abre un Pull Request (PR) contra `dev`**
   - Explica qué hiciste y por qué.
   - Asegúrate de revisar tus cambios antes de hacer merge.

5. **Una vez validado, mergea a `dev`**
   ```bash
   git checkout dev
   git pull origin dev
   git merge feat/nombre-funcionalidad
   git push origin dev
   ```

6. **Cuando se desea liberar una versión estable, mergea `dev` a `main`**
   ```bash
   git checkout main
   git pull origin main
   git merge dev
   git tag v1.0.0
   git push origin main --tags
   ```

---

## 🏷️ Convenciones de Nombres de Ramas

| Tipo de Rama    | Prefijo | Ejemplo                      |
|-----------------|---------|------------------------------|
| Nueva funcionalidad | `feat/` | `feat/login-form`         |
| Corrección de bug   | `fix/`  | `fix/token-expiry`        |
| Pruebas o ideas     | `test/` | `test/checkout-variant`   |
| Refactorización     | `ref/`  | `ref/user-model`          |

---

## 🧪 Buenas Prácticas

- Usar `.gitignore` para excluir archivos sensibles y temporales.
- Nunca hacer commits en `main` directamente.
- Revisar los cambios (diff) antes de hacer `merge`.
- Mantener `main` **siempre funcional**.

---

¡Este flujo te ayudará a mantener el código organizado, limpio y fácil de trabajar en equipo o escalar!

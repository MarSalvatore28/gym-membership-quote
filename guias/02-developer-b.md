# Guía de Samuel · Developer B (R4, R5 y R6)

Hola Samuel 👋 Tu parte del proyecto son los **descuentos y el recargo**: el descuento por grupo,
la oferta especial y el recargo premium. Tus funciones reciben un monto y devuelven otro monto,
así que **no dependes de nadie** y puedes empezar ya.

## Antes de empezar: 4 palabras que vas a ver

| Palabra | Qué significa en este taller |
|---|---|
| **Repositorio (repo)** | La carpeta del proyecto en GitHub, compartida por los 4. |
| **Rama (branch)** | Tu copia personal del proyecto. Trabajas ahí sin tocar lo de los demás. La rama principal se llama `main`. |
| **Commit** | Guardar un cambio, con un mensaje que dice qué hiciste. Cada commit queda con **tu nombre**, y esa es tu evidencia. |
| **Pull Request (PR)** | Pedirle al equipo que tu rama se una a `main`. Ahí GitHub corre los tests solo, y sale ✅ o ❌. |

**Lo que vas a hacer:** crear tu rama → subir 2 archivos (2 commits) → abrir 1 Pull Request → tomar capturas.
No necesitas instalar nada: todo es en el navegador. Tiempo aproximado: 20 minutos.

---

## Paso 0 · Entrar a GitHub

1. Abre el navegador. **En una compu de la U, usa una ventana de incógnito** (Ctrl + Shift + N)
   para que al final no quede tu cuenta abierta.
2. Entra a https://github.com/login con tu cuenta **SamuelChichande**.
3. Abre el repositorio: **https://github.com/MarSalvatore28/gym-membership-quote**
4. Arriba a la derecha debe verse **tu foto o tu inicial**. Así se nota en las capturas que eres tú.

---

## Paso 1 · Crear tu rama

1. En la página del repo, arriba a la izquierda de la lista de archivos, hay un botón que dice **`main`**
   con un ícono de rama. Haz clic.
2. En la cajita **"Find or create a branch..."** escribe exactamente:

   ```
   feature/developer-b
   ```

3. Abajo aparece **"Create branch feature/developer-b from main"**. Haz clic.
4. ✅ Revisa que el botón ahora diga **`feature/developer-b`**. **Si dice `main`, no sigas:** vuelve a elegir tu rama.

📸 **Captura 1:** la página del repo con el botón mostrando `feature/developer-b` y tu foto arriba a la derecha.
Guárdala como `samuel-1-rama.png`.

> Para tomar capturas en Windows: **Windows + Shift + S**, seleccionas el área y se copia.
> Pégala en Paint o Word y guárdala.

---

## ⚠️ Cómo copiar el código sin errores

En Python, **los espacios al inicio de cada línea importan**. Si se mueve un espacio, el código falla.

- **No copies seleccionando con el mouse.** En cada bloque de código de esta guía (abierta en GitHub),
  pasa el mouse por encima del bloque y aparece un botón **📋 (Copy)** arriba a la derecha. Usa ese.
- Pega con **Ctrl + V** en el editor de GitHub y **no cambies nada**.

---

## Paso 2 · Subir tu código (commit 1)

1. Confirma que el botón de rama dice **`feature/developer-b`**.
2. Clic en el botón **Add file** (arriba, junto al botón verde **Code**) → **Create new file**.
3. En la cajita **"Name your file..."** escribe exactamente:

   ```
   adjustments.py
   ```

4. Haz clic en el área grande de abajo (el editor) y pega este código con el botón 📋:

```python
"""Discounts and surcharge applied to an amount (R4, R5, R6)."""

GROUP_DISCOUNT_RATE = 0.10
PREMIUM_SURCHARGE_RATE = 0.15


def apply_group_discount(amount, members):
    """R4: with 2 or more members the amount gets a 10% discount."""
    if members >= 2:
        return amount * (1 - GROUP_DISCOUNT_RATE)
    return amount


def apply_special_offer(amount):
    """R5: subtract 50 if the amount is over 400, otherwise 20 if it is over 200."""
    if amount > 400:
        return amount - 50
    if amount > 200:
        return amount - 20
    return amount


def apply_premium_surcharge(amount, has_premium):
    """R6: add 15% if the selection includes a premium extra."""
    if has_premium:
        return amount * (1 + PREMIUM_SURCHARGE_RATE)
    return amount
```

5. Clic en el botón verde **Commit changes...** (arriba a la derecha).
6. Se abre una ventanita:
   - En **Commit message** borra lo que haya y escribe:

     ```
     Add group discount, special offer and premium surcharge (R4, R5, R6)
     ```

   - Abajo debe estar marcada la opción **"Commit directly to the `feature/developer-b` branch"**.
     Si dice `main`, **cancela** y vuelve al Paso 1.
   - Clic en **Commit changes**.

📸 **Captura 2:** el archivo `adjustments.py` ya subido (se ve su código y arriba tu rama).
Guárdala como `samuel-2-codigo.png`.

---

## Paso 3 · Subir tus tests (commit 2)

Los tests comprueban que tu código calcula bien. GitHub y Jenkins los corren solos.

1. Vuelve a la página principal del repo (clic en **gym-membership-quote** arriba). Revisa que siga en **`feature/developer-b`**.
2. **Add file → Create new file**.
3. Nombre del archivo:

   ```
   test_adjustments.py
   ```

4. Pega con el botón 📋:

```python
"""Unit tests for R4, R5 and R6 (Developer B)."""
import pytest

from adjustments import (
    apply_group_discount,
    apply_premium_surcharge,
    apply_special_offer,
)


def test_r4_no_discount_for_one_member():
    """R4: one member pays the full amount."""
    assert apply_group_discount(100, 1) == 100


def test_r4_ten_percent_for_two_or_more():
    """R4: 2 or more members get 10% off."""
    assert apply_group_discount(100, 2) == pytest.approx(90)
    assert apply_group_discount(340, 4) == pytest.approx(306)


def test_r5_over_400_subtracts_50():
    """R5: more than 400 subtracts 50."""
    assert apply_special_offer(594) == 544


def test_r5_over_200_subtracts_20():
    """R5: more than 200 and up to 400 subtracts 20."""
    assert apply_special_offer(306) == 286
    assert apply_special_offer(400) == 380


def test_r5_200_or_less_has_no_offer():
    """R5: 200 or less keeps the amount; the two offers never add up."""
    assert apply_special_offer(200) == 200
    assert apply_special_offer(81) == 81


def test_r6_premium_surcharge():
    """R6: a premium extra adds 15%."""
    assert apply_premium_surcharge(100, True) == pytest.approx(115)
    assert apply_premium_surcharge(100, False) == 100
```

5. **Commit changes...** → mensaje:

   ```
   Add unit tests for R4, R5 and R6
   ```

   → que esté marcada **"Commit directly to the `feature/developer-b` branch"** → **Commit changes**.

📸 **Captura 3:** tus commits. En la página del repo, con tu rama seleccionada, haz clic en el reloj
**"X Commits"** (a la derecha, encima de la lista de archivos). Deben aparecer tus 2 commits con tu nombre.
Guárdala como `samuel-3-commits.png`.

---

## Paso 4 · Abrir tu Pull Request

1. Ve a la pestaña **Pull requests** (arriba) → botón verde **New pull request**.
   (Si ves un aviso amarillo **"feature/developer-b had recent pushes"** con el botón **Compare & pull request**, puedes usar ese.)
2. Deja **base: `main`** y en **compare** elige **`feature/developer-b`**.
3. Debe decir **"Able to merge"** en verde. Clic en **Create pull request**.
4. Llena:
   - **Title:**

     ```
     Add group discount, special offer and premium surcharge (R4, R5, R6)
     ```

   - **Description** (escríbelo con tus palabras, por ejemplo):
     > Agrego el descuento grupal, la oferta especial y el recargo premium, con sus tests.
5. Clic en **Create pull request**.

---

## Paso 5 · Esperar el check de GitHub Actions

1. Abajo en tu PR aparece **CI / lint-and-test** con un círculo amarillo 🟡 (corriendo). Espera 1 o 2 minutos.
2. Cuando termine:
   - ✅ **"All checks have passed"**: listo.
   - ❌ **"Some checks were not successful"**: mira la sección **"Si sale ❌ rojo"** más abajo.

📸 **Captura 4:** tu PR con **All checks have passed** y tu nombre visible.
Guárdala como `samuel-4-pr-verde.png`.

3. Avísale a **Gabriela** por el grupo: *"Ya está mi PR, revísalo porfa"*.
   **No hagas tú el Merge.** Gabriela lo aprueba y lo une cuando Jenkins esté libre.
4. Cuando Gabriela lo una, tu PR se pone **morado** y dice **Merged**.

📸 **Captura 5:** tu PR en morado con **Merged**. Guárdala como `samuel-5-merged.png`.

Al final, **cierra sesión en GitHub** si estás en una compu de la U.

---

## Si sale ❌ rojo

1. En el PR, al lado del check rojo, haz clic en **Details**.
2. Lee el error:
   - Si dice **`IndentationError`** o **`SyntaxError`**, se movió un espacio al pegar.
   - Si dice **pylint** con un número de línea, hay algo distinto en esa línea.
3. Para arreglarlo: pestaña **Code** → tu rama → abre el archivo → ícono del **lápiz ✏️** (Edit) →
   borra todo (**Ctrl + A**, luego **Supr**) → pega otra vez con el botón 📋 →
   **Commit changes...** con el mensaje `Fix indentation` → a tu rama.
4. El check vuelve a correr solo. Si sigue en rojo, toma captura del error y pásala al grupo.

---

## Qué hace tu código (léelo, la profe puede preguntarte)

- **R4, `apply_group_discount`:** si hay 2 miembros o más, el monto se multiplica por 0.90 (10% menos).
  Con 1 miembro se queda igual. Ejemplo: 340 con 4 miembros → **306**.
- **R5, `apply_special_offer`:** se aplica al monto después de R4. Si es **mayor a 400**, resta 50;
  si no, y es **mayor a 200**, resta 20. Nunca se restan las dos. Ejemplo: 306 → **286**; 594 → **544**.
  Ojo: 400 exacto **no** es mayor a 400, así que resta 20 (da 380).
- **R6, `apply_premium_surcharge`:** si la selección tiene un extra premium, multiplica por 1.15 (15% más)
  el monto después de R5. Ejemplo: 100 → **115**.
- Los porcentajes están en constantes (`GROUP_DISCOUNT_RATE`, `PREMIUM_SURCHARGE_RATE`) para no tener
  "números mágicos" sueltos en el código.
- **Tests:** cada función `test_...` prueba un requisito. Se usa `pytest.approx` porque al multiplicar
  decimales la compu puede dar `89.99999999` en vez de `90`, y `approx` acepta esa diferencia mínima.

---

## Resumen: tus 5 capturas

| # | Archivo | Qué se ve |
|---|---|---|
| 1 | `samuel-1-rama.png` | Tu rama creada |
| 2 | `samuel-2-codigo.png` | `adjustments.py` subido |
| 3 | `samuel-3-commits.png` | Tus 2 commits con tu nombre |
| 4 | `samuel-4-pr-verde.png` | PR con ✅ All checks have passed |
| 5 | `samuel-5-merged.png` | PR morado, Merged |

Mándalas al grupo cuando termines. En **todas** se tiene que ver tu usuario
(si no se ve, escribe tu nombre encima en Paint antes de mandarla).

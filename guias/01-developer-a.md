# Guía de Kiara · Developer A (R1, R2, R3 y R7)

Hola Kiara 👋 Tu parte del proyecto es el **catálogo** del gimnasio (planes y extras con sus precios),
**validar** que lo que elige el usuario sea correcto, calcular el **subtotal** y **redondear** el total.

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
2. Entra a https://github.com/login con tu cuenta **Kcmoranj**.
3. Abre el repositorio: **https://github.com/MarSalvatore28/gym-membership-quote**
4. Arriba a la derecha debe verse **tu foto o tu inicial**. Así se nota en las capturas que eres tú.

---

## Paso 1 · Crear tu rama

1. En la página del repo, arriba a la izquierda de la lista de archivos, hay un botón que dice **`main`**
   con un ícono de rama. Haz clic.
2. En la cajita **"Find or create a branch..."** escribe exactamente:

   ```
   feature/developer-a
   ```

3. Abajo aparece **"Create branch feature/developer-a from main"**. Haz clic.
4. ✅ Revisa que el botón ahora diga **`feature/developer-a`**. **Si dice `main`, no sigas:** vuelve a elegir tu rama.

📸 **Captura 1:** la página del repo con el botón mostrando `feature/developer-a` y tu foto arriba a la derecha.
Guárdala como `kiara-1-rama.png`.

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

1. Confirma que el botón de rama dice **`feature/developer-a`**.
2. Clic en el botón **Add file** (arriba, junto al botón verde **Code**) → **Create new file**.
3. En la cajita **"Name your file..."** escribe exactamente:

   ```
   catalog.py
   ```

4. Haz clic en el área grande de abajo (el editor) y pega este código con el botón 📋:

```python
"""Catalog of plans and extras, validation, subtotal and rounding (R1, R2, R3, R7)."""
from decimal import ROUND_HALF_UP, Decimal

PLANS = {"BASIC": 30, "STANDARD": 45, "PREMIUM": 70}
EXTRAS = {
    "GROUP_CLASSES": 15,
    "PERSONAL_TRAINING": 25,
    "SPA": 30,
    "SPECIALIZED_PROGRAM": 40,
}
PREMIUM_EXTRAS = {"SPA", "SPECIALIZED_PROGRAM"}


def is_valid_selection(plan, extras, members):
    """R1, R2, R3: return True if the plan, extras and members can be quoted."""
    if plan not in PLANS:
        return False
    if isinstance(members, bool) or not isinstance(members, int) or members < 1:
        return False
    if len(set(extras)) != len(extras):
        return False
    for extra in extras:
        if extra not in EXTRAS:
            return False
        if extra in PREMIUM_EXTRAS and plan != "PREMIUM":
            return False
    return True


def subtotal(plan, extras, members):
    """R3: (plan price + price of the extras) x number of members."""
    return (PLANS[plan] + sum(EXTRAS[extra] for extra in extras)) * members


def round_half_up(amount):
    """R7: round half up to a whole number (2.5 -> 3, while round() gives 2)."""
    exact = Decimal(str(round(amount, 6)))
    return int(exact.quantize(Decimal("1"), rounding=ROUND_HALF_UP))
```

5. Clic en el botón verde **Commit changes...** (arriba a la derecha).
6. Se abre una ventanita:
   - En **Commit message** borra lo que haya y escribe:

     ```
     Add plan and extras catalog with validation (R1, R2, R3, R7)
     ```

   - Abajo debe estar marcada la opción **"Commit directly to the `feature/developer-a` branch"**.
     Si dice `main`, **cancela** y vuelve al Paso 1.
   - Clic en **Commit changes**.

📸 **Captura 2:** el archivo `catalog.py` ya subido (se ve su código y arriba tu rama).
Guárdala como `kiara-2-codigo.png`.

---

## Paso 3 · Subir tus tests (commit 2)

Los tests comprueban que tu código calcula bien. GitHub y Jenkins los corren solos.

1. Vuelve a la página principal del repo (clic en **gym-membership-quote** arriba). Revisa que siga en **`feature/developer-a`**.
2. **Add file → Create new file**.
3. Nombre del archivo:

   ```
   test_catalog.py
   ```

4. Pega con el botón 📋:

```python
"""Unit tests for R1, R2, R3 and R7 (Developer A)."""
from catalog import is_valid_selection, round_half_up, subtotal


def test_r1_known_plans_are_valid():
    """R1: every plan in the table is valid."""
    for plan in ("BASIC", "STANDARD", "PREMIUM"):
        assert is_valid_selection(plan, [], 1)


def test_r1_unknown_plan_is_invalid():
    """R1: a plan that is not in the table is invalid."""
    assert not is_valid_selection("GOLD", [], 1)


def test_r2_unknown_extra_is_invalid():
    """R2: an extra that is not in the table is invalid."""
    assert not is_valid_selection("BASIC", ["SAUNA"], 1)


def test_r2_premium_extra_needs_premium_plan():
    """R2: a premium extra is only allowed with the PREMIUM plan."""
    assert not is_valid_selection("BASIC", ["SPA"], 1)
    assert not is_valid_selection("STANDARD", ["SPECIALIZED_PROGRAM"], 1)
    assert is_valid_selection("PREMIUM", ["SPA", "SPECIALIZED_PROGRAM"], 1)


def test_r3_subtotal():
    """R3: (plan price + extras) x members."""
    assert subtotal("BASIC", [], 1) == 30
    assert subtotal("STANDARD", ["GROUP_CLASSES", "PERSONAL_TRAINING"], 4) == 340


def test_r3_members_at_least_one():
    """R3: the number of members is at least 1."""
    assert not is_valid_selection("BASIC", [], 0)
    assert not is_valid_selection("BASIC", [], -2)


def test_r7_round_half_up():
    """R7: .5 always rounds up."""
    assert round_half_up(2.5) == 3
    assert round_half_up(411.7) == 412
    assert round_half_up(81.0) == 81
    assert round_half_up(80.4) == 80
```

5. **Commit changes...** → mensaje:

   ```
   Add unit tests for R1, R2, R3 and R7
   ```

   → que esté marcada **"Commit directly to the `feature/developer-a` branch"** → **Commit changes**.

📸 **Captura 3:** tus commits. En la página del repo, con tu rama seleccionada, haz clic en el reloj
**"X Commits"** (a la derecha, encima de la lista de archivos). Deben aparecer tus 2 commits con tu nombre.
Guárdala como `kiara-3-commits.png`.

---

## Paso 4 · Abrir tu Pull Request

1. Ve a la pestaña **Pull requests** (arriba) → botón verde **New pull request**.
   (Si ves un aviso amarillo **"feature/developer-a had recent pushes"** con el botón **Compare & pull request**, puedes usar ese.)
2. Deja **base: `main`** y en **compare** elige **`feature/developer-a`**.
3. Debe decir **"Able to merge"** en verde. Clic en **Create pull request**.
4. Llena:
   - **Title:**

     ```
     Add catalog, validation, subtotal and rounding (R1, R2, R3, R7)
     ```

   - **Description** (escríbelo con tus palabras, por ejemplo):
     > Agrego el catálogo de planes y extras, la validación de la selección, el subtotal y el redondeo, con sus tests.
5. Clic en **Create pull request**.

---

## Paso 5 · Esperar el check de GitHub Actions

1. Abajo en tu PR aparece **CI / lint-and-test** con un círculo amarillo 🟡 (corriendo). Espera 1 o 2 minutos.
2. Cuando termine:
   - ✅ **"All checks have passed"**: listo.
   - ❌ **"Some checks were not successful"**: mira la sección **"Si sale ❌ rojo"** más abajo.

📸 **Captura 4:** tu PR con **All checks have passed** y tu nombre visible.
Guárdala como `kiara-4-pr-verde.png`.

3. Avísale a **Gabriela** por el grupo: *"Ya está mi PR, revísalo porfa"*.
   **No hagas tú el Merge.** Gabriela lo aprueba y lo une cuando Jenkins esté libre.
4. Cuando Gabriela lo una, tu PR se pone **morado** y dice **Merged**.

📸 **Captura 5:** tu PR en morado con **Merged**. Guárdala como `kiara-5-merged.png`.

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

- **`PLANS` y `EXTRAS`** son diccionarios con los precios de la tabla del PDF.
  `PREMIUM_EXTRAS` son los extras premium: `SPA` y `SPECIALIZED_PROGRAM`.
- **R1, `is_valid_selection`:** si el plan no está en `PLANS` (por ejemplo `GOLD`), devuelve `False`.
- **R2, también en `is_valid_selection`:** un extra que no está en `EXTRAS` es inválido, y un extra premium
  con un plan que no sea `PREMIUM` también es inválido (por ejemplo `BASIC` + `SPA`).
  Supuesto del equipo: un extra repetido (`SPA, SPA`) es inválido.
- **R3:** los miembros deben ser un número entero mayor o igual a 1.
  `subtotal` = (precio del plan + suma de los extras) × miembros.
  Ejemplo: STANDARD (45) + GROUP_CLASSES (15) + PERSONAL_TRAINING (25) = 85 × 4 = **340**.
- **R7, `round_half_up`:** redondea .5 hacia arriba. Se usa `Decimal` porque `round()` de Python
  redondea `2.5` a `2` (redondeo bancario), y el PDF pide "half up", que da `3`.
- **Tests:** cada función `test_...` prueba un requisito. `assert` significa "esto debe ser verdad":
  si no lo es, el test falla y sale ❌.

---

## Resumen: tus 5 capturas

| # | Archivo | Qué se ve |
|---|---|---|
| 1 | `kiara-1-rama.png` | Tu rama creada |
| 2 | `kiara-2-codigo.png` | `catalog.py` subido |
| 3 | `kiara-3-commits.png` | Tus 2 commits con tu nombre |
| 4 | `kiara-4-pr-verde.png` | PR con ✅ All checks have passed |
| 5 | `kiara-5-merged.png` | PR morado, Merged |

Mándalas al grupo cuando termines. En **todas** se tiene que ver tu usuario
(si no se ve, escribe tu nombre encima en Paint antes de mandarla).

# Guía de Gaby · Repository lead (revisión de PRs, R8 y GitHub Actions)

Hola Gaby 👋 Eres la **Repository lead**. Tu parte tiene 3 momentos:

1. **Revisar y unir** los Pull Requests de Kiara y Samuel (eres la que decide qué entra a `main`).
2. **Unir todo** en la calculadora final y hacer la **línea de comandos** del programa (R8).
3. **Romper un test a propósito** para mostrar GitHub Actions en ❌ rojo y luego en ✅ verde.

No necesitas usar Jenkins: eso lo maneja Marlo en su laptop. Todo lo tuyo es en el navegador.

## Antes de empezar: 4 palabras que vas a ver

| Palabra | Qué significa en este taller |
|---|---|
| **Repositorio (repo)** | La carpeta del proyecto en GitHub, compartida por los 4. |
| **Rama (branch)** | Una copia para trabajar sin tocar lo de los demás. La principal se llama `main`. |
| **Commit** | Guardar un cambio con un mensaje. Queda con **tu nombre**: es tu evidencia. |
| **Pull Request (PR)** | Pedir que una rama se una a `main`. GitHub corre los tests solo y sale ✅ o ❌. |
| **Merge** | Aceptar el PR: el código de la rama entra a `main`. Cada merge hace que **Jenkins** corra los tests. |

> 📸 Para capturas: **Windows + Shift + S**. Siempre con tu foto/usuario visible arriba a la derecha.

---

# Momento 1 · Revisar y unir los PRs de Kiara y Samuel

Abre el repo: **https://github.com/MarSalvatore28/gym-membership-quote** → pestaña **Pull requests**.

Haz esto **con un PR a la vez** (primero el que esté listo):

1. Abre el PR.
2. Baja hasta el final: el check **CI / lint-and-test** debe decir ✅ **All checks have passed**.
   Si está en ❌, no lo unas: avísale a quien lo hizo (su guía dice cómo arreglarlo).
3. Pestaña **Files changed** → mira el código → botón verde **Review changes** (arriba a la derecha) →
   escribe un comentario corto, por ejemplo `Revisé el código y los tests pasan, aprobado` →
   marca **Approve** → **Submit review**.

   📸 **Captura:** tu aprobación (sale "MGabrielaVillon approved these changes"). Guárdala como `gaby-1-aprobacion-kiara.png` (o `-samuel`).

4. **Pregúntale a Marlo:** *"¿Jenkins está libre?"*. Cuando diga que sí → vuelve a **Conversation** →
   **Merge pull request** → **Confirm merge**.

   📸 **Captura:** el PR morado con **Merged**. Guárdala como `gaby-2-merge-kiara.png` (o `-samuel`).

5. Espera a que Marlo te diga que el build de Jenkins terminó **antes de unir el siguiente PR**.

> ⚠️ Nunca unas dos PRs seguidos sin esperar a Jenkins (lo pide el PDF).

---

# Momento 2 · Tu código (cuando los PRs de Kiara y Samuel ya estén unidos)

Tu código usa los archivos de Kiara (`catalog.py`) y Samuel (`adjustments.py`), por eso va después.

## ⚠️ Cómo copiar el código sin errores

En Python **los espacios al inicio de cada línea importan**. Abre esta guía en GitHub y usa el botón **📋 (Copy)**
que aparece arriba a la derecha de cada bloque de código al pasar el mouse. No selecciones con el mouse.

## Paso 1 · Crear tu rama

1. En la página del repo, clic en el botón **`main`** (arriba a la izquierda de la lista de archivos).
2. Escribe exactamente:

   ```
   feature/repository-lead
   ```

3. Clic en **Create branch feature/repository-lead from main**.
4. ✅ El botón ahora debe decir **`feature/repository-lead`**. Si dice `main`, no sigas.

## Paso 2 · Editar `gym_quote.py` (commit 1)

Este archivo ya existe; lo vas a **reemplazar** por la versión que une el trabajo de Kiara y Samuel.

1. Con tu rama seleccionada, haz clic en el archivo **`gym_quote.py`** de la lista.
2. Clic en el ícono del **lápiz ✏️** (arriba a la derecha del código, "Edit this file").
3. Clic dentro del editor → **Ctrl + A** (selecciona todo) → **Supr** (borra todo).
4. Pega con el botón 📋:

```python
"""Gym Membership Quote: monthly cost of a gym membership."""
from adjustments import (
    apply_group_discount,
    apply_premium_surcharge,
    apply_special_offer,
)
from catalog import PREMIUM_EXTRAS, is_valid_selection, round_half_up, subtotal

INVALID = -1


class GymQuote:
    """Quote for one gym membership selection. It does no input or output."""

    def __init__(self, plan, extras, members):
        self.plan = plan
        self.extras = list(extras)
        self.members = members

    def breakdown(self):
        """Return each step of the calculation, or None if the selection is invalid."""
        if not is_valid_selection(self.plan, self.extras, self.members):
            return None
        amount = subtotal(self.plan, self.extras, self.members)
        after_group = apply_group_discount(amount, self.members)
        after_offer = apply_special_offer(after_group)
        has_premium = any(extra in PREMIUM_EXTRAS for extra in self.extras)
        after_surcharge = apply_premium_surcharge(after_offer, has_premium)
        return {
            "subtotal": amount,
            "group_discount": amount - after_group,
            "special_offer": after_group - after_offer,
            "premium_surcharge": after_surcharge - after_offer,
            "total": round_half_up(after_surcharge),
        }

    def total(self):
        """R7: return the rounded total, or -1 if the selection is invalid."""
        steps = self.breakdown()
        if steps is None:
            return INVALID
        return steps["total"]
```

5. **Commit changes...** → mensaje:

   ```
   Combine catalog and adjustments in GymQuote (R7)
   ```

   → marcada **"Commit directly to the `feature/repository-lead` branch"** → **Commit changes**.

## Paso 3 · Crear `cli.py` (commit 2)

1. Vuelve a la página principal del repo (clic en **gym-membership-quote**). Revisa que siga en tu rama.
2. **Add file → Create new file** → nombre:

   ```
   cli.py
   ```

3. Pega con 📋:

```python
"""Command-line interface for the Gym Membership Quote (R8)."""
from gym_quote import INVALID, GymQuote


def parse_extras(text):
    """Turn 'spa, group_classes' into ['SPA', 'GROUP_CLASSES']."""
    return [item.strip().upper() for item in text.split(",") if item.strip()]


def run(read=input, write=print):
    """Ask for the selection, show each step and return the total, or -1."""
    plan = read("Plan (BASIC, STANDARD, PREMIUM): ").strip().upper()
    extras = parse_extras(read("Extras separated by commas (empty for none): "))
    try:
        members = int(read("Number of members: "))
    except ValueError:
        write("Invalid selection")
        return INVALID
    steps = GymQuote(plan, extras, members).breakdown()
    if steps is None:
        write("Invalid selection")
        return INVALID
    write(f"Subtotal:           {steps['subtotal']:.2f}")
    write(f"Group discount:    -{steps['group_discount']:.2f}")
    write(f"Special offer:     -{steps['special_offer']:.2f}")
    write(f"Premium surcharge: +{steps['premium_surcharge']:.2f}")
    write(f"Total:              {steps['total']}")
    if read("Confirm (y/n): ").strip().lower() != "y":
        write("Cancelled")
        return INVALID
    return steps["total"]


if __name__ == "__main__":
    print(f"Result: {run()}")
```

4. **Commit changes...** → mensaje:

   ```
   Add command-line interface with confirmation (R8)
   ```

   → a tu rama → **Commit changes**.

## Paso 4 · Crear `test_cli.py` (commit 3)

1. **Add file → Create new file** → nombre:

   ```
   test_cli.py
   ```

2. Pega con 📋:

```python
"""Unit tests for R8, the command line."""
from cli import parse_extras, run


def fake_input(*answers):
    """Return a function that gives the answers one by one, like input()."""
    queue = list(answers)
    return lambda _prompt: queue.pop(0)


def test_r8_parse_extras():
    """R8: extras are typed separated by commas."""
    assert parse_extras(" spa, group_classes ") == ["SPA", "GROUP_CLASSES"]
    assert not parse_extras("")


def test_r8_confirm_yes_returns_total():
    """R8: answering y returns the total and shows each step."""
    shown = []
    assert run(fake_input("basic", "group_classes", "2", "y"), shown.append) == 81
    assert any("Group discount" in line for line in shown)


def test_r8_confirm_no_returns_minus_one():
    """R8: answering n cancels the quote."""
    assert run(fake_input("basic", "", "1", "n"), lambda _line: None) == -1


def test_r8_invalid_members_returns_minus_one():
    """R8: a number of members that is not a number is invalid."""
    assert run(fake_input("basic", "", "two"), lambda _line: None) == -1
```

3. **Commit changes...** → mensaje:

   ```
   Add unit tests for the command line (R8)
   ```

   → a tu rama → **Commit changes**.

📸 **Captura:** tus 3 commits (en la página del repo, con tu rama, clic en el reloj **"X Commits"**).
Guárdala como `gaby-3-commits.png`.

## Paso 5 · Tu Pull Request

1. **Pull requests → New pull request** → **base: `main`** ← **compare: `feature/repository-lead`** → **Create pull request**.
2. **Title:**

   ```
   Combine the quote and add the command line (R7, R8)
   ```

   **Description** (con tus palabras), por ejemplo:
   > Uno el catálogo y los descuentos en GymQuote y agrego la línea de comandos que pide plan, extras y miembros, muestra el detalle y pide confirmación.

3. **Create pull request** → espera el ✅ **All checks have passed**.

   📸 **Captura:** tu PR en verde. Guárdala como `gaby-4-pr-verde.png`.

4. Avísale a Marlo: él lo revisa, lo aprueba y lo une (tú no unes tu propio PR).

---

# Momento 3 · Romper el build a propósito (Actions ❌ → ✅)

Hazlo **cuando Marlo te diga que ya unió su `test_examples.py`**.

1. Crea otra rama desde `main`:

   ```
   feature/break-actions
   ```

2. Abre **`test_cli.py`** → lápiz ✏️ → busca esta línea:

   ```python
       assert run(fake_input("basic", "group_classes", "2", "y"), shown.append) == 81
   ```

   Cambia **solo** el `81` del final por `80`.
   **Commit changes...** → mensaje `Break a test on purpose to check that Actions fails` → a `feature/break-actions`.

3. Abre un PR de **`feature/break-actions`** a **`main`** con título `Check that Actions detects a failing test`.
4. Espera: el check sale **❌ Some checks were not successful**.

   📸 **Captura:** el PR con el ❌. Guárdala como `gaby-5-actions-rojo.png`.

   Clic en **Details** → abre el paso **Run tests** → se ve `assert 81 == 80` y `1 failed`.

   📸 **Captura:** el error. Guárdala como `gaby-6-actions-error.png`.

5. Arréglalo: pestaña **Code** → rama `feature/break-actions` → `test_cli.py` → lápiz ✏️ → vuelve a poner `81` →
   **Commit changes...** → mensaje `Fix the expected value` → a `feature/break-actions`.
6. El check vuelve a correr solo y sale ✅.

   📸 **Captura:** el PR en verde después del arreglo. Guárdala como `gaby-7-actions-verde.png`.

7. Avísale a Marlo para que lo apruebe y lo una.

Al final, entra a la pestaña **Actions** del repo: se ven todas las corridas (verdes y la roja).

📸 **Captura:** la lista de corridas. Guárdala como `gaby-8-actions-historial.png`.

---

## Qué hace tu código (léelo, la profe puede preguntarte)

- **`GymQuote.breakdown()`** hace el cálculo en el orden del PDF:
  valida (R1, R2, R3) → subtotal (R3) → descuento grupal (R4) → oferta especial (R5) → recargo premium (R6) →
  redondea **solo al final** (R7). Si la selección es inválida devuelve `None`, y `total()` devuelve **-1**.
- La clase **no pide datos ni imprime nada**: R8 exige que el cálculo esté separado de la entrada/salida.
  Así se puede probar con tests sin escribir en la consola.
- **`cli.py`** es la línea de comandos: pide plan, extras (separados por comas) y miembros; muestra el subtotal,
  cada descuento, el recargo y el total; y pregunta `Confirm (y/n)`. Con `n` (o cualquier cosa que no sea `y`) devuelve **-1**.
  Si los miembros no son un número (por ejemplo `two`), también devuelve -1.
- En **`test_cli.py`**, `fake_input` reemplaza al teclado: le da al programa respuestas ya escritas
  (`"basic"`, `"group_classes"`, `"2"`, `"y"`) para probarlo sin que nadie escriba. BASIC + GROUP_CLASSES con 2 miembros:
  (30 + 15) × 2 = 90 → 10% menos = **81**.
- **Romper el test a propósito** sirve para demostrar que la integración continua sí detecta errores:
  GitHub Actions no deja pasar un cambio que rompe los tests.

## Resumen: tus capturas

| Archivo | Qué se ve |
|---|---|
| `gaby-1-aprobacion-kiara.png` / `-samuel.png` | Tus aprobaciones de los PRs |
| `gaby-2-merge-kiara.png` / `-samuel.png` | Los PRs unidos (morado, Merged) |
| `gaby-3-commits.png` | Tus 3 commits |
| `gaby-4-pr-verde.png` | Tu PR con ✅ |
| `gaby-5-actions-rojo.png` | El PR roto con ❌ |
| `gaby-6-actions-error.png` | El detalle del error en Actions |
| `gaby-7-actions-verde.png` | El PR arreglado con ✅ |
| `gaby-8-actions-historial.png` | La pestaña Actions con todas las corridas |

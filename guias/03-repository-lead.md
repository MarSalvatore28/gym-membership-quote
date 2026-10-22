# Guía · Repository lead (R8 + revisión de PRs + GitHub Actions)

Tu parte: **revisar y aprobar** los PRs de Developer A y B, unir todo en `gym_quote.py`, la **línea de comandos** (R8)
y **romper el build a propósito** en un PR para mostrar GitHub Actions en rojo y en verde.
Todo se hace en el navegador. No necesitas usar Jenkins (lo maneja Marlo).

## Paso 0 · Entrar al repositorio

1. Si no tienes cuenta, créala en https://github.com/signup y pásale tu **usuario** a Marlo.
2. Cuando Marlo te invite, acepta aquí: https://github.com/MarSalvatore28/gym-membership-quote/invitations
3. Abre el repo: https://github.com/MarSalvatore28/gym-membership-quote

## Paso 1 · Crear tu rama

1. Arriba a la izquierda hay un botón que dice **main** (con un ícono de rama). Haz clic.
2. Escribe `feature/repository-lead` y haz clic en **Create branch feature/repository-lead from main**.
3. Confirma que el botón ahora dice **feature/repository-lead**. Todo lo que subas debe ir a esta rama, **nunca a main**.


> Espera a que los PRs de Developer A y Developer B estén **mergeados** antes de crear tu rama
> (tu código usa sus archivos).

## Paso 2 · Revisar los PRs de A y B (antes de tu parte)

Para cada PR (uno a la vez):

1. **Pull requests** → abre el PR.
2. Confirma que el check **CI / lint-and-test** está ✅ verde.
3. **Files changed → Review changes → Approve** → escribe "Looks good" → **Submit review**.
4. Pregúntale a Marlo si Jenkins está libre → **Merge pull request → Confirm merge**.
5. **Captura** de tu aprobación y del merge.

## Paso 3 · Unir todo en `gym_quote.py` (editar un archivo existente)

1. En tu rama, abre `gym_quote.py` y clic en el **lápiz** ✏️ (Edit this file).
2. Borra todo y pega:

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

3. **Commit changes...** → mensaje `Combine catalog and adjustments in GymQuote (R7)` → a tu rama.

## Paso 4 · La línea de comandos (R8)

**Add file → Create new file** → `cli.py`:

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

Commit: `Add command-line interface with confirmation (R8)`.

Luego **Add file → Create new file** → `test_cli.py`:

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

Commit: `Add unit tests for the command line (R8)`.

## Paso 5 · Abrir el Pull Request

1. Ve a la pestaña **Pull requests** → **New pull request**.
2. Deja **base: main** y en **compare** elige **feature/repository-lead**.
3. Clic en **Create pull request**. Título: `Combine the quote and add the command line (R7, R8)`. Clic en **Create pull request** otra vez.
4. Espera 1–2 minutos. Abajo aparece el check **CI / lint-and-test**:
   - ✅ verde: todo bien. **Toma captura** (con tu nombre visible).
   - ❌ rojo: clic en **Details**, toma captura del error y avísale a Marlo.
5. Pídele a Marlo que lo revise. Esa persona va a **Files changed → Review changes → Approve → Submit review**,
   y luego **Merge pull request → Confirm merge** (solo si el check está en verde y Jenkins no está corriendo otro build).


## Paso 6 · Romper el build a propósito en un PR (Actions rojo → verde)

Hazlo cuando Marlo ya haya mergeado su `test_examples.py`.

1. Crea otra rama: `feature/break-actions`.
2. Abre `test_cli.py` → lápiz ✏️ → en `test_r8_confirm_yes_returns_total` cambia `== 81` por `== 80`.
   Commit: `Break a test on purpose to check that Actions fails`.
3. Abre un PR de `feature/break-actions` a `main`. El check sale **❌ rojo**. **Captura** del ❌ y de **Details** con el error.
4. En la misma rama vuelve a poner `== 81`. Commit: `Fix the expected value`.
5. El check vuelve a **✅ verde**. **Captura**. Pídele a Marlo que apruebe y haz Merge.

## Qué explica tu código (por si te preguntan)

- `GymQuote.breakdown()` aplica en orden R3 → R4 → R5 → R6 y redondea solo al final (R7). **No hace input ni output**, como pide R8.
- `cli.py` pregunta plan, extras y miembros, muestra subtotal, cada descuento, el recargo y el total, y pide `y/n`. Con `n` devuelve -1.
- En `test_cli.py`, `fake_input` reemplaza al teclado para poder probar la consola sin escribir nada.

## Tus capturas para el informe

1. Tu aprobación y merge de los PRs de A y B.
2. Tus commits y tu PR en verde.
3. El PR roto en ❌ y luego arreglado en ✅.
4. La pestaña **Actions** con las corridas.

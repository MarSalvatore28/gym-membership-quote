# Guía · Developer A (R1, R2, R3, R7)

Tu parte: el **catálogo** de planes y extras, la **validación** de la selección, el **subtotal** y el **redondeo**.
Todo se hace en el navegador, sin instalar nada.

## Paso 0 · Entrar al repositorio

1. Si no tienes cuenta, créala en https://github.com/signup y pásale tu **usuario** a Marlo.
2. Cuando Marlo te invite, acepta aquí: https://github.com/MarSalvatore28/gym-membership-quote/invitations
3. Abre el repo: https://github.com/MarSalvatore28/gym-membership-quote

## Paso 1 · Crear tu rama

1. Arriba a la izquierda hay un botón que dice **main** (con un ícono de rama). Haz clic.
2. Escribe `feature/developer-a` y haz clic en **Create branch feature/developer-a from main**.
3. Confirma que el botón ahora dice **feature/developer-a**. Todo lo que subas debe ir a esta rama, **nunca a main**.


## Paso 2 · Subir el código (primer commit)

1. Con tu rama seleccionada, clic en **Add file → Create new file**.
2. Nombre del archivo: `catalog.py`
3. Pega este código completo:

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

4. Clic en **Commit changes...**. Mensaje: `Add plan and extras catalog with validation (R1, R2, R3, R7)`.
   Elige **Commit directly to the feature/developer-a branch** → **Commit changes**.

## Paso 3 · Subir los tests (segundo commit)

1. Otra vez **Add file → Create new file**. Nombre: `test_catalog.py`
2. Pega:

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

3. **Commit changes...**. Mensaje: `Add unit tests for R1, R2, R3 and R7`. Mismo branch → **Commit changes**.

## Paso 4 · Abrir el Pull Request

1. Ve a la pestaña **Pull requests** → **New pull request**.
2. Deja **base: main** y en **compare** elige **feature/developer-a**.
3. Clic en **Create pull request**. Título: `Add catalog, validation, subtotal and rounding (R1, R2, R3, R7)`. Clic en **Create pull request** otra vez.
4. Espera 1–2 minutos. Abajo aparece el check **CI / lint-and-test**:
   - ✅ verde: todo bien. **Toma captura** (con tu nombre visible).
   - ❌ rojo: clic en **Details**, toma captura del error y avísale a Marlo.
5. Pídele a la Repository lead (compañera) que lo revise. Esa persona va a **Files changed → Review changes → Approve → Submit review**,
   y luego **Merge pull request → Confirm merge** (solo si el check está en verde y Jenkins no está corriendo otro build).


## Qué explica tu código (por si te preguntan)

- **R1:** `PLANS` tiene los 3 planes; cualquier otro (como `GOLD`) es inválido.
- **R2:** un extra desconocido es inválido; `SPA` y `SPECIALIZED_PROGRAM` son *premium* y solo valen con `PREMIUM`.
- **R3:** subtotal = (precio del plan + precio de los extras) × miembros; los miembros deben ser al menos 1.
- **R7:** `round_half_up` redondea .5 hacia arriba (`round()` de Python redondea 2.5 a 2, por eso no se usa).

## Tus capturas para el informe

1. Tu rama creada (botón con `feature/developer-a`).
2. Tus 2 commits (pestaña **Commits** de tu rama).
3. Tu PR con el check ✅ verde.
4. El PR ya mergeado (morado, **Merged**).

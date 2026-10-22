# Guía · Developer B (R4, R5, R6)

Tu parte: el **descuento grupal**, la **oferta especial** y el **recargo premium**.
Tus funciones reciben un monto y devuelven un monto, así que no dependes de nadie.
Todo se hace en el navegador, sin instalar nada.

## Paso 0 · Entrar al repositorio

1. Si no tienes cuenta, créala en https://github.com/signup y pásale tu **usuario** a Marlo.
2. Cuando Marlo te invite, acepta aquí: https://github.com/MarSalvatore28/gym-membership-quote/invitations
3. Abre el repo: https://github.com/MarSalvatore28/gym-membership-quote

## Paso 1 · Crear tu rama

1. Arriba a la izquierda hay un botón que dice **main** (con un ícono de rama). Haz clic.
2. Escribe `feature/developer-b` y haz clic en **Create branch feature/developer-b from main**.
3. Confirma que el botón ahora dice **feature/developer-b**. Todo lo que subas debe ir a esta rama, **nunca a main**.


## Paso 2 · Subir el código (primer commit)

1. Con tu rama seleccionada, clic en **Add file → Create new file**.
2. Nombre del archivo: `adjustments.py`
3. Pega este código completo:

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

4. Clic en **Commit changes...**. Mensaje: `Add group discount, special offer and premium surcharge (R4, R5, R6)`.
   Elige **Commit directly to the feature/developer-b branch** → **Commit changes**.

## Paso 3 · Subir los tests (segundo commit)

1. Otra vez **Add file → Create new file**. Nombre: `test_adjustments.py`
2. Pega:

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

3. **Commit changes...**. Mensaje: `Add unit tests for R4, R5 and R6`. Mismo branch → **Commit changes**.

## Paso 4 · Abrir el Pull Request

1. Ve a la pestaña **Pull requests** → **New pull request**.
2. Deja **base: main** y en **compare** elige **feature/developer-b**.
3. Clic en **Create pull request**. Título: `Add group discount, special offer and premium surcharge (R4, R5, R6)`. Clic en **Create pull request** otra vez.
4. Espera 1–2 minutos. Abajo aparece el check **CI / lint-and-test**:
   - ✅ verde: todo bien. **Toma captura** (con tu nombre visible).
   - ❌ rojo: clic en **Details**, toma captura del error y avísale a Marlo.
5. Pídele a la Repository lead (compañera) que lo revise. Esa persona va a **Files changed → Review changes → Approve → Submit review**,
   y luego **Merge pull request → Confirm merge** (solo si el check está en verde y Jenkins no está corriendo otro build).


## Qué explica tu código (por si te preguntan)

- **R4:** con 2 o más miembros se multiplica por 0.90 (10% de descuento).
- **R5:** sobre el monto después de R4: si es mayor a 400 se restan 50; si no, si es mayor a 200 se restan 20. Nunca las dos.
- **R6:** si hay un extra premium, se multiplica por 1.15 (15% de recargo) el monto después de R5.
- En los tests se usa `pytest.approx` porque las multiplicaciones con decimales pueden dar 89.99999.

## Tus capturas para el informe

1. Tu rama creada (botón con `feature/developer-b`).
2. Tus 2 commits (pestaña **Commits** de tu rama).
3. Tu PR con el check ✅ verde.
4. El PR ya mergeado (morado, **Merged**).

# Gym Membership Quote

Command-line application that quotes the monthly cost of a gym membership.
Software Engineering II — Continuous Integration workshop (ESPOL, 2026).

- **Jenkins** runs the tests on every push to `main`.
- **GitHub Actions** runs pylint and pytest on every pull request to `main`.

## Run locally

```bash
pip install pytest pylint
pytest
pylint $(git ls-files '*.py')
```

## Agreed function signatures

Each member works in their own file and branch (`feature/<name>`), so nobody waits for anyone.
Amounts are floats; only the final total is rounded.

| File | Owner | Function | Requirement |
|---|---|---|---|
| `catalog.py` | Developer A | `PLANS`, `EXTRAS`, `PREMIUM_EXTRAS` | R1, R2 |
| `catalog.py` | Developer A | `is_valid_selection(plan, extras, members) -> bool` | R1, R2, R3 |
| `catalog.py` | Developer A | `subtotal(plan, extras, members) -> float` | R3 |
| `catalog.py` | Developer A | `round_half_up(amount) -> int` | R7 |
| `adjustments.py` | Developer B | `apply_group_discount(amount, members) -> float` | R4 |
| `adjustments.py` | Developer B | `apply_special_offer(amount) -> float` | R5 |
| `adjustments.py` | Developer B | `apply_premium_surcharge(amount, has_premium) -> float` | R6 |
| `gym_quote.py` | Repository lead | `GymQuote.total() -> int` (no input/output) | R7 |
| `cli.py` | Repository lead | `main()` asks plan, extras, members and y/n | R8 |
| `test_examples.py` | Jenkins lead | worked examples table | R9 |

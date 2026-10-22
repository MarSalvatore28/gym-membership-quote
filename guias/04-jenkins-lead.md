# Guía · Jenkins lead (Marlo)

Jenkins corre en Docker en tu laptop (`C:\Users\marsa\jenkins-workshop`) y ya trae Python y pytest.

## Antes de empezar

1. Abre Docker Desktop. En `jenkins-workshop`: `docker compose up -d`.
2. Invita a cada compañero: **Settings → Collaborators → Add people** (o pásale sus usuarios a Claude).

## Parte 2 · Plugin

**Administrar Jenkins → Plugins → Available plugins** → busca **Test Results Analyzer** → **Install**.

## Parte 3 · Dirección pública (opción C, ngrok)

En una terminal aparte: `ngrok http 8080`. Deja esa terminal abierta todo el taller.
Copia la URL `https://...ngrok-free.dev` de **Forwarding**. La URL cambia cada vez que abres ngrok.

## Parte 4 · Webhook

1. Repo → **Settings → Webhooks → Add webhook**.
2. **Payload URL:** `https://TU-URL-NGROK/github-webhook/` (con la barra final).
   **Content type:** `application/json`. **Just the push event.** → **Add webhook**.
3. Abre el webhook → **Recent Deliveries**: el *ping* debe salir con ✅ y **200**. **Captura.**

## Parte 5 · Job de Jenkins

1. **Nueva Tarea** → nombre `gym-membership-quote` → **Freestyle project** → OK.
2. **General:** marca **GitHub project** → `https://github.com/MarSalvatore28/gym-membership-quote/`
3. **Source Code Management:** **Git** → `https://github.com/MarSalvatore28/gym-membership-quote.git` → Branch `*/main`.
4. **Build Triggers:** **GitHub hook trigger for GITScm polling**.
5. **Build Steps → Execute shell** (Jenkins corre en Linux dentro de Docker, por eso *shell* y no *batch*):

   ```sh
   python -m pytest --junitxml=test-results.xml
   ```

   (pytest ya viene instalado en la imagen, por eso no hace falta `pip install`).
6. **Post-build Actions → Publish JUnit test result report** → `test-results.xml` →
   marca **Do not fail the build on empty test results**.
7. **Save → Build Now.** Build #1 debe salir ✅. **Captura.**

## Tu código: la tabla de ejemplos (R9)

Cuando estén mergeados A, B y la compañera, en tu laptop:

```sh
cd C:\Users\marsa\gym-membership-quote
git pull
git checkout -b feature/marlo
```

Crea `test_examples.py`:

```python
"""Integration tests: the worked examples table of the workshop (R9)."""
import pytest

from gym_quote import GymQuote

EXAMPLES = [
    ("BASIC", [], 1, 30),
    ("STANDARD", ["PERSONAL_TRAINING"], 1, 70),
    ("BASIC", ["GROUP_CLASSES"], 2, 81),
    ("BASIC", ["GROUP_CLASSES"], 3, 122),
    ("STANDARD", ["GROUP_CLASSES", "PERSONAL_TRAINING"], 4, 286),
    ("PREMIUM", ["GROUP_CLASSES", "SPA"], 2, 215),
    ("PREMIUM", ["SPA", "SPECIALIZED_PROGRAM"], 3, 412),
    ("PREMIUM", ["SPA", "SPECIALIZED_PROGRAM", "PERSONAL_TRAINING"], 4, 626),
    ("BASIC", ["SPA"], 1, -1),
    ("GOLD", [], 1, -1),
    ("BASIC", [], 0, -1),
]


@pytest.mark.parametrize("plan, extras, members, expected", EXAMPLES)
def test_worked_example(plan, extras, members, expected):
    """R9: every row of the table gives the expected result."""
    assert GymQuote(plan, extras, members).total() == expected
```

```sh
python -m pytest
git add test_examples.py
git commit -m "Add integration tests with the worked examples table (R9)"
git push -u origin feature/marlo
```

Abre el PR, espera ✅, pide aprobación a la compañera y haz merge. Jenkins debe arrancar solo:
en la consola del build sale **Started by GitHub push**. **Captura.**

## Romper Jenkins una vez en main

```sh
git checkout main
git pull
```

En `test_examples.py` cambia el `30` de la primera fila por `31`, y luego:

```sh
git commit -am "Break a test on purpose to check that Jenkins fails"
git push
```

Jenkins sale 🔴. **Captura** del build y de **Test Result**. Vuelve a poner `30`:

```sh
git commit -am "Fix the expected value"
git push
```

Jenkins vuelve a ✅.

## Test Results Analyzer

Con 3 builds o más: en el job → **Test Results Analyzer** → captura de la tabla y las gráficas.

## Tus capturas para el informe

Webhook con ✅ 200 · build verde · build rojo · consola con *Started by GitHub push* · gráficas de Test Results Analyzer · tu PR.

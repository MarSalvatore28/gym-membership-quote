# Plan del equipo — Workshop Continuous Integration

Lean **solo su guía**. Todo se hace desde el navegador en GitHub: nadie necesita instalar nada,
excepto Marlo, que tiene Jenkins.

| Rol (según el PDF) | Quién | Guía | Archivos que sube |
|---|---|---|---|
| Jenkins lead | Marlo (@MarSalvatore28) | [04-jenkins-lead.md](04-jenkins-lead.md) | `test_examples.py` + Jenkins, ngrok y webhook |
| Repository lead | Gabriela (@MGabrielaVillon) | [03-repository-lead.md](03-repository-lead.md) | `gym_quote.py`, `cli.py`, `test_cli.py` + revisa los PRs |
| Developer A | @Kcmoranj | [01-developer-a.md](01-developer-a.md) | `catalog.py`, `test_catalog.py` (R1, R2, R3, R7) |
| Developer B | Samuel (@SamuelChichande) | [02-developer-b.md](02-developer-b.md) | `adjustments.py`, `test_adjustments.py` (R4, R5, R6) |

## Orden del taller

1. **Todos:** creen su cuenta de GitHub (si no la tienen), pásenle su usuario a Marlo y acepten la invitación al repo.
2. **Marlo:** levanta Jenkins y ngrok, crea el webhook y el job (Build #1, en verde).
3. **Developer A y Developer B, al mismo tiempo:** cada uno crea su rama, sube sus 2 archivos y abre su Pull Request (PR).
4. **Compañera:** revisa y aprueba el PR de A → Merge. Espera a que Jenkins termine su build.
5. **Compañera:** revisa y aprueba el PR de B → Merge. Espera a Jenkins.
6. **Compañera:** sube su parte (`gym_quote.py`, `cli.py`, `test_cli.py`) en su rama → Marlo aprueba → Merge.
7. **Marlo:** sube `test_examples.py` (la tabla del PDF) → la compañera aprueba → Merge.
8. **Compañera:** rompe un test a propósito en un PR (Actions sale en ❌ rojo), lo arregla y vuelve a verde.
9. **Marlo:** rompe un test una vez en `main` (Jenkins sale en rojo), lo arregla, y guarda las gráficas de Test Results Analyzer.

> ⚠️ **No hagan Merge a dos PRs seguidos.** Esperen a que el build de Jenkins termine antes del siguiente (lo pide el PDF).

## Capturas: regla de oro

Cada captura del informe **debe mostrar el nombre de quien la hizo** (si no, son -10 por captura).
Antes de tomarla, asegúrense de que se vea su usuario de GitHub (foto o nombre arriba a la derecha) o
escriban su nombre encima de la imagen. Guárdenlas con nombre, por ejemplo `devA-pr-verde.png`.

Si alguien no tiene evidencia de su parte, pierde 50 puntos **individualmente**.

## Supuestos del equipo (van en el informe)

- Un extra repetido (por ejemplo `SPA, SPA`) se considera selección inválida.
- En la línea de comandos, plan y extras se aceptan en minúsculas o mayúsculas; los extras van separados por comas.
- El número de miembros debe ser un número entero; si no lo es, el resultado es -1.
- Los descuentos y el recargo se calculan con decimales; solo el total final se redondea (mitad hacia arriba).

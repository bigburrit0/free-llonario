# 19 · Animaciones del Papelón y la tarea con barba

> **Para vos:** el Papelón se despierta, escupe hojas («Firme aquí. Y aquí. Y aquí.») y explota en confeti cuando lo sella el brazo de Valentino. Que crezca ×3 lo hace el juego agrandándolo. La tarea con barba parpadea, se le chamusca la punta con el dragón, se completa con un tilde verde, la barba cae como alfombra y en los créditos aparece de vacaciones.
>
> **Antes:** Puerta 3.

---- COPIAR DESDE ACÁ ----

Seguí AGENTS.md, sección "Proceso de animación". Personajes: `pap` (bases `pap_dormido`, `pap_base`, `pap_papelito`) y `bar` (bases `bar_base`, `bar_tramo`, `bar_punta`).

| # | Pieza | Cuadros | Cuadro | fps | Bucle | Manera | Notas |
|---|---|---|---|---|---|---|---|
| 1 | pap_respirar | 2 | 32x32 | 3 | sí | mapa | Desde `pap_base`: en el cuadro 2 la pila se ensancha 1 px a cada lado |
| 2 | pap_despertar | 3 | 32x32 | 6 | no | imagen | Referencias: `pap_dormido` y `pap_base` |
| 3 | pap_escupir | 3 | 32x32 | 8 | no | imagen | La hoja que sale es aparte (fila 6) |
| 4 | pap_explotar | 4 | 32x32 | 10 | no | imagen | El confeti lo suma el juego |
| 5 | pap_papelito-parpadeo | 2 | 8x8 | 2 | sí | mapa | Ojos abiertos / cerrados |
| 6 | pap_hoja | 2 | 8x8 | 8 | sí | mapa | Hoja suelta volando, dos posiciones de giro, sin texto |
| 7 | bar_quieta | 2 | 24x16 | 2 | sí | mapa | Parpadeo |
| 8 | bar_punta-chamuscada | 2 | 8x8 | 6 | sí | mapa | Desde `bar_punta`: puntas oscuras en `1` y un hilito de humo en `3` que se mueve |
| 9 | bar_completada | 3 | 24x16 | 8 | no | mapa | La casilla se llena con un tilde verde (`j`, `k`) en dos pasos; ojos contentos `^ ^` |
| 10 | bar_alfombra | 1 | 32x8 | 1 | no | mapa | La barba caída en el piso, como alfombra |
| 11 | bar_vacaciones | 1 | 32x24 | 1 | no | imagen | `--tipo objeto` |

Descripciones (en inglés):

- **pap_despertar:** `Frame 1: the asleep paper pile, a single top sheet lifting by itself. Frame 2: the whole pile rising taller, sheets rustling apart. Frame 3: two big round eyes pop open between the sheets, awake and curious.`
- **pap_escupir:** `Frame 1: a gap opens between the sheets like a mouth. Frame 2: the gap wide open, the pile leaning back, about to spit. Frame 3: leaning forward after spitting, mouth closing.`
- **pap_explotar:** `Frame 1: the pile bulging outward, eyes wide in surprise. Frame 2: bursting, sheets flying out in all directions from the center. Frame 3: a loose cloud of paper scraps where the pile was, the eyes still visible in the middle. Frame 4: only a few scraps falling, the eyes gone. Cartoon, funny, not violent.`
- **bar_vacaciones:** `The same white task card from the identity reference, now with no beard, wearing tiny black sunglasses, lying relaxed on a striped beach towel, a tiny drink with a paper umbrella next to it. Drawn as a 32 by 24 pixel sprite enlarged so each art pixel is a 16 by 16 block.` Con el bloque de estilo y el fondo verde de AGENTS.md.

Al final:
1. `vistas/pap-bar_animaciones.png`: todas las tiras a ×6 con su nombre.
2. Con `componer.py`, `vistas/escenas/papelon_x4.png`: el lobby (`esc-lobby`) si ya existe (si no, gris liso), el Papelón en el cuadro 3 de `pap_escupir` con dos `pap_hoja` en el aire, y `val_brazo-sello` cuadro 3 desde la izquierda.
3. `vistas/escenas/barba_x4.png`: la cochera (`esc-cochera`) si ya existe, la tarjeta con 6 tramos de barba y la punta chamuscada.

Terminaste cuando:
- `validar.py` da OK en cada pieza.
- Existe un GIF por pieza animada y las vistas finales.

Informe según AGENTS.md, con una línea por pieza.

---- HASTA ACÁ ----

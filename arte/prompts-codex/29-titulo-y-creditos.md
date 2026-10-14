# 29 · Pantalla de título y viñetas de créditos

> **Para vos:** el título usa el exterior al amanecer (ya hecho) con lugar para el logo. El logo se dibuja cuando el juego tenga nombre (usá la plantilla 91 en ese momento). Los créditos son una pantalla de consola oscura con viñetas chiquitas: la tarea de vacaciones en la playa de Punta del Este y la Columna 2.0 con casco. El post-créditos es negro con el papelito que abre los ojos.
>
> **Antes:** prompt 21 hecho. La viñeta de la tarea usa `bar_vacaciones` (prompt 19); si todavía no existe, se hace igual sin ella.

---- COPIAR DESDE ACÁ ----

Seguí AGENTS.md.

1. **Título (`esc-titulo`)**, por código, sin generar imagen: cielo de amanecer nuevo en `cielo.py` (`m` → `n` → `X` → `d` cerca del horizonte), ciudad, `esc-ext_torres` centradas de modo que se vean las dos torres, vereda. Dejá libre un rectángulo para el logo: `logo=x,y,w,h` en el manifiesto (centrado, en el tercio de arriba, unos 220×56). Vista: `vistas/escenas/titulo_x4.png` con un rectángulo vacío de borde `s` donde va el logo y, abajo, «PRESIONÁ START» con `fuente.py`.

2. **Playa de Punta del Este (`esc-creditos-playa`)**, viñeta de 96×64, con la herramienta integrada:
   """
   Small pixel art vignette of a sunny beach: golden sand in the lower half, calm blue sea and a light sky, a striped beach umbrella, and on the left a small blank construction sign on two posts (empty board, no writing). A few seagulls far away as tiny shapes. Drawn as a 96 by 64 pixel image enlarged so each art pixel is a 12 by 12 block.
   Chunky 8-bit pixel art like late NES / early SNES games. Every art pixel is a crisp, perfectly square block of flat color. No anti-aliasing, no gradients, no blur, no glow, no texture noise. Flat fills with 2–4 tone ramps.
   No people, no text, letters, numbers, logos, watermarks, labels or grid lines anywhere.
   """
   Pixelá con `--id esc-creditos --nombre playa --tipo fondo --cuadro 96x64 --colores "d s c g h f 4 3 u L M 2"`. Anotá `cartel=x,y,w,h` (el texto «COCHERAS PDE: REQUERIMIENTOS VALIDADOS» lo pone el juego) y `toalla=x,y` (donde va `bar_vacaciones`).

3. **Fondo de créditos (`esc-creditos-consola`)**, por código: 320×180 en `0` con un marco de 1 px `1` a 4 px del borde y una línea de "cursor" `k` de 4×1 abajo a la izquierda (estilo consola vieja).

4. **Post-créditos (`esc-poscreditos`)**, por código: 320×180 en `0`; anotá `papelito=x,y` en un rincón de abajo a la derecha.

Vistas previas:
- `vistas/escenas/creditos_x4.png`: la consola con tres líneas de créditos de ejemplo (de `../guion-humor/02-guion-A-la-torta-al-piso-8.md`, sección "Final y créditos") y la viñeta de la playa con `bar_vacaciones` si existe.
- `vistas/escenas/poscreditos_x4.png`: negro, `pap_papelito` en su lugar y el texto «EL PAPELÓN VOLVERÁ.» chico debajo.

Terminaste cuando:
- `validar.py esc-titulo_fondo esc-creditos_playa esc-creditos-consola_fondo esc-poscreditos_fondo` da OK (nombrá las piezas así).
- El manifiesto tiene `logo=`, `cartel=` y `toalla=`.
- Existen las tres vistas.

Informe según AGENTS.md.

---- HASTA ACÁ ----

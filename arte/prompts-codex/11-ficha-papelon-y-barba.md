# 11 · Fichas del Papelón y la tarea con barba

> **Para vos:** los dos "villanos" son objetos, no personas. El Papelón es una montaña de formularios con ojos: tiene que dar risa, no miedo. La tarea con barba es una tarjeta de tareas genérica (sin el logo de Asana) con una barba larguísima. La barba se arma con tramos que se repiten, así el juego puede hacerla crecer un tramo por segundo.
>
> **Antes:** Puerta 1.

---- COPIAR DESDE ACÁ ----

Seguí AGENTS.md. Tarea: fichas del Papelón (`pap`) y de la tarea con barba (`bar`).

1. Cargá con `view_image` `referencias/style-frame.png` como "style reference".

2. Imagen A (Papelón):

"""
A funny, harmless paperwork monster for a pixel art game, two states side by side with a wide gap, same size, side view facing right: LEFT asleep: a neat tall pile of white and light grey paper forms, slightly messy, eyes closed as two small lines; RIGHT awake: the same pile standing up a bit taller, two big round cartoon eyes peeking between the sheets, a couple of loose sheets sticking out like little arms, two small red rubber-stamp marks on the papers (just red rectangles, no letters). Goofy and cute, not scary. Each drawn as a 32 by 32 pixel sprite enlarged so each art pixel is a 12 by 12 block.
Chunky 8-bit pixel art like late NES / early SNES games. Every art pixel is a crisp, perfectly square block of flat color. No anti-aliasing, no gradients, no blur, no glow, no texture noise, no dithering. Flat fills with 2–4 tone ramps. Selective outline on bottom and right edges with dark grey, never pure black. Light from the top-left.
Perfectly flat, solid pure green #00FF00 background. No floor, no cast shadows.
No text, letters, numbers, writing lines that look like text, logos, watermarks, labels or grid lines anywhere.
"""

3. Imagen B (tarea con barba):

"""
A funny task card character for a pixel art game, side view facing right: a white rectangular task card from a generic project-management board, with an empty checkbox square on its left side, two small dot eyes, and an extremely long grey beard hanging from its lower edge down to the floor and curling on the ground. No brand, no logo, no text on the card. The card is drawn as 24 by 16 pixels and the beard about 8 pixels wide, enlarged so each art pixel is a 16 by 16 block.
Chunky 8-bit pixel art like late NES / early SNES games. Every art pixel is a crisp, perfectly square block of flat color. No anti-aliasing, no gradients, no blur, no glow, no texture noise, no dithering. Selective outline on bottom and right edges, never pure black. Light from the top-left.
Perfectly flat, solid pure green #00FF00 background. No floor, no cast shadows.
No text, letters, numbers, logos, watermarks, labels or grid lines anywhere.
"""

4. Guardá en `crudo/pap_ficha_1.png` y `crudo/bar_ficha_1.png`. Pixelá:
   - Papelón: `--id pap --nombre ficha --tipo personaje --cuadro 32x32 --cuadros 2 --separar huecos --colores "4 3 2 1 t u 9"`. `contorno.py`. Separá `pap_dormido` y `pap_base`.
   - Tarea: pixelá solo la tarjeta (recortá la barba si hace falta) con `--id bar --nombre base --tipo objeto --cuadro 24x16 --cuadros 1 --colores "4 3 2 1 9 0"`. `contorno.py`.

5. Por mapa, usando la imagen B como guía: `bar_tramo` (8×8, barba gris `3`/`2` con mechones; tiene que repetirse hacia abajo sin que se note la unión), `bar_punta` (8×8, final enrulado de la barba) y `pap_papelito` (8×8, una sola hoja con dos ojitos). `txt2png.py`.

6. Armá `vistas/pap-bar_ficha_comparar.png` ×6: el Papelón dormido y despierto al lado de `val_base`; la tarjeta con 1, 3 y 6 tramos de barba más la punta (para ver que la unión no se note); el papelito.

Terminaste cuando:
- `validar.py pap_dormido pap_base bar_base bar_tramo bar_punta pap_papelito` da OK.
- Existe `vistas/pap-bar_ficha_comparar.png`.

Informe según AGENTS.md.

---- HASTA ACÁ ----

**Cuando lo apruebes:** `Aprobado. Pasá pap_dormido, pap_base, bar_base, bar_tramo, bar_punta y pap_papelito a "aprobado" y copiá sus vistas ×8 a referencias/fichas/pap.png y referencias/fichas/bar.png.`

# 02 · Prueba de tamaño con Cami

> **Para vos:** antes de producir, comprobamos si a 16×24 píxeles se reconoce a una persona. Se usa a Cami porque tiene rasgos claros (bob, anteojos, cárdigan). Codex hace la misma Cami de tres maneras: 16×24 desde la imagen, 24×32 desde la imagen y 16×24 dibujada a mano por mapa. Las pone lado a lado sobre un fondo del juego.
>
> **Qué decidís después:** el tamaño (16×24 o 24×32) y si los personajes chicos se hacen mejor por imagen o por mapa. Si podés, mirá la vista en una pantalla grande o un proyector.

---- COPIAR DESDE ACÁ ----

Seguí AGENTS.md. Tarea: prueba de tamaño y de manera de dibujar, con Cami (`cam`).

1. Generá 1 imagen con la herramienta integrada, con esta descripción:

"""
Pixel art game sprite of a young woman, full body, side view facing right (slight 3/4), standing idle, arms relaxed. Short dark bob haircut with side-swept bangs, large tortoiseshell glasses, black t-shirt, light cream knitted cardigan, brown belt, dark grey trousers, simple dark shoes. Drawn as a 16 by 24 pixel sprite enlarged so that each art pixel is a 16 by 16 block, centered on the canvas.
Chunky 8-bit pixel art like late NES / early SNES games. Every art pixel is a crisp, perfectly square block of flat color. No anti-aliasing, no gradients, no blur, no glow, no texture noise, no dithering. Flat fills with 2–4 tone ramps. Selective outline: bottom and right edges use the darkest tone of the adjacent color, never pure black; top and left edges have no dark outline. Light from the top-left. Cute chibi proportions (head about 45% of the body height), friendly face.
Perfectly flat, solid pure green #00FF00 background. No floor, no cast shadow.
No text, letters, numbers, logos, watermarks, labels, grid lines or frame borders anywhere.
"""

2. Guardala en `crudo/cam_prueba_1.png` y pixelala dos veces con los colores `A B C L M P Q 1 2 7 8 9 4`:
   - `--id cam --nombre prueba16 --tipo personaje --cuadro 16x24 --cuadros 1`
   - `--id cam --nombre prueba24 --tipo personaje --cuadro 24x32 --cuadros 1`
   Pasá las dos por `contorno.py`.

3. Manera 2: mirando la imagen generada, dibujá a mano un mapa de 16×24 de la misma Cami en `mapas/cam/cam_prueba-mapa_c1.txt`, con los mismos colores. Priorizá que se lean el bob con flequillo, los anteojos y el cárdigan claro. Convertilo con `txt2png.py`.

4. Agregá las tres al manifiesto con `estado=prueba`, `fps=1` y corré `validar.py` sobre las tres.

5. Armá con `componer.py` la vista `vistas/escenas/prueba-tamano.png` (×4): fondo gris claro liso de 320×180, las tres Cami en el suelo a la misma altura de pies, separadas, y debajo de cada una su retrato ampliado ×3 como referencia. Armá también `vistas/prueba-tamano-x6.png`: las tres a ×6, lado a lado.

Terminaste cuando:
- `validar.py cam_prueba16 cam_prueba24 cam_prueba-mapa` da OK en las tres.
- Existen `vistas/escenas/prueba-tamano.png` y `vistas/prueba-tamano-x6.png`.

Informe según AGENTS.md. Además, decime en dos líneas cuál de las tres se reconoce mejor y por qué.

---- HASTA ACÁ ----

**Qué mirar:** ¿se reconoce a Cami en la de 16×24? ¿El flequillo y los anteojos se leen? Si ninguna de 16×24 se reconoce, avisame: cambiar a 24×32 afecta todo el plan.

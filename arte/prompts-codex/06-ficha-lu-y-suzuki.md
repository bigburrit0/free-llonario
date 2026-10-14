# 06 · Ficha de Lu y el Suzuki rojo

> **Para vos:** Lu de costado y de frente, y su auto rojo de costado. El auto es genérico, sin logo de Suzuki: se reconoce por ser chiquito y rojo. La ropa de Lu (blusa azul marino y jean) es un supuesto: si sabés cómo se viste, cambiá esa parte del texto en inglés antes de pegarlo.
>
> **Antes:** Puerta 1 (style frame aprobado).

---- COPIAR DESDE ACÁ ----

Seguí AGENTS.md. Tarea: ficha de Lu (`lu`) y del Suzuki rojo (`ob-auto`).

1. Cargá con `view_image` `referencias/style-frame.png` y `referencias/fichas/cam.png` como "style reference".

2. Imagen A:

"""
Character model sheet of the same young woman, two poses side by side with a wide gap, same height: LEFT side view facing right, standing idle; RIGHT front view facing the viewer, neutral friendly expression. Long straight blonde hair past the shoulders, green eyes, navy blue blouse, blue jeans, simple light shoes. Drawn as 16 by 24 pixel sprites enlarged so each art pixel is a 16 by 16 block.
Chunky 8-bit pixel art like late NES / early SNES games. Every art pixel is a crisp, perfectly square block of flat color. No anti-aliasing, no gradients, no blur, no glow, no texture noise, no dithering. Flat fills with 2–4 tone ramps. Selective outline on bottom and right edges with the darkest tone of the adjacent color, never pure black. Light from the top-left. Cute chibi proportions, friendly face. Match the style reference in pixel size, outline and level of detail.
Perfectly flat, solid pure green #00FF00 background. No floor, no cast shadows.
No text, letters, numbers, logos, watermarks, labels, grid lines or frame borders anywhere.
"""

3. Imagen B:

"""
Small cute red hatchback city car, side view facing right, generic design with no brand badge, rounded friendly shape, light blue windows, two black wheels with grey hubs, small yellow rear light. Drawn as a 48 by 24 pixel sprite enlarged so each art pixel is a 16 by 16 block, centered.
Chunky 8-bit pixel art like late NES / early SNES games. Every art pixel is a crisp, perfectly square block of flat color. No anti-aliasing, no gradients, no blur, no glow, no reflections, no dithering. Selective outline on bottom and right edges with the darkest red, never pure black. Light from the top-left.
Perfectly flat, solid pure green #00FF00 background. No road, no cast shadow.
No text, letters, numbers, logos, license plate characters, watermarks, labels or grid lines anywhere.
"""

4. Guardá en `crudo/lu_ficha_1.png` y `crudo/ob-auto_ficha_1.png`. Pixelá:
   - Lu: `--id lu --nombre ficha --tipo personaje --cuadro 16x24 --cuadros 2 --separar huecos --colores "w x e f g 7 8 6 j 9 4 3"`.
   - Auto: `--id ob-auto --nombre base --tipo objeto --cuadro 48x24 --cuadros 1 --colores "r t u v h g 1 2 s 9 4"`.
   Pasá las dos por `contorno.py`.

5. Separá `lu_base` (cuadro 1) y `lu_frente` (cuadro 2) con sus mapas.

6. Armá `vistas/lu_ficha_comparar.png` ×6: Lu de costado, Lu de frente, el auto, y Lu parada al lado del auto a escala real del juego (para ver que el auto es más alto que ella hasta el techo, no más).

Terminaste cuando:
- `validar.py lu_base lu_frente ob-auto_base` da OK.
- Existe `vistas/lu_ficha_comparar.png`.

Informe según AGENTS.md.

---- HASTA ACÁ ----

**Cuando lo apruebes:** `Aprobado. Pasá lu_base, lu_frente y ob-auto_base a "aprobado" y copiá sus vistas ×8 a referencias/fichas/lu.png y referencias/fichas/ob-auto.png.`

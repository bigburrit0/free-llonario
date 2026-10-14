# 07 · Ficha de Andrea

> **Para vos:** Andrea de costado y de frente. Su gag (la que cierra, la barbera, la del termo o la de Tetris) no cambia la ficha; cambia sus animaciones del prompt 17.
>
> **Antes:** Puerta 1.

---- COPIAR DESDE ACÁ ----

Seguí AGENTS.md. Tarea: ficha de Andrea (`and`).

1. Cargá con `view_image` `referencias/style-frame.png` y `referencias/fichas/cam.png` como "style reference".

2. Imagen, con la herramienta integrada:

"""
Character model sheet of the same woman, two poses side by side with a wide gap, same height: LEFT side view facing right, standing idle, confident posture; RIGHT front view facing the viewer, calm friendly smile. Long straight black hair, black blazer over a white shirt, small round wooden earrings, black trousers, simple dark shoes. Drawn as 16 by 24 pixel sprites enlarged so each art pixel is a 16 by 16 block.
Chunky 8-bit pixel art like late NES / early SNES games. Every art pixel is a crisp, perfectly square block of flat color. No anti-aliasing, no gradients, no blur, no glow, no texture noise, no dithering. Flat fills with 2–4 tone ramps. Selective outline on bottom and right edges with the darkest tone of the adjacent color, never pure black. Light from the top-left. Cute chibi proportions, friendly face. Match the style reference in pixel size, outline and level of detail.
Perfectly flat, solid pure green #00FF00 background. No floor, no cast shadows.
No text, letters, numbers, logos, watermarks, labels, grid lines or frame borders anywhere.
"""

3. Guardá en `crudo/and_ficha_1.png`. Pixelá con `--id and --nombre ficha --tipo personaje --cuadro 16x24 --cuadros 2 --separar huecos --colores "A B C 4 3 L M 7 8 6 1 9"`. Pasá por `contorno.py`. El blazer negro no puede fundirse con el pelo negro: si pasa, corregí por mapa usando `C` para el blazer y `A`/`B` para el pelo, o al revés.

4. Separá `and_base` y `and_frente` con sus mapas.

5. Armá `vistas/and_ficha_comparar.png` ×6: Andrea de costado y de frente, y una fila con `cam_base`, `lu_base`, `and_base` y `val_base` juntos, para comparar alturas y estilo.

Terminaste cuando:
- `validar.py and_base and_frente` da OK.
- Existe `vistas/and_ficha_comparar.png`.

Informe según AGENTS.md.

---- HASTA ACÁ ----

**Cuando lo apruebes:** `Aprobado. Pasá and_base y and_frente a "aprobado" y copiá su vista ×8 a referencias/fichas/and.png.`

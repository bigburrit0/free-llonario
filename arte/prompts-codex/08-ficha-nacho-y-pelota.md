# 08 · Ficha de Nacho y la pelota XXL

> **Para vos:** Nacho es el CEO, y sus gags (la pelota gigante, el saque que rompe dos respuestas) necesitan su OK antes que ningún otro. No hay foto: el texto en inglés lo describe genérico. Si conseguís rasgos (color y largo de pelo, barba, anteojos, cómo se viste), cambiá la parte marcada antes de pegarlo. No subas una foto suya sin su OK.
>
> **Antes:** Puerta 1, rasgos de Nacho y su OK.

---- COPIAR DESDE ACÁ ----

Seguí AGENTS.md. Tarea: ficha de Nacho (`nac`), su pelota XXL (`ob-pelota`) y su raqueta.

1. Cargá con `view_image` `referencias/style-frame.png` y `referencias/fichas/cam.png` como "style reference".

2. Imagen A:

"""
Character model sheet of the same man, three poses side by side with wide gaps, same height: LEFT side view facing right, standing idle, holding an oversized tennis ball under one arm; MIDDLE front view facing the viewer, friendly confident smile, holding the same oversized ball; RIGHT side view facing right holding a tennis racket, no ball. [RASGOS: short brown hair, clean-shaven], white tennis polo shirt with a lime green collar, navy shorts, white sneakers. The tennis ball is huge: about as big as his head. Drawn as 16 by 24 pixel sprites enlarged so each art pixel is a 16 by 16 block.
Chunky 8-bit pixel art like late NES / early SNES games. Every art pixel is a crisp, perfectly square block of flat color. No anti-aliasing, no gradients, no blur, no glow, no texture noise, no dithering. Flat fills with 2–4 tone ramps. Selective outline on bottom and right edges with the darkest tone of the adjacent color, never pure black. Light from the top-left. Cute chibi proportions, friendly face. Match the style reference in pixel size, outline and level of detail.
Perfectly flat, solid pure magenta #FF00FF background. No floor, no cast shadows.
No text, letters, numbers, logos, watermarks, labels, grid lines or frame borders anywhere.
"""

3. Guardá en `crudo/nac_ficha_1.png`. Pixelá con `--id nac --nombre ficha --tipo personaje --cuadro 16x24 --cuadros 3 --separar huecos --fondo FF00FF --colores "y z 4 3 H I J 7 8 6 e 1 9"`. Pasá por `contorno.py`. Separá `nac_base`, `nac_frente` y `nac_raqueta` con sus mapas.

4. La pelota suelta va por mapa (es chica): dibujá `ob-pelota_base` de 16×16, círculo en `I` con brillo `J` arriba a la izquierda, sombra `H` abajo a la derecha y las dos costuras curvas en `4`. Hacé también `ob-pelota_chica` de 6×6 (pelota de tamaño normal, para el gag del saque de honor). `txt2png.py`.

5. Armá `vistas/nac_ficha_comparar.png` ×6: las tres poses de Nacho, la pelota grande y la chica, y Nacho al lado de `val_base` para comparar.

Terminaste cuando:
- `validar.py nac_base nac_frente nac_raqueta ob-pelota_base ob-pelota_chica` da OK.
- Existe `vistas/nac_ficha_comparar.png`.

Informe según AGENTS.md.

---- HASTA ACÁ ----

**Cuando lo apruebes (y Nacho también):** `Aprobado. Pasá nac_base, nac_frente, nac_raqueta, ob-pelota_base y ob-pelota_chica a "aprobado" y copiá sus vistas ×8 a referencias/fichas/nac.png y referencias/fichas/ob-pelota.png. Actualizá la fila nac de AGENTS.md con los rasgos definitivos.`

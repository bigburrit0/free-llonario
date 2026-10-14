# 04 · Ficha de Cami y el dragoncito

> **Para vos:** la ficha es el "modelo" del personaje: de costado (como camina en el juego) y de frente (para cuando mira a cámara o está en el ascensor). El dragoncito va aparte para que el juego lo pueda poner en el hombro de Cami o hacerlo volar. En el ejemplo visual anterior el dragón flotaba suelto; acá queda definido dónde se apoya.
>
> **Antes:** 02 aprobado. Usá el tamaño que elegiste ahí.

---- COPIAR DESDE ACÁ ----

Seguí AGENTS.md. Tarea: ficha de Cami (`cam`) y del dragoncito (`drg`).

1. Cargá con `view_image` `vistas/cam_prueba16_x8.png` como "identity and style reference" (o la de 24×32 si ese fue el tamaño elegido).

2. Imagen A, con la herramienta integrada:

"""
Character model sheet of the same young woman, two poses side by side with a wide gap, same height: LEFT side view facing right, standing idle; RIGHT front view facing the viewer, standing idle, neutral friendly expression. Short dark bob haircut with side-swept bangs, large tortoiseshell glasses, black t-shirt, light cream knitted cardigan, brown belt, dark grey trousers, simple dark shoes. Match the reference image exactly in colors, proportions and pixel size. Drawn as 16 by 24 pixel sprites enlarged so each art pixel is a 16 by 16 block.
Chunky 8-bit pixel art like late NES / early SNES games. Every art pixel is a crisp, perfectly square block of flat color. No anti-aliasing, no gradients, no blur, no glow, no texture noise, no dithering. Flat fills with 2–4 tone ramps. Selective outline on bottom and right edges with the darkest tone of the adjacent color, never pure black. Light from the top-left. Cute chibi proportions, friendly face.
Perfectly flat, solid pure green #00FF00 background. No floor, no cast shadows.
No text, letters, numbers, logos, watermarks, labels, grid lines or frame borders anywhere.
"""

3. Imagen B:

"""
Tiny cute baby dragon for a pixel art game, three poses side by side with wide gaps: LEFT side view facing right, standing on all fours; MIDDLE sitting upright as if perched on someone's shoulder, side view facing right, tail curled; RIGHT flying side view, wings up. Green body with a lighter belly, small wings, round head, big friendly eyes, tiny horns. Drawn as 12 by 12 pixel sprites enlarged so each art pixel is a 20 by 20 block.
Chunky 8-bit pixel art like late NES / early SNES games. Every art pixel is a crisp, perfectly square block of flat color. No anti-aliasing, no gradients, no blur, no glow, no dithering. Selective outline on bottom and right edges with the darkest green, never black. Light from the top-left.
Perfectly flat, solid pure magenta #FF00FF background. No floor, no cast shadows.
No text, letters, numbers, logos, watermarks, labels, grid lines or frame borders anywhere.
"""

4. Guardá en `crudo/cam_ficha_1.png` y `crudo/drg_ficha_1.png`. Pixelá:
   - Cami: `--id cam --nombre ficha --tipo personaje --cuadro 16x24 --cuadros 2 --separar huecos --colores "A B C L M P Q 1 2 7 8 9 4"`.
   - Dragón: `--id drg --nombre ficha --tipo personaje --cuadro 12x12 --cuadros 3 --separar huecos --fondo FF00FF --colores "i j k 9 4 K s"`.
   Pasá las dos por `contorno.py`. Compará la Cami de costado con `cam_prueba16` y corregí por mapa lo que se haya ido (anteojos, flequillo, cárdigan).

5. Separá cuadros sueltos, con su mapa: `cam_base` (cuadro 1), `cam_frente` (cuadro 2), `drg_base` (cuadro 1), `drg_hombro` (cuadro 2), `drg_volar-ref` (cuadro 3).

6. Calculá dónde va el dragón sentado en el hombro de Cami: el desplazamiento x,y de `drg_hombro` respecto de la esquina de `cam_base`, para que quede apoyado sobre el hombro de atrás y sin taparle la cara. Anotalo en la columna `notas` del manifiesto en `drg_hombro` (`hombro=x,y`).

7. Armá `vistas/cam_ficha_comparar.png` ×6: Cami de costado con el dragón en el hombro, Cami de frente, el dragón suelto y volando.

Terminaste cuando:
- `validar.py cam_base cam_frente drg_base drg_hombro drg_volar-ref` da OK.
- El manifiesto tiene `hombro=x,y` en `drg_hombro`.
- Existe `vistas/cam_ficha_comparar.png`.

Informe según AGENTS.md.

---- HASTA ACÁ ----

**Cuando lo apruebes,** decile a Codex: `Aprobado. Pasá cam_base, cam_frente, drg_base, drg_hombro y drg_volar-ref a "aprobado" y copiá sus vistas ×8 a referencias/fichas/cam.png y referencias/fichas/drg.png.`

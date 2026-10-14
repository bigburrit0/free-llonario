# 09 · Ficha de Fran 1.0 y Fran 2.0

> **Para vos:** Fran es la presentadora. Como no sabemos qué es hoy, el supuesto es un monitor con cara: Fran 1.0 es una pantalla verde vieja y rígida; Fran 2.0, una pantalla a color, amable. Si Fran es otra cosa (una persona, un logo, un chat), avisame antes de pegar esto: cambia el diseño.
>
> **Antes:** Puerta 1 y la decisión 6 del plan.

---- COPIAR DESDE ACÁ ----

Seguí AGENTS.md. Tarea: ficha de Fran 1.0 y Fran 2.0 (`fra`).

1. Cargá con `view_image` `referencias/style-frame.png` como "style reference".

2. Imagen, con la herramienta integrada:

"""
Two versions of the same friendly TV-host character that is a computer monitor with a face, side by side with a wide gap, both front view, same size. LEFT, version 1.0: an old boxy beige CRT monitor; its screen is monochrome green with a stiff, blocky pixel face: square eyes and a straight line mouth, slightly robotic. RIGHT, version 2.0: a sleek modern monitor with a thin dark frame; its screen is full color with a warm blue background and a friendly rounded face: big expressive eyes and a smile, a small headset microphone on the side of the frame. Each monitor drawn as a 32 by 24 pixel sprite enlarged so each art pixel is a 16 by 16 block.
Chunky 8-bit pixel art like late NES / early SNES games. Every art pixel is a crisp, perfectly square block of flat color. No anti-aliasing, no gradients, no blur, no glow, no scanline texture, no dithering. Flat fills with 2–4 tone ramps. Selective outline on bottom and right edges, never pure black. Light from the top-left. Cute and friendly.
Perfectly flat, solid pure magenta #FF00FF background. No desk, no floor, no cast shadows.
No text, letters, numbers, logos, watermarks, labels, grid lines or frame borders anywhere.
"""

3. Guardá en `crudo/fra_ficha_1.png`. Pixelá con `--id fra --nombre ficha --tipo personaje --cuadro 32x24 --cuadros 2 --separar huecos --fondo FF00FF --ancla centro --colores "P Q j k i f g h 4 1 2 G 9 0"`. Pasá por `contorno.py`. Separá `fra_v1-base` y `fra_v2-base` con sus mapas.

4. Revisá por mapa que la cara de Fran 2.0 tenga ojos de al menos 2×2 px y boca de 3 px o más: tiene que leerse desde el fondo de la sala.

5. Armá `vistas/fra_ficha_comparar.png` ×6: las dos versiones y, a escala del juego, Fran 2.0 al lado de `val_base`.

Terminaste cuando:
- `validar.py fra_v1-base fra_v2-base` da OK.
- Existe `vistas/fra_ficha_comparar.png`.

Informe según AGENTS.md.

---- HASTA ACÁ ----

**Cuando lo apruebes:** `Aprobado. Pasá fra_v1-base y fra_v2-base a "aprobado" y copiá su vista ×8 a referencias/fichas/fra.png.`

# 10 · Ficha del agente comercial

> **Para vos:** el robotito de traje que se enciende en la escena de Fran 2.0 y desde ahí sigue al protagonista como los compañeros de un RPG. Tiene que distinguirse del robot de Valentino de un vistazo: más bajito, redondo, de traje azul marino y corbata naranja.
>
> **Antes:** Puerta 1.

---- COPIAR DESDE ACÁ ----

Seguí AGENTS.md. Tarea: ficha del agente comercial (`age`).

1. Cargá con `view_image` `referencias/style-frame.png` y `referencias/fichas/val.png` como "style reference" (el agente tiene que verse distinto de ese robot).

2. Imagen, con la herramienta integrada:

"""
Character model sheet of a tiny friendly sales-assistant robot, three poses side by side with wide gaps, same height: LEFT side view facing right, standing idle holding a small brown briefcase; MIDDLE front view facing the viewer, polite smile; RIGHT side view facing right holding up a small tour-guide flag on a stick (the flag is plain orange, no symbols). The robot is short and round, with a small rectangular screen as a face showing two cyan dot eyes, wearing a navy blue suit with an orange tie, short grey metal legs. Clearly shorter and rounder than a standard character. Drawn as 12 by 16 pixel sprites enlarged so each art pixel is a 16 by 16 block.
Chunky 8-bit pixel art like late NES / early SNES games. Every art pixel is a crisp, perfectly square block of flat color. No anti-aliasing, no gradients, no blur, no glow, no texture noise, no dithering. Flat fills with 2–4 tone ramps. Selective outline on bottom and right edges, never pure black. Light from the top-left. Cute chibi proportions. Match the style reference in pixel size and level of detail.
Perfectly flat, solid pure green #00FF00 background. No floor, no cast shadows.
No text, letters, numbers, logos, watermarks, labels, grid lines or frame borders anywhere.
"""

3. Guardá en `crudo/age_ficha_1.png`. Pixelá con `--id age --nombre ficha --tipo personaje --cuadro 12x16 --cuadros 3 --separar huecos --colores "e f c b L M G D E 1 9 4"`. Pasá por `contorno.py`. Separá `age_base`, `age_frente` y `age_bandera` con sus mapas.

4. Armá `vistas/age_ficha_comparar.png` ×6: las tres poses, y el agente caminando un tile (16 px) detrás de `val_base`, como en el juego.

Terminaste cuando:
- `validar.py age_base age_frente age_bandera` da OK.
- Existe `vistas/age_ficha_comparar.png`.

Informe según AGENTS.md.

---- HASTA ACÁ ----

**Cuando lo apruebes:** `Aprobado. Pasá age_base, age_frente y age_bandera a "aprobado" y copiá su vista ×8 a referencias/fichas/age.png.`

# 03 · Valentino: tres variantes para que elija

> **Para vos:** Valentino es el protagonista y aparece como robot. Falta decidir cómo. Codex dibuja las tres opciones lado a lado, mismo tamaño y mismo estilo, para que Valentino elija mirándolas:
> - **V1 · Robot con flequillo:** robot gris con su flequillo castaño encima, como peluca. Es el gag más arriesgado del banco (`VAL-07`): solo si a él le divierte.
> - **V2 · Robot sin pelo:** antena y un cuello de camisa blanca pintado, como guiño a su camisa.
> - **V3 · Piloto:** Valentino humano adentro de la cabina de vidrio de un robot (`VAL-08`).
>
> **Antes:** prompt 02 aprobado (por el tamaño).

---- COPIAR DESDE ACÁ ----

Seguí AGENTS.md. Tarea: tres variantes del protagonista Valentino (`val`) para elegir.

1. Cargá con `view_image` la vista `vistas/cam_prueba16_x8.png` como "style reference" (mismo nivel de detalle y de pixel).

2. Generá 1 imagen con la herramienta integrada:

"""
Three variants of the same friendly game character, side by side with wide gaps, all full body, side view facing right, idle pose, all exactly the same height.
LEFT: a small friendly robot with a rounded grey metal body, a cyan visor with two simple dot eyes, a small chest panel, short sturdy legs, and a short brown human-like haircut with a fringe sitting on top of its head like a funny wig.
MIDDLE: the same robot without hair, with a short antenna with a cyan tip, and a white shirt collar painted on its chest.
RIGHT: the same grey robot body with a round transparent glass cockpit as its head; inside the cockpit, the face and shoulders of a young man with short brown hair with a fringe and a white shirt collar, piloting the robot.
Drawn as 16 by 24 pixel sprites enlarged so each art pixel is a 16 by 16 block.
Chunky 8-bit pixel art like late NES / early SNES games. Every art pixel is a crisp, perfectly square block of flat color. No anti-aliasing, no gradients, no blur, no glow, no texture noise, no dithering. Flat fills with 2–4 tone ramps. Selective outline: bottom and right edges use the darkest tone of the adjacent color, never pure black; top and left edges have no dark outline. Light from the top-left. Cute chibi proportions, friendly expressions.
Perfectly flat, solid pure green #00FF00 background. No floor, no cast shadows.
No text, letters, numbers, logos, watermarks, labels, grid lines or frame borders anywhere.
"""

3. Guardá en `crudo/val_variantes_1.png`. Pixelá con `--id val --nombre variantes --tipo personaje --cuadro 16x24 --cuadros 3 --separar huecos --colores "y z 4 3 D E G 1 2 7 8 9 h"`. Pasá por `contorno.py`. Si alguna variante pierde la idea a 16×24 (por ejemplo, no se ve la cara en la cabina), corregila por mapa.

4. Manifiesto con `estado=prueba`, `fps=1`. `validar.py val_variantes`.

5. Armá `vistas/val_variantes_comparar.png`: las tres a ×6 sobre damero, separadas, con debajo los textos "V1", "V2", "V3" usando `herramientas/fuente.py`.

Terminaste cuando:
- `validar.py val_variantes` da OK.
- Existe `vistas/val_variantes_comparar.png`.

Informe según AGENTS.md.

---- HASTA ACÁ ----

**Cuando Valentino elija,** pegale esto a Codex (cambiá `V_` por la elegida):

---- COPIAR DESDE ACÁ ----

Seguí AGENTS.md. Valentino eligió la variante V_. Separá ese cuadro de `final/personajes/val/val_variantes.png` como `final/personajes/val/val_base.png` (16×24, 1 cuadro), con su mapa en `mapas/val/val_base_c1.txt`. Agregalo al manifiesto con `estado=aprobado`, `fps=1`. Copiá la vista ×8 a `referencias/fichas/val.png`. En la tabla de fichas de AGENTS.md, en la fila `val`, reemplazá "variante por elegir (prompt 03)" por la descripción de la V_ elegida. No cambies nada más de AGENTS.md.

Después hacé la vista de frente: cargá `vistas/val_base_x8.png` como "identity reference" y generá 1 imagen con la misma descripción en inglés de la V_ en el prompt original, pero "front view facing the viewer, standing idle, neutral friendly expression", un solo personaje, mismo fondo y mismas reglas de estilo. Guardala en `crudo/val_frente_1.png`, pixelala con `--id val --nombre frente --tipo personaje --cuadro 16x24 --cuadros 1` y los mismos colores, `contorno.py`, y dejala con `estado=para-revisar`.

`validar.py val_base val_frente`. Mostrame las dos a ×6.

---- HASTA ACÁ ----

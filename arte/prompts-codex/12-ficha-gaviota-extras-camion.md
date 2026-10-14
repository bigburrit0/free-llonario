# 12 · Fichas de la gaviota, los extras y el camión

> **Para vos:** la gaviota multitarea (con y sin casco), los extras (empresarios que visitan, operario de la mudanza, representantes de organizaciones en la mesa redonda) y el camión de mudanza verde y amarillo. Los extras se dibujan una vez y las variantes salen cambiando colores, sin generar más imágenes. Nada de estereotipos: los empresarios son gente de traje, sin camisetas de fútbol ni carnaval.
>
> **Antes:** Puerta 1.

---- COPIAR DESDE ACÁ ----

Seguí AGENTS.md. Tarea: fichas de la gaviota (`gav`), los extras (`ext`) y el camión (`ob-camion`).

1. Cargá con `view_image` `referencias/style-frame.png` y `referencias/fichas/cam.png` como "style reference".

2. Imagen A (gaviota):

"""
A cute expressive seagull for a pixel art game, three poses side by side with wide gaps, side view facing right: LEFT standing idle; MIDDLE the same seagull wearing a small yellow construction hard hat, holding a pencil in its beak; RIGHT the same seagull sitting as if on a chair at a meeting table. White and light grey body, darker grey wings, orange beak and feet, big funny eyes. Each drawn as a 16 by 12 pixel sprite enlarged so each art pixel is a 20 by 20 block.
Chunky 8-bit pixel art like late NES / early SNES games. Every art pixel is a crisp, perfectly square block of flat color. No anti-aliasing, no gradients, no blur, no glow, no dithering. Selective outline on bottom and right edges with grey, never pure black. Light from the top-left.
Perfectly flat, solid pure green #00FF00 background. No floor, no cast shadows.
No text, letters, numbers, logos, watermarks, labels or grid lines anywhere.
"""

3. Imagen B (extras):

"""
Character model sheet of three different generic background characters for a pixel art game, side by side with wide gaps, all side view facing right, standing idle, same height: LEFT a business visitor in a grey suit with a light blue shirt and a small dark briefcase; MIDDLE a moving-company worker in a green overall with a yellow cap, holding a rubber stamp; RIGHT a person seated on an invisible chair, smart-casual clothes, hands together on the lap. Neutral friendly faces, simple hair. Drawn as 16 by 24 pixel sprites (the seated one 16 by 16) enlarged so each art pixel is a 16 by 16 block.
Chunky 8-bit pixel art like late NES / early SNES games. Every art pixel is a crisp, perfectly square block of flat color. No anti-aliasing, no gradients, no blur, no glow, no texture noise, no dithering. Flat fills with 2–4 tone ramps. Selective outline on bottom and right edges, never pure black. Light from the top-left. Cute chibi proportions. Match the style reference in pixel size and level of detail.
Perfectly flat, solid pure magenta #FF00FF background. No floor, no chair, no cast shadows.
No text, letters, numbers, logos, flags, watermarks, labels or grid lines anywhere.
"""

4. Imagen C (camión):

"""
A friendly cartoon moving truck, side view facing LEFT (it will back up to the right), green cab and green-and-yellow cargo box with plain panels, two black wheels, small rear lights. No flags, no brand, no text. Drawn as a 64 by 40 pixel sprite enlarged so each art pixel is a 12 by 12 block, centered.
Chunky 8-bit pixel art like late NES / early SNES games. Every art pixel is a crisp, perfectly square block of flat color. No anti-aliasing, no gradients, no blur, no glow, no reflections, no dithering. Selective outline on bottom and right edges with the darkest green, never pure black. Light from the top-left.
Perfectly flat, solid pure magenta #FF00FF background. No road, no cast shadow.
No text, letters, numbers, logos, license plates, watermarks, labels or grid lines anywhere.
"""

5. Guardá en `crudo/gav_ficha_1.png`, `crudo/ext_ficha_1.png` y `crudo/ob-camion_ficha_1.png`. Pixelá:
   - Gaviota: `--id gav --nombre ficha --tipo personaje --cuadro 16x12 --cuadros 3 --separar huecos --colores "4 3 2 1 c d s 9"`. Separá `gav_base`, `gav_casco` y `gav_sentada`.
   - Extras: el empresario y el operario con `--cuadro 16x24`, el sentado con `--cuadro 16x16` (podés pixelar la tira con `--cuadro 16x24 --cuadros 3` y después recortar el tercero a 16×16 anclado abajo). `--fondo FF00FF --colores "2 3 1 h f j k s 7 8 6 5 y A L 9 4"`. Separá `ext_empresario`, `ext_operario` y `ext_sentado`.
   - Camión: `--id ob-camion --nombre base --tipo objeto --cuadro 64x40 --cuadros 1 --fondo FF00FF --colores "i j k s d 1 2 3 h u 9 4"`. Este no se espeja: mira a la izquierda a propósito.
   Pasá todo por `contorno.py`.

6. Variantes por paleta, en `herramientas/variantes.py` (cambia códigos de un mapa por otros y guarda la pieza nueva con su mapa): 3 empresarios (`ext_empresario-1/-2/-3`: traje gris, azul marino o marrón; pelo castaño, negro o canoso; piel 7/8, 6/7 o 5/6) y 4 sentados (`ext_sentado-1` a `-4`, combinando ropa y pelo). Documentá las tablas de cambio en el mismo archivo.

7. Armá `vistas/gav-ext_ficha_comparar.png` ×6 con todo, y una fila de 6 empresarios alternando variantes, como se verá la fila de los 25.

Terminaste cuando:
- `validar.py --todo` da OK en todas las piezas de este prompt.
- Existe `vistas/gav-ext_ficha_comparar.png`.

Informe según AGENTS.md.

---- HASTA ACÁ ----

**Cuando lo apruebes:** `Aprobado. Pasá todas las piezas gav, ext y ob-camion de este prompt a "aprobado" y copiá sus vistas ×8 a referencias/fichas/.`

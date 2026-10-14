# 13 · Retratos para los diálogos

> **Para vos:** las caras de 24×24 que aparecen al lado del texto en la caja de diálogo. Siete personajes con cuatro caras cada uno: neutral, hablando, sorpresa y contento. Codex hace la cara neutral con imagen y las otras tres editando ojos y boca sobre esa misma cara, para que no cambie de persona.
>
> **Antes:** fichas 04 a 12 aprobadas. Es un prompt largo: si Codex se corta, pedile que siga desde el personaje donde quedó.
>
> **Puerta 2:** después de este prompt, mostrale a cada persona su ficha y su retrato y pedile el OK.

---- COPIAR DESDE ACÁ ----

Seguí AGENTS.md. Tarea: retratos de 24×24 de `val`, `cam`, `lu`, `and`, `nac`, `fra` (2.0) y `age`. Hacelos de a uno, en ese orden, terminando cada personaje antes de pasar al siguiente.

Para cada personaje `<id>`:

1. Cargá con `view_image` `referencias/fichas/<id>.png` como "identity reference" y `referencias/style-frame.png` como "style reference".

2. Generá 1 imagen con esta descripción (reemplazá `<DESCRIPCIÓN>` por los rasgos de la fila `<id>` de la tabla de fichas de AGENTS.md, en inglés):

"""
Pixel art dialogue portrait of <DESCRIPCIÓN>, head and shoulders, three-quarter view facing right, neutral friendly expression, centered. Must match the identity reference exactly: same hair, colors, glasses and clothes. Drawn as a 24 by 24 pixel portrait enlarged so each art pixel is a 32 by 32 block.
Chunky 8-bit pixel art like late NES / early SNES games. Every art pixel is a crisp, perfectly square block of flat color. No anti-aliasing, no gradients, no blur, no glow, no texture noise, no dithering. Flat fills with 2–4 tone ramps. Selective outline on bottom and right edges, never pure black. Light from the top-left. Friendly face, eyes clearly readable.
Perfectly flat, solid pure green #00FF00 background (use solid magenta #FF00FF instead for green subjects).
No text, letters, numbers, logos, watermarks, labels, grid lines or frame borders anywhere.
"""

3. Guardá en `crudo/<id>_retrato_1.png`. Pixelá con `--id <id> --nombre retrato-neutral --tipo retrato --cuadro 24x24 --cuadros 1 --ancla abajo` y los mismos colores de la ficha. `contorno.py`.

4. Por mapa, copiando `<id>_retrato-neutral` y cambiando **solo ojos, cejas y boca**: `<id>_retrato-habla` (boca abierta), `<id>_retrato-sorpresa` (ojos más grandes, boca en O, cejas arriba) y `<id>_retrato-contento` (ojos curvos, sonrisa). En Valentino robot y el agente, la expresión va en la pantalla o visera (ojos cian que cambian de forma). Juntá las cuatro en una tira `<id>_retratos` de 96×24 (4 cuadros) con `txt2png.py`.

5. `validar.py <id>_retratos`. Manifiesto con `fps=6` y `estado=para-revisar`.

Al final:

6. Armá `vistas/retratos_todos.png` ×6: una fila por personaje con sus cuatro caras.
7. Armá con `componer.py` `vistas/escenas/dialogo-prueba_x4.png`: la escena del style frame con la caja de diálogo usando `cam_retratos` cuadro 2 y el texto «¿POR QUÉ REDONDA?».

Terminaste cuando:
- `validar.py val_retratos cam_retratos lu_retratos and_retratos nac_retratos fra_retratos age_retratos` da OK.
- Existen `vistas/retratos_todos.png` y `vistas/escenas/dialogo-prueba_x4.png`.

Informe según AGENTS.md, con una línea por personaje.

---- HASTA ACÁ ----

**Qué mirar:** que cada persona se reconozca en su retrato y que las cuatro caras sean claramente de la misma persona.

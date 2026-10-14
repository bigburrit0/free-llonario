# 28 · Estudio del concurso

> **Para vos:** la pantalla que más tiempo está proyectada: cada pregunta pasa acá. Es un estudio de diseño propio (violeta y dorado, como dice el plan), sin copiar el decorado ni el logo del programa de TV. Arriba, un monitor grande donde aparece Fran; a la derecha, el panel donde el juego dibuja el display del ascensor; abajo, lugar libre para la pregunta y las cuatro respuestas.
>
> **Antes:** style frame aprobado.

---- COPIAR DESDE ACÁ ----

Seguí AGENTS.md, sección "Proceso de escenario". En este escenario no hay línea de piso para personajes: la parte de abajo es para la interfaz.

**Escenario: `esc-estudio`**

"""
TV quiz show studio of our own original design (do not copy any real show's set or logo). Deep violet background with a dark navy floor, warm golden spotlights shining down from the top edge in a few simple beams, a low stepped stage in the middle with a thin golden edge. Upper center: a large wall-mounted monitor with a thin dark frame, its screen a flat dark rectangle with nothing on it. Right side: a tall narrow vertical panel with a dark empty face (for a floor indicator). The entire lower 45% of the image is calm, dark and empty, only floor, to leave room for interface boxes. Elegant and dramatic, high contrast between dark violet and gold.
"""
Colores: `m n e f 0 1 2 s d c b 4 g`. (Excepción a "fondos menos saturados": el estudio es dramático, pero la mitad de abajo tiene que ser oscura y lisa.)

Anotá en el manifiesto:
- `monitor=x,y,w,h` (la pantalla de Fran).
- `panel=x,y,w,h` (el display del ascensor).
- `zona-ui=0,98,320,82` (o lo que quede libre abajo; tiene que entrar una caja de pregunta de 2 líneas y 4 cápsulas de 2 líneas en 2 columnas de 152 px).

Por código, además:
- `esc-estudio_luces-bajas`: la misma imagen con los rayos dorados apagados y todo un tono más oscuro (pregunta final y «¿última respuesta?»).

Vista previa: `vistas/escenas/estudio_x4.png` con `fra_v2-base` (si existe) centrado en el monitor, y la zona de interfaz marcada con rectángulos vacíos de borde `4`: la pregunta (304×24) y las 4 cápsulas (152×28 cada una, 2 columnas, 2 filas). Si las cajas no entran, decímelo con medidas.

Terminaste cuando:
- `validar.py esc-estudio_fondo esc-estudio_luces-bajas` da OK.
- El manifiesto tiene `monitor=`, `panel=` y `zona-ui=`.
- Existe la vista previa.

Informe según AGENTS.md.

---- HASTA ACÁ ----

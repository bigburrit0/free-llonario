# 22 · Lobby de la Torre 1 y cochera

> **Para vos:** los dos primeros escenarios del acto 1 (Innovación, mañana, naranja). En el lobby se despierta el Papelón; en la cochera aparece la tarea con barba enredada en la barrera. La barrera, la columna con colchón y el cartel «Próximamente» son objetos aparte (prompt 30), así que acá quedan los huecos.
>
> **Antes:** style frame aprobado. Mejor con fotos del lobby y la cochera en `referencias/fotos/`.

---- COPIAR DESDE ACÁ ----

Seguí AGENTS.md, sección "Proceso de escenario". Si hay fotos `lobby*` o `cochera*` en `referencias/fotos/`, cargalas como "architecture reference".

**Escenario 1: `esc-lobby`**

"""
Interior lobby of a modern office tower at morning, warm light with orange accents (this tower's color theme is orange). Left: glass entrance doors with the bright morning street visible through them. Right: a clean reception desk with nobody behind it. Back wall: light stone panels, two tall potted plants, a couple of plain framed panels with nothing on them, ceiling lights. Floor: polished light tiles. A wide clear area in the middle of the floor.
"""
Colores: `a b c d 1 2 3 4 i j k L M h W`.

**Escenario 2: `esc-cochera`**

"""
Underground parking garage, dim and moody, blue-grey concrete with a few cold ceiling lights. Painted white parking lines on the floor, two thick concrete columns in the background, a couple of generic parked cars in the far background in dark silhouette. Right side: an empty space where a parking barrier will stand, with only its small concrete base on the floor. Back wall on the right: an empty rectangular space for a sign, plain wall. Middle of the floor clear.
"""
Colores: `e f g 1 2 3 0 s 4 u`. Tiene que ser más oscuro que el lobby: la escena empieza a oscuras y el dragón hace de linterna.

Para la cochera, además:
- Anotá en el manifiesto `barrera=x,y` (dónde va la base de la barrera) y `cartel=x,y,w,h`.
- Por código, `esc-cochera_oscura`: la misma imagen con todo bajado un tono en su rampa (la escena antes de la linterna).

Vistas previas: `vistas/escenas/lobby_x4.png`, `vistas/escenas/cochera_x4.png` y `vistas/escenas/cochera-oscura_x4.png`, con `val_base` y `cam_base`.

Terminaste cuando:
- `validar.py esc-lobby_fondo esc-cochera_fondo esc-cochera_oscura` da OK (nombrá las piezas así).
- Existen las tres vistas previas.

Informe según AGENTS.md.

---- HASTA ACÁ ----

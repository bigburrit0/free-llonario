# 23 · Oficina de Innovación y sala del pizarrón

> **Para vos:** en la oficina se actualiza Fran 2.0 en una pantalla gigante (el texto «ACTUALIZANDO… 99 %» lo escribe el juego, así que la pantalla queda vacía). En la sala, los post-its llueven sobre un pizarrón vacío cuando Cami se suma al equipo.
>
> **Antes:** style frame aprobado. Mejor con fotos de la oficina o de una sala en `referencias/fotos/`.

---- COPIAR DESDE ACÁ ----

Seguí AGENTS.md, sección "Proceso de escenario".

**Escenario 1: `esc-oficina`**

"""
Open-plan tech office at morning with orange accents. Back wall: one huge wall-mounted screen in the center, turned off, its screen area a perfectly flat dark violet rectangle with nothing on it. Around it: a few desks with closed laptops and small monitors (screens dark), office chairs, two potted plants, a large window on the right showing a pale city view. Middle of the floor clear.
"""
Colores: `a b c d 1 2 3 4 m n i j k h L M`. Anotá `pantalla=x,y,w,h` (el rectángulo de la pantalla gigante, en píxeles) en el manifiesto.

**Escenario 2: `esc-sala`**

"""
Small meeting room at late morning with orange accents. The whole back wall is a large empty whiteboard with a thin aluminum frame (completely blank). In front: a simple meeting table with four chairs on the far side, a small plant, a window on the left with soft light. Middle of the floor clear in front of the table.
"""
Colores: `a b c d 1 2 3 4 i j k h L M`. Anotá `pizarron=x,y,w,h`.

Vistas previas: `vistas/escenas/oficina_x4.png` (con `fra_v2-base` centrado dentro de la pantalla si ya existe) y `vistas/escenas/sala_x4.png` (con 6 post-its `ob-postit` sobre el pizarrón si ya existen; si no, rectángulos de 6×6 en `s`, `X`, `k` y `h`).

Terminaste cuando:
- `validar.py esc-oficina_fondo esc-sala_fondo` da OK.
- El manifiesto tiene `pantalla=` y `pizarron=`.
- Existen las dos vistas previas.

Informe según AGENTS.md.

---- HASTA ACÁ ----

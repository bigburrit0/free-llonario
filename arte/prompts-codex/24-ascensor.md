# 24 · Ascensor: por dentro, el hall y las puertas

> **Para vos:** el ascensor une los actos. Por dentro: el protagonista, el agente y el dragón miran el display en silencio (los números los pone el juego). Desde el hall: las puertas se abren y, en el chiste del 8½, se abren a medias. Las hojas de la puerta van aparte para que el juego las mueva.
>
> **Antes:** style frame aprobado. Mejor con fotos del ascensor (adentro y la botonera) en `referencias/fotos/`.

---- COPIAR DESDE ACÁ ----

Seguí AGENTS.md, sección "Proceso de escenario". Si hay fotos `ascensor*`, cargalas como "architecture reference".

**Escenario 1: `esc-ascensor`** (por dentro, visto desde la puerta abierta)

"""
Inside of an office elevator cabin seen straight-on from its open doorway: brushed steel back wall with a horizontal handrail, side walls in perspective kept very shallow, warm ceiling light panel. On the left side wall: a vertical button panel with plain round buttons (no numbers) and, at the top of the panel, an empty black rectangular display slot. Floor: dark grey. The cabin fills the screen; leave the floor clear for three characters standing side by side facing the viewer.
"""
Colores: `1 2 3 4 D E 0 s d W`. Anotá `display=x,y,w,h` (el hueco negro) y `piso=<y>`.

**Escenario 2: `esc-hall`** (hall de ascensores, se usa en el 8½ y en el piso 6)

"""
Office elevator lobby on an upper floor: a wide wall with one elevator in the center. Draw only the elevator's steel door frame and, inside the frame, a completely dark opening (the doors will be added separately). Above the frame: an empty black display slot. To the sides: two potted plants, a bench, a light floor with a subtle pattern, ceiling lights.
"""
Colores: `1 2 3 4 D E 0 i j k L M h`. Anotá `hueco=x,y,w,h` (el hueco de la puerta) y `display=x,y,w,h`.

**Puertas:** por mapa, `esc-hall_hoja` (una hoja de puerta de acero, del alto del hueco y la mitad de su ancho, con una línea de brillo `E` y una sombra `D`). El juego usa dos hojas (una espejada) y las mueve. Hacé también `esc-ascensor_hoja` igual pero vista desde adentro (más oscura, `1`/`2`).

Vistas previas (con `componer.py`; si `fuente.py` todavía no tiene `½` y `¾`, agregáselos en 5×7):
- `vistas/escenas/ascensor_x4.png`: por dentro, con `val_frente`, `age_frente` y `cam_frente` (los que existan) parados uno al lado del otro, y en el display el texto «4¾» con `fuente.py`.
- `vistas/escenas/hall-8medio_x4.png`: el hall con las dos hojas abiertas a la mitad del recorrido y «8½» en el display.

Terminaste cuando:
- `validar.py esc-ascensor_fondo esc-hall_fondo esc-hall_hoja esc-ascensor_hoja` da OK.
- El manifiesto tiene `display=` en los dos escenarios y `hueco=` en el hall.
- Existen las dos vistas previas.

Informe según AGENTS.md.

---- HASTA ACÁ ----

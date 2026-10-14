# 35 · Paletas del día y filtros

> **Para vos:** el exterior se dibuja una vez y se ve en cuatro momentos (mañana, mediodía, atardecer, noche) cambiando sus colores con una tabla. También se preparan los filtros que dependen de la versión del guion: el sepia con viñeta y grano (versión B o la mezcla recomendada, donde el juego pasa de sepia a color cuando llega Fran 2.0) y el pixelado progresivo (versión C). Codex hace las tablas y las vistas previas; el juego los aplica.
>
> **Antes:** prompt 21. Los personajes no cambian de color con la hora del día: solo los fondos.

---- COPIAR DESDE ACÁ ----

Seguí AGENTS.md. Tarea: tablas de paleta y vistas previas de filtros, por código, sin generar imágenes.

1. **Paletas del día** en `herramientas/paleta_dia.py` y `paleta/dia.json`: una tabla por momento que cambia cada código de la paleta por otro código de la misma paleta (sin colores nuevos). Se aplica solo a capas de fondo.
   - `manana`: sin cambios.
   - `mediodia`: luz más fría y pareja; los naranjas claros de la luz (`d`, `W`) bajan un tono, los azules claros (`h`) quedan.
   - `atardecer`: tono cálido; azules claros → naranjas o rosas (`h` → `d`, `g` → `X`), verdes un tono más oscuros, grises claros → crema (`3` → `Q`).
   - `noche`: todo dos tonos más oscuro dentro de su rampa; azules → `e`/`N`; los blancos → `2`; las ventanas encendidas son la capa aparte del prompt 21.
   Vistas: `vistas/escenas/ext-paleta_<momento>_x4.png` (las 4) con el exterior completo (capas del prompt 21 con la tabla aplicada y su cielo), y `val_base` y `cam_base` sin cambiar.
2. **Comprobación de lectura**: en cada una de las 4 vistas, medí el contraste entre el color de contorno de los personajes y el fondo detrás de ellos. Si en algún momento un personaje se pierde (por ejemplo, de noche), proponé el ajuste en la tabla y aplicalo.
3. **Sepia** (`paleta/sepia.json`): cada código → `R`, `S`, `T` o `U` según su luminosidad. Más `ef-vineta_base` (320×180, esquinas oscuras con tramado en `R`, centro transparente) y `ef-grano_base` (tira de 3 cuadros de 320×180, 1 % de píxeles sueltos `R` y `U`, distintos en cada cuadro, 8 fps, bucle). Vista: `vistas/escenas/style-frame_sepia_x4.png` (todo en sepia, personajes incluidos, con viñeta y el cuadro 1 del grano) y un GIF `vistas/sepia-a-color.gif` de 8 cuadros donde el color vuelve de izquierda a derecha.
4. **Pixelado progresivo** (versión C): vistas del style frame renderizado a 160×90 y a 80×45 (achicado por moda de bloque) y vuelto a ampliar ×2 y ×4 con vecino más cercano: `vistas/escenas/pixelado_160_x4.png` y `pixelado_80_x4.png`.
5. **Iris**: GIF `vistas/iris.gif` de 10 cuadros sobre el style frame: un círculo que se cierra hacia el centro de Valentino, con el exterior en `0` y borde de 1 px `0`. Solo como referencia para el juego.

Terminaste cuando:
- Existen `paleta/dia.json` y `paleta/sepia.json`, y `validar.py ef-vineta_base ef-grano_base` da OK.
- Existen las 4 vistas del día, la sepia, el GIF sepia a color, las 2 de pixelado y el iris.
- El informe dice, para cada momento del día, si los personajes se leen (sí/no) y qué se ajustó.

Informe según AGENTS.md.

---- HASTA ACÁ ----

**Qué mirar:** las cuatro vistas del exterior una al lado de la otra: ¿se nota el paso del día? ¿Valentino y Cami se ven bien de noche?

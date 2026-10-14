# 34 · Pantallas de interfaz

> **Para vos:** las pantallas armadas con piezas de interfaz: la tarjeta de cada noticia (con el color de su área), la pantalla de equipo estilo RPG donde se suma Cami, la pantalla de resultado y rango, la de «ACTUALIZANDO A FRAN 2.0», el «PRESIONÁ START» y el afiche del premio «VACACIONES GRATIS» con su letra chica en tres momentos (una rayita ilegible, asoma, y la lupa que la revela). El logo del título espera el nombre del juego.
>
> **Antes:** prompts 32 y 33; para el afiche, `ob-afiche` y `ob-lupa` (prompt 30).

---- COPIAR DESDE ACÁ ----

Seguí AGENTS.md. Tarea: pantallas de interfaz, por código, con las piezas de `final/interfaz/` y las fuentes de `final/fuente/`. Sin generar imágenes.

1. **ui-tarjeta** (280x84, 9 piezas): tarjeta de noticia con una pestaña de color arriba a la izquierda según el área (naranja `c` Innovación, azul `g` Comercial, verde `j` Sostenibilidad: 3 variantes), lugar para un ícono de 16×16 y texto de hasta 5 líneas. Vista: las 13 noticias del guion en sus tarjetas, en `vistas/tarjetas_todas.png` (×2), y una a ×4 sobre el estudio en `vistas/escenas/tarjeta_x4.png`.
2. **ui-equipo** (320x180): pantalla de grupo estilo RPG: título «EQUIPO», 4 casilleros con `ui-marco-retrato` y placa para el nombre debajo, y un quinto casillero para «JUGADOR 2». Estados por código: casillero vacío que parpadea («¿?», 2 fps), casillero lleno. Vista: `vistas/escenas/equipo_x4.png` con Valen, Lu y Andre llenos, el cuarto vacío con «¿?»; y otra `equipo-lleno_x4.png` con Cami sumada y «LAIB SE UNIÓ A LA PARTIDA. JUGADOR 2» con `ob-control` en el quinto.
3. **ui-resultado** (320x180): fondo del estudio con luces bajas, rango grande (fuente grande), cantidad de aciertos, la escalera de 8 pisos con aciertos y errores, y una grilla de logros (ícono de trofeo + nombre). Vista con el rango «INTEGRANTE HONORARIO/A DE INNOVACIÓN», 6 aciertos y 4 logros.
4. **ui-actualizando**: contenido para la pantalla gigante de `esc-oficina` (del tamaño de `pantalla=`): texto «ACTUALIZANDO A FRAN 2.0…» y `ui-barra-carga` al 99 %. Vista sobre la oficina.
5. **ui-start**: «PRESIONÁ START» en fuente grande con contorno, sobre `esc-titulo`. Vista `vistas/escenas/titulo-start_x4.png`.
6. **ui-afiche-premio**: `ob-afiche` con «VACACIONES GRATIS*» en la fuente grande y la letra chica «*15 MINUTOS, EN LA TERRAZA DEL PISO 8, CON MATE PROPIO.» en tres estados:
   - `ilegible`: la letra chica es una sola rayita de puntos de 1 px.
   - `asoma`: la letra chica en la fuente chica pero reducida a la mitad (1 px por trazo, apenas legible).
   - `lupa`: como `asoma`, con `ob-lupa` encima y, dentro del vidrio, esa parte del texto en la fuente chica normal.
   Mirá `../ejemplo-visual/premio-letra-chica.html` como referencia de la idea. Vistas a ×4 de los tres estados sobre `esc-terraza_noche`.

Terminaste cuando:
- `validar.py` da OK en cada pieza nueva.
- Existen todas las vistas nombradas.
- Las 13 tarjetas entran en 5 líneas (si alguna no, decime cuál).

Informe según AGENTS.md.

---- HASTA ACÁ ----

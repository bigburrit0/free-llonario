# 33 · Interfaz del estudio y HUD

> **Para vos:** todo lo que se superpone a las escenas: la caja de diálogo, la caja de la pregunta, las cuatro cápsulas de respuesta en sus estados (neutra, elegida, correcta con ✓, incorrecta con ✗), el display del ascensor con sus números de 7 segmentos y la escalera de pisos, los comodines, las barras de votación, el cartelito de logro, los carteles de estudio para la sala (REDOBLE, SOPLEN, CONTÁ…), el zócalo de noticias y la barra de la torta. Se hace con código: se ve igual de nítido en cualquier tamaño.
>
> **Antes:** prompts 28 (estudio) y 32 (tipografía). Supone cápsulas de 2 líneas (152 px de ancho), como propuso el guion.

---- COPIAR DESDE ACÁ ----

Seguí AGENTS.md. Tarea: interfaz (`ui-…`), por código y por mapa (maneras 2 y 3), sin generar imágenes. Todo con contorno completo en `0`. Las cajas que se estiran van en 9 piezas (esquinas, bordes, centro) con un JSON de recortes. Cada fila es una pieza `<id>_base` (por ejemplo `ui-capsula_base`, con sus 4 estados como cuadros), con ancla `centro`.

| Pieza | Tamaño | Estados / cuadros | Diseño |
|---|---|---|---|
| ui-dialogo | 9 piezas de 8×8 | 1 | Fondo `0`, borde de 1 px `4` y otro de 1 px `1` adentro |
| ui-marco-retrato | 26x26 | 1 | Marco para el retrato de 24×24, mismos colores |
| ui-pregunta | 9 piezas de 8×8 | 1 | Fondo `n`, borde `s` con brillo `d` arriba |
| ui-capsula | 152x28 | 4 | Esquinas redondeadas de 2 px; a la izquierda una pestaña redonda de 14 px para la letra. Neutra: relleno `f`, borde `h`. Elegida: `c`, borde `d`. Correcta: `j`, borde `k`, con ✓ `4` a la derecha. Incorrecta: `u`, borde `v`, con ✗ `4` a la derecha. No copiar la forma hexagonal del programa de TV |
| ui-letras | 10x12 | 4 | A, B, C, D en la fuente grande, `4` con contorno `0`, para la pestaña |
| ui-digitos | 9x15 | 14 | 7 segmentos: 0–9, ½, ¾, vacío y "todo apagado". Encendido `u` con centro `v`, apagado `r` |
| ui-panel-display | 40x24 | 1 | Marco del display: `1`/`2` con tornillitos `3` |
| ui-escalera | 48x10 | 5 | Fila de piso: pendiente (`1`, número en `2`), actual (`s`, número en `0`), acierto (`j` con ✓), error (`2` con ✗ `u`), y la especial "8½" |
| ui-comodin | 16x16 | 6 | Saque de Nacho (pelota con rayas de movimiento), Preguntale al lobby (barras con cabecitas), Mandalo a Asana (tarjetita con barba, sin logo); cada uno normal y usado (gris con ✗) |
| ui-votacion | 120x48 | 1 | Marco con 4 barras vacías y lugar para etiquetas (A–D o SIM, NÃO, TALVEZ) |
| ui-logro | 120x20 | 1 | Cartelito con trofeo `s` de 12×12 a la izquierda y lugar para el texto |
| ui-cartel | 96x24 | 2 | Cartel luminoso con borde de foquitos `s`/`d` que se alternan (2 cuadros, se muestra a 2 fps: nunca más de 3 parpadeos por segundo) |
| ui-cartel-icono | 16x16 | 6 | REDOBLE (dos manos golpeando una mesa), SOPLEN (cara soplando), CONTÁ (mano con dedos), APLAUSOS (manos aplaudiendo), RISAS (cara riéndose), ¡UUUH! (cara sorprendida) |
| ui-zocalo | 320x12 | 1 | Franja `0` con borde superior `u` y a la izquierda una pestaña `u` de 64 px para «ÚLTIMO MOMENTO» |
| ui-torta-hud | 64x12 | 1 | Ícono de torta 12×10 y barra de 48×6 (marco `0`, relleno `X`, vacío `1`) |
| ui-botones | 12x12 | 6 | Saltar (⏩), pausa, sonido sí, sonido no, y la versión resaltada de saltar y pausa |
| ui-barra-carga | 120x10 | 1 | Barra de carga para «ACTUALIZANDO A FRAN 2.0… 99 %»: marco `4`, relleno `G` |

Exportá a `final/interfaz/` con sus JSON. Agregá todo al manifiesto.

Vistas con `componer.py` (×4), con textos de la pregunta 1 del guion elegido (si no hay, la versión A):
1. `vistas/escenas/pregunta_x4.png`: estudio, Fran en el monitor, caja de pregunta, 4 cápsulas neutras con su letra y texto, display en «1», escalera con el piso 1 actual, 3 comodines arriba, barra de la torta, botón saltar.
2. `vistas/escenas/revelacion_x4.png`: igual, con la B correcta, la D incorrecta y la escalera con el piso 1 en acierto.
3. `vistas/escenas/cartel-redoble_x4.png`: estudio con luces bajas y el cartel REDOBLE con su ícono en el centro.
4. `vistas/escenas/hud-caminata_x4.png`: exterior con zócalo abajo («ÚLTIMO MOMENTO: columna sigue en su lugar. Se investiga.»), un logro arriba a la derecha y la barra de la torta arriba a la izquierda.
5. `vistas/interfaz_todas.png`: todas las piezas a ×4 con su nombre.

Terminaste cuando:
- `validar.py` da OK en cada pieza.
- Existen las 5 vistas.
- En la vista 1 entran los textos de las 4 opciones (si no, decime cuáles no).

Informe según AGENTS.md.

---- HASTA ACÁ ----

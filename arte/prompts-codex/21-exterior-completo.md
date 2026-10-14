# 21 · Exterior completo en capas

> **Para vos:** el exterior es el escenario que más se usa (intro, caminatas, pórtico, final). Se arma en capas que se mueven a distinta velocidad cuando el personaje camina (parallax): cielo, ciudad lejana, torres, vereda y adornos de adelante. El pórtico con las columnas va aparte porque Lu choca contra una. Se dibuja una vez y el prompt 35 lo pasa a mediodía, atardecer y noche.
>
> **Antes:** style frame aprobado (05). Mejor con fotos de las torres y del pórtico en `referencias/fotos/`.

---- COPIAR DESDE ACÁ ----

Seguí AGENTS.md, sección "Proceso de escenario". Escenario: `esc-ext`. Partí de lo aprobado en el style frame.

Capas a producir:

| Capa | Tamaño | Manera | Se mueve al |
|---|---|---|---|
| `esc-ext_cielo-manana`, `-mediodia`, `-atardecer`, `-noche` | 320×180 | código (`cielo.py`) | 0 % |
| `esc-ext_ciudad` | 320×60, se repite en horizontal | código | 20 % |
| `esc-ext_torres` | 480×160, transparente arriba | imagen | 50 % |
| `esc-ext_vereda` | tiles de 16×16 | mapa | 100 % |
| `esc-ext_portico` | 96×72 | imagen | 100 % |
| `esc-ext_adornos` | 4 piezas de 16×32 | imagen | 100 % o 120 % |
| `esc-ext_ventanas-noche` | 480×160, transparente | código | 50 % |

1. **Cielos:** ampliá `herramientas/cielo.py` con cuatro cielos en bandas tramadas: mañana (`g` → `h` → `d`), mediodía (`f` → `g` → `h`), atardecer (`n` → `c` → `d`, con `X`), noche (`N` → `e`, con algunas estrellas en `4`). Nubes en mañana y mediodía; ninguna de noche.
2. **Ciudad:** rehacé `esc-ext_ciudad` para que se repita sin costura a los lados (el borde izquierdo continúa al derecho).
3. **Torres:** cargá el style frame y las fotos que haya. Generá una imagen panorámica 3:1:
   """
   Very wide panoramic 3:1 background layer of two office towers seen straight-on at morning light from the top-left: on the left third a tall square office tower (rectangular prism) with a regular grid facade and vertical warm orange stripes; on the right third a tall cylindrical office tower with vertical blue bands, windows that narrow toward the curved edges, and an elliptical roof; a lower glass connecting building between them; a few smaller generic low buildings at both ends. Only the buildings: the sky AND the ground are perfectly flat solid magenta #FF00FF. The bases of the buildings sit on a straight horizontal line at the bottom of the image.
   """
   Pixelá con `--id esc-ext --nombre torres --tipo fondo --cuadro 480x160 --fondo FF00FF --limpiar --colores "a b c d e f g h 1 2 3 4 W"`. Tiene que quedar transparente todo lo que era magenta.
4. **Vereda:** por mapa, 4 tiles de 16×16 que se repitan sin costura: vereda lisa, vereda con junta, cordón, asfalto. Tira `esc-ext_vereda` de 64×16.
5. **Pórtico:** generá sobre verde `A simple modern entrance portico seen straight-on: a flat concrete roof slab on two white cylindrical columns, open in the middle, nothing behind it.` (con el bloque de estilo de personajes de AGENTS.md, no el de fondo, porque está en el plano del personaje). Pixelá a `--cuadro 96x72 --tipo objeto --colores "1 2 3 4 h 9"` y `contorno.py`. Anotá en el manifiesto la posición x de cada columna (`columnas=x1,x2`).
6. **Adornos:** generá sobre magenta, cuatro piezas separadas: `a planter box with a green shrub`, `a modern street lamp`, `a simple bench`, `a small young tree in a square planter`. Pixelá con `--cuadro 16x32 --cuadros 4 --separar huecos --tipo objeto --fondo FF00FF --colores "1 2 3 4 i j k L M s"`, `contorno.py`.
7. **Ventanas de noche:** por código, detectá los píxeles de ventana de `esc-ext_torres` y hacé una capa con un 60 % de ellas encendidas en `W` y `d` (fijas, elegidas al azar con semilla fija).
8. Vista previa con `componer.py`, 4 escenas en `vistas/escenas/ext_<momento>_x4.png`: mañana, mediodía, atardecer y noche (la de noche con la capa de ventanas). Torres apoyadas sobre la vereda, pórtico en el medio, dos adornos, `val_base` y `cam_base` con pies en y=128. Esta vista todavía no cambia la paleta de las torres (eso es el prompt 35).

Terminaste cuando:
- `validar.py` da OK en todas las capas.
- La ciudad y la vereda se repiten sin costura: armá `vistas/ext_costuras.png` con cada una repetida 3 veces seguidas.
- Existen las 4 vistas de `vistas/escenas/ext_*_x4.png`.

Informe según AGENTS.md.

---- HASTA ACÁ ----

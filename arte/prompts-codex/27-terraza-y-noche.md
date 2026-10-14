# 27 · Terraza del piso 8 y final de noche

> **Para vos:** la última escena: la terraza al atardecer, la torta, las 12 velitas y la revelación del premio («VACACIONES GRATIS*» con letra chica: 15 minutos en esta misma terraza, con mate propio). Después baja la noche. La versión de noche sale cambiando colores y prendiendo guirnaldas, sin generar otra imagen.
>
> **Antes:** style frame aprobado. Mejor con fotos de la terraza o de la vista en `referencias/fotos/`.

---- COPIAR DESDE ACÁ ----

Seguí AGENTS.md, sección "Proceso de escenario". Si hay fotos `terraza*`, cargalas como "architecture reference".

**Escenario: `esc-terraza`**

"""
Rooftop terrace of an office tower at sunset: a wooden deck floor, a glass and steel railing along the back, potted plants and two planters, a string of small unlit bulbs hanging across the top of the image. In the center: a small round table, empty. Behind the railing: the city skyline in silhouette and a wide calm sea horizon, warm sunset sky with orange, pink and violet bands. Floor clear on both sides of the table.
"""
Colores: `c d X n m e f g i j k L M 1 2 3 W s`.

Anotá `mesa=x,y` (donde va la torta), `reposera=x,y` (lugar libre a la derecha para la reposera del premio) y `guirnalda=` las posiciones de cada foquito.

Versión de noche, por código:
- `esc-terraza_noche`: cielo con la rampa de noche (`N`, `e`, `f`), mar y ciudad más oscuros, algunas ventanas de la ciudad en `W`, y los foquitos de la guirnalda encendidos en `W` y `s`.
- `esc-terraza_noche-guirnalda`: una capa transparente solo con los foquitos encendidos, para que el juego los prenda de a uno.

Vistas previas:
- `vistas/escenas/terraza_x4.png`: atardecer, con la torta `ob-torta_base` (cuadro 4) en la mesa (si existe; si no, un rectángulo `P` de 24×20), el elenco que exista con los pies en el piso.
- `vistas/escenas/terraza-noche_x4.png`: de noche, con la reposera, el mate y el termo (si existen) en `reposera=x,y`.

Terminaste cuando:
- `validar.py esc-terraza_fondo esc-terraza_noche esc-terraza_noche-guirnalda` da OK.
- Existen las dos vistas previas.

Informe según AGENTS.md.

---- HASTA ACÁ ----

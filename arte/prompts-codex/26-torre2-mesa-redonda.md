# 26 · Torre 2 y la mesa redonda

> **Para vos:** el acto 3 (Sostenibilidad, atardecer, verde). Adentro de la torre redonda todo es curvo, y la mesa redonda del ROUNDTABLE ocupa el centro. Las personas sentadas son los extras del prompt 12, que el juego ubica alrededor. Es la escena "respiro": tranquila y cálida.
>
> **Antes:** style frame aprobado. Mejor con fotos del interior de la Torre 2 en `referencias/fotos/`.

---- COPIAR DESDE ACÁ ----

Seguí AGENTS.md, sección "Proceso de escenario". Si hay fotos `torre2*`, cargalas como "architecture reference".

**Escenario: `esc-torre2`**

"""
Interior of a floor inside a cylindrical office tower at sunset: the back wall is a gently curved glass facade with vertical blue mullions, warm orange-pink sunset light coming through and the city skyline in silhouette outside. In the center: a large round meeting table seen from the side (a wide flattened ellipse), with simple chairs around it, all empty. Green accents: plants along the curved wall (this area's color theme is green). Calm, warm atmosphere. Floor clear in front of the table.
"""
Colores: `i j k e f g h c d X 1 2 3 4 L M W`.

Anotá en el manifiesto:
- `mesa=x,y,w,h`.
- `asientos=` una lista de 16 posiciones x,y alrededor de la mesa donde el juego sienta a los extras: 8 del lado de atrás (se ven enteros) y 8 del lado de adelante (se ven de espaldas o tapados por la mesa; si no se pueden ver, usá 12 atrás y 4 en los extremos).

Vista previa: `vistas/escenas/torre2_x4.png` con 16 `ext_sentado-*` (si existen; si no, rectángulos grises de 16×16) en los asientos, la gaviota `gav_sentada` en uno de ellos, `cam_base` y `lu_base` de pie adelante.

Terminaste cuando:
- `validar.py esc-torre2_fondo` da OK.
- El manifiesto tiene `mesa=` y 16 `asientos=`.
- Existe la vista previa.

Informe según AGENTS.md.

---- HASTA ACÁ ----

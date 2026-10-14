# 91 · Plantilla para pedir una pieza nueva

> **Para vos:** para algo que no está en la lista (por ejemplo, el logo cuando haya nombre, un personaje nuevo o un objeto que sumó el guion). Completá lo que está entre `< >`. Si es un personaje que es una persona real, primero pedile el OK.

---- COPIAR DESDE ACÁ ----

Seguí AGENTS.md. Pieza nueva.

- Nombre: `<id>_<accion>`, por ejemplo `ob-trofeo` o `ui-logo`.
- Qué es: `<descripción en una o dos frases, en español>`.
- Dónde aparece: `<escena o pantalla>`.
- Tamaño de cuadro: `<ancho>x<alto>`; cuadros: `<N>`; fps: `<n>`; bucle: `<sí/no>`.
- Colores: `<códigos de la paleta>` (si no sabés, elegilos vos dentro de la paleta y decime cuáles usaste).
- Manera: `<imagen / mapa / código>` (si no sabés, elegí según AGENTS.md: imagen para 24 px o más, mapa para lo chico, código para interfaz).

Si es por imagen:
1. Cargá con `view_image` `referencias/style-frame.png` como "style reference" (y la ficha del personaje si corresponde).
2. Escribí la descripción en inglés con la estructura de AGENTS.md (qué es, pose, vista de costado mirando a la derecha, tamaño en píxeles ampliado, bloque de estilo, fondo verde o magenta, sin texto). Mostrámela antes de generar.
3. Seguí el proceso obligatorio de AGENTS.md.

**Caso logo** (`ui-logo`): el nombre del juego es `<NOMBRE>`. Hacelo por código y mapa, no por imagen: letras de la fuente grande rediseñadas a 2 o 3 veces su tamaño, con contorno `0`, relleno en rampa `c`/`d`/`s`, una sombra de 2 px en `a` y un detalle de las dos torres (naranja y azul) integrado. Tiene que entrar en `logo=` del manifiesto (`esc-titulo`). Dame 3 propuestas lado a lado en `vistas/logo_propuestas.png` (×4) antes de elegir.

Terminaste cuando `validar.py <pieza>` da OK y existe su vista. Informe según AGENTS.md.

---- HASTA ACÁ ----

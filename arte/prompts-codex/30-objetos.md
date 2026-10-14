# 30 · Objetos de la historia

> **Para vos:** todas las cosas que los personajes usan o que aparecen en escena: la torta y sus velitas, el botón rojo, la barrera, el colchón de la columna, las cajas de la mudanza, el control del "jugador 2", el afiche del premio y la lupa, la reposera con el mate, los post-its. Los carteles salen en blanco: el juego les escribe encima. Lo grande se genera; lo chico, Codex lo dibuja por mapa.
>
> **Antes:** Puerta 3 para la torta (depende de que el guion mantenga la misión de la torta). El resto se puede hacer ya, después del style frame.

---- COPIAR DESDE ACÁ ----

Seguí AGENTS.md. Tarea: objetos (`ob-…`). Todos con `--tipo objeto`, `contorno.py` y anclados abajo, salvo que diga otra cosa. Cada fila es una pieza `<id>_base` (por ejemplo `ob-torta_base`, con sus 4 cuadros).

| Pieza | Cuadro | Cuadros | Manera | Qué es |
|---|---|---|---|---|
| ob-torta | 24x20 | 4 | imagen (estado 1) + mapa (2–4) | 1: caja de torta abierta con una torta blanca con crema y frutillas (100 %). 2: la misma con confeti de colores encima (97 %). 3: con un rectángulo de sello rojo en un costado, sin letras (90 %). 4: le falta una porción en triángulo (75 %) |
| ob-velita | 2x6 | 1 | mapa | Velita de cumpleaños a rayas `4`/`X` |
| ob-llama | 3x4 | 2 | mapa | Llamita en `K`, `s`, `W`; 2 posiciones, 8 fps, bucle |
| ob-humito | 3x5 | 2 | mapa | Humo de velita apagada en `3`/`2` |
| ob-porcion | 6x5 | 1 | mapa | La porción que roba la gaviota |
| ob-boton | 16x16 | 2 | mapa | Botón rojo enorme sobre un pedestal gris: normal y apretado (1 px más bajo) |
| ob-sello-marca | 24x10 | 1 | mapa | Marco rectangular rojo `t` de sello, vacío (el juego escribe VALIDADO) |
| ob-barrera | 48x48 | 3 | imagen (cerrada) + código (girar) | Barrera de cochera a rayas `u`/`4` sobre un poste gris, anclada abajo a la izquierda: cerrada (horizontal), subiendo (45°), abierta (vertical). Girá por código con vecino más cercano y limpiá por mapa |
| ob-colchon | 20x32 | 1 | imagen | Colchón azul y blanco atado alrededor de una columna (se superpone a la columna) |
| ob-cono | 8x10 | 1 | imagen | Cono de tránsito naranja con franja blanca |
| ob-casco | 20x10 | 1 | imagen | Casco amarillo de obra gigante para la Columna 2.0 |
| ob-airbag | 24x16 | 1 | imagen | Airbag blanco inflado |
| ob-cartelito | 12x8 | 1 | mapa | Cartelito blanco en un palito (el de la columna: «Yo estaba primero.») |
| ob-cartel-pronto | 48x32 | 1 | mapa | Cartel de obra en blanco sobre dos postes (el juego escribe «PRÓXIMAMENTE: PUNTA DEL ESTE») |
| ob-caja | 16x16 | 2 | mapa | Caja de cartón `M`/`L` con cinta; la 2 con un rectángulo de etiqueta en blanco |
| ob-control | 16x12 | 1 | mapa | Joystick genérico de dos botones con cable, sin marca |
| ob-credencial | 8x10 | 1 | mapa | Credencial colgante con área en blanco (el juego escribe VISITANTE, CASI, EQUIPO) |
| ob-afiche | 96x64 | 1 | imagen | Marco de afiche publicitario retro con sol radiante y una palmera en una esquina, centro en blanco |
| ob-lupa | 16x16 | 1 | mapa | Lupa con mango `L`/`M` y vidrio `h` con brillo `4` |
| ob-reposera | 24x16 | 1 | imagen | Reposera de playa a rayas `c`/`4` |
| ob-mate | 8x8 | 1 | mapa | Mate con bombilla |
| ob-termo | 6x14 | 1 | mapa | Termo `1`/`2` |
| ob-mate-premio | 12x12 | 2 | mapa | Mate coleccionable con un destello que alterna; 4 fps, bucle |
| ob-postit | 6x6 | 4 | mapa | Post-it cuadrado en `s`, `X`, `k` y `h`, con la esquina doblada |
| ob-folleto | 4x5 | 1 | mapa | Folleto blanco doblado |

Generaciones con la herramienta integrada (con `referencias/style-frame.png` como "style reference" y el bloque de estilo de personajes de AGENTS.md; fondo verde salvo que el objeto sea verde):

1. `ob-torta` estado 1: `A cute birthday cake in an open white cake box, side view: white frosting, a row of red strawberries on top, cream layers visible. Drawn as a 24 by 20 pixel sprite enlarged so each art pixel is a 16 by 16 block.` Colores `4 3 P Q X u t v L M 9`.
2. Un juego de cuatro piezas separadas, después recortadas: `four separate objects with wide gaps: a blue and white striped mattress strapped vertically as if wrapped around a pole; an orange traffic cone with a white stripe; a giant yellow construction hard hat; a puffy white inflated airbag.` Colores `f g h 4 3 c d s 2 1 9`.
3. `ob-barrera` cerrada: `a parking barrier gate, closed: a grey post with a long horizontal red and white striped arm extending to the right.` Colores `u 4 3 2 1 9`.
4. `ob-afiche`: `an empty retro advertising poster frame: decorative border, a radiant sun in the top right corner and a small palm tree in the bottom left corner, the center is a large plain cream area with nothing on it.` Colores `c d s P Q j k L M 9`. `--ancla centro`.
5. `ob-reposera`: `a striped beach deck chair, side view, unfolded.` Colores `c 4 L M 9`.

Recordatorios: la torta tiene que leerse a escala del juego en las manos del protagonista (comprobalo en la vista); las velitas: anotá en el manifiesto, en `ob-torta_base`, `velas=` 12 posiciones x,y sobre la torta (el juego pone una `ob-velita` y una `ob-llama` en cada una).

Al final:
1. `vistas/objetos_todos.png`: todos los objetos a ×6 con su nombre.
2. Con `componer.py`, `vistas/escenas/velitas_x4.png`: la terraza (si existe) con `ob-torta` estado 4 en la mesa, 12 velitas, 8 encendidas y 4 con humito.

Terminaste cuando:
- `validar.py` da OK en cada pieza.
- `ob-torta_base` tiene `velas=` con 12 posiciones.
- Existen las dos vistas.

Informe según AGENTS.md, con una línea por pieza.

---- HASTA ACÁ ----

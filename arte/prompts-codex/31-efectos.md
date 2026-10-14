# 31 · Efectos y partículas

> **Para vos:** las piezas chiquitas que el juego multiplica y mueve: confeti, chispas, humo, estrellitas del choque, el fuego del dragón, notas musicales, los pedacitos de la respuesta que rompe la pelota, los fuegos artificiales del final. Son tan chicas que Codex las dibuja directamente píxel por píxel, sin generar imágenes.
>
> **Antes:** prompt 01. Se puede hacer en cualquier momento.

---- COPIAR DESDE ACÁ ----

Seguí AGENTS.md. Tarea: efectos (`ef-…`), todos por mapa (manera 2), sin generar imágenes. Cada fila es una pieza `<id>_base` (por ejemplo `ef-humo_base`), con ancla `centro`. Alfa binaria: las transparencias se simulan con tramado (un píxel sí, uno no).

| Pieza | Cuadro | Cuadros | fps | Bucle | Qué es |
|---|---|---|---|---|---|
| ef-confeti | 2x2 | 6 | — | — | Un cuadradito por color: `u`, `s`, `k`, `h`, `X`, `c` (el juego elige uno al azar) |
| ef-chispa | 3x3 | 2 | 10 | sí | Chispa en `s`/`K`: cruz y punto |
| ef-humo | 8x8 | 3 | 8 | no | Nube `3` con borde `2` que se agranda y se deshace en tramado |
| ef-polvo | 6x4 | 3 | 10 | no | Polvo al pisar o chocar, en `3`/`2` |
| ef-estrellas | 7x7 | 2 | 6 | sí | Estrellita de golpe `s` con brillo `4`, dos tamaños |
| ef-fuego | 24x12 | 3 | 10 | sí | Llamarada del dragón hacia la derecha: núcleo `W`/`s`, cuerpo `K`, bordes `u`; se ensancha al final |
| ef-cono-luz | 48x32 | 1 | — | — | Haz de linterna hacia la derecha, en tramado `W` sobre transparente (ancho al final, angosto al empezar) |
| ef-notas | 6x8 | 2 | 4 | sí | Nota musical `4` con borde `1`, dos inclinaciones |
| ef-ladrillo | 4x4 | 3 | — | — | Pedacitos de cápsula rota en `f`, `g` y `h` |
| ef-gotita | 3x4 | 1 | — | — | Gota de sudor `h` con brillo `4` |
| ef-ondas | 8x8 | 2 | 4 | sí | Dos ondas curvas de sonido (el "BIP BIP" del camión, sin letras) |
| ef-adelantar | 8x8 | 2 | 3 | sí | Ícono ⏩ en `4` con borde `0`, encendido y apagado |
| ef-brillo | 5x5 | 2 | 6 | sí | Destello en cruz `4`/`s` |
| ef-fuegos-chispa | 3x3 | 2 | 10 | sí | Chispa de fuegos artificiales (el juego arma la explosión y le cambia el color) |
| ef-lagrima | 1x2 | 1 | — | — | La lágrima de un píxel de Fran, en `h` |
| ef-iris | — | — | — | — | No es una pieza: anotá en `INFORME.md` que la transición de iris la hace el juego (círculo que se cierra, borde de 1 px `0`) |

Al final:
1. `vistas/efectos_todos.png`: todos a ×8, con su nombre, sobre fondo `1` (para ver los claros).
2. Un GIF por cada efecto con bucle.
3. Con `componer.py`, `vistas/escenas/efectos_x4.png`: el exterior con `ob-auto_chocado` (si existe), 3 `ef-estrellas` y 2 `ef-humo` sobre el capó; y a la derecha 30 `ef-confeti` desparramados.

Terminaste cuando:
- `validar.py` da OK en cada pieza.
- Existen la vista general, los GIF y la escena.

Informe según AGENTS.md.

---- HASTA ACÁ ----

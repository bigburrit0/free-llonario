# 20 · Animaciones de la gaviota, los extras y el camión

> **Para vos:** la gaviota vuela, roba una porción de torta y tilda la checklist con casco. Los extras caminan (la fila de los 25 es un mismo empresario repetido en 3 variantes de color), saludan, sellan cajas y aplauden en la mesa redonda. El camión da marcha atrás.
>
> **Antes:** Puerta 3.

---- COPIAR DESDE ACÁ ----

Seguí AGENTS.md, sección "Proceso de animación". Personajes: `gav` (bases `gav_base`, `gav_casco`, `gav_sentada`), `ext` (bases `ext_empresario`, `ext_operario`, `ext_sentado`) y `ob-camion` (base `ob-camion_base`).

| # | Pieza | Cuadros | Cuadro | fps | Bucle | Manera | Notas |
|---|---|---|---|---|---|---|---|
| 1 | gav_quieta | 2 | 16x12 | 3 | sí | mapa | La cabeza baja 1 px en el cuadro 2 |
| 2 | gav_volar | 4 | 16x16 | 10 | sí | imagen | `--ancla centro` |
| 3 | gav_robar | 3 | 16x16 | 8 | no | imagen | `--ancla centro` |
| 4 | gav_tildar | 2 | 16x12 | 4 | sí | mapa | Desde `gav_casco`: el lápiz arriba / abajo |
| 5 | ext_empresario-caminar | 4 | 16x24 | 8 | sí | imagen | Caminar estándar, cabeza fija `0,-1,0,-1` |
| 6 | ext_empresario-saludar | 2 | 16x24 | 6 | sí | mapa | Mano levantada a un lado y al otro |
| 7 | ext_operario-sellar | 3 | 16x24 | 8 | sí | imagen | — |
| 8 | ext_sentado-aplaudir | 2 | 16x16 | 8 | sí | mapa | Manos separadas / juntas |
| 9 | ob-camion_reversa | 2 | 64x40 | 6 | sí | mapa | Ruedas giradas, carrocería sube 1 px en el cuadro 2, luces traseras alternan `u` y `v` |

Descripciones (en inglés):

- **gav_volar:** `Side view facing right, flying. Frame 1: wings fully up. Frame 2: wings level, mid-stroke. Frame 3: wings fully down. Frame 4: wings level again.`
- **gav_robar:** `Frame 1: swooping down diagonally, beak open. Frame 2: grabbing a small slice of cake in its beak (cream and pink layers). Frame 3: flying up and away with the slice in its beak, smug face.`
- **ext_operario-sellar:** `Frame 1: rubber stamp raised high with both hands. Frame 2: stamp pressed down firmly at waist height, body leaning forward. Frame 3: lifting the stamp, looking pleased.`

Después, con `herramientas/variantes.py` (prompt 12), generá las variantes de color de las filas 5 y 6 (`-1`, `-2`, `-3`) y de la fila 8 (`-1` a `-4`), con las mismas tablas de cambio de la ficha.

Al final:
1. `vistas/gav-ext_animaciones.png`: todas las tiras a ×6 con su nombre.
2. Con `componer.py`, `vistas/escenas/fila-25_x4.png`: el hall del piso 6 (`esc-piso6`) si ya existe (si no, gris liso), `age_bandera-caminar` adelante y 7 empresarios detrás alternando variantes y cuadros de caminata.

Terminaste cuando:
- `validar.py` da OK en cada pieza y cada variante.
- Existe un GIF por pieza y las dos vistas finales.

Informe según AGENTS.md, con una línea por pieza.

---- HASTA ACÁ ----

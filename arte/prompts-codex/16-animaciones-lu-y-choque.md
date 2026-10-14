# 16 · Animaciones de Lu y el choque del Suzuki

> **Para vos:** el arranque del juego: el Suzuki entra, choca contra la columna (sin daño a nadie, solo al capó), Lu baja y mira la columna. Más tarde estaciona perfecto. Las estrellitas y el humo son efectos aparte (prompt 31).
>
> **Antes:** Puerta 3 y el OK de Lu con el choque.

---- COPIAR DESDE ACÁ ----

Seguí AGENTS.md, sección "Proceso de animación". Personajes: `lu` (base `lu_base`, de frente `lu_frente`) y `ob-auto` (base `ob-auto_base`).

| # | Pieza | Cuadros | Cuadro | fps | Bucle | Manera | Rebote / notas |
|---|---|---|---|---|---|---|---|
| 1 | lu_quieta | 2 | 16x24 | 3 | sí | mapa | Quieto estándar |
| 2 | lu_hablar | 2 | 16x24 | 6 | sí | mapa | Hablar estándar |
| 3 | lu_caminar | 4 | 16x24 | 8 | sí | imagen | Caminar estándar, cabeza fija `0,-1,0,-1`. El pelo largo puede moverse 1 px atrás en los cuadros 2 y 4 |
| 4 | lu_bajar-auto | 3 | 16x24 | 8 | no | imagen | — |
| 5 | lu_mirar-arriba | 1 | 16x24 | 1 | no | mapa | Desde `lu_base`: cabeza 1 px hacia atrás, ojos mirando arriba (a la columna) |
| 6 | ob-auto_andar | 2 | 48x24 | 8 | sí | mapa | Rayos de las ruedas girados; en el cuadro 2 la carrocería sube 1 px |
| 7 | ob-auto_choque | 3 | 48x24 | 10 | no | imagen | Cargá `ob-auto_base` como "identity reference" |
| 8 | ob-auto_chocado | 1 | 48x24 | 1 | no | mapa | Igual al cuadro 3 del choque, quieto |
| 9 | ob-auto_puerta | 1 | 48x24 | 1 | no | mapa | `ob-auto_chocado` con la puerta del conductor abierta (interior en `1`) |

Descripciones por cuadro (en inglés):

- **lu_bajar-auto:** `Stepping out of a car (the car is not drawn). Frame 1: crouched with the head ducked low, one leg forward. Frame 2: rising, one foot planted forward, one hand resting on an invisible car door. Frame 3: standing straight, looking ahead, calm.`
- **ob-auto_choque:** `The same small red car crashes front-first into a wall on its right (the wall is not drawn). Frame 1: impact, front bumper flattened by two pixels, rear wheels lifting slightly. Frame 2: maximum squash, the hood crumpled upward, the whole car compressed horizontally and tilted forward. Frame 3: rebound, car back to almost normal length but with a crumpled hood. Cartoon style, nothing broken off, no fire.`

Al final:
1. `vistas/lu-auto_animaciones.png`: todas las tiras a ×6 con su nombre.
2. Con `componer.py`, la secuencia del choque en 4 escenas de 320×180 sobre el exterior (`vistas/escenas/choque_1_x4.png` a `_4`): auto andando a la izquierda del pórtico; impacto contra la columna izquierda (cuadro 2 del choque); auto chocado con la puerta abierta y Lu bajando (cuadro 2); Lu mirando arriba al lado de la columna.

Terminaste cuando:
- `validar.py` da OK en cada pieza.
- Existe un GIF por pieza y las cuatro escenas.

Informe según AGENTS.md, con una línea por pieza.

---- HASTA ACÁ ----

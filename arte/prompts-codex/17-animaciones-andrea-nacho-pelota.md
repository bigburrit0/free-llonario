# 17 · Animaciones de Andrea, Nacho y la pelota

> **Para vos:** Andrea "cierra" todo con un toque (si eligió ese gag; si eligió la barbera, se suma afeitar). Nacho pica la pelota gigante, saca (el comodín que rompe dos respuestas), la gira como un globo terráqueo y cuenta. La pelota que cruza la pantalla la mueve el juego; acá solo rueda.
>
> **Antes:** Puerta 3, el gag que eligió Andrea y el OK de Nacho. Si Andrea eligió otro gag que no sea la que cierra ni la barbera, borrá las filas 4 y 5 antes de pegar.

---- COPIAR DESDE ACÁ ----

Seguí AGENTS.md, sección "Proceso de animación". Personajes: `and` (base `and_base`, de frente `and_frente`), `nac` (bases `nac_base`, `nac_frente`, `nac_raqueta`) y `ob-pelota` (base `ob-pelota_base`).

| # | Pieza | Cuadros | Cuadro | fps | Bucle | Manera | Rebote / notas |
|---|---|---|---|---|---|---|---|
| 1 | and_quieta | 2 | 16x24 | 3 | sí | mapa | Quieto estándar |
| 2 | and_hablar | 2 | 16x24 | 6 | sí | mapa | Hablar estándar |
| 3 | and_caminar | 4 | 16x24 | 8 | sí | imagen | Caminar estándar, cabeza fija `0,-1,0,-1` |
| 4 | and_completar | 3 | 16x24 | 8 | no | imagen | Gag "la que cierra" |
| 5 | and_afeitar | 3 | 16x24 | 10 | no | imagen | Solo si eligió "la barbera" |
| 6 | and_frente-arriba | 1 | 16x24 | 1 | no | mapa | Desde `and_frente`: ojos arriba |
| 7 | nac_quieto | 2 | 16x24 | 3 | sí | mapa | Desde `nac_base`: en el cuadro 2 la pelota baja 3 px (la pica) |
| 8 | nac_caminar | 4 | 16x24 | 8 | sí | imagen | Caminar estándar con la pelota bajo el brazo, cabeza fija `0,-1,0,-1` |
| 9 | nac_saque | 5 | 16x24 | 10 | no | imagen | Usá `nac_raqueta` como base. Sin pelota dibujada |
| 10 | nac_globo | 3 | 16x24 | 6 | sí | mapa | Desde `nac_base`: la pelota apoyada en un dedo levantado; las costuras en 3 posiciones de giro |
| 11 | nac_contar | 2 | 16x24 | 4 | no | mapa | Cuadro 1: un dedo levantado. Cuadro 2: dos dedos |
| 12 | nac_frente-arriba | 1 | 16x24 | 1 | no | mapa | Desde `nac_frente`: ojos arriba |
| 13 | ob-pelota_rodar | 4 | 16x16 | 10 | sí | mapa | Las costuras giran 90° por cuadro |

Descripciones por cuadro (en inglés):

- **and_completar:** `Frame 1: raising the right index finger with a confident look. Frame 2: tapping forward in the air with the arm fully extended, as if pressing a floating button. Frame 3: arm down, small satisfied smile, eyes closed for a moment.`
- **and_afeitar:** `Frame 1: holding a small electric razor up near the face, determined look. Frame 2: one swift swipe forward and down with the arm extended. Frame 3: brushing off the hands, proud.`
- **nac_saque:** `Tennis serve, no ball drawn. Frame 1: ready stance holding the racket low. Frame 2: free hand raised high as if tossing a ball, racket still low. Frame 3: racket swung back behind the head, body arched. Frame 4: hitting high in front, arm fully extended upward. Frame 5: follow-through, racket down across the body.`

Al final:
1. `vistas/and-nac_animaciones.png`: todas las tiras a ×6 con su nombre.
2. Con `componer.py`, `vistas/escenas/saque_x4.png`: el fondo `esc-estudio` si ya existe (si no, gris liso), Nacho en el cuadro 4 del saque a la izquierda y la pelota a mitad de camino hacia la derecha.

Terminaste cuando:
- `validar.py` da OK en cada pieza hecha.
- Existe un GIF por pieza y las dos vistas finales.

Informe según AGENTS.md, con una línea por pieza.

---- HASTA ACÁ ----

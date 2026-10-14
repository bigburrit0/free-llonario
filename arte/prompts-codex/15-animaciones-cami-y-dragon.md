# 15 · Animaciones de Cami y el dragoncito

> **Para vos:** Cami camina, habla, saluda cuando se suma al equipo y gira en la silla de rueditas en la mesa redonda (si el guion nuevo lo mantiene). El dragón tiene su arco: estornuda chispas inútiles, hace de linterna y al final prende las velitas con una llamarada. El fuego y las chispas son efectos aparte (prompt 31).
>
> **Antes:** Puerta 3.

---- COPIAR DESDE ACÁ ----

Seguí AGENTS.md, sección "Proceso de animación". Personajes: `cam` (base `cam_base`, de frente `cam_frente`) y `drg` (bases `drg_base`, `drg_hombro`, `drg_volar-ref`; fondo magenta para las imágenes del dragón).

| # | Pieza | Cuadros | Cuadro | fps | Bucle | Manera | Rebote / notas |
|---|---|---|---|---|---|---|---|
| 1 | cam_quieta | 2 | 16x24 | 3 | sí | mapa | Quieto estándar |
| 2 | cam_hablar | 2 | 16x24 | 6 | sí | mapa | Hablar estándar |
| 3 | cam_caminar | 4 | 16x24 | 8 | sí | imagen | Caminar estándar, cabeza fija `0,-1,0,-1` |
| 4 | cam_saludo | 2 | 16x24 | 6 | sí | mapa | Cuadro 1: brazo levantado con la mano abierta sobre la cabeza. Cuadro 2: la mano inclinada hacia el otro lado |
| 5 | cam_frente-arriba | 1 | 16x24 | 1 | no | mapa | Desde `cam_frente`: ojos mirando hacia arriba |
| 6 | cam_silla | 4 | 16x24 | 6 | sí | imagen | Incluye la silla. Sin cabeza fija (gira) |
| 7 | drg_hombro-anim | 2 | 12x12 | 3 | sí | mapa | Desde `drg_hombro`: la cola se mueve 1 px |
| 8 | drg_estornudo | 3 | 12x12 | 8 | no | imagen | — |
| 9 | drg_llamarada | 4 | 12x12 | 8 | no | imagen | Sin fuego dibujado |
| 10 | drg_linterna | 1 | 12x12 | 1 | no | mapa | Boca abierta con brillo `W` adentro; el haz de luz lo hace el juego |
| 11 | drg_volar | 2 | 12x12 | 6 | sí | mapa | Desde `drg_volar-ref`: alas arriba y alas abajo |

Descripciones por cuadro (en inglés):

- **cam_silla:** `Sitting on a small office chair with wheels, spinning in place. Frame 1: side view facing right. Frame 2: front view facing the viewer. Frame 3: side view facing left. Frame 4: back view. The chair is the same in all frames.`
- **drg_estornudo:** `Frame 1: inhaling, body puffed up, eyes half closed, head tilted back. Frame 2: sneezing, head jerked forward, eyes shut tight, mouth open. Frame 3: recovered, surprised blink, mouth closed.`
- **drg_llamarada:** `Frame 1: big inhale, body squashed and puffed up. Frame 2: stretching the neck forward, mouth starting to open. Frame 3: mouth wide open, breathing out, no fire drawn. Frame 4: same as frame 3, holding.`

Notas:
- Cuando Cami camina con el dragón en el hombro, el juego mueve el dragón con el mismo rebote que la cabeza. Anotá en el manifiesto, en `cam_caminar`, `dragon-rebote=0,-1,0,-1`.
- Si el guion final no tiene la silla, salteá la fila 6 y avisá.

Al final:
1. `vistas/cam-drg_animaciones.png`: todas las tiras a ×6 con su nombre.
2. Con `componer.py`, `vistas/escenas/cam_prueba_x4.png`: Cami caminando (cuadro 3) con el dragón en el hombro, y el dragón suelto en el cuadro 3 de `drg_llamarada` a la derecha.

Terminaste cuando:
- `validar.py` da OK en cada pieza hecha.
- Existe un GIF por pieza y las dos vistas finales.

Informe según AGENTS.md, con una línea por pieza.

---- HASTA ACÁ ----

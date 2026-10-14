# 14 · Animaciones de Valentino

> **Para vos:** el protagonista es el que más se mueve. Quieto, hablar y festejar salen editando su ficha (baratos); caminar, sorpresa, apretar el botón, el brazo-sello y caminar agachado se generan como imagen. La barra de carga en el pecho va solo si eligió una variante robot. "Caminar con la torta" espera a que la torta esté aprobada (prompt 30) y a que el guion la mantenga.
>
> **Antes:** Puerta 3 (guion definitivo y prototipo cronometrado). Si el guion nuevo saca o suma acciones, editá la tabla antes de pegar.

---- COPIAR DESDE ACÁ ----

Seguí AGENTS.md, sección "Proceso de animación". Personaje: `val`, rasgos de su fila en la tabla de fichas. Base: `val_base`; de frente: `val_frente`.

| # | Acción | Cuadros | Cuadro | fps | Bucle | Manera | Rebote / notas |
|---|---|---|---|---|---|---|---|
| 1 | quieto | 2 | 16x24 | 3 | sí | mapa | Quieto estándar |
| 2 | hablar | 2 | 16x24 | 6 | sí | mapa | Hablar estándar |
| 3 | caminar | 4 | 16x24 | 8 | sí | imagen | Caminar estándar, cabeza fija `0,-1,0,-1` |
| 4 | sorpresa | 2 | 16x24 | 6 | no | imagen | — |
| 5 | apretar-boton | 3 | 16x24 | 8 | no | imagen | — |
| 6 | brazo-sello | 6 | 48x24 | 10 | no | imagen | `--ancla abajo-izq`; el cuerpo queda en x=0..15 en los 6 cuadros, igual que la base |
| 7 | agachado | 4 | 16x24 | 8 | sí | imagen | Cabeza fija, corrida hacia abajo lo que baje el cuerpo |
| 8 | festejar | 2 | 16x24 | 6 | sí | mapa | Cuadro 1: brazos arriba, ojos contentos. Cuadro 2: brazos a la altura de los hombros |
| 9 | carga-pecho | 3 | 16x24 | 4 | no | mapa | Solo variantes robot: en el pecho, barra de carga en `G` a 1/3, 2/3 y llena |
| 10 | frente-arriba | 1 | 16x24 | 1 | no | mapa | Desde `val_frente`: ojos mirando hacia arriba (display del ascensor) |
| 11 | caminar-torta | 4 | 16x24 | 8 | sí | imagen | **Solo si existe `ob-torta_base` aprobado** (cuadro 1); cargalo también como "object reference". Cabeza fija `0,-1,0,-1` |

Descripciones por cuadro para las acciones por imagen (en inglés, para el bloque "Frame 1: …"):

- **sorpresa:** `Frame 1: looking back over the shoulder toward the left with a puzzled face, body still facing right. Frame 2: jumping back slightly with both arms raised, eyes wide open, surprised.`
- **apretar-boton:** `Frame 1: reaching forward with the right arm extended at chest height. Frame 2: pressing down firmly, body squashed one pixel lower, arm straight down in front. Frame 3: arm back at the side, satisfied little smile.`
- **brazo-sello:** `The character's arm is telescopic and holds a big rubber stamp with a plain red handle and a flat bottom, no text. Frame 1: winding up, arm pulled back, stamp raised. Frame 2: arm extending to the right, half extended, stamp still raised. Frame 3: arm fully extended far to the right, about twice the body width, stamp pressing down at waist height. Frame 4: arm retracting halfway. Frame 5: arm fully extended again, stamping, slight squash. Frame 6: smear frame showing three overlapping copies of the extended arm and stamp at slightly different heights, as if stamping very fast.` Si la variante es piloto, el brazo es del robot.
- **agachado:** `Crouched walk: knees deeply bent, head lowered about a third of the body height, back slightly hunched, small careful steps. Frame 1: right foot forward. Frame 2: feet together. Frame 3: left foot forward. Frame 4: feet together.`
- **caminar-torta:** Caminar estándar, agregando `walking carefully while carrying a white cake box with both hands in front of the chest, matching the object reference`.

Al final:
1. `vistas/val_animaciones.png`: todas las tiras a ×6, una debajo de otra, con el nombre de cada una.
2. Con `componer.py`, `vistas/escenas/val_prueba_x4.png`: el exterior del style frame con Valentino en el cuadro 3 de `caminar` y, a la derecha, el cuadro 3 de `brazo-sello`.

Terminaste cuando:
- `validar.py` da OK en cada `val_<accion>` hecha.
- Existe un GIF en `vistas/` por cada acción.
- Existen `vistas/val_animaciones.png` y `vistas/escenas/val_prueba_x4.png`.

Informe según AGENTS.md, con una línea por acción.

---- HASTA ACÁ ----

**Qué mirar:** abrí los GIF. ¿Valentino es el mismo en todos los cuadros? ¿Caminar se ve fluido y no "patina"? Para corregir un cuadro, usá la plantilla 90.

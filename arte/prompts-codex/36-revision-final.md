# 36 · Revisión final y entrega al juego

> **Para vos:** Codex revisa todo de punta a punta: que cada pieza pase la revisión, que no falte nada del inventario del plan, que los personajes tengan alturas y estilo parejos, y arma el paquete para quien programe el juego (un archivo con la lista de piezas y un instructivo). Te devuelve una lista de lo que falta o hay que corregir.
>
> **Antes:** todo lo demás hecho y aprobado.

---- COPIAR DESDE ACÁ ----

Seguí AGENTS.md. Tarea: revisión general y paquete de entrega. No generes imágenes ni cambies piezas aprobadas; si encontrás algo para corregir, anotalo.

1. `python herramientas/validar.py --todo`. Copiá la salida completa a `INFORME.md`.
2. **Faltantes**: compará `manifiesto.csv` con el inventario de `PLAN-ARTE.md` (secciones "Inventario completo" y las tablas de los prompts 14 a 34). Escribí `vistas/faltantes.txt`: una línea por pieza del inventario con `LISTA`, `FALTA`, `SIN APROBAR` o `DESCARTADA (motivo)`.
3. **Parejo**:
   - `vistas/elenco_alturas.png` ×6: todos los personajes de 16×24 en su cuadro base, lado a lado sobre una línea de piso, con una regla de alto a la izquierda.
   - `vistas/colores_por_pieza.txt`: por pieza, cuántos colores usa y cuáles; marcá las que pasen de 16 (o 24 en fondos).
   - Revisá que todas las piezas de personajes miren a la derecha (salvo `ob-camion`) y estén ancladas abajo.
4. **Hoja general**: `python herramientas/hoja.py --todo` → `vistas/hoja-general.png`.
5. **Recorrido**: con `componer.py`, una escena por bloque del guion (intro, E1 a E8, ascensor, pórtico, final, créditos), cada una con su fondo, sus personajes en una pose clave y su interfaz, en `vistas/recorrido/NN_<bloque>_x4.png`. Es la primera vez que se ve el juego entero en imágenes fijas.
6. **Paquete para el juego**:
   - `manifiesto.json` generado desde `manifiesto.csv`: por pieza, archivo, tipo, tamaño de cuadro, cantidad de cuadros, fps, bucle, ancla y las notas como campos (`piso`, `hombro`, `display`, `velas`, `asientos`, etc.).
   - `LEEME-JUEGO.md`: cómo están armadas las tiras, el ancla, qué espeja el juego, las capas del parallax y sus velocidades (cielo 0 %, ciudad 20 %, torres 50 %, vereda y pórtico 100 %, adornos de adelante 120 %), las tablas de paleta, las fuentes (atlas + JSON), las cajas de 9 piezas, y la lista de lo que hace el juego por código (temblores, zoom, iris, partículas, crecer, parpadeos de 3 por segundo como máximo).
   - `entrega/arte-v1.zip` con `final/`, `paleta/`, `manifiesto.json` y `LEEME-JUEGO.md` (con el módulo `zipfile` de Python).

Terminaste cuando:
- `validar.py --todo` da OK en todo, o `INFORME.md` lista cada FALLA con su pieza.
- Existen `vistas/faltantes.txt`, `vistas/elenco_alturas.png`, `vistas/colores_por_pieza.txt`, `vistas/hoja-general.png` y las escenas de `vistas/recorrido/`.
- Existen `manifiesto.json`, `LEEME-JUEGO.md` y `entrega/arte-v1.zip`.

Informe según AGENTS.md, con un resumen: piezas listas, faltantes, sin aprobar y fallas.

---- HASTA ACÁ ----

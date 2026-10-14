# 05 · Style frame: una pantalla terminada

> **Para vos:** es la prueba más importante. Una pantalla del juego tal como se va a ver: exterior de mañana con las dos torres y el pórtico, Valentino caminando, Cami con el dragón en el hombro y una caja de diálogo. Todo lo que venga después se compara contra esta imagen.
>
> **Antes:** 03 elegido y 04 aprobado. Si tenés fotos de las torres, ponelas en `arte/referencias/fotos/` antes de pegar el prompt.
>
> **Puerta 1:** no sigas con el resto hasta aprobar esta pantalla.

---- COPIAR DESDE ACÁ ----

Seguí AGENTS.md. Tarea: style frame del juego (`esc-ext`, primer tramo).

1. Cargá con `view_image`: `referencias/fichas/val.png` y `referencias/fichas/cam.png` como "style reference". Si hay fotos en `referencias/fotos/` que muestren las torres o el pórtico, cargalas como "architecture reference" (solo para formas y proporciones, no para colores).

2. Imagen A (torres y pórtico, sin cielo), con la herramienta integrada, horizontal 16:9:

"""
Side-scrolling video game background layer, straight-on flat 2D view like a platformer, morning light from the top-left. LEFT: a tall square office tower (rectangular prism) with a regular grid facade and vertical warm orange stripes. RIGHT: a tall cylindrical office tower with vertical blue bands, windows that get narrower toward the curved edges, and an elliptical roof. CENTER, between the towers at street level: a simple entrance portico with a flat roof slab and two white columns. BOTTOM: a grey paved sidewalk band that starts at about 70% of the image height and fills the bottom, with two planters with green shrubs. Towers reach near the top of the image. The entire sky area must be perfectly flat solid magenta #FF00FF (it will be replaced). No clouds, no distant city.
Chunky 8-bit pixel art like late NES / early SNES games. Every art pixel is a crisp, perfectly square block of flat color. No anti-aliasing, no gradients, no blur, no glow, no texture noise. Flat fills with 2–4 tone ramps. Background art: slightly desaturated and lower contrast than characters, minimal outlines.
No people, no cars, no text, letters, numbers, logos, signs, watermarks, labels or grid lines anywhere.
"""

3. Guardá en `crudo/esc-ext_style_1.png`. Pixelá con `--id esc-ext --nombre torres-style --tipo fondo --cuadro 320x180 --fondo FF00FF --limpiar --colores "a b c d e f g h 1 2 3 4 i j k W"`. El magenta tiene que quedar transparente.

4. Por código, en `herramientas/cielo.py`: cielo de mañana de 320×180 en bandas con tramado ordenado 2×2 en las uniones (como `referencias/mockup/scene.py`, función `sky`), de `g` arriba a `h` y `d` cerca del horizonte, más 3 nubes simples en `4` y `3`. Y una capa de ciudad lejana: siluetas de edificios en `h` con ventanitas en `4`, sin contorno, entre y=90 e y=125. Guardá `final/escenarios/esc-ext/esc-ext_cielo-manana.png` y `esc-ext_ciudad.png`.

5. Componé con `componer.py` la escena `vistas/escenas/style-frame.json` → `vistas/escenas/style-frame_x4.png`:
   - Capas: cielo, ciudad, torres.
   - `val_base` mirando a la derecha, con los pies en y=128, cerca de x=96.
   - `cam_base` a 20 px detrás de Valentino, mismos pies, con `drg_hombro` en el desplazamiento anotado en el manifiesto.
   - Si la vereda pixelada no empieza cerca de y=128, corré la capa de torres hacia arriba o abajo para que los pies queden sobre la vereda, y anotá el corrimiento.
   - Caja de diálogo en x=8–312, y=134–176: fondo `0`, borde de 1 px `4` y otro de 1 px `1` adentro; a la izquierda un recuadro de 24×24 para el retrato, ahora con `val_base` recortado de la cintura para arriba; texto con `fuente.py`: «PRIMER DÍA. ¿QUÉ TAN DIFÍCIL PUEDE SER?»

6. Copiá la escena a `referencias/style-frame.png` (×4) y la imagen cruda a `referencias/style-frame-crudo.png`.

7. Manifiesto: `esc-ext_torres-style`, `esc-ext_cielo-manana` y `esc-ext_ciudad` con `estado=para-revisar`.

Terminaste cuando:
- `validar.py esc-ext_torres-style esc-ext_cielo-manana esc-ext_ciudad` da OK.
- Existe `vistas/escenas/style-frame_x4.png` (1280×720).

Informe según AGENTS.md. Además, decime en tres líneas: ¿los personajes se leen sobre el fondo? ¿El fondo compite con ellos? ¿Qué ajustarías?

---- HASTA ACÁ ----

**Qué mirar:** abrí `style-frame_x4.png` en grande. ¿Se reconoce a Valentino y a Cami? ¿Se distinguen las dos torres? ¿El texto se lee? Si algo del estilo no te gusta (colores, contorno, nivel de detalle), es ahora: usá la plantilla 90.

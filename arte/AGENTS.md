# Reglas de arte — juego de noticias WTC Free Zone

Leé este archivo entero antes de cada tarea. Si un pedido contradice estas reglas, pará y preguntá.

## Qué es

Juego pixel art 8-bit (side scroller + concurso de preguntas con diseño propio) para presentar 13 noticias del equipo en una reunión. Se proyecta en una sala. Vos (Codex) hacés todo el arte: personajes, retratos, escenarios, objetos, efectos e interfaz. El juego lo programa otro equipo después: tu entrega son PNG, mapas de texto y el manifiesto.

## Límites (obligatorios)

- Escribí solo dentro de esta carpeta (`arte/`). Podés leer `../mockup/`, `../claude/`, `../guion-humor/` y `../ejemplo-visual/`; no los modifiques.
- Si una imagen generada trae piezas de distintos tamaños, recortalas del crudo antes de pixelar y guardá cada recorte en `crudo/` con sufijo (`_a`, `_b`…).
- No instales nada. Si falta un programa o una librería, pará y avisá qué falta.
- Usá solo la herramienta de imágenes integrada de Codex. No uses el modo por línea de comandos (`scripts/image_gen.py`) ni claves de API: cobran por imagen.
- No borres archivos. Antes de sobrescribir un archivo de `final/`, copiá la versión vieja a `historial/AAAA-MM-DD_<nombre>`. Las imágenes crudas nunca se sobrescriben: `_2`, `_3`.
- Nunca pidas texto, letras, números, logos ni marcas de agua dentro de una imagen generada. Los textos los pone el juego con su tipografía.
- No uses fotos de personas como referencia salvo que el pedido diga que esa persona dio el OK. Fotos de edificios, sí.
- Nada de logos ni identidad visual de marcas reales (Asana, Suzuki, WTC, QI TECH, DANNEMANN, Laib, PepsiCo), ni el logo, el decorado o la música de ningún programa de TV real.
- En Windows, si `python` no anda, probá `py`.

## Especificación técnica

- Pantalla base 320×180. El juego escala ×4 o ×6 entero, sin suavizado.
- Tiles de 16×16. Personajes en cuadros de 16×24 (cabeza grande, ~10 px de alto). Retratos de 24×24.
- Luz desde arriba a la izquierda.
- Alfa binaria: cada píxel es opaco o transparente. Nada semitransparente. Nunca negro puro `#000000`.
- Animación a 8–10 cuadros por segundo (quieto: 3; hablar: 6). Caminar: 4 cuadros. Quieto: 2.
- Tiras horizontales: todos los cuadros del mismo tamaño, de izquierda a derecha, sin separación.
- Personajes anclados abajo al centro: los pies tocan la última fila del cuadro. Mirando a la derecha; el juego espeja para la izquierda.
- Composición de pantalla: la línea de piso (donde apoyan los pies) va en y=128. La caja de diálogo ocupa x=8–312, y=134–176. La franja de arriba (y=0–16) queda libre para el HUD (torta, comodines, logros). En cada escenario anotá en el manifiesto `piso=<y>` si no es 128.

## Paleta maestra (la única permitida)

Código de una letra o número por color; `.` = transparente. Cada pieza usa un subconjunto: personajes y objetos hasta 16 colores, fondos hasta 24. La columna "contorno" dice qué color usar en el borde de abajo y de la derecha cuando ese color toca el exterior de la figura.

| Cód. | Hex | Nombre | Contorno |
|---|---|---|---|
| 0 | #12111A | tinta (solo interfaz) | 0 |
| 1 | #3B3A4F | gris oscuro | 0 |
| 2 | #7C7B91 | gris medio | 1 |
| 3 | #C6C5D6 | gris claro | 2 |
| 4 | #F5F4FA | blanco | 2 |
| 5 | #4D3022 | piel 1 (oscura) | 9 |
| 6 | #8E5B3B | piel 2 | 5 |
| 7 | #D19A6A | piel 3 | 6 |
| 8 | #F3CFA9 | piel 4 (clara) | 6 |
| 9 | #2B1B2E | ciruela (contorno comodín) | 9 |
| a | #4A1F0E | naranja 1 | 9 |
| b | #A3471B | naranja 2 | a |
| c | #E8772E | naranja 3 | a |
| d | #FFB765 | naranja 4 | b |
| e | #0F1E45 | azul 1 | 9 |
| f | #1E4F9A | azul 2 | e |
| g | #3D8FE0 | azul 3 | e |
| h | #A8DBFF | azul 4 | f |
| i | #1C4430 | verde 1 | 9 |
| j | #3F8A3C | verde 2 | i |
| k | #95C653 | verde 3 | i |
| m | #1A0F3D | violeta estudio 1 | m |
| n | #3A1F7A | violeta estudio 2 | m |
| s | #FFD43B | oro | b |
| r | #5A0E14 | rojo 1 | 9 |
| t | #A3202A | rojo 2 | r |
| u | #E23A3A | rojo 3 (error) | r |
| v | #FF8A80 | rojo 4 | t |
| w | #C99A4A | rubio 1 | y |
| x | #F2D27A | rubio 2 | w |
| y | #6B4226 | castaño 1 | L |
| z | #9A6438 | castaño 2 | y |
| A | #1B1620 | pelo negro 1 | A |
| B | #2A2230 | pelo negro 2 | A |
| C | #4A4058 | pelo negro 3 | A |
| D | #6E7A8C | metal 1 | 1 |
| E | #C3CCD8 | metal 2 | D |
| G | #5CF2FF | luz cian | f |
| H | #7E8A1E | pelota 1 | i |
| I | #D4E34A | pelota 2 | H |
| J | #EEF58A | pelota 3 | I |
| K | #FF8A3D | fuego | b |
| L | #5A3218 | madera / carey 1 | 9 |
| M | #A0623A | madera / carey 2 | L |
| N | #0A0A1F | cielo de noche | N |
| P | #EADBC4 | crema (tejido) | Q |
| Q | #B9A58A | crema 2 | M |
| W | #FFF1C9 | luz cálida (ventanas) | d |
| X | #E08A8A | rosa | t |
| R | #2B1D14 | sepia 1 (solo filtro) | R |
| S | #6B4E35 | sepia 2 (solo filtro) | R |
| T | #B08D63 | sepia 3 (solo filtro) | S |
| U | #E8D5B0 | sepia 4 (solo filtro) | T |

Colores por área: Innovación naranja (`a b c d`), Comercial azul (`e f g h`), Sostenibilidad verde (`i j k`). Torre 1 = naranja; Torre 2 = azul.

## Estilo

- 8-bit inspirado: NES con algunos tonos más. Bloques de color plano con rampas de 2 a 4 tonos. Sin degradados, brillos, desenfoque ni antialiasing.
- Contorno selectivo: el borde exterior de abajo y de la derecha usa el color de la columna "contorno"; el de arriba y la izquierda (lado de la luz) queda del color de relleno. Líneas internas mínimas. Capas lejanas del fondo, sin contorno. La interfaz sí lleva contorno oscuro completo (`0`).
- Proporciones chibi y caras amables. Cada persona se reconoce por el pelo, los anteojos, la ropa y los accesorios. Nunca exagerar cuerpo, nariz, peso ni edad: el chiste nunca es el cuerpo de nadie.
- Fondos con menos saturación y contraste que los personajes, para que ellos se lean primero.
- Respeto: nada de estereotipos sobre Brasil o los brasileros; en lo relacionado con OMBIJAM, nada de rejas, cárceles ni uniformes; el villano es el papeleo, no una institución.

## Fichas de personajes

Fuente: `../claude/elenco.md`. Cuando una ficha esté aprobada, su imagen vive en `referencias/fichas/<id>.png` y manda sobre esta tabla.

| id | Personaje | Rasgos | Accesorios / notas | Colores |
|---|---|---|---|---|
| val | Valentino, protagonista | Humano: varón joven, pelo castaño corto con flequillo, camisa blanca. Aparece como robot; variante por elegir (prompt 03) | Brazo telescópico con sello | y z, 4 3, D E G, 7 8 |
| cam | Cami | Bob oscuro con flequillo de lado, anteojos grandes de carey, remera negra, cárdigan tejido claro, cinturón marrón | Dragoncito verde en el hombro | A B C, L M, P Q, 1 2, 7 8 |
| drg | Dragoncito de Cami | Chiquito, verde, panza clara, alitas, cara simpática | Escupe fuego | i j k, K s u |
| lu | Lu | Pelo rubio largo y lacio, ojos verdes. Ropa (supuesta): blusa azul marino y jean | Suzuki rojo, sin logo | w x, e f g, 7 8, j |
| and | Andrea | Pelo negro largo, blazer negro, camisa blanca, aros de madera | — | A B C, 4 3, L M, 7 8 |
| nac | Nacho | Sin foto: pelo castaño corto, chomba blanca de tenis (genérico hasta que haya rasgos) | Pelota de tenis XXL, raqueta | y z, 4 3, H I J, 7 8 |
| fra | Fran 1.0 y 2.0 | Supuesto: monitor con cara. 1.0: pantalla verde monocromo, cara de bloques, carcasa beige. 2.0: pantalla a color, cara amable y redondeada | Presentador | j k, P Q, f g h, G |
| age | Agente comercial | Robotito bajito y redondeado, pantallita-cara con ojos cian, traje azul marino, corbata naranja, maletín marrón | Banderita de guía | e f, c, L M, G, D E |
| pap | El Papelón | Montaña de formularios con dos ojos grandes, hojas como brazos, sellos rojos. Gracioso, no da miedo | — | 4 3 2, t u |
| bar | La tarea con barba | Tarjeta de tarea blanca genérica, sin logo, con casilla vacía, ojitos de punto y una barba gris larguísima | — | 4 3 2 1 |
| gav | Gaviota | Blanca y gris, pico naranja, ojos expresivos. Variante con casco amarillo de obra | — | 4 3 2, c d, s |
| ext | Extras | Empresarios de traje, operario de mudanza, representantes de organizaciones sociales. Variantes por cambio de paleta | Sin estereotipos | según variante |

## Tres maneras de hacer cada pieza

1. **Imagen + pixelado:** personajes, retratos, escenarios y objetos de 24 px o más. Generás grande y el script lo baja a la grilla y la paleta.
2. **Mapa de píxeles:** piezas de menos de 24 px, partículas, correcciones y cuadros de animación que tienen que coincidir exacto. Escribís el dibujo como texto (un código de la paleta por píxel) y `txt2png.py` lo convierte.
3. **Código:** interfaz (cajas, botones, dígitos, tipografía), cielos, tablas de paleta y vistas previas de filtros.

## Proceso obligatorio para la manera 1

1. Cargá las referencias con `view_image` y etiquetá su papel ("style reference", "identity reference").
2. Generá con la herramienta integrada. Fondo liso `#00FF00`; si el sujeto tiene verdes (dragón, plantas, camión, Fran 1.0), usá `#FF00FF`. Sin piso, sin sombras proyectadas, figuras separadas por mucho espacio vacío.
3. Copiá la imagen tal cual a `crudo/<id>_<nombre>_<n>.png`. Nunca la dejes solo en la carpeta interna de Codex.
4. `python herramientas/pixelar.py ...` → tamaño y paleta exactos.
5. Personajes y objetos: `python herramientas/contorno.py ...`.
6. Mirá la vista ×8. Corregí píxeles sueltos editando el mapa `.txt` y regenerá con `python herramientas/txt2png.py ...`.
7. `python herramientas/validar.py <id>_<nombre>` tiene que dar OK.
8. `python herramientas/hoja.py <id>_<nombre>` → vistas ×6 y ×8 y GIF. Toda pieza que separes de otra (por ejemplo `cam_base` de `cam_ficha`) también pasa por `hoja.py` y entra al manifiesto.
9. Actualizá `manifiesto.csv`. Estados: `crudo` → `pixelado` → `para-revisar`. Solo la usuaria pasa algo a `aprobado`.
10. Sumá una entrada a `INFORME.md`.

## Consistencia

- Toda generación de un personaje lleva como referencia su ficha aprobada y `referencias/style-frame.png` (cuando existan).
- Todos los cuadros de una animación se generan en una sola imagen, en fila, mismo tamaño, misma escala.
- En ciclos (caminar, hablar, quieto), la cabeza se copia del cuadro base aprobado, con un rebote máximo de 1 px. Si la generación cambió la cara, rehacé ese cuadro desde el mapa.
- Un cambio por pedido: "cambiá solo X; dejá todo lo demás igual".

## Proceso de animación

Cada prompt de animación trae una tabla: acción, cuadros, tamaño, fps, bucle, manera (imagen o mapa), rebote de cabeza y qué pasa en cada cuadro. Hacé las animaciones de a una, en el orden de la tabla.

- **Manera "mapa":** copiá los mapas del cuadro base (`mapas/<id>/<id>_base_c1.txt` o el que diga la tabla) y cambiá solo lo que se mueve. `txt2png.py`.
- **Manera "imagen":**
  1. Cargá con `view_image` `referencias/fichas/<id>.png` como "identity reference" y `referencias/style-frame.png` como "style reference".
  2. Generá **una** imagen con esta descripción, completando lo que va entre `< >`:
     ```
     Animation sprite sheet of the SAME character as the identity reference: <rasgos de la ficha, en inglés>. <N> frames in a single horizontal row, left to right, evenly spaced with wide empty gaps, all at exactly the same scale, standing on the same baseline, facing right. Frame 1: <…>. Frame 2: <…>. (…)
     Chunky 8-bit pixel art like late NES / early SNES games. Every art pixel is a crisp, perfectly square block of flat color. No anti-aliasing, no gradients, no blur, no glow, no motion-blur, no texture noise, no dithering. Flat fills with 2–4 tone ramps. Selective outline on bottom and right edges, never pure black. Light from the top-left. Match the identity reference exactly in colors, proportions, hair, glasses, clothes and pixel size.
     Perfectly flat, solid pure green #00FF00 background (solid magenta #FF00FF for green subjects). No floor, no cast shadows.
     No text, letters, numbers, logos, watermarks, labels, grid lines or frame borders anywhere.
     ```
  3. `crudo/<id>_<accion>_<n>.png` → `pixelar.py --cuadros <N> --separar huecos --alto-figura <alto de la figura en el cuadro base>` con los colores de la ficha → `contorno.py`.
- **Cabeza fija** (caminar, quieto, hablar y toda acción marcada "cabeza fija"): reemplazá las filas de la cabeza de cada cuadro por las del cuadro base, corridas según el rebote de la tabla (por ejemplo `0,-1,0,-1` = el cuadro 2 y el 4 suben 1 px).
- Compará cada cuadro con la base a ×8: colores, largo de pelo, anteojos, ropa, tamaño. Lo que cambió, corregilo por mapa.
- Manifiesto con fps y bucle de la tabla. `validar.py` y `hoja.py` (el GIF es lo que mira la usuaria).

**Caminar estándar** (4 cuadros, 8 fps, bucle, rebote `0,-1,0,-1`, de costado): cuadro 1 contacto, pierna derecha adelante, brazo izquierdo adelante · cuadro 2 paso, piernas juntas bajo el cuerpo, cuerpo 1 px más arriba · cuadro 3 contacto, pierna izquierda adelante, brazo derecho adelante · cuadro 4 paso, como el 2 con la otra pierna. En inglés: `Frame 1: contact pose, right leg forward, left leg back, left arm forward. Frame 2: passing pose, legs together under the body, body one pixel higher. Frame 3: contact pose, left leg forward, right leg back, right arm forward. Frame 4: passing pose, legs together, body one pixel higher.`

**Quieto estándar** (2 cuadros, 3 fps, bucle, rebote `0,1`, mapa): cuadro 2 = base con hombros y cabeza 1 px más abajo (respira).

**Hablar estándar** (2 cuadros, 6 fps, bucle, mapa): cuadro 1 = base; cuadro 2 = boca abierta (2 px). En robots, la visera o pantalla cambia la forma de los ojos.

## Proceso de escenario

1. Cargá con `view_image` `referencias/style-frame.png` como "style reference" y, si el prompt lo dice, las fotos de `referencias/fotos/` como "architecture reference" (solo formas y proporciones; los colores salen de la paleta).
2. Generá **una** imagen horizontal 16:9 (o la proporción que diga el prompt) con la descripción del prompt seguida de este bloque:
   ```
   Side-scrolling video game background, straight-on flat 2D view like a platformer: no strong perspective, the floor is a horizontal band starting at about 70% of the image height. Chunky 8-bit pixel art like late NES / early SNES games. Every art pixel is a crisp, perfectly square block of flat color. No anti-aliasing, no gradients, no blur, no glow, no texture noise. Flat fills with 2–4 tone ramps. Background art: slightly desaturated and lower contrast than characters, minimal outlines. Keep the middle of the floor clear for characters. Match the style reference.
   No people, no animals, no text, letters, numbers, logos, signs with writing, watermarks, labels or grid lines anywhere.
   ```
3. `crudo/<id>_<nombre>_<n>.png` → `pixelar.py --tipo fondo --cuadro 320x180 --limpiar` con los colores del prompt (hasta 24).
4. Revisá a ×4: si quedan manchas de ruido o colores sueltos, limpiá por código o por mapa. Las superficies grandes tienen que ser planas.
5. Vista previa con `componer.py`: el fondo con `val_base` y `cam_base` parados con los pies en y=128 (o en el piso que corresponda) y la caja de diálogo vacía. Tiene que verse dónde se paran y que el fondo no compita con ellos.
6. Manifiesto con `piso=<y>` y las zonas importantes en `notas` (por ejemplo `pantalla=x,y,w,h`). `validar.py` y vista ×4 en `vistas/escenas/`.

## Nombres y carpetas

- Cada pieza se llama `<id>_<nombre>`; si no tiene acción, `<nombre>` es `base`. Es el nombre que usan `validar.py`, `hoja.py` y el manifiesto.
- ids: `val cam drg lu and nac fra age pap bar gav ext`; objetos `ob-…`; escenarios `esc-…`; interfaz `ui-…`; efectos `ef-…`.
- `final/personajes/<id>/<id>_<accion>.png` (tira) · `final/retratos/` · `final/escenarios/` · `final/objetos/` · `final/efectos/` · `final/interfaz/` · `final/fuente/`.
- `mapas/<id>/<id>_<accion>_c<n>.txt` · `vistas/` (×6, ×8, GIF, escenas compuestas) · `crudo/` · `referencias/` · `historial/` · `herramientas/`.

## Informe al terminar cada pedido

1. Rutas de todo lo que guardaste.
2. El texto completo de la descripción final que le pasaste al generador.
3. Herramienta usada (la integrada; nunca la línea de comandos).
4. Salida de `validar.py`, copiada.
5. Qué no salió bien y qué proponés.
6. Mostrá la vista ×6 o la escena compuesta.

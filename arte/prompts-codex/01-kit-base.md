# 01 · Kit base: carpetas, paleta y programas

> **Para vos:** Codex arma la carpeta de trabajo y escribe los programas que bajan cada imagen a pixel art de verdad y revisan que cumpla las reglas. No genera ninguna imagen. Al final te muestra una prueba con un dibujo falso: tiene que decir OK en el bueno y FALLA en el malo.
>
> **Antes:** decisiones 1 y 2 del plan (Codex y Python con Pillow).

---- COPIAR DESDE ACÁ ----

Seguí AGENTS.md. Tarea: armar el kit base de arte. En esta tarea no generes imágenes.

0. Comprobá que existan Python 3 y Pillow (`python --version`, o `py --version`, y `python -c "import PIL; print(PIL.__version__)"`). Si falta algo, pará y decime qué falta. No instales nada.

1. Creá las carpetas: `crudo/ mapas/ referencias/fichas/ referencias/fotos/ final/personajes/ final/retratos/ final/escenarios/ final/objetos/ final/efectos/ final/interfaz/ final/fuente/ vistas/escenas/ historial/ herramientas/ paleta/`.

2. Copiá a `referencias/mockup/` los archivos `../mockup/font.py`, `../mockup/sprites.py` y `../mockup/scene.py`, y `../claude/elenco.md` a `referencias/`. Si no podés leer fuera de esta carpeta, pará y pedime que los copie yo.

3. Paleta, a partir de la tabla de AGENTS.md:
   - `paleta/paleta-maestra.txt`: una línea por color, `codigo;hex;nombre;contorno`.
   - `paleta/paleta-maestra.gpl` (formato GIMP, también lo abren Aseprite y LibreSprite).
   - `paleta/muestra.png`: muestras de 16×16 con el código abajo, ×4.

4. Programas en `herramientas/` (Python 3 + Pillow, sin otras librerías, comentados en español, con `--help`):

   - `paleta.py` (módulo): lee `paleta-maestra.txt`; convierte hex↔código; color más cercano en espacio CIELAB (ΔE76), restringido a una lista de códigos permitidos.
   - `pixelar.py`: imagen generada → pixel art exacto. Opciones: `--entrada`, `--id`, `--nombre`, `--tipo personaje|retrato|objeto|fondo`, `--cuadro WxH`, `--cuadros N`, `--separar huecos|grilla:CxF`, `--colores "códigos separados por espacio"`, `--fondo auto|00FF00|FF00FF`, `--alto-figura px` (por defecto, el alto del cuadro), `--ancla abajo|abajo-izq|centro`, `--limpiar`.
     1. Quita el fondo: color de fondo = el más frecuente del borde (o el indicado); los píxeles a menos de ~80 de distancia RGB, transparentes. Quita el halo verde o magenta de los bordes.
     2. Separa cuadros: `huecos` corta por columnas totalmente transparentes de 8 px o más, de izquierda a derecha; si encuentra una cantidad distinta de `--cuadros`, frena con un error claro. `grilla:CxF` corta en celdas iguales.
     3. Usa **la misma escala para todos los cuadros**, calculada con la figura más alta para que mida `--alto-figura`. Si el ancho no entra en el cuadro, ajusta por ancho y avisa.
     4. Antes de achicar, cuantiza la imagen grande a los colores permitidos. Después achica por **moda de bloque**: cada píxel final toma el color más frecuente de su bloque; si el bloque es más de la mitad transparente, queda transparente.
     5. `--limpiar`: reemplaza píxeles aislados (ningún vecino de su color) por el color mayoritario de sus 8 vecinos.
     6. Ancla cada figura en su cuadro (`abajo`: pies en la última fila, centrada en horizontal; `abajo-izq`: pies en la última fila, pegada a la izquierda, para acciones que se estiran hacia la derecha). Tipo `fondo`: recorta al centro con la proporción del cuadro y achica entero, sin separar ni anclar.
     7. Guarda: tira PNG en `final/<carpeta según tipo>/<id>/<id>_<nombre>.png`; un mapa por cuadro en `mapas/<id>/<id>_<nombre>_c<n>.txt` (un código por píxel, `.` = transparente); vista ×8 en `vistas/<id>_<nombre>_x8.png`. Si el PNG final ya existe, antes lo copia a `historial/`.
   - `contorno.py`: contorno selectivo según AGENTS.md. Trabaja solo sobre el borde exterior (píxeles opacos con un vecino transparente en 4 direcciones). Si el vecino transparente está abajo o a la derecha, el píxel toma el color "contorno" de su relleno. Si está solo arriba o a la izquierda, toma el color de relleno. Para saber el relleno, mira el primer píxel hacia adentro que no sea `0` ni `9`. Actualiza PNG y mapas.
   - `txt2png.py`: mapas → tira PNG (para correcciones a mano). Mismo historial.
   - `validar.py <id>_<nombre> [...]` o `--todo`: por cada pieza imprime `OK` o `FALLA: <motivo>` y sale con código 1 si algo falla. Revisa: tamaño = cuadro × cuadros (según `manifiesto.csv`); solo colores de la paleta y de los permitidos; alfa binaria; sin `#000000`; si el ancla es `abajo` o `abajo-izq`, píxeles en la última fila de cada cuadro; hasta 16 colores (fondos, 24); los mapas existen y coinciden con el PNG; la pieza está en el manifiesto.
   - `hoja.py <id>_<nombre>`: vista ×6 de los cuadros sobre damero gris, con el número de cada cuadro, en `vistas/<id>_<nombre>_x6.png`; vista ×8 sin números en `vistas/<id>_<nombre>_x8.png` (la que se usa como referencia); y GIF animado ×6 a los cuadros por segundo del manifiesto, sobre fondo `#C6C5D6`, en `vistas/<id>_<nombre>.gif`. `--todo` arma `vistas/hoja-general.png` con todo lo aprobado.
   - `componer.py <escena.json>`: arma una pantalla de 320×180 con capas de fondo, sprites (archivo, cuadro, x, y, espejar) y, si se pide, una caja de diálogo con retrato y texto. Exporta ×4 a `vistas/escenas/`. Para el texto, portá la tipografía 5×7 de `referencias/mockup/font.py` a `herramientas/fuente.py` (provisoria hasta el prompt 32).
   - `autoprueba.py`: crea una imagen falsa de 4 figuras de bloques de 12 px sobre verde, con un poco de ruido y bordes suavizados; la pasa por `pixelar.py` y `contorno.py` a 16×24; corre `validar.py` (tiene que dar OK). Después crea una pieza mala a propósito (un color fuera de paleta y un píxel semitransparente) y verifica que `validar.py` dé FALLA. Imprime el resultado de las dos.

5. `manifiesto.csv` con encabezado: `pieza,archivo,tipo,cuadro,cuadros,fps,bucle,ancla,colores,prompt,estado,notas`. Las piezas de prueba van con `estado=prueba`.

6. `INFORME.md` con una primera entrada: qué se creó y la salida de `autoprueba.py`.

Terminaste cuando:
- `python herramientas/autoprueba.py` muestra OK para la pieza buena y FALLA para la mala.
- Existen `paleta/paleta-maestra.txt` (53 colores), `paleta/paleta-maestra.gpl` y `paleta/muestra.png`.
- `python herramientas/pixelar.py --help` funciona.

Informe según AGENTS.md. Mostrame `paleta/muestra.png` y la vista ×6 de la prueba.

---- HASTA ACÁ ----

**Qué mirar:** que la autoprueba diga OK y FALLA donde corresponde, y que la muestra de la paleta tenga los colores del plan.

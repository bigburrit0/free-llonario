# 32 · Tipografía

> **Para vos:** el juego escribe todos sus textos con dos letras propias, dibujadas píxel por píxel: una chica para diálogos, preguntas y respuestas, y una grande para títulos y carteles. Se agregan los signos que faltaban (% ½ ¾ « » paréntesis, ✓ ✗). Codex prueba que todas las preguntas y respuestas del guion entren en sus cajas y te dice cuáles no. También arma dos versiones de prueba, solo mayúsculas o mayúsculas y minúsculas, para que elijas la que se lee mejor en el proyector.
>
> **Antes:** prompt 01. Se puede hacer en cualquier momento.

---- COPIAR DESDE ACÁ ----

Seguí AGENTS.md. Tarea: tipografías del juego (`ui-fuente`), por mapa (manera 2), sin generar imágenes. Partí de `referencias/mockup/font.py` (5×7, solo mayúsculas).

1. **Fuente chica**: alto de mayúscula 7 px, descendentes de 2 px, interlineado de 10 px, ancho variable (de 1 a 5 px) con 1 px de separación. Caracteres: A–Z, a–z, 0–9, Á É Í Ó Ú Ü Ñ á é í ó ú ü ñ, ¿ ? ¡ ! . , : ; ' " « » ( ) % ½ ¾ + - = / * # & _ @ ✓ ✗ ⏩ ♪ y espacio (3 px).
2. **Fuente grande**: alto de mayúscula 14 px (el doble de la chica, rediseñada, no ampliada), interlineado de 18 px. Caracteres: A–Z, 0–9, Á É Í Ó Ú Ü Ñ, ¿ ? ¡ ! . , : % ½ ¾ - ✓ ✗ y espacio.
3. Cada glifo dibujado en `4` sobre transparente. Para cada fuente, también una versión con contorno de 1 px en `0` alrededor (para escribir sobre fondos).
4. Exportá a `final/fuente/`: `chica.png`, `chica-contorno.png`, `grande.png`, `grande-contorno.png` (atlas en una grilla) y `chica.json`, `grande.json` con, por caracter, posición en el atlas, ancho, y los datos generales (alto, línea base, interlineado). Reemplazá `herramientas/fuente.py` para que use estas fuentes (mantené la vieja como `fuente_mockup.py`).
5. **Prueba de que entra todo**: leé las preguntas, las cuatro opciones y las tarjetas de noticia del guion de la versión elegida (si no hay versión elegida, `../guion-humor/02-guion-A-la-torta-al-piso-8.md`). Medí con la fuente chica:
   - Pregunta: hasta 2 líneas de 296 px.
   - Cada opción: hasta 2 líneas de 136 px (cápsula de 152 px menos la pestaña de la letra y márgenes).
   - Tarjeta de noticia: hasta 5 líneas de 264 px.
   - Diálogo: hasta 3 líneas de 264 px.
   Escribí `vistas/fuente_cabe.txt` con una línea por texto: `OK` o `NO ENTRA` + el texto + cuánto sobra.
6. **Vistas** a ×4: `vistas/fuente_chica.png` y `vistas/fuente_grande.png` (todos los caracteres); `vistas/fuente_mayus-vs-minus.png`: la pregunta 1 y sus 4 opciones escritas dos veces, una en solo mayúsculas y otra en mayúsculas y minúsculas, sobre fondo `m`.

Terminaste cuando:
- Existen los 4 atlas, los 2 JSON y las vistas.
- `vistas/fuente_cabe.txt` existe y tiene una línea por cada pregunta, opción, tarjeta y diálogo del guion.
- `componer.py` escribe con las fuentes nuevas.

Informe según AGENTS.md. Incluí cuántos textos dan `NO ENTRA`.

---- HASTA ACÁ ----

**Qué mirar:** `fuente_mayus-vs-minus.png` en grande: ¿cuál se lee mejor? Y la lista de `NO ENTRA`: esos textos hay que acortarlos en el guion (es tarea de guion, no de arte).

# Plan de arte con Codex

Juego de noticias WTC Free Zone · actualizado el 13/10/2026

## En pocas palabras

Codex hace todo el pixel art, de tres maneras según el tamaño de la pieza. Lo grande (personajes, escenarios) lo genera como imagen y un programa lo ajusta a la grilla y la paleta del juego. Lo chico lo dibuja píxel por píxel, escribiendo un mapa de texto. La interfaz la arma con código. Vos pegás un prompt por vez, mirás la vista ampliada y aprobás o pedís un cambio.

**Esto cambia una decisión del 11/10** ("vos dibujás los personajes; Claude, escenarios e interfaz"): ahora todo lo hace Codex. Claude planifica y revisa.

## Qué hay en esta carpeta

| Archivo | Qué es |
|---|---|
| `PLAN-ARTE.md` | Este plan |
| `AGENTS.md` | Las reglas fijas que Codex lee solo al arrancar: paleta, tamaños, estilo, fichas de personajes y proceso |
| `prompts-codex/00-COMO-USAR.md` | Cómo usar los prompts, paso a paso |
| `prompts-codex/01` a `36` | Un prompt por pieza o grupo de piezas, en orden |
| `prompts-codex/90` y `91` | Plantillas para corregir algo o pedir una pieza nueva |

## Lo verificado y lo supuesto

**Verificado (13/10/2026):**

- Codex tiene una skill oficial de imágenes, `imagegen`. Por defecto usa su herramienta integrada, que no necesita clave de API. El modo por línea de comandos sí necesita clave y solo se usa si lo pedís. Las imágenes se guardan en una carpeta interna de Codex y hay que copiarlas al proyecto. Para editar una imagen, primero tiene que cargarla con `view_image`. Recomienda pedir un cambio por vez ("cambiá solo X; dejá Y igual") y guardar versiones nuevas en lugar de pisar. Fuente: el archivo oficial de la skill en `github.com/openai/skills`.
- Codex lee solo un archivo `AGENTS.md` con instrucciones. Si la carpeta no es un repositorio git, mira solo la carpeta donde lo abrís. Tope de 32 KiB. Fuente: guía oficial de OpenAI sobre `AGENTS.md`. Por eso hay que abrir Codex **dentro de `arte/`**.
- En esta PC **Python no está instalado**: el comando `python` solo muestra el aviso de la Microsoft Store. Node sí está (v24.19.0).
- En esta PC **no encontré Codex**: no existe la carpeta `C:\Users\gomez\.codex`.

**Supuesto (fuentes de terceros o sin comprobar):**

- El modelo de imágenes por defecto es gpt-image-2, desde el 21/04/2026.
- La herramienta integrada no hace fondos transparentes; se genera sobre verde liso y se recorta. Por eso todos los prompts piden fondo `#00FF00` (o magenta si el sujeto es verde).
- El plan gratuito de ChatGPT no incluye generación de imágenes, y generar imágenes gasta el límite de uso de 3 a 5 veces más rápido que el texto.
- Que Codex pueda leer las carpetas de al lado (`../mockup`, `../claude`). Si no puede, el prompt 01 te pide copiarlas.
- Cómo es Fran, la ropa de Lu y los rasgos de Nacho (ver Decisiones).

## Por qué no alcanza con pedirle la imagen

Los generadores hacen dibujos que *parecen* pixel art pero no lo son: los "píxeles" tienen tamaños distintos, los bordes están suavizados, hay cientos de colores y cada imagen sale un poco distinta. En el proyector se ven bordes borrosos, y el personaje cambia de cara entre un cuadro y el siguiente.

Por eso cada imagen pasa por un programa que Codex escribe en el prompt 01: le saca el fondo verde, la baja al tamaño exacto (16×24 por personaje, 320×180 por escenario), la obliga a usar solo los 53 colores de la paleta, normaliza el contorno y deja un mapa de texto editable. Otro programa revisa que todo cumpla y responde OK o FALLA.

## Las tres maneras

| Manera | Para qué | Cómo |
|---|---|---|
| 1 · Imagen + pixelado | Personajes, retratos, escenarios, objetos de 24 px o más | Codex genera grande sobre verde y el programa lo ajusta |
| 2 · Mapa de píxeles | Piezas chicas, partículas, correcciones, cuadros que tienen que coincidir exacto | Codex escribe el dibujo como texto, una letra por píxel |
| 3 · Código | Interfaz, tipografía, cielos, paletas del día, vistas previas de filtros | Codex lo programa |

## Cómo se cuida que todo parezca del mismo juego

1. **Primero el "style frame"**: una pantalla terminada del juego (prompt 05). No se produce nada más hasta que la apruebes.
2. **Ficha antes de animar.** Cada personaje tiene una ficha aprobada que va como referencia en todos sus prompts.
3. **Paleta fija** de 53 colores. El programa no deja pasar otros.
4. **Cabeza fija** en los ciclos: en caminar, hablar y quieto se copia la cabeza del cuadro aprobado.
5. **Sin texto en las imágenes.** Los carteles salen en blanco y el juego escribe encima.
6. **Un cambio por pedido**, y nunca se pisa una versión aprobada.

## Medidas del juego (decididas el 11/10)

- Pantalla base 320×180 (16:9), escalada ×4 o ×6, sin suavizado. Tiles de 16×16.
- Personajes de 16×24 con cabeza grande; retratos de 24×24. El prompt 02 lo pone a prueba (ver Decisión 4).
- Luz desde arriba a la izquierda. Contorno selectivo con el tono más oscuro de cada color, nunca negro.
- Caminar en 4 cuadros, quieto en 2, a 8–10 cuadros por segundo. Transiciones con iris.
- Paleta: las rampas del plan (naranja Torre 1, azul Torre 2, neutros, verdes, pieles, estudio, error) más pelos, metal, pelota, fuego, madera y sepia. La tabla completa con códigos está en `AGENTS.md`.

## Inventario completo

Las animaciones con asterisco (*) dependen de la reescritura del guion con Valentino protagonista y pueden cambiar.

### Personajes (animaciones dibujadas, con cantidad de cuadros)

| id | Personaje | Cuadro | Animaciones | Ficha / animación |
|---|---|---|---|---|
| val | Valentino, protagonista | 16×24 | quieto 2 · caminar 4 · hablar 2 · de frente 1 · sorpresa 2 · apretar botón 3 · brazo-sello 6 (cuadro 48×24) · caminar agachado 4 · festejar 2 · barra de carga en el pecho 3 · mirar arriba 1 · caminar con la torta 4* | 03 / 14 |
| cam | Cami | 16×24 | quieta 2 · caminar 4 · hablar 2 · de frente 1 · mirar arriba 1 · saludo al sumarse 2 · girar en la silla 4* | 02, 04 / 15 |
| drg | Dragoncito | 12×12 | en el hombro 2 · estornudo 3 · llamarada 4 · linterna 1 · volar 2 | 04 / 15 |
| lu | Lu | 16×24 | quieta 2 · caminar 4 · hablar 2 · de frente 1 · mirar arriba 1 · bajar del auto 3 | 06 / 16 |
| ob-auto | Suzuki rojo | 48×24 | andar 2 · choque 3 · chocado 1 · chocado con la puerta abierta 1 · estacionado 1 | 06 / 16 |
| and | Andrea | 16×24 | quieta 2 · caminar 4 · hablar 2 · de frente 1 · mirar arriba 1 · tocar «completar» 3 · afeitar 3 (solo si elige ese gag) | 07 / 17 |
| nac | Nacho | 16×24 | quieto picando la pelota 2 · saque 5 · girar la pelota como globo 3 · contar 2 · de frente 1 | 08 / 17 |
| ob-pelota | Pelota XXL | 16×16 | rodar 4 | 08 / 17 |
| fra | Fran 1.0 y 2.0 | 32×24 | 1.0: quieto 2 · tildado 2. 2.0: quieto 2 · hablar 2 · tres saludos 3 · mareado 2 · lágrima 1. Zoom: cara 64×48, cara 128×96, un ojo 128×96 | 09 / 18 |
| age | Agente comercial | 12×16 | quieto 2 · caminar 4 · hablar 2 · caminar con banderita 4 · ofrecer folleto 2 · tararear 2 | 10 / 18 |
| pap | El Papelón | 32×32 | dormido 1 · despertar 3 · escupir hojas 3 · explotar 4. Papelito con ojos (8×8): parpadear 2 | 11 / 19 |
| bar | Tarea con barba | 24×16 + tramo 8×8 | quieta 2 · punta chamuscada 2 · completada 3 · se cae la barba 3 · de vacaciones 1 (32×24) | 11 / 19 |
| gav | Gaviota | 16×12 (volar y robar, 16×16) | quieta 2 · volar 4 · robar porción 3 · con casco tildando 2 · sentada con cartelito 1 | 12 / 20 |
| ext | Extras | 16×24 y 16×16 | empresario: caminar 4, saludar 2 · operario: sellar 3 · representante sentado: aplaudir 2. Variantes por cambio de paleta (3 empresarios, 4 representantes) | 12 / 20 |
| ob-camion | Camión de mudanza | 64×40 | marcha atrás 2 | 12 / 20 |

Total: unos 190 cuadros dibujados.

### Retratos (24×24, prompt 13)

Valentino, Cami, Lu, Andrea, Nacho, Fran 2.0 y el agente, cada uno con 4 caras: neutral, hablando, sorpresa y contento. Son 28 retratos.

### Escenarios (320×180 salvo aclaración)

| id | Escenario | Dónde se usa | Prompt |
|---|---|---|---|
| esc-ext | Exterior: cielo, ciudad lejana, las dos torres, pórtico con columnas, vereda, plantas | Intro, caminatas, pórtico, final | 05 (primer tramo), 21 (completo, 640 px de ancho, en capas) |
| esc-lobby | Lobby de la Torre 1 | E1 · Papelón | 22 |
| esc-cochera | Cochera oscura | E2 · tarea con barba | 22 |
| esc-oficina | Oficina de Innovación con pantalla gigante | E3 · Fran 2.0 | 23 |
| esc-sala | Sala con pizarrón | E4 · Cami se suma | 23 |
| esc-ascensor | Ascensor por dentro, hall con puertas, puertas animadas | Cambios de acto, 8½ | 24 |
| esc-carga | Zona de carga al pie de la torre | E5 · mudanza | 25 |
| esc-piso6 | Hall del piso 6 | E6 · los 25 | 25 |
| esc-torre2 | Interior curvo de la Torre 2 con mesa redonda | E7 · ROUNDTABLE | 26 |
| esc-terraza | Terraza del piso 8, atardecer y noche | E8 · velitas, premio, final | 27 |
| esc-estudio | Estudio del concurso, diseño propio | Todas las preguntas | 28 |
| esc-titulo | Pantalla de título | Inicio | 29 |
| esc-creditos | Viñetas de créditos: playa de Punta del Este y fondo de consola | Créditos y post-créditos | 29 |

### Objetos (prompt 30, salvo aclaración)

Torta en 4 estados (100 %, 97 % con confeti, 90 % con sello, 75 % sin una porción) y la porción que roba la gaviota · velita, llama (2 cuadros) y humito, que el juego pone 12 veces · botón rojo enorme · marco del sello VALIDADO · barrera de la cochera (cerrada, subiendo, abierta) · colchón, cono, casco y airbag que se superponen a las columnas, y el cartelito «Yo estaba primero» · cajas de mudanza sin logos · segundo control "jugador 2" · credencial · cartel en blanco «Próximamente» · afiche del premio con marco + lupa · reposera, mate y termo · mate coleccionable · post-its de 4 colores · folleto. (La silla con rueditas va dentro de la animación de Cami; la banderita, en la del agente; las ventanas encendidas, en el exterior.)

### Efectos (prompt 31, como mapa de píxeles)

Confeti · chispas · humo (3 cuadros) · polvo · estrellitas de golpe (2) · fuego del dragón (3) · haz de la linterna · notas musicales · trozos de ladrillo · gotita · ondas del BIP · ícono ⏩ · destello · chispa de fuegos artificiales · lágrima de un píxel.

### Interfaz (prompts 32 a 34, por código)

- Tipografía chica 5×7 con tildes, ñ, ¿¡ y los signos que faltaban (% ½ ¾ ( ) « » ' ; ✓ ✗ ⏩), y una grande para títulos y carteles.
- Caja de diálogo con lugar para el retrato. Caja de pregunta de 2 líneas. 4 cápsulas de respuesta de 2 líneas en 4 estados: neutra azul, elegida naranja, correcta verde con ✓, incorrecta roja con ✗.
- Display del ascensor con dígitos de 7 segmentos (0–9, ½, ¾) y escalera de 8 pisos (pendiente, acierto, error).
- 3 comodines (ícono normal y usado), barras de votación, logro de 2 s, carteles de estudio (REDOBLE, SOPLEN, CONTÁ, APLAUSOS, RISAS, ¡UUUH!), zócalo «ÚLTIMO MOMENTO», barra de la torta, botones de saltar, pausa y sonido.
- Pantallas: tarjeta de noticia, equipo estilo RPG, resultado y rango, barra «ACTUALIZANDO 99 %», «PRESIONÁ START», afiche «VACACIONES GRATIS» con letra chica.

### Paletas y filtros (prompt 35)

Mañana, mediodía, atardecer y noche. Sepia con viñeta y grano (si va la versión B o la mezcla). Pixelado progresivo (si va la C). Codex hace las tablas y las vistas previas; el juego los aplica.

## Animaciones: dibujadas o hechas por código

Muchos movimientos no necesitan cuadros dibujados: los hace el juego moviendo, escalando o repitiendo piezas. Así se gasta menos y todo queda más parejo.

| Movimiento | Quién lo hace |
|---|---|
| Ciclos del cuerpo: caminar, hablar, saque, llamarada, choque | **Cuadros dibujados** (inventario de arriba) |
| Cruzar la pantalla, la fila de los 25, el parallax | El juego mueve el sprite |
| Temblor: choque, Fran 1.0 tildado, «¿última respuesta?» | El juego |
| Crecer: Papelón ×3, pelota cada vez más grande, barba por tramos, mesa que se estira | El juego escala o repite piezas |
| Rebotes y aplastar/estirar simples: pelota, logro que entra | El juego |
| Parpadeos (PRESIONÁ START, display), siempre menos de 3 por segundo | El juego |
| Zoom de Fran, iris, fundidos, sepia → color, pixelado | El juego |
| Confeti, fuegos artificiales, post-its que llueven, chispas | El juego, con las piezas de efectos |
| Ascensor que baja medio piso, puerta a medias, ⏩ al doble de velocidad | El juego mueve las piezas |

## Orden de trabajo y puertas

| Fase | Prompts | Qué sale | Puerta para seguir |
|---|---|---|---|
| 0 · Preparar | 01 | Carpetas, paleta, programas de pixelado y revisión, manifiesto | Decisiones 1 y 2 |
| 1 · El look | 02, 03, 04, 05 | Prueba de tamaño, variantes de Valentino, Cami y el dragón, style frame | **Puerta 1:** aprobás el style frame y Valentino elige su variante |
| 2 · Fichas | 06 a 13 | Fichas de todos los personajes y retratos | **Puerta 2:** aprobás cada ficha y cada persona da el OK de su dibujo |
| 3 · Escenarios | 21 a 29, 35 | Fondos de todas las escenas, estudio, título, paletas | Puede ir en paralelo con la fase 2. Mejor con fotos |
| 4 · Interfaz | 32, 33, 34 | Tipografía, estudio, HUD, pantallas | Puede ir en cualquier momento después del 01 |
| 5 · Animación | 14 a 20, 30, 31 | Todas las animaciones, objetos y efectos | **Puerta 3:** guion definitivo y prototipo cronometrado, para no animar lo que se corta |
| 6 · Cierre | 36 | Revisión general, hoja de todo, faltantes | — |

## Lista de prompts

| # | Prompt | ¿Se puede ya? |
|---|---|---|
| 01 | Kit base: carpetas, paleta y programas | Sí, después de las decisiones 1 y 2 |
| 02 | Prueba de tamaño con Cami (16×24 contra 24×32, imagen contra mapa) | Sí |
| 03 | Valentino: tres variantes para elegir | Sí |
| 04 | Ficha de Cami y el dragoncito | Sí |
| 05 | Style frame: exterior de mañana, Valentino, Cami, dragón y diálogo | Sí. Mejor con fotos de las torres |
| 06 | Ficha de Lu y el Suzuki | Sí (el OK de Lu es para animar el choque) |
| 07 | Ficha de Andrea | Sí |
| 08 | Ficha de Nacho y la pelota | Esperar sus rasgos y su OK |
| 09 | Ficha de Fran 1.0 y 2.0 | Esperar qué es Fran, o hacerla con el supuesto |
| 10 | Ficha del agente comercial | Sí |
| 11 | Fichas del Papelón y la tarea con barba | Sí |
| 12 | Fichas de la gaviota, los extras y el camión | Sí |
| 13 | Retratos | Después de 04 a 12 |
| 14 | Animaciones de Valentino | Esperar Puerta 3 |
| 15 | Animaciones de Cami y el dragón | Esperar Puerta 3 |
| 16 | Animaciones de Lu y el choque | Esperar Puerta 3 y el OK de Lu |
| 17 | Animaciones de Andrea, Nacho y la pelota | Esperar Puerta 3 y el gag de Andrea |
| 18 | Animaciones de Fran y el agente | Esperar Puerta 3 |
| 19 | Animaciones del Papelón y la barba | Esperar Puerta 3 |
| 20 | Animaciones de la gaviota, los extras y el camión | Esperar Puerta 3 |
| 21 | Exterior completo en capas | Después de 05 |
| 22 | Lobby y cochera | Sí. Mejor con fotos |
| 23 | Oficina de Innovación y sala del pizarrón | Sí. Mejor con fotos |
| 24 | Ascensor: por dentro, hall y puertas | Sí. Mejor con fotos |
| 25 | Zona de carga y hall del piso 6 | Sí |
| 26 | Torre 2 y la mesa redonda | Sí. Mejor con fotos |
| 27 | Terraza del piso 8 y final de noche | Sí. Mejor con fotos |
| 28 | Estudio del concurso | Sí |
| 29 | Título y viñetas de créditos | Las viñetas sí; el logo espera el nombre |
| 30 | Objetos de la historia | La torta depende del guion; el resto sí |
| 31 | Efectos y partículas | Sí, después del 01 |
| 32 | Tipografía | Sí, después del 01 |
| 33 | Interfaz del estudio y HUD | Después de 28 y 32 (supone cápsulas de 2 líneas) |
| 34 | Pantallas de interfaz | Después de 33; el logo espera el nombre |
| 35 | Paletas del día y filtros | Después de 21 |
| 36 | Revisión final | Al final |
| 90 | Plantilla: corregir una pieza | Cuando haga falta |
| 91 | Plantilla: pedir una pieza nueva | Cuando haga falta |

## Decisiones que necesito

1. **Dónde corre Codex.** No lo encontré en esta PC. Recomiendo la app de Codex o el Codex de terminal en esta PC, abierto en la carpeta `arte`. Necesita un plan de ChatGPT que incluya imágenes. Instalarlo y elegir el plan es tuyo: **puede costar plata**.
2. **Python y Pillow.** Los programas de pixelado los necesitan, y no están. Son gratis. Si decidís instalarlos, estos son los comandos (en una terminal nueva después del primero):

   ```bash
   winget install --id Python.Python.3.12 -e
   ```

   ```bash
   py -m pip install pillow
   ```

   Alternativa sin instalar nada: adapto el prompt 01 a Node, que ya está. Funciona solo con imágenes PNG y es menos probado.
3. **Valentino: robot con flequillo, robot sin pelo o piloto en una cabina.** El prompt 03 arma las tres lado a lado para que elija él.
4. **Tamaño de los personajes.** 16×24 está decidido. El prompt 02 compara con 24×32 usando a Cami. Si a 16×24 no se reconoce a nadie en el proyector, conviene pasar a 24×32, aunque cambia la escala de todo.
5. **Fotos.** Las del edificio (torres, lobby, cochera, ascensor, terraza) mejoran mucho los escenarios: van a `arte/referencias/fotos/`. **Las fotos de tus compañeros no**, salvo que cada uno dé el OK, porque se mandan a OpenAI. Los prompts describen rasgos con palabras.
6. **Fran.** ¿Qué es hoy y cómo se ve? El supuesto es un monitor con cara.
7. **Lu y Nacho.** La ropa de Lu es supuesta. Nacho necesita rasgos o foto (con su OK) y que apruebe sus gags antes que nadie.
8. **Versión del guion y nombre del juego.** Definen la lista final de animaciones (fase 5) y el logo.

## Costo y límites

- La herramienta integrada de Codex usa tu plan de ChatGPT, sin cobro por imagen (verificado: no necesita clave de API). Cuánto aguanta el límite es un supuesto.
- `AGENTS.md` le prohíbe a Codex usar el modo con clave de API, que cobra cada imagen.
- Estimación: entre 80 y 120 imágenes generadas en total. Por eso las animaciones esperan a la Puerta 3.

## Riesgos

| Riesgo | Qué hacemos |
|---|---|
| El personaje cambia de cara entre cuadros | Cabeza copiada del cuadro aprobado, ficha como referencia, corrección por mapa |
| A 16×24 no se reconoce a nadie | Prueba del prompt 02 antes de producir; retratos de 24×24 para las caras |
| Píxeles sucios o colores de más | Pixelado y revisión obligatorios; FALLA frena la entrega |
| Se acaba el límite de Codex a mitad de camino | Producir por fases; animar solo con el guion definitivo |
| Se parece demasiado al programa de TV | Estudio de diseño propio, sin logo ni decorado real |
| Alguien no se siente cómodo con su dibujo | Ficha de OK antes de animar |
| Fotos de compañeros en un servicio externo | Solo rasgos descritos, salvo OK explícito |
| Codex escribe fuera de `arte/` o borra algo | `AGENTS.md` lo prohíbe; se guarda historial antes de pisar |

## Fuentes

- Skill oficial `imagegen` de Codex: https://raw.githubusercontent.com/openai/skills/main/skills/.system/imagegen/SKILL.md (consultado el 13/10/2026)
- Guía oficial de `AGENTS.md`: https://developers.openai.com/codex/guides/agents-md (consultado el 13/10/2026)
- Terceros, sin confirmar: https://codex.danielvaughan.com/2026/06/04/codex-cli-visual-workflows-image-input-gpt-image-2-generation-asset-pipelines-v0137/ (modelo, transparencia con verde, límites de uso)

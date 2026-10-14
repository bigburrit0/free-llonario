# Cómo retomar este proyecto (para Codex u otro agente)

Leé este archivo entero antes de hacer nada.

## Qué es

Un juego pixel art 8-bit para presentar las 13 noticias del equipo de WTC Free Zone en una reunión. Es un side scroller con un concurso de preguntas de diseño propio: 8 preguntas, que son los 8 pisos de un ascensor, en 3 actos. Se proyecta en una sala: una persona maneja y la sala grita las respuestas. Dura unos 6 minutos. La usuaria es arteterapeuta y artista, no es desarrolladora. Escribile en español rioplatense, con voseo, claro y sin jerga.

## Dónde está cada cosa

| Carpeta o archivo | Qué es |
|---|---|
| `arte/PLAN-ARTE.md` | Plan del arte: inventario, orden, puertas de aprobación, decisiones pendientes |
| `arte/AGENTS.md` | **Reglas obligatorias del arte**: paleta, tamaños, estilo, fichas de personajes, procesos |
| `arte/prompts-codex/` | Los pedidos de arte en orden, del `01` al `36`, más las plantillas `90` (corregir) y `91` (pieza nueva) |
| `claude/plan.md` | Plan general del juego (el guion que tiene está desactualizado) |
| `claude/elenco.md` | Personajes y rasgos |
| `guion-humor/` | Tres versiones del guion (A, B, C), banco de gags y guía de tiempos. Leé primero `00-propuesta.md` |
| `investigacion-wtc/00-sintesis.md` | Datos reales de WTC Free Zone, cada uno con su estado (verificado o supuesto) |
| `investigacion-humor/` | Investigación de humor. Ya está resumida: no hay que rehacerla |
| `mockup/` | Mockup viejo en Python: sprites en texto, fuente 5×7, escenas |
| `ejemplo-visual/`, `propuestas-rundown.html` | Ejemplos en HTML ya entregados |
| `.claude/handoff/HANDOFF.md` | Último traspaso de la sesión de Claude: decisiones y pendientes |

## Estado al 13/10/2026

- **Decidido:**
  - Protagonista: Valentino. Falta saber si va como robot o como piloto de un robot.
  - Todo el arte lo hace Codex.
  - Resolución base de 320×180 y personajes de 16×24.
  - Premio final «VACACIONES GRATIS» con letra chica.
  - Humor que se ríe *con* las personas, nunca *de* ellas.
- **Arte:** ningún prompt se corrió todavía. Se empieza por `arte/prompts-codex/01-kit-base.md`. Antes hacen falta Python 3 y Pillow, y una cuenta con generación de imágenes. **No los instales vos**: pedíselo a la usuaria.
- **Pendiente de la usuaria:**
  - versión del guion (A, B, C o la mezcla);
  - nombre del juego;
  - duración (5 o 7 minutos);
  - qué es Fran;
  - rasgos de Nacho y su OK;
  - el gag de Andrea;
  - fotos del edificio.
- **El código del juego** (HTML + canvas) todavía no existe. Viene después del guion definitivo y de un prototipo con cajas grises cronometrado.

## Cómo retomar

1. Leé `.claude/handoff/HANDOFF.md` y `arte/PLAN-ARTE.md`.
2. Para trabajar en arte, **abrí la sesión dentro de `arte/`**, así se cargan sus reglas. Seguí los prompts en orden y respetá las puertas:
   - **Puerta 1:** style frame aprobado (prompt 05).
   - **Puerta 2:** OK de cada persona sobre su dibujo (después del prompt 13).
   - **Puerta 3:** guion definitivo antes de animar (prompt 14).
3. Mirá el estado de cada pieza en `arte/manifiesto.csv` y lo hecho en `arte/INFORME.md`. Los dos aparecen después del prompt 01.
4. Al terminar una sesión, sumá una entrada a `arte/INFORME.md` y actualizá la sección "Estado" de este archivo.

## Reglas

- Planificá primero y esperá la aprobación de la usuaria antes de escribir código o generar imágenes.
- No instales software, no hagas push ni deploy, no crees cuentas y no borres archivos sin que ella lo pida.
- Nunca uses claves de API ni el modo de imágenes que cobra por imagen.
- Antes de algo que cueste plata, preguntá.
- Separá siempre lo verificado (con fuente y fecha) de lo supuesto.
- Personas reales: no subas fotos de compañeros sin su OK, y cada persona aprueba su escena.
- Datos sin fuente pública (empresas, los 25 de Brasil, el medio piso 8): no salen en pantalla sin confirmación de la usuaria.
- Entregá archivos (PNG, HTML, PDF), no links a servicios que la usuaria tenga que abrir desde el iPhone.

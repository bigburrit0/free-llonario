# Traspaso — Juego de noticias WTC Free Zone (ex "Free-llonario") — 2026-10-12 22:35

## Próximo paso exacto
Pedirle a la usuaria tres cosas y esperar: (1) el texto de "Copiar mis respuestas" de `propuestas-rundown.html` (sus respuestas viven en el localStorage de su iPhone; Claude no puede leerlas); (2) Valentino como protagonista: ¿**robot** (`VAL-01`…`07`) o **él manejando al robot** (`VAL-08`)?; (3) nombre del juego. Con eso, despachar una tarjeta (implementador o mecanico según el caso) que reescriba la versión elegida con Valentino protagonista + premio con letra chica + arco del dragón ajustado, y pasarla a `claude/plan.md`. Comprobar: el guion nuevo tiene 8 escenas, cubre las 13 noticias y no queda "Cami protagonista" en ningún lado.

## Objetivo
Juego pixel art 8-bit (formato "¿Quién quiere ser millonario?", side scroller, 8 pisos de ascensor) para presentar las 13 noticias del equipo de WTC Free Zone en una reunión: se proyecta, una persona maneja, la sala grita. ~6 min (falta definir 5 o 7).

## En curso (interrumpido)
Nada a medias. Ningún archivo quedó editado a medias.

## Contexto que solo estaba en la conversación
- **Protagonista: Valentino**, ya no Cami (pedido de la usuaria, 12/10). Valentino **aceptó** (lo dijo la usuaria). Falta: robot o piloto del robot. Por qué encaja: el robot que automatiza vs. el Papelón (papeleo) = noticia 1 contada como historia.
- Cami pasa a ser personaje secundario: su noticia ("Cami se unió al equipo", E4) queda como escena con el gag de la credencial VISITANTE→CASI→EQUIPO (`CAM-06`). El dragón es de Cami: su arco (falla E1, falla E2, acierta E8) hay que rehacerlo — propuesta: aparece cuando Cami se suma (piso 4) y remata en el piso 8 (velitas o quemar/iluminar la letra chica), o se le escapa a Cami y acompaña a Valentino.
- **Gag principal nuevo: premio con letra chica**, inspirado en un cartel de pub que dice en grande "FREE … BEER" y en chico "wifi & great". Elegido: **«VACACIONES GRATIS»** con letra chica **«*15 MINUTOS, EN LA TERRAZA DEL PISO 8, CON MATE PROPIO.»** Arco en 3 tiempos: intro (rayita ilegible), mitad (asoma), final (lupa y revelación). Idea extra: escalera de premios con letra chica en cada piso. Con relevo/equipo: «VACACIONES GRATIS PARA TODO EL EQUIPO*». Otras opciones descartadas por ahora: «100 % LIBRE DE IMPUESTOS» / «MEDIO PISO PARA VOS» (el 8½) / «VIAJE A BRASIL» / «UNA TORTA ENTERA (97 %)».
- **Animación:** la usuaria está dispuesta a gastar tokens en animación → la versión B (cine mudo, la más cara) vuelve a ser viable; rehacer la recomendación cuando lleguen sus respuestas.
- **Nombre:** "Free-llonario" no le gusta. Propuestos: "WTC: Who Takes the Cake" (favorito si va A, por la torta), "¿Quién quiere ser Franco?", "Piso 8½", "Letra chica", "Sujeto a propuesta comercial". Sin elegir.
- **Nacho es el CEO** de WTC Free Zone (dato de la usuaria; Uruguay XXI lista a "Ignacio Del" como CEO). En pantalla solo "Nacho", sin apellido. Sus gags (pelota XXL, saque 50:50) necesitan su OK antes que nadie. No es candidato a protagonista (riesgo de chupamedias o de burla al jefe).
- **Escenarios y fotos:** la usuaria ofreció mandar fotos de WTC Free Zone. Pedidas: fachada y pasarela entre torres, lobby, ascensor por dentro (botonera, display), cochera (y la columna de Lu), oficina o sala, terraza y vista, logo y colores. Después: armar una "guía de escenarios" (espacio por piso, paleta, objetos).
- Investigación WTC (resumen en `investigacion-wtc/00-sintesis.md`): nombre en pantalla **"WTC Free Zone"** (no "Zona Franca WTC"); ROUNDTABLE = **16 organizaciones sociales** (no "fundaciones") [sin verificar del todo]; **OMBIJAM es una asociación civil** que trabaja con personas privadas de libertad/liberadas y familias → el final con torta es una fiesta **para** ellos, sin chistes sobre su tema; 12 vs 10 años [sin verificar]; 2 torres / 44 pisos según sitio oficial [sin verificar del todo]; posible piso 22 como piso real de eventos [sin verificar]. Sin fuente pública: QI TECH, DANNEMANN, Laib, Fran, agente comercial, 25 empresarios de Brasil, medio piso 8, colores/logo.
- Ajustes pendientes del ejemplo visual (vistos por el orquestador): el acercamiento "mira a cámara" queda abierto (debería ser solo la cara); el dragón flota suelto (debería ir en el hombro); el protagonista se ve chico al lado del afiche → usar primeros planos. Y ahora: cambiar a Cami por Valentino (el mockup tiene sprite `VALE` en `mockup/sprites.py`).

## Decisiones (no reabrir)
- Se proyecta en reunión; una persona maneja, la sala responde.
- **Arte: todo con Codex** (decisión de la usuaria del 13/10/2026; reemplaza "arte mixto"). Plan, reglas y prompts en `arte/` (`PLAN-ARTE.md`, `AGENTS.md`, `prompts-codex/`). Los sprites del mockup son provisorios.
- **Protagonista: Valentino** (aceptó). Reemplaza la decisión anterior "Protagonista Cami".
- Premio final: «VACACIONES GRATIS» con letra chica (texto arriba).
- 8 preguntas = 8 pisos, 3 actos.
- Humor: reírse con, no de; el villano es el papeleo (no BPS ni DGI); un localismo por escena; sin humor negro; todo se entiende sin audio.
- Tras cada remate, el juego espera a quien maneja.
- Escena de chiste: 2 cuadros de 90 caracteres o 3 de 50; remate en cuadro propio.
- Entregables como archivo local (HTML/PDF/PNG), nunca artifacts.

## No repetir
- No investigar humor de nuevo (`investigacion-humor/00-sintesis.md`).
- No mandar artifacts: el iPhone de la usuaria no los abre.
- No intentar correr los `.py` del mockup en esta PC: **Python no está instalado** ("Python was not found", 12/10). Instalarlo requiere su OK. Se usa HTML + canvas y Node (v24.19.0, sí está).
- No investigar de nuevo WTC Free Zone en la web: ya está en `investigacion-wtc/00-sintesis.md` y en la biblioteca (`wtc-free-zone`). Lo que falta lo da la usuaria.
- El plan viejo en Docs artifact (https://claude.ai/code/artifact/76deb3f4-c0ca-496a-bb98-0802fd2f6732) está desactualizado; la fuente buena son los archivos locales.

## Pendientes en orden
1. Recibir respuestas del HTML, robot o piloto, nombre, duración (5 o 7 min).
2. Reescribir el guion elegido con Valentino + letra chica + dragón; pasarlo a `claude/plan.md`; actualizar `claude/elenco.md`.
3. Tarjeta de ajustes del ejemplo visual (Valentino, primer plano, dragón en el hombro).
4. Fotos → guía de escenarios.
5. Fichas de OK por persona (`guion-humor/06-guia-de-timing.md` §11): Nacho primero; también Lu, Andrea, Cami, Valentino (robot/piloto).
6. Fichas técnicas por personaje para que la usuaria dibuje.
7. Prototipo en cajas grises, cronometrado (pruebas de `06` §10).
8. Arte final, audio, integración, prueba con 3–5 personas; entrega + video de respaldo.

## Preguntas abiertas para el usuario
- Valentino: ¿robot o piloto del robot?
- ¿Nombre del juego? ¿Duración 5 o 7 min?
- ¿Qué gag elige Andrea? ¿Nacho da el OK a la pelota/50:50?
- ¿Qué son Fran, QI TECH, DANNEMANN, Laib, el agente comercial? ¿Fuente de los 25 de Brasil y del medio piso 8?
- ¿El destino es el piso 8 (inventado) o el 22?
- ¿Copiar la síntesis WTC también a `D:\New\biblioteca\raw\`? (pregunta del librarian)
- Fecha de la reunión, ¿hay parlantes?, ¿hay oradores?

## Hecho en esta sesión
- Página para recorrer las 3 propuestas + mezcla, con reacciones por escena, decisiones y "Copiar mis respuestas" → `propuestas-rundown.html` — verificado (aceptación node 10/10 OK; navegador 375 px sin scroll lateral, sin errores; copiar cae al recuadro manual en la vista previa). Entregado a la usuaria.
- Investigación WTC Free Zone (3 investigadores) → `investigacion-wtc/00-sintesis.md` — verificado que existe; datos con su estado adentro.
- Ingesta en biblioteca → `D:\New\biblioteca\wiki\wtc-free-zone.md`, `wiki\fuente-sintesis-wtc-free-zone-2026-10-12.md`, `index.md` (líneas 10 y 13), `log.md` — verificado con grep en index.
- Ejemplo visual animado del premio → `ejemplo-visual/premio-letra-chica.html` — verificado (aceptación 10/10 OK; cuadros 3,2 / 8,5 / 10,5 / 11,4 / 12 / 13 s revisados en navegador, sin errores). «Guardar PNG» y el iPhone [sin verificar]. Usa Cami (hay que cambiarla).
- Rundown del dragón entregado en el chat (tabla por versión; piezas en `guion-humor/01-banco-de-gags.md` §1, `CAM-01`…`CAM-10`).

## Mapa
- Leer si hace falta: `guion-humor/00-propuesta.md` (comparación y decisiones §4) — al recomendar versión; `guion-humor/02|03|04-guion-*.md` — al reescribir; `guion-humor/01-banco-de-gags.md` §1 (Cami/dragón) y la sección de Valentino (`VAL-*`) — al reescribir; `guion-humor/06-guia-de-timing.md` §3, §5, §10, §11 — límites, recorte a 5 min, pruebas, fichas de OK; `claude/elenco.md` — al actualizar elenco; `investigacion-wtc/00-sintesis.md` — datos reales.
- No hace falta releer: `investigacion-humor/` (resumido en `00-sintesis.md`); `.claude/handoff/HANDOFF-2026-10-12-2235.md` (traspaso anterior, ya integrado acá); `claude/HANDOFF.md` (traspaso del 11/10).
- Mockup (referencia para portar a JS): `mockup/font.py` (fuente 5×7; se agregó `*` en el HTML), `mockup/sprites.py` (`PAL`, `CAMI`, `VALE`, `DRAGON`, `FLAME`…), `mockup/studio.py` (estudio de TV), `mockup/scene.py` (`W`,`Hh`=320×180).
- Comandos: aceptación del ejemplo visual: `node "C:\Users\gomez\AppData\Local\Temp\claude\D--New-free-llonario\866a4f82-47e7-4d4f-a548-0be7c484476d\scratchpad\check-fl06.js"` (el scratchpad es de esta sesión; puede no existir en otra) [sin verificar en sesión nueva]. Ver los HTML: abrir el archivo en el navegador integrado (`file:///D:/New/free-llonario/free-llonario/...`).
- Ojo con la ruta: el proyecto está en `D:\New\free-llonario\free-llonario\` (carpeta anidada), no en `D:\New\free-llonario\`.
- Cambios sin commitear: no es repo git.

## Preferencias del usuario
- Español rioplatense con voseo, claro, sin jerga; no es desarrolladora.
- Trabaja desde el iPhone: entregar HTML/PDF/PNG como archivo, no artifacts.
- Plan primero y esperar aprobación; el orquestador planifica y verifica, los subagentes escriben (tarjetas según `D:\New\equipos\REGLAS-TARJETAS.md`).
- Separar verificado de supuesto, con fecha.
- Humor cariñoso; cada persona aprueba su escena.

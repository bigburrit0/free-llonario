# Traspaso — Free-llonario (juego de noticias WTC Free Zone) — 2026-10-11 22:25

## Próximo paso exacto
Esperar que el usuario elija versión de guion (A, B, C o la mezcla recomendada: A + carteles de C + sepia→color de B + zócalo) y responda las decisiones de `guion-humor/00-propuesta.md`, sección 4. Con eso, pasar la versión elegida a `plan.md` (sección "Guion por escenas") y actualizar estructura, tiempos y reglas de humor.

## Objetivo
Videojuego pixel art 8-bit, side scroller, selective outline, formato "¿Quién quiere ser millonario?" en modo story time, para presentar las noticias del equipo en el WTC Free Zone. Proyectado en una reunión. Duración en discusión: la descripción del proyecto dice ≤ 5 min y el plan dice ≤ 7.

## En curso
Ninguno. Investigación de humor y propuesta de guiones entregadas; falta la elección del usuario.

## Contexto que solo estaba en la conversación
- Las 13 noticias están en `plan.md` (tabla "Cobertura de las 13 noticias").
- Torre 1 = cuadrada, temática naranja. Torre 2 = redonda, temática azul.
- El iPhone del usuario NO abre artifacts de claude.ai: entregar PDF o PNG. El PDF de la propuesta de humor (66 págs. A5) se le mandó como archivo; se regenera con pandoc + wkhtmltopdf a partir de `guion-humor/*.md`.
- Mockup: con la tipografía 5×7, las cápsulas de respuesta entran ~15 letras en una línea. Se propuso ensanchar a 2 × 152 px y 2 líneas (~36 caracteres). Faltan glifos: % ½ ¾ ( ) « » ' ;
- Doc original del plan (artifact Docs, desactualizado): https://claude.ai/code/artifact/76deb3f4-c0ca-496a-bb98-0802fd2f6732

## Decisiones (no reabrir)
- Se juega proyectado en reunión; una persona maneja, la sala responde.
- Arte mixto: el usuario dibuja personajes; Claude escenarios e interfaz.
- Protagonista: Cami. Público: solo el equipo (se permiten chistes internos).
- Estructura: 8 preguntas = 8 pisos del ascensor; 3 actos; ~6 min.
- Humor: reírse con, no de; el villano es el papeleo, no BPS ni DGI; un localismo por escena.

## Pendientes en orden
1. Elección de versión y decisiones de `guion-humor/00-propuesta.md` §4 (duración, cápsulas, parlantes, OK de Valentino/Lu/Andrea/Nacho/Cami, qué es Fran).
2. Pasar el guion elegido a `plan.md`.
3. Fichas de OK por persona (`guion-humor/06-guia-de-timing.md` §11).
4. Fichas técnicas por personaje para que el usuario dibuje.
5. Prototipo con cajas grises, cronometrado; las 4 pruebas de `06-guia-de-timing.md` §10.
6. Arte final, audio, integración, prueba con 3–5 personas, entrega + video de respaldo.

## Preguntas abiertas para el usuario
- Foto o rasgos de Nacho; ¿es del Equipo de Innovación? ¿Qué gag elige Andrea?
- ¿Los secundarios los dibuja el usuario o Claude?
- ¿Qué es Fran hoy? ¿Qué es OMBIJAM? ¿A qué se dedican QI TECH, DANNEMANN y Laib?
- Colores oficiales, logo, fotos de las torres. ¿Dónde fue el ROUNDTABLE? Fecha, ¿hay parlantes?

## Hecho
- Plan completo → `claude/plan.md`; elenco → `claude/elenco.md`; mockup → `mockup/*.py`.
- Investigación de humor con 10 enfoques + síntesis → `investigacion-humor/` (verificado).
- Propuesta de humor y guiones → `guion-humor/` (verificado: textos dentro de los límites de pantalla, relojes A 6:30 / B 6:32 / C 6:28, las 13 noticias en las 3 versiones).

## Mapa
- `guion-humor/00-propuesta.md` — análisis del plan, comparación A/B/C, recomendación, decisiones. Leer primero.
- `guion-humor/01-banco-de-gags.md` — 82 gags con códigos (CAM, VAL, LU, NAC, AND, FRAN, AGE, GAV, PAP, BAR, ASC, TOR, MEC), logros, opciones de respuesta.
- `guion-humor/02`, `03`, `04` — guiones completos A (torta), B (cine mudo), C (TV en vivo).
- `guion-humor/05-skits-y-capas.md` — avisos falsos, murga, skits, post-créditos.
- `guion-humor/06-guia-de-timing.md` — plantilla de escena de 10 s, límites de texto, latido de ~38 s, corte a 5 min, pruebas, ficha de OK.
- `investigacion-humor/00-sintesis.md` — evidencia que respalda las reglas.
- `claude/plan.md` — plan completo; su guion todavía es el original (sin la reescritura de humor).
- Comandos del mockup: `cd mockup && python3 scene.py && python3 studio.py && python3 cast.py` (Pillow).

## Preferencias del usuario
- Español rioplatense. Usuario arteterapeuta/artista, trabaja desde iPhone: entregar PDF/PNG.
- Quiere planificar a fondo y que se le hagan preguntas para sacar dudas.

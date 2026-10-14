# Cómo usar estos prompts

## Antes de empezar (una sola vez)

1. Resolvé las decisiones 1 y 2 de `../PLAN-ARTE.md` (Codex instalado con un plan que genere imágenes; Python y Pillow).
2. Si tenés fotos del edificio, ponelas en `arte/referencias/fotos/` con nombres claros: `torres-frente.jpg`, `lobby.jpg`, `cochera.jpg`, `ascensor-adentro.jpg`, `terraza.jpg`. Fotos de compañeros, no (salvo que cada uno dé el OK).
3. Abrí Codex **dentro de la carpeta `arte`**: `D:\New\free-llonario\free-llonario\arte`. Si lo abrís en otra carpeta, no lee `AGENTS.md` y no sigue las reglas.

## Cada vez

1. Abrí el archivo del prompt que toca, en orden (01, 02, 03…).
2. Copiá **solo** lo que está entre `COPIAR DESDE ACÁ` y `HASTA ACÁ`.
3. Pegalo en Codex y esperá. Codex genera, pixela, revisa y te muestra una vista ampliada.
4. Mirá la vista y el informe. Fijate que diga `validar.py: OK`.
5. Si te gusta, escribile a Codex: `Aprobado. Pasá <nombre de la pieza> a "aprobado" en el manifiesto.`
6. Si algo no te gusta, usá la plantilla `90-corregir.md`. **Un cambio por vez.**
7. Antes de cerrar Codex, verificá que la pieza esté en `arte/final/` y no solo en la conversación.

## Por qué hay partes en inglés

La descripción que Codex le pasa al generador de imágenes está en inglés a propósito: el vocabulario del pixel art ("selective outline", "no anti-aliasing") funciona mejor así. No hace falta que la entiendas; las instrucciones para Codex están en español.

## Puertas: dónde parar

- **Después del 05 (style frame):** no sigas hasta aprobar cómo se ve el juego. Si algo del estilo no te convence, es acá donde conviene cambiarlo.
- **Después del 13 (retratos):** mostrale a cada persona su ficha y su retrato y pedile el OK.
- **Antes del 14 (animaciones):** esperá el guion definitivo y el prototipo cronometrado. Animar lo que después se corta gasta límite de Codex.

## Si algo sale mal

- **Codex dice que falta Python o Pillow:** volvé a la decisión 2 del plan.
- **Codex quiere usar una clave de API o el modo por línea de comandos:** decile que no. `AGENTS.md` lo prohíbe porque cobra por imagen.
- **`validar.py` da FALLA dos veces seguidas en la misma pieza:** pará y avisame (a Claude), con el informe de Codex.
- **El personaje sale distinto en cada cuadro:** pedile a Codex que rehaga los cuadros desde el mapa del cuadro base, copiando la cabeza (está en `AGENTS.md`, "Consistencia").
- **Se te terminó el límite de Codex:** anotá el número del último prompt aprobado y seguí otro día. Nada se pierde: todo queda en `arte/`.

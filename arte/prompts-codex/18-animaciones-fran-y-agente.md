# 18 · Animaciones de Fran y el agente comercial

> **Para vos:** Fran 1.0 se tilda; Fran 2.0 habla, saluda distinto a cada uno, se marea y suelta una lágrima de un píxel en el final. Los tres zooms son el chiste del suspenso: en cada «¿última respuesta?» Fran se acerca más, hasta que en la pregunta final solo se ve un ojo. El agente camina detrás del protagonista, guía a los 25 con la banderita, ofrece folletos y tararea en el ascensor.
>
> **Antes:** Puerta 3.

---- COPIAR DESDE ACÁ ----

Seguí AGENTS.md, sección "Proceso de animación". Personajes: `fra` (bases `fra_v1-base` y `fra_v2-base`; fondo magenta) y `age` (bases `age_base`, `age_frente`, `age_bandera`).

| # | Pieza | Cuadros | Cuadro | fps | Bucle | Manera | Notas |
|---|---|---|---|---|---|---|---|
| 1 | fra_v1-quieto | 2 | 32x24 | 3 | sí | mapa | Los ojos de bloque parpadean |
| 2 | fra_v1-tildado | 2 | 32x24 | 12 | sí | mapa | Cuadro 2: la cara corrida 2 px a la derecha con una franja horizontal cortada |
| 3 | fra_v2-quieto | 2 | 32x24 | 3 | sí | mapa | Parpadeo |
| 4 | fra_v2-hablar | 2 | 32x24 | 6 | sí | mapa | Boca cerrada / abierta |
| 5 | fra_v2-saludos | 3 | 32x24 | 1 | no | mapa | 1: guiño y sonrisa amplia (a la sala). 2: ojos cuadrados de robot y boca recta (a Valentino). 3: ojos redondos y boca en O como un pico (a la gaviota) |
| 6 | fra_v2-mareado | 2 | 32x24 | 6 | sí | mapa | Ojos en espiral que giran |
| 7 | fra_v2-lagrima | 1 | 32x24 | 1 | no | mapa | Sonrisa emocionada y una lágrima de 1 px en `h` bajo un ojo |
| 8 | fra_zoom1 | 1 | 64x48 | 1 | no | imagen | `--tipo fondo` (imagen llena, sin transparencia) |
| 9 | fra_zoom2 | 1 | 128x96 | 1 | no | imagen | `--tipo fondo` |
| 10 | fra_zoom3 | 1 | 128x96 | 1 | no | imagen | `--tipo fondo` |
| 11 | age_quieto | 2 | 12x16 | 3 | sí | mapa | Quieto estándar |
| 12 | age_hablar | 2 | 12x16 | 6 | sí | mapa | Hablar estándar (los ojos de la pantallita cambian) |
| 13 | age_caminar | 4 | 12x16 | 8 | sí | imagen | Caminar estándar con pasitos cortos, cabeza fija `0,-1,0,-1` |
| 14 | age_bandera-caminar | 4 | 12x16 | 8 | sí | imagen | Caminar estándar con la banderita en alto (base `age_bandera`) |
| 15 | age_folleto | 2 | 12x16 | 4 | no | mapa | Cuadro 1: brazo estirado con un folleto blanco de 3×4 px. Cuadro 2: brazo un poco más adelante |
| 16 | age_tararear | 2 | 12x16 | 4 | sí | mapa | Ojos cerrados como `^ ^`, la cabeza se inclina a un lado y al otro |

Descripciones de los zooms (cada uno es una imagen aparte, con `fra_v2-base` como "identity reference"; estas imágenes ocupan todo el cuadro, sin fondo verde):

- **fra_zoom1:** `Close-up of the friendly monitor TV host (version 2.0 from the identity reference): the monitor fills most of the image, face clearly visible on its blue screen, looking straight at the viewer with a suspenseful, slightly raised eyebrow. Drawn as a 64 by 48 pixel image enlarged so each art pixel is a 16 by 16 block.`
- **fra_zoom2:** `Extreme close-up: only the screen face of the same monitor host, filling the whole image, eyes narrowed in suspense, tiny smirk. Drawn as a 128 by 96 pixel image enlarged so each art pixel is an 8 by 8 block.`
- **fra_zoom3:** `Macro close-up of a single big eye of the same screen face, filling the whole image, pupil looking straight at the viewer, dramatic suspense. Drawn as a 128 by 96 pixel image enlarged so each art pixel is an 8 by 8 block.`

Agregá a cada una el bloque de estilo de AGENTS.md (sin la línea del fondo verde) y "No text, letters, numbers, logos, watermarks, labels or grid lines anywhere."

Al final:
1. `vistas/fra-age_animaciones.png`: todas las tiras a ×6 con su nombre, y los tres zooms lado a lado.
2. Con `componer.py`, `vistas/escenas/agente-sigue_x4.png`: exterior con `val_caminar` cuadro 1 y `age_caminar` cuadro 3, 16 px atrás.

Terminaste cuando:
- `validar.py` da OK en cada pieza.
- Existe un GIF por pieza animada y las dos vistas finales.

Informe según AGENTS.md, con una línea por pieza.

---- HASTA ACÁ ----

# ¿Quién quiere ser Free-llonario? — Plan del juego de noticias

Actualizado: 11 de octubre de 2026

> **Cambios del 11/10 (prevalecen sobre el resto del plan):** el equipo es Valentino Franchini ("Valen", varón, aparece como robot), Lu (Lucía Licio), Andrea Cuervo ("Andre") y Camila Arrarte ("Cami", fan de los dragones). Se suma Ignacio "Nacho", siempre con una pelota de tenis XXL. Escena nueva: Lu llega en su Suzuki rojo, choca contra una columna y dice "¿Quién dejó esa columna ahí?". Todos aceptaron ser personajes. Ver `elenco.md`.

## Resumen y concepto

Un side-scroller pixel art de unos 6 minutos donde Cami vive su primer día en el WTC Free Zone y descubre, escena por escena, lo que hizo el equipo. Cada noticia termina en una pregunta estilo "¿Quién quiere ser millonario?" y cada respuesta sube el ascensor un piso, hasta llegar al piso 8.

**Cómo conviven los tres formatos**

- **Story time es la columna vertebral:** una protagonista, un día que avanza de la mañana a la noche y personajes que cuentan las noticias.
- **El side-scroller es el pasillo entre noticias:** caminar hacia la derecha por el campus y las torres. No se muere, no se pierde, no se repite.
- **El formato Millonario es el momento de cada noticia:** pregunta, 4 opciones, "¿última respuesta?" y revelación.

**La idea que ata todo:** la escalera de premios es el display del ascensor. 8 preguntas, 8 pisos, y el gran premio es "el medio piso del 8 (sujeto a propuesta comercial)".

**Títulos posibles:** ¿Quién quiere ser Free-llonario? (recomendado) · ¿Quién quiere llegar al piso 8? · Torre a Torre: edición noticias.

## Decisiones y supuestos

| Tema | Decisión o supuesto |
| --- | --- |
| Cómo se juega | **Decidido:** proyectado en una reunión; una persona maneja y la sala responde en voz alta |
| Protagonista | **Decidido:** Cami, en su primer día en el Equipo de Innovación |
| Arte | **Decidido, mixto:** vos dibujás los personajes; Claude hace escenarios e interfaz |
| Público | **Decidido:** solo el equipo; hay lugar para chistes internos |
| Presentador | Fran 2.0 (supuesto) |
| Idioma | Español rioplatense con voseo, guiños en portugués en el acto comercial |
| Formato técnico | Una página web (HTML) sin instalación |
| Ediciones futuras | Textos separados del código para reusar el juego |

## Estructura y tiempos

| Bloque | Qué pasa | Momento del día | Preguntas | Duración |
| --- | --- | --- | --- | --- |
| Título e intro | "Presioná Start" y Fran explica la regla | Amanecer | 0 | 0:30 |
| Acto 1 · Innovación | El Papelón, la tarea con barba, Fran 2.0 y el equipo | Mañana | 4 | 2:30 |
| Acto 2 · Comercial | La mudanza brasilera, el tour de los 25 y el piso 8½ | Mediodía | 2 | 1:20 |
| Acto 3 · Sostenibilidad | La mesa redonda y las 12 velitas | Atardecer | 2 | 1:10 |
| Final | Torres iluminadas, resultado y créditos | Noche | 0 | 0:35 |
| **Total** | | | **8** | **6:05** |

**El latido de cada noticia (unos 36 s):** caminar 5 s → escena con chiste 10 s → pregunta hasta 12 s → "¿última respuesta?" y revelación 3 s → tarjeta de noticia 6 s.

**Cómo se cuida el tope de 7 minutos**

- Si nadie toca nada 3 s durante una caminata, Cami camina sola.
- A los 20 s sin respuesta Fran tira una pista; a los 30 s se revela.
- Botón "Saltar escena" siempre visible.
- Máximo 3 cuadros de diálogo por escena, unos 90 caracteres cada uno.
- Se cronometra con un prototipo sin arte antes de producir.

## Flujo del usuario

1. Pantalla de título (Presioná Start)
2. Fran explica la regla (2 cuadros y controles)
3. Cami llega al campus al amanecer
4. **Ciclo × 8:** Caminar → Escena → Pregunta → Revelación → Tarjeta (tras las escenas 4 y 6: ascensor y cambio de acto)
5. Resultado y rango
6. Créditos con repaso de las 13 noticias
7. Jugar de nuevo o fin

La tarjeta de cada noticia aparece siempre, se acierte o no.

## Gameplay y controles

**Mecánicas**

- Caminar hacia la derecha. Saltar es opcional y solo sirve para juntar mates.
- Sin enemigos ni vidas. El "jefe", El Papelón, es una escena guionada.
- Un momento interactivo por acto: desarmar al Papelón, contar a los 25 empresarios, soplar las 12 velitas.
- Logros de 2 s: "Sobreviviste al Papelón", "Jugador 2 se unió", "Contaste hasta 25".
- Coleccionable opcional: 12 mates.

| Acción | Teclado | Celular |
| --- | --- | --- |
| Caminar | Flecha derecha | Mantener lado derecho |
| Saltar | Flecha arriba | Botón A |
| Avanzar o confirmar | Espacio, Enter o AvPág | Tocar la pantalla |
| Elegir respuesta | Teclas 1 a 4 | Tocar la opción |
| Comodines | F, L y A | Tocar el ícono |
| Pausa y sonido | Esc y M | Íconos arriba |

En modo presentación, AvPág permite usar un clicker. Quien maneja elige lo que grita la sala, y "Preguntale al lobby" puede ser la sala votando a mano alzada.

**Comodines (uno de cada uno)**

| Comodín | Equivale a | El chiste |
| --- | --- | --- |
| Preguntale a Fran | 50:50 | Fran 2.0 "personaliza" la ayuda y saca 2 incorrectas |
| Preguntale al lobby | Público | Barras de votación; en el acto 2 votan en portugués |
| Mandalo a Asana | Llamar a un amigo | "Tiempo estimado: casi un año… mentira, ya está cerrado" |

**Escalera = display del ascensor:** pisos 1 a 8. Acierto: verde con tilde. Error: gris con cruz, pero el ascensor sube igual.

| Aciertos | Rango | Remate |
| --- | --- | --- |
| 8 | Free-llonario/a | Te ganaste el medio piso del 8 (sujeto a propuesta comercial) |
| 5 a 7 | Integrante honorario/a de Innovación | Cami te guarda un lugar en el pizarrón |
| 2 a 4 | Visitante VIP | Como los 25 de Brasil, pero sin tour |
| 0 a 1 | Recién llegado/a | Igual que Cami el primer día. Tranqui |

## Guion por escenas y preguntas

### Intro
Fran 1.0, robótico: "Bienvenidos. A. ¿Quién quiere ser Free-llonario? Cada noticia es una pregunta. Cada acierto, un piso." Corte a Cami llegando al amanecer: "Primer día. ¿Qué tan difícil puede ser?"

### Escena 1 · El Papelón (Innovación, piso 1)
- **Dónde:** lobby de la Torre 1, mañana.
- **Qué pasa:** Valentino (robot) recibe a Cami. Se levanta El Papelón, una montaña de formularios con ojos. Lu: "Tranqui, apretá el botón." Un brazo robot sella VALIDADO y el Papelón se desarma en confeti.
- **Pregunta:** ¿Qué automatizó el Equipo de Innovación? A) Las excusas para llegar tarde · **B) La validación de documentación de proveedores en BPS y DGI** · C) El sorteo de quién lava las tazas · D) Imprimir todo en 3 copias
- **Tarjeta:** Automatizamos la validación de documentación de proveedores en BPS y DGI.

### Escena 2 · La tarea con barba (Innovación, piso 2)
- **Dónde:** la cochera.
- **Qué pasa:** junto a la barrera, una tarjeta de Asana con barba larguísima: "Abierta hace… casi un año." Andre la completa: fuegos artificiales, se cae la barba, la barrera se abre. Al fondo, cartel "Próximamente: Punta del Este" y una gaviota con casco tildando una checklist.
- **Pregunta:** ¿Cuánto estuvo abierto el proyecto de cocheras en Asana? A) 15 minutos · B) Desde que se inventó el auto · C) Sigue abierto, no le digas a nadie · **D) Casi un año**
- **Tarjeta:** Cerramos el proyecto de cocheras tras casi un año e implementamos integralmente los sistemas de cocheras. Además, validamos los requerimientos del nuevo sistema para Punta del Este.

### Escena 3 · Actualizando a Fran 2.0 (Innovación, piso 3)
- **Dónde:** oficina de Innovación.
- **Qué pasa:** "Actualizando a Fran 2.0… 99%… 99%… 100%". Fran saluda en tres modos: formal, uruguayo y brasilero. Se enciende un robotito de traje: "Agente comercial, listo para acompañar y agilizar." Desde acá sigue a Cami.
- **Pregunta:** ¿Qué tiene de nuevo Fran 2.0? A) Ahora ceba mate · B) Contesta todo con "ta" · **C) Es más personalizada y se adapta a distintos públicos** · D) Modo oscuro y opiniones de fútbol
- **Tarjeta:** Desarrollamos Fran 2.0 y el agente comercial, que acompaña y agiliza la gestión comercial.

### Escena 4 · ¡Cami se unió al equipo! (Innovación, piso 4)
- **Dónde:** sala con pizarrón de post-its.
- **Qué pasa:** pantalla de grupo estilo RPG con Valen, Lu y Andre; entra Cami. Llueven post-its: "Estudio de Innovación: nueva metodología". Aviso: "Laib se unió a la partida. Jugador 2".
- **Pregunta:** Completá el equipo: Valen, Lu, Andre y… **A) Cami** · B) El robot de la cochera · C) Fran en forma humana · D) Una gaviota que vino a todas las reuniones
- **Tarjeta:** El Equipo de Innovación crece con Cami. Con el Estudio de Innovación diseñamos una nueva metodología y profundizamos el trabajo con Laib como partner tecnológico.

**Transición:** ascensor con bossa nova chiptune. Fran: "Olá!"

### Escena 5 · La mudanza (Comercial, piso 5)
- **Qué pasa:** llega un camión verde y amarillo; bajan cajas QI TECH y DANNEMANN y se prenden dos ventanas nuevas. "Bem-vindos!"
- **Pregunta:** ¿De dónde vienen QI TECH y DANNEMANN? A) Del piso de arriba · **B) De Brasil** · C) De un Excel con 40 pestañas · D) De Marte, con buena conexión
- **Tarjeta:** Se instalaron QI TECH y DANNEMANN, dos empresas brasileras.

### Escena 6 · El tour de los 25 (Comercial, piso 6)
- **Qué pasa:** el agente comercial, con banderita de guía, encabeza una fila de 25 empresarios que se pueden contar.
- **Pregunta:** ¿Cuántos empresarios de Brasil vinieron? A) 5 · B) 12 · **C) 25** · D) Uno solo que dio 25 vueltas
- **Tarjeta:** Nos visitaron 25 empresarios de Brasil, y trabajamos en propuestas para el medio piso del 8.
- **Remate:** el ascensor marca 8½ y la puerta se abre a medias. Cami: "¿Medio piso? ¿Entro agachada?"

### Escena 7 · La mesa redonda (Sostenibilidad, piso 7)
- **Dónde:** Torre 2, la redonda, al atardecer.
- **Qué pasa:** mesa redonda con 16 representantes de fundaciones. Cami: "¿Por qué redonda?" Lu: "Así nadie se pelea por la cabecera."
- **Pregunta:** ¿Cuántas fundaciones reunió el ROUNDTABLE? **A) 16** · B) 160 · C) 1.600 · D) Las que entraron alrededor de la mesa
- **Tarjeta:** Realizamos el ROUNDTABLE, que reunió a 16 fundaciones.

### Escena 8 · Doce velitas (Sostenibilidad, piso 8, pregunta final)
- **Qué pasa:** torta con 12 velas en la terraza; se soplan, bajan las luces: pregunta final.
- **Pregunta:** ¿Cuántos años cumplió OMBIJAM? A) 21 · **B) 12** · C) 1,2 · D) 120 (se nos fue un cero)
- **Tarjeta:** Acompañamos a OMBIJAM en sus 12 años.

### Final
Noche, torres iluminadas en naranja y azul, fuegos lentos. Resultado, rango y logros. Créditos estilo consola con las 13 noticias, la tarea de Asana afeitada de vacaciones y "Gracias, equipo".

## Cobertura de las 13 noticias

| # | Noticia | Escena | Cómo aparece |
| --- | --- | --- | --- |
| 1 | Validación de proveedores BPS/DGI | 1 | Papelón, pregunta, tarjeta |
| 2 | Cierre Asana cocheras e implementación | 2 | Tarea con barba, pregunta, tarjeta |
| 3 | Requerimientos cocheras Punta del Este | 2 | Cartel y gaviota, tarjeta |
| 4 | Fran 2.0 | 3 | Pregunta, tarjeta, presentador |
| 5 | Agente comercial | 3 en adelante | Personaje acompañante, tarjeta |
| 6 | Equipo: Valentino, Lu, Andrea y Cami | 4 | Pregunta, protagonista |
| 7 | Metodología con Estudio de Innovación | 4 | Post-its, tarjeta |
| 8 | Laib como partner | 4 | "Jugador 2", tarjeta |
| 9 | QI TECH y DANNEMANN | 5 | Mudanza, pregunta, tarjeta |
| 10 | 25 empresarios de Brasil | 6 | Fila, pregunta, tarjeta |
| 11 | Medio piso del 8 | 6 y final | Ascensor 8½, premio mayor |
| 12 | ROUNDTABLE 16 fundaciones | 7 | Mesa redonda, pregunta |
| 13 | OMBIJAM 12 años | 8 | Velitas, pregunta final |

## Humor

Cariñoso y autorreferencial: nos reímos de situaciones de oficina, nunca de una persona. El chiste va en la escena y en las opciones absurdas; el dato va limpio en la tarjeta.

- Reírse con, no de. BPS y DGI no son villanos: el villano es el papeleo.
- Cada pregunta: una correcta, a veces una plausible, el resto absurdas.
- Un localismo por escena como máximo (mate, "ta", gaviotas).
- Humor gamer como pegamento: logros, barras de carga, "Jugador 2 se unió".
- Cada persona que aparece ve su escena antes de publicar.

**Chistes recurrentes:** Fran 1.0 vs 2.0 · la tarea de Asana con barba (afeitada en los créditos) · el agente comercial que acompaña · la gaviota multitarea ("interpretada por ella misma") · el ascensor y el piso 8½ · "sujeto a propuesta comercial".

## Dirección de arte

"8-bit inspirado": resolución baja y paleta limitada, con algunos tonos más por sprite para que funcione el selective outline.

- Resolución base 320 × 180 (16:9), escala entera ×4 o ×6, sin suavizado. Tiles de 16 × 16.
- Personajes de 16 × 24 px con cabeza grande; retratos de 24 × 24.
- Luz desde arriba a la izquierda.

| Rampa | Oscuro a claro | Uso |
| --- | --- | --- |
| Torre 1 naranja | #4A1F0E · #A3471B · #E8772E · #FFB765 | Torre 1, Innovación, respuesta elegida |
| Torre 2 azul | #0F1E45 · #1E4F9A · #3D8FE0 · #A8DBFF | Torre 2, cielo, Comercial |
| Neutros | #12111A · #3B3A4F · #7C7B91 · #C6C5D6 · #F5F4FA | Texto, interfaz |
| Verdes | #1C4430 · #3F8A3C · #95C653 | Plantas, aciertos, Sostenibilidad |
| Pieles | #4D3022 · #8E5B3B · #D19A6A · #F3CFA9 | Personajes |
| Estudio | #1A0F3D · #3A1F7A · #FFD43B | Fondo del show |
| Error | #E23A3A | Incorrecta, con cruz |

**Selective outline:** contorno con el tono más oscuro de la propia rampa (no negro); del lado de la luz se aclara o desaparece; líneas internas mínimas; capas lejanas sin contorno; la interfaz sí lleva contorno oscuro completo.

**Las torres:** Torre 1 = prisma cuadrado, fachada en grilla con franjas naranjas. Torre 2 = cilindro con bandas verticales azules, ventanas que se angostan hacia los bordes y techo elíptico. Hacen falta fotos para clavar proporciones.

**Un día en 4 paletas:** el exterior se dibuja una vez y se reusa en mañana, mediodía, atardecer y noche.

**Parallax:** cielo tramado · ciudad lejana 20 % · torres 50 % · calle 100 % · adornos delanteros 120 %.

**Interfaz:** caja de diálogo con retrato; estudio violeta con 4 respuestas en 2 × 2 (neutra azul, elegida naranja, correcta verde con tilde, incorrecta roja con cruz); display de ascensor de 7 segmentos; color por área (Innovación naranja, Comercial azul, Sostenibilidad verde). Fuentes a probar: Press Start 2P, Silkscreen, Pixelify Sans.

**Animación:** caminata de 4 cuadros, reposo de 2, a 8–10 fps; transiciones con iris.

## Audio

Todo se entiende sin sonido. Chiptune original, sin música ni logo del programa de TV. Tema principal, tema de estudio con tensión, pregunta final más lenta, muzak de ascensor (bossa nova en el acto 2), jingles cortos (el de error, amable) y efectos de 8 bits. Herramientas: BeepBox y jsfxr.

## UX, accesibilidad y legibilidad

- Título con un solo botón; la primera escena enseña jugando.
- Texto mínimo 8 px en base (48 px en 1080p), siempre sobre caja de diálogo.
- Probar en el proyector real.
- Correcto/incorrecto con tilde y cruz además de color; nada parpadea más de 3 veces por segundo.
- Siempre a mano: saltar escena, pausa y silencio. Al errar, la tarjeta da el dato igual.

## Técnica y entrega

Una sola página web (HTML + canvas), textos en un bloque de datos aparte, sprites reemplazables por tus PNG, se puede abrir sin internet. Plan B: video grabado del recorrido completo.

## Producción

1. Cerrar decisiones pendientes.
2. Guion definitivo validado con cada área.
3. Style frame: una pantalla terminada con las dos torres, Cami y un diálogo.
4. Prototipo con cajas grises, cronometrado (≤ 6 min).
5. Producción de arte y sonido.
6. Integración y pulido.
7. Prueba con 3 a 5 personas.
8. Entrega: link, archivo y video de respaldo.

**Tus personajes:** Aseprite, LibreSprite o Piskel. Exportar tiras de cuadros en PNG a tamaño real sobre la paleta acordada. Antes te paso una ficha por personaje.

## Riesgos

| Riesgo | Mitigación |
| --- | --- |
| Se pasa de 7 min | Recortar diálogos, auto-caminar, saltar |
| Un chiste cae mal | Cada persona revisa su escena |
| Un dato está mal | Validación con cada área |
| Se ve mal en el proyector | Probar en la sala real |
| No hay sonido | Todo se entiende sin audio |
| Falla la tecnología | Archivo descargado y video |
| Parecido excesivo al programa | Título, música y arte propios |

## Preguntas abiertas

- [x] Cómo se juega: proyectado en reunión.
- [x] Arte: mixto.
- [x] Protagonista: Cami.
- [x] Público: solo el equipo.
- [x] Todos aceptan ser personajes; fotos recibidas (falta foto de Nacho).
- [ ] Secundarios (agente, gaviota, Papelón, tarea, multitudes): ¿los dibujás vos o yo?
- [ ] ¿Qué es Fran hoy y tiene avatar?
- [ ] ¿Qué es OMBIJAM y cómo fue el acompañamiento?
- [ ] ¿A qué se dedican QI TECH y DANNEMANN, y qué es Laib?
- [ ] ¿Anécdotas o chistes internos para sumar?
- [ ] Colores oficiales, logo y fotos de las torres.
- [ ] ¿Dónde fue el ROUNDTABLE?
- [ ] Fecha de la presentación y ¿hay parlantes?
- [ ] ¿Edición única o se repite?

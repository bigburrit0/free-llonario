# Guía de timing y escritura cómica

Actualizado: 11/10/2026. Reglas prácticas para escribir, animar y presentar el humor del juego. Salen de `investigacion-humor/` y valen para las tres versiones del guion.

## 1. Siete principios (con su respaldo)

| # | Principio | En el juego | Evidencia |
|---|---|---|---|
| 1 | Lo gracioso es una violación benigna: algo "está mal" y a la vez es inofensivo | El Papelón, la columna, la tarea con barba, el 8½ | Moderada |
| 2 | El blanco decide el riesgo | Objetos, sistemas y el propio juego; nunca rasgos de personas | Baja–Moderada |
| 3 | La expectativa tiene que verse antes de romperse | Setup visible: cartel, regla, repetición | Opinión (Kant, Suls) |
| 4 | Pausa antes del remate | Beat sin texto antes del golpe | Baja (Ma et al., 2026) |
| 5 | Espacio después del remate | La escena espera a que la sala ría | Baja (Lehmann-Willenbrock y Allen, 2014) |
| 6 | La risa es de la sala | Carteles de participación: REDOBLE, SOPLEN, CONTÁ | Moderada (cualitativo) |
| 7 | Si dudás, la versión amable | Un chiste amable que falla no cuesta nada; uno ácido que falla, sí | Moderada (Bitterly et al., 2017) |

## 2. Plantilla de escena de chiste (10 s)

| Tiempo | Qué pasa | Texto |
|---|---|---|
| 0–2 s | **Imagen sola.** La situación se entiende sin leer. | Ninguno |
| 2–5 s | **Setup.** Un solo dato o expectativa. | Cuadro 1, ≤ 50 caracteres |
| 5–6 s | **Beat.** Nada se mueve, o solo un detalle (un ojo, un parpadeo). | Ninguno |
| 6–8,5 s | **Remate.** En un cuadro propio, nunca junto al setup. | Cuadro 2, ≤ 50 caracteres |
| 8,5–10 s | **Reacción.** Doble take, mirada a cámara, logro. Acá ríe la sala. | Ninguno |
| + manual | **Espera.** El juego no avanza hasta que quien maneja aprieta. | — |

Variante de 12 s para escenas con dos golpes: se suma un tag (un segundo remate chico, casi siempre visual) entre el 10 y el 12.

## 3. Límites de texto

Las cifras salen de la velocidad de lectura (~238 palabras por minuto, `investigacion-humor/04` y `07`) y de la tipografía 5×7 del mockup (6 px por letra, en base 320×180).

| Elemento | Límite | Por qué |
|---|---|---|
| Cuadro de diálogo | ≤ 90 caracteres (2 líneas de ~43) | Lo que entra en la caja del mockup |
| Diálogo por escena | 2 cuadros de 90 **o** 3 de 50 | Tres de 90 tardan ~11 s, más que la escena |
| Pregunta | ≤ 60 caracteres (2 líneas) | Se lee en voz alta en ~4 s |
| Opción de respuesta | ≤ 36 caracteres (2 líneas de ~21) | Con el mockup actual entra **una línea de ~15 letras**; hace falta ensanchar las cápsulas a todo el ancho (2 × 152 px) y hacerlas de dos líneas (ver `00-propuesta.md`) |
| Tarjeta de noticia | ≤ 140 caracteres y avance manual | Es el dato serio: se lee completo |
| Intertítulo (versión B) | ≤ 40 caracteres | Es cartel de cine mudo: corto y grande |
| Zócalo | Libre | No compite con nada; nadie está obligado a leerlo |

**Glifos que faltan en `mockup/font.py`:** `%`, `½`, `¾`, `(`, `)`, `«`, `»`, `'`, `;`, `⏩`, `✓`. Hay que dibujarlos antes de producir: varios chistes dependen de «8½» y «99 %».

## 4. El latido revisado de cada noticia (~38 s)

| Tramo | Tiempo | Quién avanza | Cambio frente al plan |
|---|---|---|---|
| Caminata (con zócalo) | 3–4 s | Automático | −1 s |
| Escena con chiste | 10–12 s | Automático hasta el remate; **después, manual** | Espera la risa |
| Pregunta | 8–10 s | Manual (la sala grita) | Pista de Fran a los 20 s; revelación sola a los 30 s |
| «¿Última respuesta?» + REDOBLE | 3 s | Automático | **Es el beat más fuerte del formato:** pausa antes del remate de mayor sorpresa |
| Revelación + remate | 4 s | Manual | Acierto y error tienen cada uno su chiste |
| Tarjeta | 5 s | Manual | Dato limpio, sin chiste |

**Arreglo de una inconsistencia del plan:** el latido decía "pregunta hasta 12 s" pero las ayudas llegaban a los 20 y a los 30 s. Quedan así: 12 s de objetivo, pista a los 20 s, revelación automática a los 30 s como red de seguridad.

## 5. Presupuesto de tiempo y corte a 5 minutos

La descripción del proyecto dice "no más de 5 minutos" y el plan dice "máximo 7". **Hay que decidir cuál vale.** Las tres versiones están armadas para ~6:15–6:30 de reloj puro; en sala, con gritos y risas, sumar 30–60 s.

**Receta para bajar a ≤ 5 minutos (cualquier versión):**
1. Fusionar las escenas 1 y 2 (Papelón + cochera) en una sola pregunta. Ahorra ~35 s.
2. Fusionar las escenas 5 y 6 (mudanza + tour) en una sola pregunta. Ahorra ~35 s.
3. Tarjetas de 3 s, con la lista completa de las 13 noticias en los créditos. Ahorra ~15 s.
4. Sacar una transición de ascensor. Ahorra ~8 s.
Resultado: 6 preguntas en lugar de 8 y unos 5:10 de reloj. La escalera queda de 6 pisos y el «8½» pasa a ser «6½» (o el display salta del 6 al 8½: un chiste más).

## 6. Glosario de técnicas (y cómo se animan en 16×24 px)

| Técnica | Qué es | Cómo se hace en sprite | Ejemplo en el juego |
|---|---|---|---|
| Anticipación | Un movimiento chico que avisa el grande | 1–2 cuadros hacia el lado contrario | El dragón inhala antes de soplar |
| Doble take | Mirar, seguir, volver a mirar con sorpresa | Mirada normal, 4 cuadros, giro rápido y ojos agrandados | Cami ve la hoja que se mueve |
| Slow burn | Una reacción que crece despacio | Hold largo y un píxel de ceja por segundo | Cami con el «99 %» |
| Hold | Congelar para que el golpe se registre | Repetir el cuadro 0,5–1 s | La columna intacta después del choque |
| Smash cut | Corte seco a lo contrario de lo dicho | Corte sin transición | «¿Qué tan difícil puede ser?» y aparece el Papelón |
| Regla de tres | Dos iguales y una variación | La tercera vez cambia el resultado | El dragón falla, falla, acierta |
| Callback | Volver a un chiste anterior | Mismo sprite u objeto, contexto nuevo | La barba en los créditos |
| Escalada | Cada repetición, más grande | Duplicar velocidad, tamaño o cantidad | Sellos 1-2-4-16 |
| Understatement | Algo enorme que nadie comenta | Ningún diálogo | La pelota que crece |
| Literalismo | Lo mecánico encima de lo vivo (Bergson) | Movimientos rígidos, texto robótico | Fran 1.0, Valen procesando |
| Reversal | El resultado opuesto al esperado | Setup clásico, remate invertido | La pregunta obvia con suspenso máximo |
| Button | Un remate chiquito después del remate | 1 cuadro o un cartelito | «Yo estaba primero.» |
| Squash and stretch | Deformar para vender el impacto | Aplastar 1–2 px en el golpe, estirar en el salto | El Suzuki contra la columna |
| Iris | Cierre circular de cine viejo | Máscara circular de 6–8 cuadros | Fin de acto en la versión B |

## 7. Guion de mano para quien maneja

1. **Antes de empezar:** modo demo en pantalla («INSERTE MATE PARA CONTINUAR»). Explicar en una frase: «Ustedes contestan a los gritos; yo aprieto.»
2. **Después de cada remate, esperar.** Si la sala se ríe, se avanza cuando la risa baja. Si nadie se ríe, se avanza enseguida, sin explicar nada (`investigacion-humor/09`).
3. **En REDOBLE,** golpear la mesa primero: la sala copia.
4. **Elegir la respuesta que más se grita**, aunque sea la absurda: el error tiene su propio chiste.
5. **Si el reloj aprieta:** el botón de saltar escena está siempre visible y no pregunta nada.

## 8. Curva de energía del show

```
risa
 ▲            ▲pico 2 (8½)               ▲pico 3 (velitas)
 │ ▲pico 1    │                          │
 │ │(choque)  │        ▲respiro          │      ▲(créditos)
 │ │   ▲ ▲ ▲  │  ▲     │(mesa redonda)   │      │
 └─┴───┴─┴─┴──┴──┴─────┴─────────────────┴──────┴──► tiempo
   intro  acto 1      acto 2      acto 3       final
```

- **Abrir fuerte:** un gag físico en los primeros 20 s (el choque de Lu).
- **Acto 1:** golpes seguidos y cortos; la sala aprende las reglas (REDOBLE, ascensor que sube igual).
- **Acto 2:** el pico del 8½.
- **Acto 3:** un respiro (la mesa redonda, más tranquila) antes del último pico (las velitas y SOPLEN).
- **Final:** emotivo y con créditos graciosos. Terminar con risa, no con datos.

## 9. Checklist de cada chiste (antes de que entre al guion)

- [ ] ¿El blanco es un objeto, un sistema, el juego o alguien que eligió reírse de sí mismo?
- [ ] ¿Toca cuerpo, género, origen, salud o vida privada? Si toca, afuera.
- [ ] ¿Se entiende sin audio?
- [ ] ¿Se entiende si lo ve alguien que no conoce el chiste interno? Si no, ¿lo conoce toda la sala?
- [ ] ¿El setup se ve antes del golpe?
- [ ] ¿El remate está en su propio cuadro, y entran los textos en el tiempo?
- [ ] ¿Hay un hueco después para la risa?
- [ ] Si falla, ¿le cuesta algo a alguien? Si sí, usar la versión amable.
- [ ] ¿La persona que aparece lo aprobó?

## 10. Cuatro pruebas antes de la reunión

1. **Prueba muda:** proyectar sin audio y pedirle a alguien que cuente qué pasó en cada gag. Si no lo puede contar, el gag falla.
2. **Prueba de referencia:** dos o tres personas explican cada chiste interno en una frase. Si no coinciden, se reescribe.
3. **Prueba de proyector:** escala entera (×4 o ×6) y lectura desde la última fila.
4. **Piloto con 2–3 personas:** cronometrar el total y comparar un beat de 0,5 s con uno de 1,5 s. Anotar dónde se ríen y dónde no.

## 11. Ficha de OK por persona

Una por cada persona que aparece. Se le muestra su escena terminada, no el guion.

```
Nombre: ________   Escena(s): ________
Gags donde aparecés: ________
1. ¿Te hace reír a vos o te expone?        [ me hace reír ] [ me expone ]
2. ¿Hay algo que cambiarías?               ________
3. ¿Preferís la opción alternativa?        [ sí ] [ no ]   (cuál: ____)
OK final: [ sí ]  Fecha: ____
```

Prioridad: **Valentino** (gag de robot), **Lu** (choque), **Andrea** (elegir su gag), **Nacho** (pelota y rol), **Cami** (protagonista y dragón).

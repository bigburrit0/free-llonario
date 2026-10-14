# Elenco y arte — Free-llonario

Actualizado 11/10/2026. Todos aceptaron aparecer como personajes.

| Personaje | Nombre real | Rasgos (según fotos) | Gag / rol |
| --- | --- | --- | --- |
| Cami (protagonista) | Camila Arrarte | Bob oscuro con flequillo de lado, anteojos grandes carey, remera negra, cardigan tejido claro, cinturón marrón | Fan de los dragones: la acompaña un dragoncito verde que escupe fuego |
| Valentino ("Valen") | Valentino Franchini | Varón joven, pelo castaño corto con flequillo, camisa blanca | Es un robot (con su pelo castaño encima como chiste) |
| Lu | Lucía Licio | Rubia, pelo largo lacio, ojos verdes | Llega en su Suzuki rojo, choca una columna: "¿Quién dejó esa columna ahí?" |
| Andrea ("Andre") | Andrea Cuervo | Pelo negro largo, blazer negro, camisa blanca, aros de madera | — (a definir) |
| Nacho | Ignacio | Sin foto todavía (sprite genérico: pelo castaño, ropa de tenis) | Siempre lleva una pelota de tenis "oversized" |

## Mockup de arte (enviado, sin feedback todavía)
Las imágenes no se pueden guardar en el proyecto (solo texto); se regeneran con el código de `mockup/`. Nombres entregados al usuario: `1-exterior-choque-de-Lu.png`, `2-estudio-millonario.png`, `3-elenco-y-props.png`.
- Resolución base 320×180, exportado ×4. Sprites 16×24, contorno selectivo color oscuro (no negro).
- Torre 1 cuadrada naranja (izquierda), Torre 2 cilíndrica azul (derecha), pórtico con columnas en el medio.
- Tipografía: bitmap 5×7 propia en mayúsculas con tildes (`mockup/font.py`); no se pudo descargar Press Start 2P desde la nube.

## Cómo regenerar el mockup
Copiar `mockup/*.py` a una carpeta y correr: `python3 scene.py && python3 studio.py && python3 cast.py` (requiere Pillow). Genera `s1x4.png`, `s2x4.png`, `s3x4.png`.
- `sprites.py`: personajes como mapas ASCII + paleta `PAL`, función `blit`.
- `scene.py`: torres, auto, pelota, caja de diálogo, escena exterior.
- `studio.py`: pantalla de pregunta. `cast.py`: hoja de elenco.

# 90 · Plantilla para corregir una pieza

> **Para vos:** cuando algo no te gusta, pedí **un solo cambio por vez** y decí qué tiene que quedar igual. Completá lo que está entre `< >` y pegalo. Ejemplos de cambios: "el pelo de Cami más corto, a la altura de la mandíbula", "en el cuadro 3 de caminar, el brazo izquierdo está al revés", "la torre redonda se ve gris: tiene que ser azul".

---- COPIAR DESDE ACÁ ----

Seguí AGENTS.md. Corrección de una pieza.

- Pieza: `<nombre de la pieza, por ejemplo cam_caminar>`
- Cuadro: `<número de cuadro, o "todos">`
- Cambiá solo esto: `<qué cambiar, en una frase>`
- Dejá igual todo lo demás: colores, tamaño, proporciones, posición de los pies y el resto de los cuadros.

Cómo:
1. Si el cambio es chico (unos pocos píxeles, un color, un brazo), hacelo editando el mapa en `mapas/` y `txt2png.py`. No generes imágenes.
2. Si el cambio es grande (otra pose, otro diseño), cargá la pieza actual con `view_image` como "edit target" y la ficha del personaje como "identity reference", y pedí el cambio a la herramienta integrada con la frase: "Change only <X>; keep everything else exactly the same." Guardá el crudo con un número nuevo y volvé a pixelar con los mismos parámetros que la primera vez (están en el manifiesto o en `INFORME.md`).
3. La versión anterior va a `historial/` antes de pisar.
4. `validar.py <pieza>` y `hoja.py <pieza>`.

Mostrame el antes y el después a ×6, lado a lado, en `vistas/correccion_<pieza>.png`.

---- HASTA ACÁ ----

**Si la corrección falla dos veces seguidas,** pará y avisame (a Claude) con las dos imágenes.

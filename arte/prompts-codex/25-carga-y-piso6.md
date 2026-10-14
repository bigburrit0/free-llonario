# 25 · Zona de carga y hall del piso 6

> **Para vos:** el acto 2 (Comercial, mediodía, azul). En la zona de carga llega el camión verde y amarillo con las cajas de las dos empresas brasileras. En el piso 6 pasa la fila de los 25 empresarios y todos intentan entrar al ascensor. El piso 6 reusa el hall del prompt 24 con otra paleta y otros adornos, para no generar de más.
>
> **Antes:** style frame aprobado y prompt 24 hecho.

---- COPIAR DESDE ACÁ ----

Seguí AGENTS.md, sección "Proceso de escenario".

**Escenario 1: `esc-carga`**

"""
Street-level loading area beside a modern office tower at bright midday, blue accents (this area's color theme is blue). Left: the side of the tower with a wide closed roll-up loading door and a small loading dock platform. Right: open sidewalk and a strip of street where a truck can back in. A few bollards, a potted plant, clear blue midday light. The street area on the right must be clear.
"""
Colores: `e f g h 1 2 3 4 i j k s W`. Anotá `camion=x` (dónde frena el camión) y `piso=<y>`.

**Escenario 2: `esc-piso6`** (sin generar imagen nueva)

- Por código, a partir de `esc-hall_fondo`: cambiá los acentos al azul de Comercial (los `c`/`d` que haya pasan a `g`/`h`) y agregá a la izquierda una ventana grande con cielo de mediodía (`h`, `g`) y la Torre 2 recortada a lo lejos (tomada de `esc-ext_torres`, reducida a la mitad con vecino más cercano).
- Mantené el `hueco=` y el `display=` del hall en el manifiesto.

Vistas previas:
- `vistas/escenas/carga_x4.png`: con `ob-camion_base` (si existe) frenado en `camion=x`, `val_base` y `cam_base`.
- `vistas/escenas/piso6_x4.png`: con las dos hojas de la puerta cerradas, `age_bandera` y tres `ext_empresario-*` (si existen).

Terminaste cuando:
- `validar.py esc-carga_fondo esc-piso6_fondo` da OK.
- Existen las dos vistas previas.

Informe según AGENTS.md.

---- HASTA ACÁ ----

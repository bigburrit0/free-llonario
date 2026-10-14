# Herramientas de guion-humor

- `check.py`: verifica que diálogos, opciones, preguntas, tarjetas e intertítulos entren en pantalla (tipografía 5×7 de `mockup/font.py`). Correr desde la carpeta que contiene `guion-humor/`: `python3 guion-humor/herramientas/check.py`.
- PDF para iPhone (requiere pandoc y wkhtmltopdf), desde `guion-humor/`:
  `pandoc herramientas/portada.md 00-propuesta.md 02-*.md 03-*.md 04-*.md 01-*.md 05-*.md 06-*.md -s --metadata pagetitle=Free-llonario -c herramientas/estilo.css -o propuesta.html && wkhtmltopdf --enable-local-file-access --page-size A5 propuesta.html Free-llonario-propuesta-humor.pdf`

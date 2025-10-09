# Calculadora Gráfica de Cálculo II - Paquete listo

Contenido del paquete:
- `app.py` : aplicación Streamlit principal.
- `requirements.txt`: dependencias Python.
- `README.md` : instrucciones rápidas.

## Ejecutar localmente (prueba rápida)
1. Instala Python 3.10+ y agrega a PATH (si aún no lo tienes).
2. Abre una terminal en la carpeta donde descomprimiste este paquete.
3. Crea un entorno virtual (opcional pero recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\\Scripts\\activate    # Windows (PowerShell o cmd)
   ```
4. Instala dependencias:
   ```bash
   pip install -r requirements.txt
   ```
5. Ejecuta la app:
   ```bash
   streamlit run app.py
   ```
6. Se abrirá en tu navegador en `http://localhost:8501`

## Subir a Streamlit Cloud (para entregar)
1. Crea una cuenta en https://github.com y sube `app.py` y `requirements.txt` a un nuevo repositorio.
2. Ve a https://share.streamlit.io/ (Streamlit Cloud), conecta tu GitHub y despliega un nuevo app señalando tu repo y el archivo `app.py`.
3. Streamlit Cloud instalará las dependencias automaticamente usando `requirements.txt` y te dará un enlace público (ese enlace es el que debes entregar).

## Notas y consejos
- Usa sintaxis compatible con SymPy: potencias con `**`, funciones `sin(x)`, `cos(x)`, `exp(x)`, etc.
- Si la función contiene divisiones (por ejemplo `1/(x-1)`), evita límites que provoquen división por cero.
- Para la exposición: prepara 2-3 ejemplos (derivada, área definida y volumen) y comparte tu link de Streamlit Cloud.

---
¡Listo! Si quieres, puedo subir este repositorio a un GitHub si me das acceso (o guiarte paso a paso para crear el repo y subir los archivos).
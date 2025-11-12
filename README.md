         Guia de ejecucion
Este proyecto fue creado con Python 3.13. Se recomienda usar la misma versión para evitar problemas de compatibilidad.
Primero ingresa a PowerShell y realiza lo siguiente:

Crear entorno virtual
py -m venv .venv

Permitir scripts temporalmente
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

Activar entorno virtual
.\.venv\Scripts\Activate.ps1

Instalar dependencias
pip install -r requirements.txt

Ejecutar proyecto
python Main.py



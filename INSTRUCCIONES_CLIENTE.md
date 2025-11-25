Cliente Python — Instrucciones rápidas

Requisitos
- Python 3.8+
- Dependencias listadas en `requirements.txt` (incluye `requests`).

Instalación
1. Crear y activar virtualenv:
   ```bash
   python -m venv venv
   venv\\Scripts\\activate
   ```
2. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

Uso del cliente
1. Editar `cliente_python.py` y ajustar `BASE_URL`, `USERNAME` y `PASSWORD` según tu entorno.
2. Ejecutar:
   ```bash
   python cliente_python.py
   ```

Notas
- El script muestra cómo obtener el token JWT y listar contactos.
- Para crear un contacto, descomenta la sección marcada en `cliente_python.py`.

Entrega
- `cliente_python.py` (código fuente).
- `INSTRUCCIONES_CLIENTE.md` (estas instrucciones).
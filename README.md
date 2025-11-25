# Contactos — Resumen

Descripción
- Aplicación Django para gestionar contactos (CRUD) con API REST y autenticación JWT.

Instalación y ejecución (resumen)
1. Clonar el repositorio.
2. Crear y activar virtualenv: `python -m venv venv` → `venv\\Scripts\\activate` (Windows).
3. `pip install -r requirements.txt`.
4. `python manage.py migrate`.
5. `python manage.py createsuperuser` (opcional).
6. `python manage.py runserver`.

Rutas principales de la API
- `POST /api/token/` — obtener tokens (access y refresh).
- `POST /api/token/refresh/` — refrescar access token.
- `GET/POST /api/contactos/` — listar y crear contactos.
- `GET/PUT/PATCH/DELETE /api/contactos/{id}/` — operaciones sobre contacto.
- `GET/POST /api/users/` — usuarios (API protegida).
- `GET/POST /api/groups/` — grupos (API protegida).

Autenticación (ejemplo)
- Request:
```
POST /api/token/
{ "username": "admin", "password": "pass" }
```
- Respuesta:
```
{ "refresh": "...", "access": "..." }
```
- Usar header: `Authorization: Bearer <access>`

Despliegue en la nube
- URL pública: N/A (no hay despliegue configurado).
- Opciones recomendadas: Render, Heroku, Railway. Configurar `DEBUG=False` y variables de entorno.
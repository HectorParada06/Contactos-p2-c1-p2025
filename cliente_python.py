import requests
import json

# --- Configuración ---
BASE_URL = 'http://127.0.0.1:8000'
USERNAME = 'Hadmin'
PASSWORD = 'admin'  

# --- Endpoints ---
TOKEN_URL = f"{BASE_URL}/api/token/"
CONTACTOS_URL = f"{BASE_URL}/api/contactos/"


def obtener_tokens(username, password):
    payload = {"username": username, "password": password}
    r = requests.post(TOKEN_URL, json=payload)
    r.raise_for_status()
    return r.json()  # {'access': '...', 'refresh': '...'}


def listar_contactos(access_token):
    headers = {"Authorization": f"Bearer {access_token}"}
    r = requests.get(CONTACTOS_URL, headers=headers)
    r.raise_for_status()
    return r.json()


def crear_contacto(access_token, nombre, telefono, correo, direccion):
    headers = {"Authorization": f"Bearer {access_token}", "Content-Type": "application/json"}
    payload = {
        "nombre": nombre,
        "telefono": telefono,
        "correo": correo,
        "direccion": direccion
    }
    r = requests.post(CONTACTOS_URL, headers=headers, json=payload)
    r.raise_for_status()
    return r.json()


def main():
    print('Obteniendo tokens...')
    tokens = obtener_tokens(USERNAME, PASSWORD)
    access = tokens.get('access')
    print('Access token obtenido.')

    print('\nListando contactos:')
    data = listar_contactos(access)
    print(json.dumps(data, indent=2, ensure_ascii=False))

    # Ejemplo de creación (descomentar para usar)
    # print('\nCreando contacto de prueba...')
    # nuevo = crear_contacto(access, 'Cliente Demo', '+34123456789', 'demo@example.com', 'Calle Demo 1')
    # print(json.dumps(nuevo, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    main()

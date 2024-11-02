import requests
from bs4 import BeautifulSoup
def iniciar_sesion():
    while(1):
        # URL de inicio de sesión
        login_url = "https://dmoj.uclv.edu.cu/accounts/login/?next="

        # Crear una sesión
        session = requests.Session()

        # Cabeceras comunes para simular un navegador
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Referer": login_url  # Agregar Referer como encabezado adicional
        }

        # Realizar una solicitud GET inicial para obtener el token CSRF y cookies
        login_page = session.get(login_url, headers=headers)
        soup = BeautifulSoup(login_page.text, 'html.parser')

        # Extraer el token CSRF
        csrf_token = soup.find("input", {"name": "csrfmiddlewaretoken"})["value"]

        # Configurar el payload con el token CSRF y credenciales
        
        payload = {
            "username": input("Inserte el usuario: "),
            "password": input("Inserte la contrasenna: "),
            "csrfmiddlewaretoken": csrf_token
        }

        # Realizar el inicio de sesión con el token y las credenciales
        login_response = session.post(login_url, data=payload, headers=headers, cookies=session.cookies)

        # Verificar si el inicio de sesión fue exitoso
        if login_response.ok and "Log out" in login_response.text:
            print("Inicio de sesión exitoso")
            return session
        else:
            print("Error en el inicio de sesión:", login_response.status_code)
import requests
from bs4 import BeautifulSoup
from Assets.login import iniciar_sesion
from Assets.Scraping import Problemas_Scraping, Main_Scraping

if __name__ == "__main__":
    # Iniciar sesión
    user_session = iniciar_sesion()
    
    # Verificar si la sesión fue exitosa antes de proceder al scraping
    if user_session:
        problem_list = Problemas_Scraping(user_session)
        Main_Scraping(user_session, problem_list)
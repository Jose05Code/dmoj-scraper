from .login import login
from .Scraping import Problemas_Scraping, Main_Scraping

def full_scraping():
    user_session = login()
    
    if user_session:
        problem_list = Problemas_Scraping(user_session)
        Main_Scraping(user_session, problem_list)
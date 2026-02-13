from bs4 import BeautifulSoup
from unidecode import unidecode  # Importar la biblioteca para quitar tildes
from .file_data import mkdir
from .login import login

# main function
def full_scrapping():
    user_session = login()
    
    if user_session:
        problem_list = scrapping_problems(user_session)
        main_scrapping(user_session, problem_list)

# Función para convertir HTML a Markdown y quitar tildes
def format_description(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    formatted_text = ""

    # Recorrer los elementos y formatear
    for element in soup:
        if element.name == 'h4':
            formatted_text += f"## {element.text}\n\n"  # Títulos de nivel 2 en Markdown
        elif element.name == 'pre':
            formatted_text += f"```\n{element.text}\n```\n"  # Bloques de código en Markdown
        else:
            # Agregar texto normal y limpiar espacios adicionales
            # Eliminar birgulillas y subrayados
            clean_text = element.text.strip().replace("~", "")
            formatted_text += f"{clean_text}\n\n"

    # Quitar tildes y acentos del texto formateado
    return unidecode(formatted_text)

# Obtener una lista con cada URL de problemas resueltos
def scrapping_problems(session):
    print("Recolectando Problemas...")
    flag = 1
    problem_list = []
    pag = 1
    while(flag):

        problems_url = "https://dmoj.uclv.edu.cu/problems/?order=-solved&page="+ str(pag)  # lista de Problemas
        response = session.get(problems_url)

        soup = BeautifulSoup(response.text, 'html.parser')

        for i in range(1, 51):
            check = soup.select_one(f"#problem-table > tbody > tr:nth-child({i}) > td:nth-child(1)")

            if check:
                if check.get('solved') == '1':
                    link = check.find('a')
                    if link:
                        href = link['href']
                    problem_list.append(href)
                else:
                    flag = 0
                    break

        pag = pag + 1

    print(f"Problemas Encontrados : {len(problem_list)}")
    return problem_list

def main_scrapping(session, problem_set):
    for problem_url in problem_set:
        url = f"https://dmoj.uclv.edu.cu/{problem_url}"
        response = session.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        #   Sacar código
        submissions = soup.select_one("#submissions-table")
        sub_result = submissions.select_one('.sub-result.AC')
        if sub_result:
            submission_row = sub_result.find_parent('div', class_='submission-row')
            submission_id = submission_row.get('id')  # Obtenemos el id
            language_element = submission_row.select_one('div.state > span.language').text  # lenguaje
            # scraping del código del problema
            url_solve = f"https://dmoj.uclv.edu.cu/src/{submission_id}/raw"
            response_solve = session.get(url_solve)

            code = response_solve.text  # Código del primer AC
            # print(code)
        else:
            print("No se encontró ningún elemento 'sub-result AC'.")

        #   Sacar Descripción
        problem_parts = problem_url.split('/')
        description_url = f"https://dmoj.uclv.edu.cu/problem/{problem_parts[2]}"
        description_response = session.get(description_url)
        description_soup = BeautifulSoup(description_response.text, 'html.parser')

        tittle = description_soup.select_one("#content > div.problem-title > h2").text
        # Extraer el contenido HTML de la descripción
        description = description_soup.select_one("#content-left > div.content-description.screen > div").decode_contents()

        # Formatear la descripción y quitar tildes
        formatted_description = format_description(description)

        mkdir(tittle, code, formatted_description, language_element)

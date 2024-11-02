import requests
from bs4 import BeautifulSoup
from unidecode import unidecode  # Importar la biblioteca para quitar tildes
from .login import iniciar_sesion
from .fichero_data import crear_carpeta

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
def Problemas_Scraping(session):
    print("Recolectando Problemas...")
    flag = 1
    problem_list = []
    pag = 1
    while(flag):

        problemas_url = "https://dmoj.uclv.edu.cu/problems/?order=-solved&page="+ str(pag)  # lista de Problemas
        response = session.get(problemas_url)

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

def Main_Scraping(session, problemas_url):
    for problema_url in problemas_url:
        url = f"https://dmoj.uclv.edu.cu/{problema_url}"
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
        problema_parts = problema_url.split('/')
        description_url = f"https://dmoj.uclv.edu.cu/problem/{problema_parts[2]}"
        description_response = session.get(description_url)
        description_soup = BeautifulSoup(description_response.text, 'html.parser')

        Titulo = description_soup.select_one("#content > div.problem-title > h2").text
        # Extraer el contenido HTML de la descripción
        Description = description_soup.select_one("#content-left > div.content-description.screen > div").decode_contents()

        # Formatear la descripción y quitar tildes
        formatted_description = format_description(Description)

        crear_carpeta(Titulo, code, formatted_description, language_element)

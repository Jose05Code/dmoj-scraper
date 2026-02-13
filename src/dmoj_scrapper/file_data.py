import os
import re

def clear_string(name):
    # Reemplaza caracteres inválidos en nombres de archivos y carpetas
    return re.sub(r'[<>:"/\\|?*]', '_', name)

def mkdir(tittle, code, problem, language_element):
    # Limpia el título para que sea un nombre de directorio válido
    clean_title = clear_string(tittle)

    # Define the base path for the directories
    base_path = os.path.join(os.path.expanduser("~"), "Documents", "DMOJ.uclv")

    # Dictionary for language file extensions
    language_extensions = {
        "GAS64": ".asm",
        "C": ".c",
        "MONOCS": ".cs",
        "C++03": ".cpp",
        "C++11": ".cpp",
        "C++14": ".cpp",
        "C++17": ".cpp",
        "C++20": ".cpp",
        "JAVA": ".java",
        "JAVA8": ".java",
        "PAS": ".pas",
        "PY2": ".py",
        "PY3": ".py",
        "V8JS": ".js",
    }

    # Get the appropriate file extension for the specified language
    extension = language_extensions.get(language_element, ".txt")
    # Define the full directory path
    full_path = os.path.join(base_path, clean_title)
    file_name = f"solve{extension}"

    if os.path.exists(full_path):
        print(f"La carpeta '{full_path}' ya existe.")
    else:
        try:
            # Create the directory structure
            os.makedirs(full_path)

            # Create README.md with the problem description
            with open(os.path.join(full_path, 'README.md'), 'w') as readme:
                readme.write(str(problem))

            # Create the solution file with the provided code
            with open(os.path.join(full_path, file_name), 'w') as solve_file:
                solve_file.write(str(code))

            print(f"Estructura de carpetas y archivos creada en '{full_path}'.")
        except Exception as e:
            print(f"Error al crear la carpeta: {e}")

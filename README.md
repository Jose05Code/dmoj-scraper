
Este repositorio contiene un script en Python que permite a los usuarios del juez virtual DMOJ realizar scraping de su perfil. Al proporcionar sus credenciales de inicio de sesión, el script accede a la cuenta del usuario y recopila todos los problemas que han sido resueltos (con el estado "AC"). Para cada problema, el script crea una carpeta en el directorio de Documentos que incluye:

- Una carpeta con el nombre del problema.
- Un archivo `README.md` que contiene la descripción del problema.
- Un archivo `solve.extension` que contiene el código de la solución.

Este proyecto es ideal para quienes deseen mantener un registro organizado de sus soluciones a problemas de programación y compartirlas fácilmente en plataformas como GitHub.

### Cómo Usar
1. Clona este repositorio en tu máquina local.
2. Navega al directorio del proyecto e instala las dependencias requeridas ejecutando:
   ```bash
   pip install -r requirements.txt
   ```
3. Ejecuta el script principal usando:
   ```bash
   python main.py
   ```
4. Cuando se te pida, ingresa tu nombre de usuario y contraseña de DMOJ. El script realizará automáticamente el scraping de tu perfil, recopilará todos los problemas resueltos y los organizará en el directorio de Documentos. ¡Solo queda esperar a que el proceso se complete!

# 🔍 DMOJ Profile Scraper

A Python script that allows DMOJ online judge users to scrape their profile and automatically organize their accepted solutions.

## 📋 Description

This repository contains a Python script that enables users of the DMOJ virtual judge to scrape their profile. By providing their login credentials, the script accesses the user's account and collects all problems that have been solved (with "AC" status). For each problem, the script creates a folder in the Documents directory that includes:

- 📁 A folder with the problem's name
- 📄 A `README.md` file containing the problem description
- 💻 A `solve.extension` file containing the solution code

This project is ideal for those who want to maintain an organized record of their programming solutions and easily share them on platforms like GitHub.

## ✨ Features

- 🔐 Secure login to DMOJ platform
- 📊 Automatic collection of all accepted (AC) problems
- 📂 Organized folder structure for each problem
- 🌐 Problem descriptions in Markdown format
- 💾 Solution code with appropriate file extensions
- 🚀 Easy to use command-line interface

## 🔧 Requirements

- Python 3.x
- Dependencies listed in `requirements.txt`:
  - beautifulsoup4
  - requests
  - unidecode

## 🚀 How to Use

1. **Clone this repository** to your local machine:
   ```bash
   git clone https://github.com/Jose05Code/dmoj-scraper.git
   cd dmoj-scraper
   ```

2. **Install the required dependencies** by running:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the main script** using:
   ```bash
   python main.py
   ```

4. **Enter your credentials** when prompted. Input your DMOJ username and password. The script will automatically scrape your profile, collect all solved problems, and organize them in the Documents directory. Just wait for the process to complete!

## 📁 Output Structure

The script creates the following structure in your Documents folder:

```
~/Documents/DMOJ.uclv/
├── Problem_Name_1/
│   ├── README.md
│   └── solve.py
├── Problem_Name_2/
│   ├── README.md
│   └── solve.cpp
└── ...
```

## Installing from pip
**The package is available at PyPI repositories, execute the following command for installing**:
```bash
pip install dmoj-scrapper
```

## Packaging
    
### 1. **Install packing dependencies**
 ```bash 
pip install build
 ```
### 2. **Packing** 
```bash
python -m build # at the root of the project
# It will generate 2 files at ./dist/
```
### 3. Installing package
```bash
pip install ./dist/file.whl
# replace file name with your .whl file generated at ./dist
```

### **Usage**
1. **Execute in terminal**
```bash
dmoj-scrapper -h
# It will show you how to use by cli
```
2. **Import to python file**
```python
from dmoj_scrapper import full_scrapping, login, main_scrapping, scrapping_problems
from requests import Session

full_scrapping()
 # main function, execs the full scrapping process by launching an interactive menu where the
 # user introduces the info

""" These functions are also available: """

 # user's info
my_user = "your_user"
my_password = "my_password"

login(my_user, my_password)
 # attempts a login, 
 # returns a requests.Session object if success
 # args are optional, if not given, it will display an interactive menu for input

session = Session() # assume a valid session from login()
 
problems_list = scrapping_problems(session)
 # receives a valid session and returns a list with every solved problem's url

main_scrapping(session, problems_list)
 # gets the info of every problem, and makes de whole structure

```

## 🤝 Contributing

Contributions are welcome! Feel free to:
- 🐛 Report bugs
- 💡 Suggest new features
- 🔧 Submit pull requests

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
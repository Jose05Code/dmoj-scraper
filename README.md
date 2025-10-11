
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

## 🤝 Contributing

Contributions are welcome! Feel free to:
- 🐛 Report bugs
- 💡 Suggest new features
- 🔧 Submit pull requests

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This tool is intended for personal use to organize your own solutions. Please respect the DMOJ platform's terms of service and use this tool responsibly.
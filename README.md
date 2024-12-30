# event-app
## Description
This is a REST API program developed using Python, Django, and the Django REST Framework for an event management application. It features a customised user model, along with token-based authentication to ensure secure communication. The application supports, sponsors, user login, password recovery, and comprehensive event management, including the active event, activities, and schedules for users. Additionally, it offers the implementation of reports to see how many people registered in the event period.

## Requirements
Here are the recommended versions to use. If you have a different version of Python, feel free to try it. If the program does not work, try using the same version or a similar version.
- Python 3.12.4

## Instalation
### Download
- **Option 1:** Download the code as a ZIP file directly from the repository.
- **Option 2:** Use Git Bash to clone the repository with the following command.
```bash
git clone https://github.com/fancyydev/event-app.git
```

### Virtual enviroment creation
It is recommended to use a virtual environment to avoid conflicts between library versions and to ensure a smooth execution. How to set it up is explained below:

- **Step one:** Navigate to the project folder in your terminal:
```bash
cd .\event-app\
```
- **Step two:** Create a virtual environment using venv, Python's default tool for this purpose:
```bash
python -m venv venv
```
- **Step three:** Activate the virtual environment to install the required libraries and packages:
```bash
.\venv\Scripts\activate
```
Alternatively, navigate manually:
```bash
cd .\venv\
cd .\Scripts\
.\activate
# Go back to the main folder:
cd..
cd..
```
## Package instalation
Once the virtual environment is activated and you are in the main folder, install the required packages by running:
```bash
pip install -r requirements.txt
```

## Running the program
To run and test the API:
- Ensure the virtual environment is active.
- Use the following command (adjust paths as needed for your system):
- Go inside of the folder eventapp
```
cd .\eventapp\
```

As I use powershell I need to use & to be able to send parameters to the script, in this case I use the path to the python interpreter in my virtual environment and then the name of the python program.
```
& "C:\Users\David Fregoso\Desktop\EVENT-APEAJAL\event-app\venv\Scripts\python.exe" .\manage.py runserver
```

## Explanation
### Endpoints

**List of all activities:**

**List of all activities by user:**

**List of all activities by user for active event:**

**Details of the active event:**

**Images of the active event schedule**

**List of sponsors for the active event**

**List of sponsors for the active event**

**List of countries, states and municipalities:**

**PDF report showing the registration count for the active event period:**
**EXCEL report showing the registration count for the active event period**



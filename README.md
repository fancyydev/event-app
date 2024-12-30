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

#### **List of all activities by user for the active event:**
- **Endpoint:** `http://127.0.0.1:8000/api/event/listActiveActivitiesByUser`
- **Method:** `GET`
- **Description:** Retrieves a list of all activities scheduled for the active event that are associated with the authenticated user.
- **Example Request:**
```json
{
	"Authorization": "Token 7042624ee3df404d7a67d95f3c0d177240227e99"
}
```
- **Example Response:**
```json
[
    {
        "id": 1,
        "title_activity": "Justificación de la poda en aguacate",
        "slug": "justificacion-de-la-poda-en-aguacate",
        "description": "BIOESTIMULANDO ANDO",
        "date_time": "28/08/2024, 09:00, 10:00",
        "author": "M. C. Mauricio Navarro Garcia",
        "event": 2,
        "room": "Sala 1",
        "is_selected": false
    },
    {
        "id": 2,
        "title_activity": "Portainjertos Clonales: Presente y futuro en la industria del aguacate",
        "slug": "portainjertos-clonales-presente-y-futuro-en-la-industria-del-aguacate",
        "description": "BROKAW NURSERY",
        "date_time": "28/08/2024, 10:00, 10:30",
        "author": "Ing. Consuelo Fernández Noguera",
        "event": 2,
        "room": "Sala 1",
        "is_selected": false
    },
    ...
]
```
#### **Details of the active event:**
- **Endpoint:** `http://127.0.0.1:8000/api/event/activeEvent`
- **Method:** `GET`
- **Description:** Provides detailed information about the currently active event, including its name, description, duration, and logo.
- **Example Response:**
```json
{
    "id": 2,
    "name_event": "8 Congreso de aguacate Jalisco 2024",
    "description": "Este congreso reúne a expertos, productores, y líderes de la industria para compartir conocimientos, estrategias y avances en la producción, comercialización y sostenibilidad del aguacate. Jalisco, conocido como uno de los principales productores de aguacate en México, es el escenario perfecto para este evento de alto perfil.",
    "initial_date": "2024-08-16",
    "end_date": "2024-12-30",
    "logo_url": "http://127.0.0.1:8000/media/events/logos/logo_congreso.png",
    "is_active": true
}
```

#### **Images of the active event schedule**
- **Endpoint:** `http://127.0.0.1:8000/api/event/activeEventImages`
- **Method:** `GET`
- **Description:** Retrieves a list of images representing the schedule for the active event.
- **Example Response:**
```json
[
    {
        "id": 1,
        "image_url": "http://127.0.0.1:8000/media/event/images/SALA_1.png",
        "event": 2
    },
    {
        "id": 2,
        "image_url": "http://127.0.0.1:8000/media/event/images/SALA_2.jpg",
        "event": 2
    },
    ...
]
```

#### **Schedule of the active event**
- **Endpoint:** `http://127.0.0.1:8000/api/event/activeProgramEvent`
- **Method:** `GET`
- **Description:** Automatically downloads the complete schedule of the active event in PDF format.

#### **List of sponsors for the active event**
- **Endpoint:** `http://127.0.0.1:8000/api/event/activeSponsorsEvent`
- **Method:** `GET`
- **Description:** Returns a list of sponsors for the active event, including their names, links, and logos.
- **Example Response:**
```json
[
    {
        "name": "msc",
        "link": "https://www.msc.com/",
        "logo_url": "http://127.0.0.1:8000/media/sponsors/logos/MSC-1.png",
        "event": 2
    },
    {
        "name": "Gonzamex",
        "link": "https://www.agrogonzamex.com/es",
        "logo_url": "http://127.0.0.1:8000/media/sponsors/logos/AGROGON-1.png",
        "event": 2
    },
    ...
]
```

#### **List of countries, states and municipalities:**
- **Endpoint:** `http://127.0.0.1:8000/api/geo/locationList`
- **Method:** `GET`
- **Description:** Provides a hierarchical list of registered countries, states, and their corresponding municipalities. 
- **Example Response:**
```json
[
    {
        "id": 1,
        "name": "México",
        "states": [
            {
                "id": 1,
                "name": "Jalisco",
                "municipalities": [
                    {
                        "id": 1,
                        "name": "Acatic"
                    },
                    ...
                ]
            },
            ...
        ]
    },
    {
        "id": 2,
        "name": "República de china",
        "states": [
            {
                "id": 8,
                "name": "Shangai",
                "municipalities": [
                    {
                        "id": 639,
                        "name": "Shangai"
                    },
                    ...
                ]
            },
            ...
        ]
    },
]
```

#### **PDF report showing the registration count for the active event period:**
- **Endpoint:** `http://127.0.0.1:8000/api/user/report/<int:event_id>/`
- **Method:** `GET`
- **Description:** Generates a PDF report with the number and data of registered users during the active event period. Accessible only with an administrator token, and the file is downloaded automatically based on the event ID provided.
- **Example Request:**
```json
{
	"Authorization": "Token 7042624ee3df404d7a67d95f3c0d177240227e99"
}
```

#### **EXCEL report showing the registration count for the active event period**
- **Endpoint:** `http://127.0.0.1:8000/api/user/reportExcel/<int:event_id>/`
- **Method:** `GET`
- **Description:**  Generates a EXCEL report with the number and data of registered users during the active event period. Accessible only with an administrator token, and the file is downloaded automatically based on the event ID provided.
- **Example Request:**
```json
{
	"Authorization": "Token 7042624ee3df404d7a67d95f3c0d177240227e99"
}
```

#### **login:**
- **Endpoint:** `http://127.0.0.1:8000/api/user/login`
- **Method:** `POST`
- **Description:** Authenticates a user by validating their credentials and returns their authentication token and account information.
- **Example Request:**
  ```json
  {
    "email": "user@gmail.com",
    "password": "contraseña"
  }
  ```
- **Example Response:**
  ```json
  {
    "token": "7a5a0cdb130701498502385117f3530ef4aa9057",
    "user": {
        "email": "user@gmail.com",
        "name": "user",
        "phone": "3751197174",
        "municipality": "Zapotlán el grande",
        "state": "Jalisco",
        "country": "México",
        "occupation": "Developer",
        "company": "Tech Corp",
        "ticket": 12345,
        "created": "2024-12-29T19:25:59.177314-06:00",
        "is_active": true,
        "is_superuser": false,
        "password": "pbkdf2_sha256$600000$xKQrri1e2LAutUYrRbCRrJ$E2SHIo8rPGuO/LS896bPnG8jo/Mb9XVrDuF53I8aTIM="
    }
  }
  ```
#### **Register:**
- **Endpoint:** `http://127.0.0.1:8000/api/user/register`
- **Method:** `POST`
- **Description:** Registers a new user by creating an account with their provided details.
- **Example Request:**
  ```json
  {
    "email": "user@gmail.com",
    "name": "user",
    "phone": "3751197174",
    "municipality": "Zapotlán el grande",
    "state": "Jalisco",
    "country": "México",
    "occupation": "Developer",
    "company": "Tech Corp",
    "ticket": 12345,
    "password": "contraseña"
  }
  ```
- **Example Response:**
  ```json
  "d777a7691dc6c7416b096d5d0b51e53acf641a16"
  ```

#### **Password recovery:**
- **Endpoint:** `http://127.0.0.1:8000/api/user/passwordRecovery`
- **Method:** `POST`
- **Description:** Sends a password recovery email containing a link for the user to reset their password.
- **Example Request:**
```json
{
    "email": "davidfregosoleon12@gmail.com"
}
```
- **Example Response:**
```json
{
    "detail": "Password reset email has been sent."
}
```

#### **Schedule activities:**
- **Endpoint:** `http://127.0.0.1:8000/api/event/assignUserActivity/<int:id_activity>/`
- **Method:** `POST`
- **Description:** Assigns an activity to the authenticated user based on the activity ID provided.
- **Example Request:**
```json
{
	"Authorization": "Token 7042624ee3df404d7a67d95f3c0d177240227e99"
}
```
- **Example Response:**
```json
{
    "id": 5,
    "user": 17,
    "activity": 1,
    "created_at": "2024-12-30T14:46:33.006898-06:00"
}
```

#### **Remove activities:**
- **Endpoint:** `http://127.0.0.1:8000/api/event/removeUserActivity/<int:id_activity>/`
- **Method:** `DEL`
- **Description:** 
- **Example Request:** Removes an activity from the authenticated user’s schedule based on the activity ID provided.
```json
{
	"Authorization": "Token 7042624ee3df404d7a67d95f3c0d177240227e99"
}
```
- **Example Response:**
```json
{
    "detail": "Activity successfully unscheduled."
}
```


#from django.test import TestCase
from eventapp.wsgi import *
from .models import Country, State, Municipality
import pandas as pd
# # Agregar paises ------------------------------

# excel_file = 'C:\\Users\\David Fregoso\\Desktop\\EVENT-APEAJAL\\event-app\\eventapp\\geodata\\paises.xlsx'
# df = pd.read_excel(excel_file, engine='openpyxl')
        
# # Asumimos que la primera columna contiene los nombres de los países
# paises = df.iloc[:, 0].tolist()  # Obtener todos los valores de la primera columna como una lista
# print (paises)

# #Insertar los datos en la base de datos de prueba
# for pais in paises:
#    pais_formateado = pais.capitalize()
#    Country.objects.create(name=pais_formateado)
   
# # Agregar estados ----------------------------
# excel_file = 'C:\\Users\\David Fregoso\\Desktop\\EVENT-APEAJAL\\event-app\\eventapp\\geodata\\estados.xlsx'
# df = pd.read_excel(excel_file, engine='openpyxl')

# # Asumimos que la primera columna contiene los nombres de los países y la segunda columna los nombres de los estados
# paises_estados_municipios = df.values.tolist()

# for pais, estado in paises_estados_municipios:
#     pais_formateado = pais.capitalize()
#     estado_formateado = estado.capitalize()

#     # Crear o obtener el país
#     country, created = Country.objects.get_or_create(name=pais_formateado)
    
#     # Crear el estado asociado al país
#     State.objects.create(name=estado_formateado, country=country)

# # Agregar municipios ----------------------------
# Cargar el archivo Excel que contiene países, estados y municipios
excel_file = 'C:\\Users\\David Fregoso\\Desktop\\EVENT-APEAJAL\\event-app\\eventapp\\geodata\\municipios.xlsx'
df = pd.read_excel(excel_file, engine='openpyxl')

# Leer los datos del archivo Excel
paises_estados_municipios = df.values.tolist()

for pais, estado, municipio in paises_estados_municipios:
    pais_formateado = pais.capitalize()
    estado_formateado = estado.capitalize()
    municipio_formateado = municipio.capitalize()

    # Crear o obtener el país
    country, created = Country.objects.get_or_create(name=pais_formateado)
    
    # Crear o obtener el estado asociado al país
    state, created = State.objects.get_or_create(name=estado_formateado, country=country)
    
    # Crear el municipio asociado al estado
    Municipality.objects.create(name=municipio_formateado, state=state)

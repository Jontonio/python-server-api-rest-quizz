from flask import Flask
import pandas as pd
from flask import Flask
from urllib.error import HTTPError
from my_class.HttpResponse import HttpResponse
response = HttpResponse()

app = Flask(__name__)

@app.route("/")
def main_route():
    try:
        return response.res_success("WELCOME TO SERVER  - SOFTWARE X", 200, None)
    except HTTPError as e:
        return response.res_error("Ocurrio un error", 500, None)

@app.route("/grados-seccion")
def grade_section():
    try:
        ruta = 'files/encuesta.xlsx'
        df = pd.read_excel(ruta)
        df.columns = df.columns.str.strip().str.lower()
        df_group = df.groupby(['grado','sección']) 

        result_dict = df_group.size().reset_index(name='count').to_dict(orient='records')

        return response.res_success("Número de estudiantes por grado y sección", 200, result_dict)
    except HTTPError as e:
        return response.res_error("Ocurrio un error", 500, None)

if __name__ == "__main__":
    app.run()
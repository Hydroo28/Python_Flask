from flask import Flask

app = Flask(__name__)

@app.route("/")

def hola():
    lista = [
        "hola",
        "adios",
        "buenos dias",
        "buenas noches"
    ]

    for i in lista:
        return "<br>".join(lista) # esto es para recorrer una lista 
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/Ejercicio1")

def ejercicio1():
    

    kwargs = {
        "nombre": "Zapatillas",
        "descripcion": "Zapatillas de goma para ir a la feria"
    }
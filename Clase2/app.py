from flask import Flask, render_template


app = Flask(__name__)



class Pelicula:
    def __init__(self, nombre, año, protagonista):
        self.nombre = nombre
        self.año= año
        self.protagonista= protagonista





volver = Pelicula("Regreso al futuro", 1985, "Michael.J.Fox")

@app.route("/")

def estructura_datos():
    peliculas = [
        "pelicula1",
        "pelicula2",
        "pelicula3",
        "pelicula4"
    ]

    lobo= {
        "nombre" : "El lobo de wall street",
        "año" : 2013,
        "protagonista" : "Leonardo DiCaprio"
    }
    return render_template("estructura.html", movies=peliculas, destacada=lobo, favorita=volver)
   
   
   
    # for i in peliculas:
    #     return "<br>".join(peliculas) # esto es para recorrer una lista 
    

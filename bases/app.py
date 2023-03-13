from flask import Flask
app = Flask(__name__)

@app.route("/") # Primer endPoint
def hello_world():
    return "<p>Hola mundo</p>"

@app.route("/saludar/<nombre>")
def hello(nombre):
    return f"<h1>Hola te saludo {nombre}</h1>"
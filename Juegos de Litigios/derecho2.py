from flask import Flask

print("Iniciando la aplicación...")

app = Flask(__name__)

@app.route('/')
def hello():
    return "¡Hola, mundo!"

@app.route('/test')
def test():
    return "¡La aplicación está funcionando!"

print("Flask está listo para recibir solicitudes.")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

from flask import Flask

app = Flask(__name__)

@app.route('/')
def inicio():
    return """
    <h1>Hola Mundo</h1>
    <p>Mi primera app</p>
    """

if __name__ == '__main__':
    app.run(debug=True)
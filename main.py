from flask import Flask

app = Flask(__name__)

@app.route('/')
def inicio():
    return """
    <!DOCTYPE html>
    <html>

    <head>

        <title>Calculadora</title>

        <style>

            body{
                background:#0f172a;
                display:flex;
                justify-content:center;
                align-items:center;
                height:100vh;
                font-family:Arial;
            }

            .calculadora{
                background:#1e293b;
                padding:20px;
                border-radius:20px;
                width:320px;
                box-shadow:0px 0px 20px black;
            }

            #pantalla{
                width:100%;
                height:70px;
                font-size:30px;
                margin-bottom:15px;
                text-align:right;
                border:none;
                border-radius:10px;
                padding-right:10px;
                background:#e2e8f0;
            }

            .botones{
                display:grid;
                grid-template-columns:repeat(4,1fr);
                gap:10px;
            }

            button{
                height:60px;
                font-size:22px;
                border:none;
                border-radius:10px;
                cursor:pointer;
                background:#334155;
                color:white;
            }

            button:hover{
                background:#475569;
            }

            .igual{
                background:#22c55e;
            }

            .igual:hover{
                background:#16a34a;
            }

            .operador{
                background:#3b82f6;
            }

            .operador:hover{
                background:#2563eb;
            }

        </style>

    </head>

    <body>

        <div class="calculadora">

            <input type="text" id="pantalla" disabled>

            <div class="botones">

                <button onclick="agregar('7')">7</button>
                <button onclick="agregar('8')">8</button>
                <button onclick="agregar('9')">9</button>
                <button class="operador" onclick="agregar('/')">÷</button>

                <button onclick="agregar('4')">4</button>
                <button onclick="agregar('5')">5</button>
                <button onclick="agregar('6')">6</button>
                <button class="operador" onclick="agregar('*')">×</button>

                <button onclick="agregar('1')">1</button>
                <button onclick="agregar('2')">2</button>
                <button onclick="agregar('3')">3</button>
                <button class="operador" onclick="agregar('-')">−</button>

                <button onclick="agregar('0')">0</button>
                <button onclick="agregar('.')">.</button>
                <button onclick="borrar()">C</button>
                <button class="operador" onclick="agregar('+')">+</button>

                <button class="igual"
                style="grid-column:span 4;"
                onclick="calcular()">
                    =
                </button>

            </div>

        </div>

        <script>

            let pantalla =
            document.getElementById("pantalla")

            function agregar(valor){
                pantalla.value += valor
            }

            function borrar(){
                pantalla.value = ""
            }

            function calcular(){

                try{
                    pantalla.value =
                    eval(pantalla.value)
                }

                catch{
                    pantalla.value = "Error"
                }

            }

        </script>

    </body>

    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)
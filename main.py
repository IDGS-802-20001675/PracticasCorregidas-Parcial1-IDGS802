from flask import Flask,render_template,request,jsonify
from forms import ResistanceForm


app = Flask(__name__)
color_css_mapping = {
    'Negro': 'negro',
    'Cafe': 'cafe',
    'Rojo': 'rojo',
    'Naranja': 'naranja',
    'Amarillo': 'amarillo',
    'Verde': 'verde',
    'Azul': 'azul',
    'Violeta': 'violeta',
    'Gris': 'gris',
    'Blanco': 'blanco'
}

#Practica 1 Numeros es clase aparte
#Practica 2 Pirámide es clase aparte

#Práctica 3 Operaciones básicas
@app.route("/", methods=["GET", "POST"])
def operaciones():
    if request.method == "POST":
        num1 = int(request.form.get("n1"))
        num2 = int(request.form.get("n2"))
        operacion = request.form.get("operation")

        if operacion == "suma":
            resultado = num1 + num2
        elif operacion == "resta":
            resultado = num1 - num2
        elif operacion == "multiplica":
            resultado = num1 * num2
        elif operacion == "divide":
            resultado = num1 / num2
        else:
            return "Operación no válida"

        return f"<h1>El resultado es: {resultado}</h1>"
    else:
        return render_template("formulario1.html")
    

#Practica 4 Distancias
@app.route("/distancias", methods=["GET", "POST"])
def calcular_distancia():
    if request.method == "POST":
        x1 = float(request.form.get("x1"))
        y1 = float(request.form.get("y1"))
        x2 = float(request.form.get("x2"))
        y2 = float(request.form.get("y2"))

        # Fórmula de distancia entre dos puntos en un plano cartesiano
        distancia = ((x2 - x1)**2 + (y2 - y1)**2)**0.5

        return "<h1>La distancia entre los puntos es: {}</h1>".format(distancia)
    else:
        return render_template("formulario.html")
    
#Practica 5 Resistencias
@app.route("/resistencias",methods=["GET","POST"])
def res():
    operadores = {
        0: 1,
        1: 10,
        2: 100,
        3: 1000,
        4: 10000,
        5: 100000,
        6: 1000000,
        7: 10000000,
        8: 100000000,
        9: 1000000000
    }
    colores = {
        0: 'Negro',
        1: 'Cafe',
        2: 'Rojo',
        3: 'Naranja',
        4: 'Amarillo',
        5: 'Verde', 
        6: 'Azul',
        7: 'Violeta',
        8: 'Gris',
        9: 'Blanco',
    }
    
    color1_nombre = ""
    color2_nombre = ""
    color3_nombre = ""
    tolerancia = 0
    resistencia = 0
    resistenciaMin = 0
    resistenciaMax = 0
    porcentaje_tolerancia = 0.0
    resistencia_form = ResistanceForm(request.form) 
    
    if request.method == 'POST':
        color1 = int(resistencia_form.color1.data)
        color2 = int(resistencia_form.color2.data)
        color3 = int(resistencia_form.color3.data)
        tolerancia = int(resistencia_form.tolerancia.data)
        
        color1_nombre = colores[color1]
        color2_nombre = colores[color2]
        color3_nombre = colores[color3]
        
        concat = str(color1) + str(color2)
        resistencia = int(concat) * operadores.get(color3, 1)
        porcentaje_tolerancia = resistencia * (tolerancia / 100)
        resistenciaMin = resistencia - porcentaje_tolerancia
        resistenciaMax = resistencia + porcentaje_tolerancia

    return render_template("resistencias.html", form=resistencia_form, color1=color1_nombre, color2=color2_nombre, color3=color3_nombre, tolerancia=tolerancia, resistencia=resistencia ,resistenciaMin=resistenciaMin, resistenciaMax=resistenciaMax, color_css_mapping=color_css_mapping)


if __name__ == "__main__":
    app.run(debug=True)

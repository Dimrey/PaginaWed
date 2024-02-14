from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    plunger = float(request.form['plunger'])
    stroke = float(request.form['stroke'])
    velocity = float(request.form['velocity'])
    efficiency = float(request.form['efficiency'])
    unit_system = request.form['unit_system'].lower()

    constant_ingles = 0.1166
    displacement_efficiency_ingles = constant_ingles * velocity * (plunger**2) * stroke * efficiency
    displacement_100_efficiency_ingles = constant_ingles * velocity * (plunger**2) * stroke * 1.0  # Assume 100% efficiency

    displacement_efficiency_metrico = displacement_efficiency_ingles * 0.159
    displacement_100_efficiency_metrico =  displacement_100_efficiency_ingles * 0.159  # Assume 100% efficiency

    datos = {"Plunger": plunger, "Stroke": stroke, "SPM": velocity, "Eficiency": efficiency}

    if unit_system == "metrico":
        result = {
            "displacement_efficiency": f"{displacement_efficiency_metrico:.2f} m^3/day",
            "displacement_100_efficiency": f"{displacement_100_efficiency_metrico:.2f} m^3/day"
        }
    elif unit_system == "sistema ingles":
        result = {
            "displacement_efficiency": f"{displacement_efficiency_ingles:.2f} BPD",
            "displacement_100_efficiency": f"{displacement_100_efficiency_ingles:.2f} BPD"
        }
    else:
        result = {"error": "Invalid unit system. Please choose Metrico or Sistema Ingles."}

    return render_template('result.html', datos=datos, result=result)

@app.route('/redirect', methods=['GET'])
def redirect_to_index():
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)

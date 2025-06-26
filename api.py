from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/analizar-numeros', methods=['POST'])
def analizar_numeros():
    data = request.get_json()

    # Validar entrada
    if not data or 'numeros' not in data:
        return jsonify({"error": "Debes enviar una lista de números en 'numeros'"}), 400

    numeros = data['numeros']

    # Validar que sea una lista de números
    if not isinstance(numeros, list) or not all(isinstance(n, (int, float)) for n in numeros):
        return jsonify({"error": "La lista debe contener solo números"}), 400

    # Procesamiento
    mayor = max(numeros)
    promedio = sum(numeros) / len(numeros)

    resultado = {
        "numeros": numeros,
        "mayor": mayor,
        "promedio": promedio
    }

    return jsonify(resultado), 200

if __name__ == '__main__':
    app.run(debug=True, port=8000)

### python api.py

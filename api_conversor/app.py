from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/convertir-temperatura', methods=['POST'])
def convertir_temperatura():
    """
    Endpoint que recibe un valor de temperatura y su escala de origen,
    aplica la fórmula de conversión correspondiente y devuelve el resultado.

    Ejemplo de entrada (Celsius a Fahrenheit):
    {
        "valor": 100,
        "escala": "C"
    }

    Ejemplo de salida:
    {
        "valor_original": 100,
        "escala_origen": "Celsius",
        "valor_convertido": 212.0,
        "escala_destino": "Fahrenheit"
    }

    Ejemplo de entrada (Fahrenheit a Celsius):
    {
        "valor": 212,
        "escala": "F"
    }

    Ejemplo de salida:
    {
        "valor_original": 212,
        "escala_origen": "Fahrenheit",
        "valor_convertido": 100.0,
        "escala_destino": "Celsius"
    }
    """
    # Obtener los datos JSON enviados en la solicitud
    datos = request.get_json()

    # Validar que se enviaron datos
    if datos is None:
        return jsonify({"error": "No se enviaron datos JSON"}), 400

    # Validar que existan los campos requeridos
    if 'valor' not in datos or 'escala' not in datos:
        return jsonify({"error": "Se requieren los campos 'valor' y 'escala'"}), 400

    valor = datos['valor']
    escala = datos['escala'].upper()  # Convertir a mayúsculas para estandarizar

    # Validar que el valor sea numérico
    if not isinstance(valor, (int, float)):
        return jsonify({"error": "El valor debe ser un número"}), 400

    # Aplicar la fórmula de conversión según la escala de origen
    if escala == 'C':
        # Conversión de Celsius a Fahrenheit: F = (C × 9/5) + 32
        valor_convertido = (valor * 9 / 5) + 32
        respuesta = {
            "valor_original": valor,
            "escala_origen": "Celsius",
            "valor_convertido": round(valor_convertido, 2),
            "escala_destino": "Fahrenheit"
        }
    elif escala == 'F':
        # Conversión de Fahrenheit a Celsius: C = (F − 32) × 5/9
        valor_convertido = (valor - 32) * 5 / 9
        respuesta = {
            "valor_original": valor,
            "escala_origen": "Fahrenheit",
            "valor_convertido": round(valor_convertido, 2),
            "escala_destino": "Celsius"
        }
    else:
        return jsonify({"error": "La escala debe ser 'C' (Celsius) o 'F' (Fahrenheit)"}), 400

    return jsonify(respuesta)


if __name__ == '__main__':
    app.run(debug=True, port=5001)

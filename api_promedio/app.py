from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/promedio', methods=['POST'])
def calcular_promedio():
    """
    Endpoint que recibe el nombre de un estudiante y una lista de calificaciones,
    calcula el promedio y devuelve el resultado en formato JSON.

    Ejemplo de entrada (JSON):
    {
        "nombre": "Juan",
        "calificaciones": [80, 90, 85, 70]
    }

    Ejemplo de salida (JSON):
    {
        "nombre": "Juan",
        "promedio": 81.25
    }
    """
    # Obtener los datos JSON enviados en la solicitud
    datos = request.get_json()

    # Validar que se enviaron datos
    if datos is None:
        return jsonify({"error": "No se enviaron datos JSON"}), 400

    # Validar que existan los campos requeridos
    if 'nombre' not in datos or 'calificaciones' not in datos:
        return jsonify({"error": "Se requieren los campos 'nombre' y 'calificaciones'"}), 400

    # Validar que calificaciones sea una lista no vacía
    if not isinstance(datos['calificaciones'], list) or len(datos['calificaciones']) == 0:
        return jsonify({"error": "Las calificaciones deben ser una lista no vacía"}), 400

    # Obtener los valores
    nombre = datos['nombre']
    calificaciones = datos['calificaciones']

    # Calcular el promedio
    # sum() suma todas las calificaciones
    # len() cuenta cuántas calificaciones existen
    promedio = sum(calificaciones) / len(calificaciones)

    # Crear la respuesta en formato JSON
    respuesta = {
        "nombre": nombre,
        "promedio": promedio
    }

    return jsonify(respuesta)


if __name__ == '__main__':
    app.run(debug=True)

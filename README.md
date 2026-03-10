# Ejercicios de API con Flask

Este repositorio contiene dos ejercicios básicos para practicar el desarrollo de APIs con Python y Flask.

## Estructura del Proyecto

```
/3.5. Ejercicios de API
│
├── api_promedio/          # Ejercicio 1: Cálculo de promedio
│   ├── app.py
│   └── venv/
│
└── api_conversor/         # Ejercicio 2: Conversor de temperatura
    ├── app.py
    └── venv/
```

## Ejercicio 1: API de Promedio

Calcula el promedio de una lista de calificaciones para un estudiante.

- **Endpoint**: `POST /promedio` (Puerto 5000)
- **Entrada (JSON)**:
  ```json
  {
      "nombre": "Juan",
      "calificaciones": [80, 90, 85, 70]
  }
  ```
- **Salida**:
  ```json
  {
      "nombre": "Juan",
      "promedio": 81.25
  }
  ```

## Ejercicio 2: API Conversor de Temperatura

Convierte temperaturas entre Celsius (C) y Fahrenheit (F).

- **Endpoint**: `POST /convertir-temperatura` (Puerto 5001)
- **Entrada (JSON)**:
  ```json
  {
      "valor": 100,
      "escala": "C"
  }
  ```
- **Salida**:
  ```json
  {
      "valor_original": 100,
      "escala_origen": "Celsius",
      "valor_convertido": 212.0,
      "escala_destino": "Fahrenheit"
  }
  ```

## Cómo Ejecutar

1. Navegar a la carpeta del ejercicio correspondiente.
2. Activar el entorno virtual (`venv\Scripts\activate`).
3. Ejecutar `python app.py`.
4. Realizar las peticiones utilizando Postman o `curl`.

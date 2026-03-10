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
<img width="814" height="816" alt="image" src="https://github.com/user-attachments/assets/152d516d-c4a1-467d-82f3-586c3a86b5c4" />


## Ejercicio 2: API Conversor de Temperatura

Convierte temperaturas entre Celsius (C) y Fahrenheit (F).

- **Endpoint**: `POST /convertir-temperatura` (Puerto 5001)
<img width="791" height="840" alt="image" src="https://github.com/user-attachments/assets/69d2a512-297e-4a5e-862f-af4956704760" />


## Cómo Ejecutar

1. Navegar a la carpeta del ejercicio correspondiente.
2. Activar el entorno virtual (`venv\Scripts\activate`).
3. Ejecutar `python app.py`.
4. Realizar las peticiones utilizando Postman o `curl`.

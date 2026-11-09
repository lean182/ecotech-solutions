import re

# Función para limpiar y normalizar los registros de sensores
def limpiar_registro_sensor(registro_raw):
    registro_limpio = {}

    # 1. Normalizar el sensor_id (asigna "DESCONOCIDO" si está vacío o nulo)
    sensor_id_raw = str(registro_raw.get("sensor_id") or "").strip()
    registro_limpio["sensor_id"] = sensor_id_raw or "DESCONOCIDO"

    # 2. Normalizar la temperatura (extrae valor numérico y convierte a float, asigna 0.0 si no es válido)
    temperatura_raw = registro_raw.get("temperatura")
    if temperatura_raw is not None:
        match = re.search(r"[-+]?\d+(?:\.\d+)?", str(temperatura_raw))
        if match:
            registro_limpio["temperatura"] = float(match.group())
        else:
            registro_limpio["temperatura"] = 0.0
    else:
        registro_limpio["temperatura"] = 0.0

    # 3. Normalizar la ubicación (asigna "Ubicación no registrada" si está vacía o nula)
    ubicacion_raw = registro_raw.get("ubicacion")
    if ubicacion_raw and str(ubicacion_raw).strip():
        registro_limpio["ubicacion"] = str(ubicacion_raw).strip()
    else:
        registro_limpio["ubicacion"] = "Ubicación no registrada"

    return registro_limpio

# Función para generar un resumen de sensores y alertas
def generar_resumen_sensores(lista_sensores_limpios, umbral_temperatura=30.0):
    sensores_alerta = []
    temperaturas_validas = []

    for sensor in lista_sensores_limpios:
        temp = sensor.get("temperatura")
        if temp is not None:
            temperaturas_validas.append(temp)
            if temp > umbral_temperatura:
                sensores_alerta.append(sensor["sensor_id"])

    promedio_temperatura = 0.0
    if temperaturas_validas:
        promedio_temperatura = sum(temperaturas_validas) / len(temperaturas_validas)

    return sensores_alerta, promedio_temperatura

# Ejemplo de uso
if __name__ == "__main__":
    # Datos crudos de ejemplo
    datos_crudos = [
        {"sensor_id": "SENSOR-001", "temperatura": "24.5C", "ubicacion": "Planta Norte"},
        {"sensor_id": "SENSOR-002", "temperatura": "32.8C", "ubicacion": "Planta Sur"},
        {"sensor_id": "SENSOR-003", "temperatura": "28.0C", "ubicacion": "Depósito Central"}
    ]

    print("--- Limpiando registros de EcoTech ---")
    sensores_limpios = [limpiar_registro_sensor(r) for r in datos_crudos]
    for s in sensores_limpios:
        print(s)

    print("\n--- Generando resumen y alertas ---")
    alertas, promedio = generar_resumen_sensores(sensores_limpios, umbral_temperatura=30.0)
    print(f"Sensores en alerta (>30°C): {alertas}")
    print(f"Temperatura promedio global: {promedio:.2f}°C")
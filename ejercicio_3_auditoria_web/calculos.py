# Calculos de consumo y emisiones de carbono
def calcular_emisiones_carbono(consumo_kwh, factor_emision=0.4):
    if consumo_kwh < 0:
        raise ValueError("El consumo no puede ser negativo.")
    return round(consumo_kwh * factor_emision, 2)

# Obtención de métricas de consumo
def obtener_metricas_consumo(registros_consumo):
    if not registros_consumo:
        return {"total_kwh": 0.0, "promedio_kwh": 0.0, "total_emisiones": 0.0}

    total_kwh = sum(r.get("consumo_kwh", 0.0) for r in registros_consumo)
    promedio_kwh = total_kwh / len(registros_consumo)
    total_emisiones = calcular_emisiones_carbono(total_kwh)

    return {
        "total_kwh": round(total_kwh, 2),
        "promedio_kwh": round(promedio_kwh, 2),
        "total_emisiones": round(total_emisiones, 2)
    }
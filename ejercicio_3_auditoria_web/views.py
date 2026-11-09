from ejercicio_3_auditoria_web.calculos import obtener_metricas_consumo

# Vista para el panel de sustentabilidad
def vista_panel_sustentabilidad(request):
    # Simulación de registros de consumo de la empresa
    registros_historicos = [
        {"mes": "Enero", "consumo_kwh": 150.5},
        {"mes": "Febrero", "consumo_kwh": 120.0},
        {"mes": "Marzo", "consumo_kwh": 135.2}
    ]

    # Obtención de métricas de consumo y emisiones
    metricas = obtener_metricas_consumo(registros_historicos)

    # Preparación del contexto para la plantilla
    contexto = {
        "titulo": "Panel de Sustentabilidad - EcoTech",
        "metricas": metricas,
        "registros": registros_historicos
    }
    
    return contexto
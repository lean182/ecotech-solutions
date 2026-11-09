import unittest
from ejercicio_3_auditoria_web.calculos import calcular_emisiones_carbono, obtener_metricas_consumo

# Pruebas unitarias para los cálculos de consumo y emisiones de carbono
class TestCalculoEmisiones(unittest.TestCase):

    # Prueba de cálculo de emisiones con consumo válido
    def test_calcular_emisiones_valido(self):
        resultado = calcular_emisiones_carbono(100.0)
        self.assertEqual(resultado, 40.0)

    # Prueba de cálculo de emisiones con factor de emisión personalizado
    def test_calcular_emisiones_factor_personalizado(self):
        resultado = calcular_emisiones_carbono(100.0, factor_emision=0.5)
        self.assertEqual(resultado, 50.0)

    # Prueba de cálculo de emisiones con consumo negativo
    def test_calcular_emisiones_consumo_negativo(self):
        with self.assertRaises(ValueError):
            calcular_emisiones_carbono(-50.0)

    # Prueba de obtención de métricas con registros vacíos
    def test_obtener_metricas_consumo_vacio(self):
        metricas = obtener_metricas_consumo([])
        self.assertEqual(metricas["total_kwh"], 0.0)
        self.assertEqual(metricas["promedio_kwh"], 0.0)
        self.assertEqual(metricas["total_emisiones"], 0.0)
        
    # Prueba de obtención de métricas con registros válidos   
    def test_obtener_metricas_consumo(self):
        registros = [
            {"consumo_kwh": 100.0},
            {"consumo_kwh": 200.0}
        ]
        metricas = obtener_metricas_consumo(registros)
        self.assertEqual(metricas["total_kwh"], 300.0)
        self.assertEqual(metricas["promedio_kwh"], 150.0)
        self.assertEqual(metricas["total_emisiones"], 120.0)


if __name__ == "__main__":
    unittest.main()
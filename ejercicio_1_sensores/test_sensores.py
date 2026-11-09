import unittest

from ejercicio_1_sensores.sensores import (
    generar_resumen_sensores,
    limpiar_registro_sensor,
)


class TestSensores(unittest.TestCase):

    def test_limpiar_registro_sensor_valido(self):
        # Prueba que los datos se limpien correctamente
        crudo = {"sensor_id": " SENSOR-001 ", "temperatura": "24.5C", "ubicacion": "Planta Norte"}
        limpio = limpiar_registro_sensor(crudo)
        
        self.assertEqual(limpio["sensor_id"], "SENSOR-001")
        self.assertEqual(limpio["temperatura"], 24.5)
        self.assertEqual(limpio["ubicacion"], "Planta Norte")

    def test_limpiar_registro_sensor_defecto(self):
        # Prueba que los valores por defecto se asignen correctamente
        crudo = {"sensor_id": "", "temperatura": None, "ubicacion": ""}
        limpio = limpiar_registro_sensor(crudo)
        
        self.assertEqual(limpio["sensor_id"], "DESCONOCIDO")
        self.assertIsNone(limpio["temperatura"])
        self.assertEqual(limpio["ubicacion"], "Ubicación no registrada")

    def test_generar_resumen_sensores(self):
        # Prueba que se generen correctamente las alertas y el promedio
        sensores_limpios = [
            {"sensor_id": "S1", "temperatura": 20.0, "ubicacion": "A"},
            {"sensor_id": "S2", "temperatura": 35.0, "ubicacion": "B"},
            {"sensor_id": "S3", "temperatura": None, "ubicacion": "C"}
        ]
        alertas, promedio = generar_resumen_sensores(sensores_limpios, umbral_temperatura=30.0)
        
        self.assertEqual(alertas, ["S2"])
        self.assertEqual(promedio, 27.5) 
        

if __name__ == "__main__":
    unittest.main()
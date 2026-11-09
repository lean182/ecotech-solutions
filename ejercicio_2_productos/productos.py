import json

# Definición de excepción personalizada para stock inválido
class StockInvalidoError(Exception):
    pass

# Clase base para dispositivos ecológicos
class DispositivoEcológico:
    def __init__(self, nombre, stock_inicial):
        self.nombre = nombre
        self.__stock = 0
        self.stock = stock_inicial  

    @property
    def stock(self):
        return self.__stock

    @stock.setter
    def stock(self, valor):
    
        if not isinstance(valor, (int, float)):
            raise TypeError("El stock debe ser un valor numérico.")
        if valor < 0:
            raise StockInvalidoError(f"Error: El stock no puede ser negativo ({valor}).")
        self.__stock = int(valor)

    def ficha_tecnica(self):
        return f"Dispositivo: {self.nombre} | Stock disponible: {self.__stock}"

    def to_dict(self):
        return {
            "tipo": "DispositivoEcológico",
            "nombre": self.nombre,
            "stock": self.__stock
        }

# Clase derivada para paneles solares
class PanelSolar(DispositivoEcológico):
    def __init__(self, nombre, stock_inicial, potencia_w):
        super().__init__(nombre, stock_inicial)
        self.potencia_w = potencia_w

    # Redefinición del método ficha_tecnica para incluir potencia (Polimorfismo)
    def ficha_tecnica(self):
        return f"Panel Solar: {self.nombre} | Potencia: {self.potencia_w}W | Stock: {self.stock}"

    def to_dict(self):
        data = super().to_dict()
        data["tipo"] = "PanelSolar"
        data["potencia_w"] = self.potencia_w
        return data

# Clase para gestionar el inventario y guardar datos en JSON
class GestorInventario:
    @staticmethod
    def guardar_catalogo_json(lista_dispositivos, ruta_archivo):
        try:
            datos_serializables = [dispositivo.to_dict() for dispositivo in lista_dispositivos]
            with open(ruta_archivo, "w", encoding="utf-8") as archivo:
                json.dump(datos_serializables, archivo, indent=4, ensure_ascii=False)
            print(f"Catálogo guardado exitosamente en: {ruta_archivo}")
        except Exception as e:
            print(f"Error al guardar el archivo JSON: {e}")

# Ejemplo de uso y pruebas
if __name__ == "__main__":
    print("--- 1. Probando control de excepciones con stock negativo ---")
    try:
        panel_defectuoso = PanelSolar("Panel Genérico", -5, 300)
    except StockInvalidoError as error:
        print(f"Excepción capturada con éxito -> {error}")

    print("\n--- 2. Creando catálogo válido de EcoTech ---")
    try:
        p1 = PanelSolar("EcoPanel Pro 400W", 15, 400.0)
        p2 = PanelSolar("SolarGrid Mini 200W", 8, 200.0)
        
        catalogo = [p1, p2]

        print("Fichas técnicas generadas:")
        for item in catalogo:
            print(item.ficha_tecnica())

        print("\n--- 3. Guardando catálogo en disco ---")
        GestorInventario.guardar_catalogo_json(catalogo, "catalogo_ecotech.json")

    except (StockInvalidoError, TypeError) as error:
        print(f"Error crítico en el inventario: {error}")
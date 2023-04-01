from inmueble import Inmueble
class Casa(Inmueble):
    def __init__(self, precio: int, ubicacion: str, estado: str, pisos : int, color : str) -> None:
        self.pisos = pisos
        self.color = color
        super().__init__(precio, ubicacion, estado)
    def incrementarPisos(self, incremento : int):
        self.pisos += incremento
    def getColor(self):
         return self.color
    def getPrecio(self):
        return self.precio
    def setPrecio(self, precio):
        self.precio = precio
    def getInfo(self):
            info = "--------Información del Inmueble--------"
            info += f"\n Precio:  + {self.getPrecio()}"
            info += "\n Ubicación: " + self.getUbicacion()
            info += "\n Color: " + self.getColor()
            return info
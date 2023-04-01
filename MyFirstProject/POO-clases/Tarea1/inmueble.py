class Inmueble:
    def __init__(self, precio : int, ubicacion : str, estado : str) -> None:
        self.precio = precio
        self.ubicacion = ubicacion
        self.estado = estado
    def aumentarPrecio(self, incremento : int):
        self.precio += incremento
    def reducirPrecio(self, decremento : int):
        self.precio -= decremento
    def getUbicacion(self):
        return self.ubicacion
    def setEstado(self, estado):
        self.estado = estado
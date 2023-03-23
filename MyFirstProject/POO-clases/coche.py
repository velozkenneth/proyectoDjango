class Coche:
    #Atributos o propiedades

    def __init__(self, color, marca, velocidad, modelo) -> None:
        self.color = color
        self.marca = marca
        self.velocidad = velocidad
        self.modelo = modelo

    def acelerar(self):
        self.velocidad += 1

    def desacelerar(self):
        self.velocidad -=1

    def setColor(self,color):
        self.color = color

    def getColor(self):
        return self.color

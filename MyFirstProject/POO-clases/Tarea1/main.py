from casa import Casa
from edificio import Edificio

casa1 = Casa(precio=40000,ubicacion="Sauces", estado="Nuevo", pisos=2, color="Verde")

edificio1 = Edificio(precio=150000,ubicacion="Urdesa",estado="Antiguo",pisos=12, color="Blanco")

print(edificio1.getInfo())
print(casa1.getInfo())

print(type(casa1))
print(type(edificio1))
from transportes.carro import Carro
from transportes.bicicleta import Bicicleta
from transportes.aviao import Aviao

transportes = [
    Carro(),
    Bicicleta(),
    Aviao()
]

for transporte in transportes:
    transporte.mover()

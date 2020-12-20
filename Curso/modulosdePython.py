#aqui veremos todos los modulos que python ofrece ya por defecto, primeramente si se desea ver la mayoria podemos ir a google
#y busca PYTHON 3 MODULE INDEX
import random

for i in range(3):
    #aqui random.random se encarga de mandar un numero random entre 0 y 1
    print(random.random())
    #si queremos que sea entre un rango de datos usamos lo que es randint()
    print(random.randint(10, 20))



miembros = ("magikaro", "marra", "sketti")
#aqui esto lo que hace es elegir un dato de una lista dada
lider = random.choice(miembros)
print(lider)

class Dice:
    def roll(self):
        values = (1, 2, 3, 4, 5, 6)
        print(f'({values[random.randint(0, 5)]}, {values[random.randint(0, 5)]})')

dado = Dice()

dado.roll()
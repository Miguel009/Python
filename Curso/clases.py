#para clases es buena practica que se coloque las primeras letras de cada palabra y que quede unido
class Point:

#para definir las funciones es necesario poner un argumento en este caso  colocamos la palabra reservada self
    def move(self):
        print("move")

    def draw(self):
        print("draw")

#aqui de esta manera mandamos a llamar al objeto  o mejor dicho a la clase point es decir aqui se crea el primer punto
punto1 = Point()
#como se puede ver aqui se pueden definir variables dentro del objeto
punto1.x = 10
punto1.y = 20
print(punto1.x)
punto1.draw()

punto2 = Point()
punto2.x = 1
print(punto2.x)

#********************************************* CONSTRUCTORES ****************************************
class PointW:
    #self es una referencia al objeto de este momento
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self):
        print("move")

    def draw(self):
        print("draw")

punto3 = PointW(10, 35)
punto3.x = 11
print(punto3.x)

class Person:

    def __init__(self, name):
        self.name = name

    def hello(self):
        print(f"Hola {self.name}")

persona1 = Person("Enrique")

persona1.hello()
#aqui lo que estamos haciendo es definir una clase la cual tiene metodos que las clases de dog y cat pueden utilizar es decir estamos heredando el metodo
class Mammal:
    def walk(self):
        print("walk")

#aqui lo que hemos hecho es decirles que la clase perro y gato van a a heradar a mammal o que son hijos de mamal y la palabra es pass es nada mas 
#para decir que aunque la clase este vacia queremos dejerla asi que no lo tome como un error
class Dog(Mammal):
    def bark(self):
        print("barking")

class Cat(Mammal):
    def miau(self):
        print("miau")


dog1 = Dog()
dog1.walk()
dog1.bark()

cat1 = Cat()
cat1.miau()
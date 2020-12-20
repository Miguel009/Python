#esta es la funcion utilizando la palabra reservada def
def bienvenida():
    print('hi there')
    print('bienvenido!')
#segun se entiende aunque no es necesario es buena idea dejar dos lineas limpias despues de la funcion para mantener un orden


print("Start")
bienvenida()
print("Finish")

#/*********************************************PARAMETROS***************************************
#argunmento es el dato que se manda y parametro seria la variable que en este caso seria name
def bienvenida1(name, second):
    print('hi there '+name+" "+second)
    print('bienvenido!')

bienvenida1("hola", "pruebas")

#**************************************Argumentos palabras clave**********************************
#en python se tienen la funciones normales en donde el orden en el que estan las variables es el orden en el que se deben colocar los argumentos
#pero tambien hay otra opcion que es pasar argumentos utilizando palabras clave

bienvenida1(second="clave", name="palabras")
#cuando se usa este tipo de datos es buena idea no combinar es decir si se va ahacer por posicion hacerlo por posicion sino pues utilizar palabras clave
#aunque igual se puede usar de esta manera pero no es muy recomandable
bienvenida1("clave", second="palabras")

#************************************** RETURN ****************************************************
def square(number):
    return number*number

magikarp = square(3)

print(magikarp)

#************************ Creando una funcion reautilizable *********************************
def emojis(mensaje):
    words = mensaje.split(' ')

    emojis = {
        ":)" : "😊",
        ":(" : "😢",
        ":v" : "pacman"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word)+" "
    print(output)

mensa = input(">")
emojis(mensa)

#********************************* Excepciones *****************************************
try:
    age = int(input('AÑOS: '))
    var = 10000/age
    print(var)
except ZeroDivisionError:
    print("la edad no puede ser 0")
except ValueError: #este es solo un tipo de error que se puede manejar
    print("Dato erroneo")



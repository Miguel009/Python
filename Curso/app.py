print("Hola mi amor")
print('o----')
print(' ||||')
#aqui lo que hacemos es que el string que tenemos se multiplica por 10 es decir aparecera 10 veces un *
print('*' * 10)
#**************************VARIABLES****************************
price= 10
print(price)

price = 10
price = 20
print(price)

#python es casesensitive por lo que si hay diferencia entre mayusculas y minusculas
#los datos que agarra python pueden ser
rating = 4.2132 #floats
name = 'Miguel' #strings
is_true = True #booleanos
nice = 35 #integers 
#aunque tambien pueden usarse cosas mas complejas como: 
#****************************************INPUTS*****************************************

#mood = input('Que tal estas ? ')
#print('que bien que esta '+mood)

#***********************************CONVERSIONES**************************************

#aqui con el input siempre se obtendra un string entonces es necesario convertirlo a un float o un int si necesitamos nuemros.
anio = input('Año de nacimiento: ')
age = 2020- int(anio)
print(age)
print(type(age))

lb = input('Digite su peso en libras: ')
kg = float(lb) *0.453592
print('su peso de '+lb+' lb son '+str(kg) +' en kilogramos')

#************************************************STRINGS***********************************************

#curso = 'python's para principiantes' en este caso si lo dejamos asi nos dara un error porque el ' de python's lo reconocera como cierre de las comillas entonces lo despues no lo toomara dentro del string
curso = "python's para principiantes" #aqui podemos ver utilizando " " si se pude colocar al normal '
curso = 'python para "principiantes"' #aqui podemos ver que utilizando las '' podemos utilizar los "" adentro del string
curso = '''
Ah que interesante
este es un string con multilengua

solo es necesario usar 3 veces las comillas simples

'''
print(curso)
curso = "python's para principiantes"
#aqui podemos separar el string en chars
print(curso[0]) #en este caso nos retoranaria la p unicamente

#aqui hay algo diferente y es que si colocamos un index negativo va a la direccion contraria es decir de derecha a izquierda
print(curso[-1])

#aqui podemos tambier decir cuantos caracteres del string queremos

print(curso[0:3])
print(curso[0:])
print(curso[1:])

otro = curso[:]
print(otro)

#***************************************************STRING FORMATEADOS**************************************

#es es la forma normal
uno = 'John'
dos = 'Lennon'
mensaje= uno + ' ['+dos+'] es programador'
print(mensaje)

#forma formateada
msg = f'{uno} [{dos}] es programador'
print(msg)

#metodos de un string

clases = "python para principiantes"
#aqui lo que podemos ver es el tamañao del string
print(len(clases))
#hacerlo mayusculas
print(clases.upper())
#hacerlo minusculas
print(clases.lower())
#aqui esta nos ayuda a buscar letras en nuestra cadena y obtenemos el index de esa palabra esta es CASESENSITIVE es decir hace diferencias entre mayusculas y minusculas
#ademas si colocamos una palabra  por ejemplo para agarra el index a donde inicia la palabra
print(clases.find('p'))
print(clases.find('para'))
#este replace nos permite cambiar una palabra o un caracter por otra
print(clases.replace('para', 'poro'))
#esto lo que nos permite es verificar si una palabra existe en nuestro caracteres y devolvera ya sea true o false obviamente tambien es casesensitive
print('python' in clases)

#-------------------------------------------------OPERACIONES ARITMETICAS---------------------------------------------------
print(10 +3)
print(10-3)
print(10*6)
#para la division existen dos formas de realizarse
print(10/3) #este devuelve un float
print(10//3) #este devuelve solo el entero
print(10 %3) #aqui obtenemos el residuo de la division
print(10**3) #aqui es la potencia es decir 10^3
x=10
x=x+3
x+=3 #aqui se esta haciendo lo mismo que en la linea 107 y se puede tambien hacer esto mismo al restar -= asi o multiplica *= asi
print(x)

#/*************************************************PRESEDENCIA DE OPERADORES***********************************************************
y= 10 + 3 * 2 #aqui se va a ejecutar primero la multiplicacion porque es el que tiene pioridad
print(y)
#pioridades
#parentesis
#exponenciales
#multiplicacion o division
#suma y resta

#****************************************************FUNCIONES MATEMATICAS**********************************************************
x=2.9
#esta funcion nos permite redondear un numero
print(round(x))
#aqui retorna un numero positivo siempre
print(abs(-2.9))
#aqui para usar muchas otras opciones tenemos que importar la libreria o modulo que trae python que en este caso se llama math
import math
#obtenemos el cielo de este numero en este caso 3
print(math.ceil(2.9))
#con esta obtenemos lo mas bajo o mejor dicho el entero menor del numero
print(math.floor(2.9))

#********************************************************IF*************************************************************

is_hot = True
is_cold = False
if is_hot:
    print("Es un dia muy caliente")#AQUI TIENE QUE ESTA DE ESTA MANERA
    print("Es un dia muy caliente PAPA")
#aqui ya es como un else if
elif is_cold:
    print("Dia de chill PA PA")
else:
    print("Que buen dia")
#YA QUE SI LO DEJAMOS ASI YA NO ESTA DENTRO DE NUESTRO IF
print(f"Ten un buen dia {is_hot}")

#****************************************************OPERADORES LOGICOS***************************************

pose_dinero=True
pose_credito=True
#aqui el and se escribe asi literalmente para hacer lo de Si esto se cumple y esto tambien entonces pasa
if pose_credito and pose_credito:
    print("Si puede obtener")
#aqui asi es la manera de colocara el or
if pose_credito or pose_credito:
    print("Si puede obtener")
#para hacer el inverso entonces se utiliza el not
if pose_credito or not pose_credito:
    print("Si puede obtener")

#****************************************************OPERADORES MATEMATICOS COMPARACION***********************
temp=30
# operadores > == >= <= !=
if temp>=30:
    print("Haceee calor")
else:
    print("No Hacee calorr")

#****************************************************WHILE LOOPS*************************************************
i = 1
while i<=5:
    print("*"*i)
    i+=1

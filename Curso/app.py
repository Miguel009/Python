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
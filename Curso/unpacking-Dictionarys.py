coordenadas = (1, 2, 3)
coordenadas2 = [1, 2, 3]
#para poder asignar datos a variables tendriamos que hacer esto pero python da otra opcion
x = coordenadas[0]
y = coordenadas[1]
z = coordenadas[2]
#la cual es esta es decir que las tres varibales agarrarian cabal los datos de x=1, y=2, z=3 en este caso ah esto se le llama unpacking
x, y, z = coordenadas
x1, y1, z1 = coordenadas2

print(z)

print(x1)

#dictionary o diccionario
#como se puede ver es el manejo de un objeto con diferentes datos
customer = {
    "name": "Miguel Flores",
    "age": 43, 
    "is_verified": True
}
#recordando que python es caseSensitive por lo que debe de mantenerse las mayusculas y minusculas iguales
print(customer["name"])
#con el uso de la funcion get lo que podemos hacer es evitar que aparesca un error por si el atributo buscado no existe y en lugar de eso enviar un "None"
print(customer.get("age"))

print(customer.get("sa"))

#ademas que si se nota que el atributo no existe se puede colocar uno por defecto

print(customer.get("sa", "Dato por Defecto"))

#ademas como en los objetos se pueden cambiar los atributos
customer["name"] = "nuevo nombre"
print(customer["name"])

#y ademas se  pueden agregar atributos de la sigueinte manera

customer["atrib1"] = "Este es un atributo creado"

print(customer["atrib1"])


#convertidor de emojis+

mensaje = input(">")

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

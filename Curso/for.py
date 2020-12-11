#aqui lo que estamos diciendo es que que por cada caracter de python se va a crear un item y vamos a imprimr esto e este caso se mostraria p luego la y y asi sucesivamente
for item in 'Python':
    print(item)

for items in ['Mosh', 'John', 'Maria']:
    print(items)

for items in [1, 2, 3]:
    print(items)
#range nos permite imprimr lo que son una cierta cantidad de numeros iniciando del 0 en este caso que le colocamos 10 pues mostraria del 0 al 9
for items in range(10):
    print(items)

#tambien como la palabra lo dice podemos agregarle un rango en este caso digamos que inice en 5
for items in range(5, 10):
    print(items)
#y tambien se puede agregar el numero de saltos que se quiren por ejemplo aqui le colocamos lo que es un 2 es decir que de 5 va a subir a 7 y luego a 9
for items in range(5, 10, 2):
    print(items)

presio = [10, 20, 35, 40]
suma=0
for items in presio:
    suma +=items

print(suma)
names = ['Josh', 'Bob', 'Moshj', 'Sarah', 'Maria']
print(names)
print(names[1])
print(names[-1])
print(names[1:3])
print(names[2:])

number = [4, 5, 65, 76, 87, 56,55]
maxs=0
for num in number:
    if num > maxs:
        maxs=num

print(maxs)

#listas en 2d
matrix = [
    [1, 2, 3],
    [3, 5, 6],
    [7, 8, 9]
]
matrix[0][2] = 20
print(matrix[0][2])

for row in matrix:
    for item in row:
        print(item)

#Funciones de las listas

numbers = [3, 54, 65, 43, 4,3]
#aqui lo que hacemos es insertar un nuevo dato a nuestra lista/arreglo solo que siempre se colocan al final
numbers.append(14)
print(numbers)
#aqui con esta funcion inser podemos decidir en que posicicon se van a insertar los datos
#en este caso hemos puesto que en la primera posicion queremos que se inserte el numero 20
numbers.insert(0,20)
print(numbers)
#aqui colocamos que datos deseamos eliminar de nuestra lista/arreglo 
#en este caos eh colocado que se elimine el numero 54 de nuestra lista
numbers.remove(54)
print(numbers)
#con index lo que hacemos es que buscamos el index en donde esta un dato en nuestra lista
print(numbers.index(43))
#con count se pueden contar la cantidad de veces que hay un dato en el array en este caso eh puesto
# que busque 3 en el array y como se puede ver hay 2
print(numbers.count(3))
#ademas de este se puede usar el in para generar un booleanos de true o false
print(65 in numbers)

#con sort lo que pasa es que se ordenan los datos de menor a mayor
numbers.sort()
print(numbers)

#y con reverse pues se le da la vuelta a nuestro arreglo
numbers.reverse()
print(numbers)
#aqui con pop lo que hacemos es que se elimina el ultimo elemento de nuestra lista
numbers.pop()
print(numbers)

#con copy se puede copiar el arreglo
numbers2 = numbers.copy()
print(numbers2)
#con clear eliminamos todos los datos de nuestra lista/arreglo
numbers.clear()
print(numbers)

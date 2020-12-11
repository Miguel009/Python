#nested loop es tener loops encadenados
for x in range(4):
    for y in range(3):
        print(f'({x},{y})')


numeros = [5, 2, 5, 2, 2]

for x in numeros:
    output =""
    for y in range(x):
        output += "x"
    print(output)
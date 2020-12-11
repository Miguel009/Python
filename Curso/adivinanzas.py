import math
oportunidades = 0
numero = 9
while oportunidades < 3:
    guess = input("Escriba su respuest: ")
    if int(guess) == numero:
        print("Hey lo adivinaste nice")
        break
    else:
        oportunidades+=1
else: #aqui el while puede tener un else el cual se ejecutara cuando ya termine o se complete el while y para evitar que se ejecute si la persona sabe la palabra utilizamos el break que nos sacara del loop
    print("ni modo lo intentaste")


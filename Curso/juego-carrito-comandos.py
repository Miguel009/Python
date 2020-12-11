opcion = ""
start = False
while opcion != "exit":
    opcion = input(">").lower()

    if opcion == "help":
        print('''
        start->Inicializa el carro

        stop->detiene el carro

        exit->finaliza el programa
        
        ''')
    elif opcion == "start":
        if not start:
            start=True
            print("carro iniciado")
        else:
            print("carro ya iniciado")
    elif opcion == "stop":
        if start:
            start=False
            print("carro detenido")
        else:
            print("carro ya detenido")
    elif opcion == "exit":
        print("Finalizando")
    else:
        print("No esa opcion")

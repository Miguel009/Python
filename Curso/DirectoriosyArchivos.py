from pathlib import Path

#direccion absoluta: iniciamos desde el root es decir desde la raiz

#direccion relativa: iniciamos desde donde inicio el programa

#aqui la clase path si la iniciamos sin nada entonces tomara la direccion relativa si le colocamos algo entonces seria la direccion de estos mommento mas la que se le ha mandado
path = Path("Curso/modulos")


#print(path.mkdir()) mkdir es uitlizado para crear un nuevo directorio

#print(path.rmdir()) rmdir es para eliminar el directorio
#AQUI CON PATH LO QUE PASA ES QUE SE COLOCA EN EL DIRECTORIO QUE ESTAMOS ACTUALMENTE Y DE AHI Busca lo demas, OJO es desde el directorio que esta abierto no en donde esta el archivo, sino el directorio
#que se tiene el el proyecto para este curso la carpeta que esta viendo es python y de ahi es deglosar a los demas
path2 = Path("Curso/modulos")
print(path2.exists()) #aqui este retorna un booleano el cual dice si la carpeta existe o no 
#path2.mkdir()
#glob es usado para buscar datos dentro del directorio
for files in path.glob('*.py'):
    print(files)
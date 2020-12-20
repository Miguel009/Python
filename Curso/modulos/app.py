#para poder usar los modulos de otro archivo lo que hay que hacer es colocar la palabra import y luego el nombre del archivo que se desea importar en este caso se llama convertidor
# y como se puede ver ya se pueden utilizar los metodos que estan dentro de convertidor
import convertidor
#ademas tambien se puede llamar a una funcion en especifico de la siguiente manera y de esa manera ya no es necsario que se coloque el convertidor al inicio sino que solo se manda a llamar la opcion
from convertidor import lbs_to_kgs

import utils

print(convertidor.kg_to_lbs(70))

print(lbs_to_kgs(100))

utils.find_max([15, 75, 85, 65])
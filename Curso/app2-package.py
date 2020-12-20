#aqui para importar un modulo de algun paquete se puede hacer de las siguiente maneras:
#1. podemos ver de la manera tradicional colocando el nombre de la carpeta que en este caso es package luego un punto y el nombre del modulo que se desea
import package.ship
#2. tambien igual que en los modulos se puede llamar unicamente a una funcion
from package.ship import calc_shipping
#3. o sino tambien se puede realizar de esta forma que de la carpeta package sea dea importar el modulo ship
from package import ship
package.ship.calc_shipping()

ship.calc_shipping()
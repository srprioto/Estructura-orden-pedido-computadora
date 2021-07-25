import os
os.system("clear")

from Monitor import Monitor
from Raton import Raton
from Teclado import Teclado
from Computadora import Computadora
from Orden import Orden

teclado1 = Teclado("hp", "USB")
raton1 = Raton("hp", "USB")
monitor1 = Monitor("hp", 15)

teclado2 = Teclado("acer", "bluetooth")
raton2 = Raton("acer", "bluetooth")
monitor2 = Monitor("acer", 20)

computadora1 = Computadora("HP", monitor1, raton1, teclado1)
computadora2 = Computadora("acer", monitor2, raton2, teclado2)


computadoras1 = [computadora1, computadora2]
orden1 = Orden(computadoras1)


print(orden1)
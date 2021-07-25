from Monitor import Monitor
from Raton import Raton
from Teclado import Teclado


class Computadora:
    
    contadorComputadoras = 0

    def __init__(self, nombre, monitor, raton, teclado):
        Computadora.contadorComputadoras += 1
        self.idComputadora = Computadora.contadorComputadoras
        self.nombre = nombre
        self.monitor = monitor
        self.teclado = teclado
        self.raton = raton


    def __str__(self):
        return f"""
            {self.nombre}: {self.idComputadora}
            Monitor:    {self.monitor}
            Teclado:    {self.teclado}
            raton:      {self.raton}
        """



teclado1 = Teclado("hp", "USB")
raton1 = Raton("hp", "USB")
monitor1 = Monitor("hp", 15)

teclado2 = Teclado("acer", "bluetooth")
raton2 = Raton("acer", "bluetooth")
monitor2 = Monitor("acer", 20)


if __name__ == '__main__':
    computadora1 = Computadora("HP", monitor1, raton1, teclado1)
    computadora2 = Computadora("acer", monitor2, raton2, teclado2)
    print(computadora1)
    print(computadora2)
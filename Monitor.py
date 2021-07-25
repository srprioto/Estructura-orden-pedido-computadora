class Monitor:
    
    contadorMonitor = 0

    def __init__(self, marca, tamano):
        self.marca = marca
        self.tamano = tamano
        self.idMonitor = Monitor.contador()

    @staticmethod
    def contador():
        Monitor.contadorMonitor += 1
        return Monitor.contadorMonitor


    def __str__(self):
        return f"id: {self.idMonitor}, marca: {self.marca}, tipo: {self.tamano} pulgadas"



class Orden:
    
    contadorOrden = 0

    def __init__(self, computadoras):
        Orden.contadorOrden += 1
        self.idOrden = Orden.contadorOrden
        self.computadoras = computadoras

    def agregar_computadoras(self, computadora):
        self.computadoras.append(computadora)

    
    def __str__(self):
        computadoras_str = ''
        for computadora in self.computadoras:
            computadoras_str += computadora.__str__()

        return f'''
            Orden: {self.idOrden}
            Computadoras: {computadoras_str}
        '''
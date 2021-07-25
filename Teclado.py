from DispositivoEntrada import DispositivoEntrada

class Teclado(DispositivoEntrada):
    
    contadorTeclado = 0

    def __init__(self, marca, tipoEntrada):
        super().__init__(marca, tipoEntrada)
        self.idTeclado = Teclado.contador()

    @classmethod
    def contador(cls):
        cls.contadorTeclado += 1
        return cls.contadorTeclado

    def __str__(self):
        return f"id: {self.idTeclado}, tipo: {self.tipoEntrada}, marca: {self.marca}"


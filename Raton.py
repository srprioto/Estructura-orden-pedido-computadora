from DispositivoEntrada import DispositivoEntrada

class Raton(DispositivoEntrada):
    
    contadorRaton = 0

    def __init__(self, marca, tipoEntrada):
        super().__init__(marca, tipoEntrada)
        Raton.contadorRaton += 1
        self.idRaton = Raton.contadorRaton

    def __str__(self):
        return f"id: {self.idRaton}, marca: {self.marca}, tipo: {self.tipoEntrada}"

    

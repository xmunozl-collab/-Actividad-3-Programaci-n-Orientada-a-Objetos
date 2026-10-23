from figura_geometrica import FiguraGeometrica


class Cubo(FiguraGeometrica):
    def __init__(self, lado):
        super().__init__()
        self.lado = lado
        self.set_volumen(self.calcular_volumen())
        self.set_superficie(self.calcular_superficie())

    def calcular_volumen(self):
        return self.lado ** 3

    def calcular_superficie(self):
        return 6 * self.lado ** 2

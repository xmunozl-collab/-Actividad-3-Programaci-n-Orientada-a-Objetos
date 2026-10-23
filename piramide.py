from figura_geometrica import FiguraGeometrica


class Piramide(FiguraGeometrica):
    def __init__(self, base, altura, apotema):
        super().__init__()
        self.base = base
        self.altura = altura
        self.apotema = apotema
        self.set_volumen(self.calcular_volumen())
        self.set_superficie(self.calcular_superficie())

    def calcular_volumen(self):
        return self.base ** 2 * self.altura / 3

    def calcular_superficie(self):
        # area de la base + area de las 4 caras laterales
        area_base = self.base ** 2
        area_lados = 2 * self.base * self.apotema
        return area_base + area_lados

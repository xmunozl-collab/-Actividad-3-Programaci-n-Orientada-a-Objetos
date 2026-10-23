import tkinter as tk
from ventana_figura import VentanaFigura
from cilindro import Cilindro
from esfera import Esfera
from piramide import Piramide
from cubo import Cubo
from prisma import Prisma


class VentanaFiguras(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Figuras")
        self.resizable(False, False)

        tk.Label(self, text="Seleccione una figura geométrica:").place(x=20, y=15)

        # un boton por cada figura
        boton_cilindro = tk.Button(self, text="Cilindro", command=self.abrir_cilindro)
        boton_cilindro.place(x=20, y=50, width=80, height=23)
        boton_esfera = tk.Button(self, text="Esfera", command=self.abrir_esfera)
        boton_esfera.place(x=110, y=50, width=80, height=23)
        boton_piramide = tk.Button(self, text="Pirámide", command=self.abrir_piramide)
        boton_piramide.place(x=200, y=50, width=80, height=23)
        boton_cubo = tk.Button(self, text="Cubo", command=self.abrir_cubo)
        boton_cubo.place(x=290, y=50, width=80, height=23)
        boton_prisma = tk.Button(self, text="Prisma", command=self.abrir_prisma)
        boton_prisma.place(x=380, y=50, width=80, height=23)

        # ventana centrada en la pantalla
        x = (self.winfo_screenwidth() - 480) // 2
        y = (self.winfo_screenheight() - 110) // 2
        self.geometry(f"480x110+{x}+{y}")

    # eventos de los botones: cada uno abre la ventana de su figura
    def abrir_cilindro(self):
        VentanaFigura(self, "Cilindro", ["Radio (cms):", "Altura (cms):"], Cilindro, "cilindro.png")

    def abrir_esfera(self):
        VentanaFigura(self, "Esfera", ["Radio (cms):"], Esfera, "esfera.png")

    def abrir_piramide(self):
        VentanaFigura(self, "Pirámide", ["Base (cms):", "Altura (cms):", "Apotema (cms):"],
                      Piramide, "piramide.png")

    def abrir_cubo(self):
        VentanaFigura(self, "Cubo", ["Lado (cms):"], Cubo, "cubo.png")

    def abrir_prisma(self):
        VentanaFigura(self, "Prisma", ["Largo (cms):", "Ancho (cms):", "Altura (cms):"],
                      Prisma, "prisma.png")

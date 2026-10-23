import os
import tkinter as tk
from tkinter import messagebox


class VentanaFigura(tk.Toplevel):
    def __init__(self, padre, titulo, campos, clase_figura, imagen):
        super().__init__(padre)
        self.title(titulo)
        self.resizable(False, False)
        self.clase_figura = clase_figura

        # un campo de texto por cada dato que pide la figura
        self.campos = []
        for i in range(len(campos)):
            etiqueta = tk.Label(self, text=campos[i], anchor="w")
            etiqueta.place(x=20, y=20 + 30 * i, width=110, height=23)
            campo = tk.Entry(self)
            campo.place(x=130, y=20 + 30 * i, width=100, height=23)
            self.campos.append(campo)

        y = 20 + 30 * len(campos)
        self.boton_calcular = tk.Button(self, text="Calcular", command=self.calcular)
        self.boton_calcular.place(x=130, y=y, width=100, height=23)

        self.volumen = tk.Label(self, text="Volumen (cm3):", anchor="w")
        self.volumen.place(x=20, y=y + 40, width=240, height=23)
        self.superficie = tk.Label(self, text="Superficie (cm2):", anchor="w")
        self.superficie.place(x=20, y=y + 70, width=240, height=23)

        # parte propuesta: imagen de la figura
        try:
            ruta = os.path.join(os.path.dirname(os.path.abspath(__file__)), imagen)
            self.foto = tk.PhotoImage(file=ruta)
            tk.Label(self, image=self.foto).place(x=270, y=20)
        except tk.TclError:
            pass  # si no esta la imagen la ventana funciona igual

        # ventana centrada en la pantalla
        ancho = 410
        alto = y + 110
        x_ventana = (self.winfo_screenwidth() - ancho) // 2
        y_ventana = (self.winfo_screenheight() - alto) // 2
        self.geometry(f"{ancho}x{alto}+{x_ventana}+{y_ventana}")

    # evento del boton Calcular
    def calcular(self):
        valores = []
        try:
            for campo in self.campos:
                valores.append(float(campo.get().replace(",", ".")))
        except ValueError:
            messagebox.showerror("Error", "Campo nulo o error en formato de número", parent=self)
            return

        for valor in valores:
            if valor <= 0:
                messagebox.showerror("Error", "Los valores deben ser mayores que cero", parent=self)
                return

        # se crea la figura con los datos ingresados
        figura = self.clase_figura(*valores)
        self.volumen.config(text=f"Volumen (cm3): {figura.get_volumen():.2f}")
        self.superficie.config(text=f"Superficie (cm2): {figura.get_superficie():.2f}")

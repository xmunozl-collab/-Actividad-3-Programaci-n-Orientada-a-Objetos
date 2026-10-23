import tkinter as tk
from tkinter import messagebox
from notas import Notas


class VentanaNotas(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Notas")
        self.resizable(False, False)

        # campos de texto para las 5 notas
        self.campos = []
        for i in range(5):
            etiqueta = tk.Label(self, text=f"Nota {i + 1}:", anchor="w")
            etiqueta.place(x=20, y=20 + 30 * i, width=80, height=23)
            campo = tk.Entry(self)
            campo.place(x=105, y=20 + 30 * i, width=135, height=23)
            self.campos.append(campo)

        # botones
        self.boton_calcular = tk.Button(self, text="Calcular", command=self.calcular)
        self.boton_calcular.place(x=20, y=170, width=100, height=23)
        self.boton_limpiar = tk.Button(self, text="Limpiar", command=self.limpiar)
        self.boton_limpiar.place(x=125, y=170, width=80, height=23)

        # etiquetas donde se muestran los resultados
        self.promedio = tk.Label(self, text="Promedio = ", anchor="w")
        self.promedio.place(x=20, y=210, width=230, height=23)
        self.desviacion = tk.Label(self, text="Desviación estándar = ", anchor="w")
        self.desviacion.place(x=20, y=240, width=230, height=23)
        self.mayor = tk.Label(self, text="Nota mayor = ", anchor="w")
        self.mayor.place(x=20, y=270, width=230, height=23)
        self.menor = tk.Label(self, text="Nota menor = ", anchor="w")
        self.menor.place(x=20, y=300, width=230, height=23)

        # ventana centrada en la pantalla
        x = (self.winfo_screenwidth() - 280) // 2
        y = (self.winfo_screenheight() - 350) // 2
        self.geometry(f"280x350+{x}+{y}")

    # evento del boton Calcular
    def calcular(self):
        notas = Notas()

        for i in range(5):
            texto = self.campos[i].get().strip().replace(",", ".")

            # parte propuesta: las 5 notas son obligatorias
            if texto == "":
                messagebox.showwarning("Alerta", f"Falta ingresar la nota {i + 1}.")
                return

            # parte propuesta: solo se aceptan numeros
            try:
                notas.lista_notas[i] = float(texto)
            except ValueError:
                messagebox.showerror("Error", f"La nota {i + 1} no es un número válido.")
                return

        self.promedio.config(text=f"Promedio = {notas.calcular_promedio():.2f}")
        self.desviacion.config(text=f"Desviación estándar = {notas.calcular_desviacion():.2f}")
        self.mayor.config(text=f"Nota mayor = {notas.calcular_mayor()}")
        self.menor.config(text=f"Nota menor = {notas.calcular_menor()}")

    # evento del boton Limpiar
    def limpiar(self):
        for campo in self.campos:
            campo.delete(0, tk.END)
        self.promedio.config(text="Promedio = ")
        self.desviacion.config(text="Desviación estándar = ")
        self.mayor.config(text="Nota mayor = ")
        self.menor.config(text="Nota menor = ")

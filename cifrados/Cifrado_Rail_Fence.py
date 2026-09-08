import tkinter as tk
from tkinter import messagebox

def AbrirCifradoRailFence(parent):
    ventana = tk.Toplevel(parent)
    ventana.title("Cifrado Rail Fence")
    ventana.geometry("300x150")

    def cifrar():
        try:
            NumeroRieles = int(NumeroDeRieles.get())
        except ValueError:
            messagebox.showerror("Error", "Debe ingresar un numero entero para los rieles.", parent=ventana)
            return

        if NumeroRieles <= 1:
            messagebox.showerror("Error", "El numero de rieles debe ser mayor a 1.", parent=ventana)
            return

        TextoACifrar = TextoACifrarTK.get().upper().replace(" ", "")

        rieles = ["" for _ in range(NumeroRieles)]
        RielActual = 0
        direccion = 1 

        for letra in TextoACifrar:
            rieles[RielActual] += letra
            
            if RielActual == 0:
                direccion = 1
            elif RielActual == NumeroRieles - 1:
                direccion = -1

            RielActual += direccion

        TextoCifrado = "".join(rieles)
        
        messagebox.showinfo("Resultado", "Texto cifrado: " + TextoCifrado, parent=ventana)

    tk.Label(ventana, text="Numero de rieles:").pack()
    NumeroDeRieles = tk.Entry(ventana)
    NumeroDeRieles.pack()

    tk.Label(ventana, text="Texto a cifrar:").pack()
    TextoACifrarTK = tk.Entry(ventana)
    TextoACifrarTK.pack()

    tk.Button(ventana, text="Cifrar", command=cifrar).pack(pady=20)
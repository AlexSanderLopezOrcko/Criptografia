import tkinter as tk
from tkinter import messagebox

def AbrirCifradoRailFence(parent):
    ventana = tk.Toplevel(parent)
    ventana.title("Rail Fence")
    ventana.geometry("320x180")
    ventana.transient(parent)
    ventana.grab_set()

    def obtener_datos():
        try:
            rieles = int(NumeroDeRieles.get())
        except ValueError:
            messagebox.showerror("Error", "Debe ingresar un número entero para los rieles.", parent=ventana)
            return None, None

        if rieles <= 1:
            messagebox.showerror("Error", "El número de rieles debe ser mayor a 1.", parent=ventana)
            return None, None

        texto = TextoTK.get().upper().replace(" ", "")
        if not texto:
            messagebox.showerror("Error", "Debe ingresar un texto.", parent=ventana)
            return None, None

        if rieles >= len(texto):
            messagebox.showerror("Error", "El número de rieles debe ser menor a la longitud del texto.", parent=ventana)
            return None, None

        return rieles, texto

    def cifrar():
        NumeroRieles, TextoACifrar = obtener_datos()
        if NumeroRieles is None:
            return

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
        ventana.clipboard_clear()
        ventana.clipboard_append(TextoCifrado)
        messagebox.showinfo("Resultado", f"Texto cifrado: {TextoCifrado}", parent=ventana)

    def descifrar():
        NumeroRieles, TextoADescifrar = obtener_datos()
        if NumeroRieles is None:
            return

        patron = [["" for _ in range(len(TextoADescifrar))] for _ in range(NumeroRieles)]
        RielActual = 0
        direccion = 1

        for col in range(len(TextoADescifrar)):
            patron[RielActual][col] = "*"
            if RielActual == 0:
                direccion = 1
            elif RielActual == NumeroRieles - 1:
                direccion = -1
            RielActual += direccion

        idx = 0
        for r in range(NumeroRieles):
            for c in range(len(TextoADescifrar)):
                if patron[r][c] == "*" and idx < len(TextoADescifrar):
                    patron[r][c] = TextoADescifrar[idx]
                    idx += 1

        TextoDescifrado = []
        RielActual = 0
        direccion = 1
        for col in range(len(TextoADescifrar)):
            TextoDescifrado.append(patron[RielActual][col])
            if RielActual == 0:
                direccion = 1
            elif RielActual == NumeroRieles - 1:
                direccion = -1
            RielActual += direccion

        resultado = "".join(TextoDescifrado)
        ventana.clipboard_clear()
        ventana.clipboard_append(resultado)
        messagebox.showinfo("Resultado", f"Texto descifrado: {resultado}", parent=ventana)

    tk.Label(ventana, text="Número de rieles:").pack(pady=(5, 0))
    NumeroDeRieles = tk.Entry(ventana)
    NumeroDeRieles.pack()

    tk.Label(ventana, text="Texto:").pack(pady=(5, 0))
    TextoTK = tk.Entry(ventana)
    TextoTK.pack()

    frame_botones = tk.Frame(ventana)
    frame_botones.pack(pady=15)

    tk.Button(frame_botones, text="Cifrar", command=cifrar, width=10).pack(side=tk.LEFT, padx=5)
    tk.Button(frame_botones, text="Descifrar", command=descifrar, width=10).pack(side=tk.LEFT, padx=5)
import tkinter as tk
from tkinter import messagebox

def AbrirCifradoVigenere(parent):

    ventana = tk.Toplevel(parent)
    ventana.title("Cifrado Vigenere")
    ventana.geometry("300x180")

    def cifrar():
        TextoACifrar = TextoACifrarTK.get().upper().replace(" ", "")
        Clave = ClaveTK.get().upper().replace(" ", "")

        if Clave == "":
            messagebox.showerror(
                "Error",
                "Debe ingresar una clave.",
                parent=ventana
            )
            return

        TextoCifrado = ""

        for i in range(len(TextoACifrar)):
            LetraTexto = ord(TextoACifrar[i]) - ord("A")
            LetraClave = ord(Clave[i % len(Clave)]) - ord("A")

            NuevaLetra = (LetraTexto + LetraClave) % 26

            TextoCifrado += chr(NuevaLetra + ord("A"))

        messagebox.showinfo(
            "Resultado",
            "Texto cifrado: " + TextoCifrado,
            parent=ventana
        )

    tk.Label(ventana, text="Texto a cifrar:").pack(pady=5)
    TextoACifrarTK = tk.Entry(ventana)
    TextoACifrarTK.pack()

    tk.Label(ventana, text="Clave:").pack(pady=5)
    ClaveTK = tk.Entry(ventana)
    ClaveTK.pack()

    tk.Button(
        ventana,
        text="Cifrar",
        command=cifrar
    ).pack(pady=15)

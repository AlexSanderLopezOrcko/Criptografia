import tkinter as tk
from tkinter import messagebox

def AbrirCifradoVigenere(parent):
    ventana = tk.Toplevel(parent)
    ventana.title("Vigenère")
    ventana.geometry("320x190")
    ventana.transient(parent)
    ventana.grab_set()

    def obtener_datos():
        texto = TextoTK.get().upper().replace(" ", "")
        clave = ClaveTK.get().upper().replace(" ", "")

        if not texto:
            messagebox.showerror("Error", "Debe ingresar un texto.", parent=ventana)
            return None, None

        if not clave:
            messagebox.showerror("Error", "Debe ingresar una clave.", parent=ventana)
            return None, None

        if not (texto.isalpha() and all("A" <= c <= "Z" for c in texto)):
            messagebox.showerror("Error", "El texto debe contener solo letras estándar (A-Z, sin tildes ni Ñ).", parent=ventana)
            return None, None

        if not (clave.isalpha() and all("A" <= c <= "Z" for c in clave)):
            messagebox.showerror("Error", "La clave debe contener solo letras estándar (A-Z, sin tildes ni Ñ).", parent=ventana)
            return None, None

        return texto, clave

    def cifrar():
        TextoACifrar, Clave = obtener_datos()
        if TextoACifrar is None:
            return

        TextoCifrado = ""
        for i in range(len(TextoACifrar)):
            LetraTexto = ord(TextoACifrar[i]) - ord("A")
            LetraClave = ord(Clave[i % len(Clave)]) - ord("A")
            NuevaLetra = (LetraTexto + LetraClave) % 26
            TextoCifrado += chr(NuevaLetra + ord("A"))

        ventana.clipboard_clear()
        ventana.clipboard_append(TextoCifrado)
        messagebox.showinfo("Resultado", f"Texto cifrado: {TextoCifrado}", parent=ventana)

    def descifrar():
        TextoADescifrar, Clave = obtener_datos()
        if TextoADescifrar is None:
            return

        TextoDescifrado = ""
        for i in range(len(TextoADescifrar)):
            LetraTexto = ord(TextoADescifrar[i]) - ord("A")
            LetraClave = ord(Clave[i % len(Clave)]) - ord("A")
            NuevaLetra = (LetraTexto - LetraClave) % 26
            TextoDescifrado += chr(NuevaLetra + ord("A"))

        ventana.clipboard_clear()
        ventana.clipboard_append(TextoDescifrado)
        messagebox.showinfo("Resultado", f"Texto descifrado: {TextoDescifrado}", parent=ventana)

    tk.Label(ventana, text="Texto:").pack(pady=(5, 0))
    TextoTK = tk.Entry(ventana)
    TextoTK.pack()

    tk.Label(ventana, text="Clave:").pack(pady=(5, 0))
    ClaveTK = tk.Entry(ventana)
    ClaveTK.pack()

    frame_botones = tk.Frame(ventana)
    frame_botones.pack(pady=15)

    tk.Button(frame_botones, text="Cifrar", command=cifrar, width=10).pack(side=tk.LEFT, padx=5)
    tk.Button(frame_botones, text="Descifrar", command=descifrar, width=10).pack(side=tk.LEFT, padx=5)

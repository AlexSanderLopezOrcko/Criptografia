import tkinter as tk
from cifrados.Cifrado_Rail_Fence import AbrirCifradoRailFence
from cifrados.Cifrado_Vigenere import AbrirCifradoVigenere

ventaprincipal = tk.Tk()
ventaprincipal.title("Menú Principal")
ventaprincipal.geometry("300x230")

tk.Label(ventaprincipal, text="Menú de Cifrados", font=("Arial", 14)).pack(pady=15)

tk.Button(
    ventaprincipal, 
    text="1. Cifrado Rail Fence", 
    command=lambda: AbrirCifradoRailFence(ventaprincipal),
    width=20
).pack(pady=5)

tk.Button(
    ventaprincipal, 
    text="2. Cifrado Vigenère", 
    command=lambda: AbrirCifradoVigenere(ventaprincipal),
    width=20
).pack(pady=5)

tk.Button(
    ventaprincipal, 
    text="Salir", 
    command=ventaprincipal.quit,
    width=20
).pack(pady=15)

ventaprincipal.mainloop()

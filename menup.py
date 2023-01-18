import tkinter as tk
from tkinter import *
from tkinter import messagebox as MessageBox
from tkinter import ttk
# Configuración de la raíz
root = tk.Tk()
root.config(width=800, height=200)
img_boton = tk.PhotoImage(file="interfas_usuario/iconos/eliminar.png",width=30, height=30)
boton = ttk.Button(text="Buscar archivo", image=img_boton, compound=tk.RIGHT)
boton.place(x=50, y=50)
# Finalmente bucle de la aplicación
root.mainloop()
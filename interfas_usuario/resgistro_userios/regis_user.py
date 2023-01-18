import tkinter as tk
from tkinter import *
from tkinter import messagebox as MessageBox


from  comnexion import *

ventana = tk.Tk()
ventana.title("Ventana de registro de usuarios")
ventana.config(bg='#202020')
ventana.geometry("440x300+390+290")
# icono de la ventana
icon = tk.PhotoImage(file="../iconos/logot2.png")
ventana.iconphoto(True, icon)

db = DataBase()
modificar = False
 # esta enlazodo con labers y entri dni
nombres = StringVar()
contra = StringVar()
# menu
menubar = Menu(ventana)
ventana.config(menu=menubar)
# lista de opciones
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Nuevo")
filemenu.add_command(label="Abrir")
filemenu.add_command(label="Guardar")
filemenu.add_command(label="Cerrar")
filemenu.add_separator()
filemenu.add_command(label="Salir", command=lambda: salir())

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Cortar")
editmenu.add_command(label="Copiar")
editmenu.add_command(label="Pegar")

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Ayuda")
helpmenu.add_separator()
helpmenu.add_command(label="Acerca de...", command=lambda: info())
# sub-Menu
menubar.add_cascade(label="Archivo", menu=filemenu)
menubar.add_cascade(label="Editar", menu=editmenu)
menubar.add_cascade(label="Ayuda", menu=helpmenu)

marco = LabelFrame(ventana, text="Formulario de registro de usuario", fg="white", font=('Arial', 10, 'bold'))
marco.config(bg='#202020')
marco.place(x=30, y=30, width=400, height=250)

# Labers y entrys


lblNombres = Label(marco, text="Nombres de Usuario:", fg="white", bg="#202020", font=('Arial', 10, 'bold')).grid(
    column=5, row=0, padx=5, pady=5)
txtNombres = Entry(marco, textvariable=nombres, bg="#202020", fg="white", highlightbackground="black",
                   highlightcolor="#77dd77", highlightthickness=2, width=29)
txtNombres.grid(column=6, row=0)

lblcontra = Label(marco, text="Contraseña:", fg="white", bg="#202020", font=('Arial', 10, 'bold')).grid(column=5,
                                                                                                          row=1, padx=5,
                                                                                                          pady=5)
txtcontra = Entry(marco, textvariable=contra, bg="#202020", fg="white", highlightbackground="black",
                     highlightcolor="#77dd77", highlightthickness=2, width=29)
txtcontra.grid(column=6, row=1)



# boton de guardar
img_boton2 = tk.PhotoImage(file="../iconos/guadar.png", width=30, height=25)
btnNuevo = Button(marco, text="Guardar ", image=img_boton2, compound=tk.RIGHT, activebackground='#bdbfbf', bg='#202020',
                  fg='white',
                  font=('Arial', 10, 'bold'), command=lambda: nuevo())
btnNuevo.grid(column=6, row=5)

# Funciones del menu
def info():
    MessageBox.showinfo("Información del programa!", "Versión beta 0.0.3")
    #mese.config(bg='pink', font=('times', 16, 'italic'))
def salir():
    resultado = MessageBox.askquestion("Salir","¿Está seguro que desea salir de esta ventana?")
    if resultado == "yes":
        ventana.quit()

def validar():
    return len(nombres.get()) and len(contra.get())
def limpiar():
    nombres.set("")
    contra.set("")

def nuevo():
    resultado = MessageBox.askquestion("Alerta!", "¿Está seguro que desea registra este usuario?")
    if resultado == "yes":
        if validar():
            val = (nombres.get(), contra.get(), "A")
            sql = "insert into usuario (nombre_user, pass_user, estado) values(%s,%s,%s)"
            db.cursor.execute(sql, val)
            db.miconexion.commit()
            limpiar()
            MessageBox.showinfo("Alerta!", "Se a registrado correctamente el usuario")
        else:
            MessageBox.showwarning("Alerta!", "Los campos no deben estar vacíos")


ventana.mainloop()

import pickle

import tkinter as tk
from tkinter import *
from tkinter import messagebox as MessageBox

ventana = tk.Tk()
ventana.title("Ventana de registro de usuarios")
ventana.config(bg='#202020')
ventana.geometry("440x300+390+290")
# icono de la ventana

modificar = False
# esta enlazodo con labers y entri dni
ipserver1 = StringVar()
ipserver2 = StringVar()
ipserver3 = StringVar()
ipserver4 = StringVar()
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

variable = pickle.load(open("variabledatos.dat", "rb"))
print(variable)



marco = LabelFrame(ventana, text="Ip del programa", fg="white", font=('Arial', 10, 'bold'))
marco.config(bg='#202020')
marco.place(x=20, y=10, width=400, height=250)

lblMensaje = Label(ventana, text="Ultima ip guardada: "+variable, fg="black", font=('Lucida Sans', 10, 'bold'))
lblMensaje.grid(column=9, row=7, padx=80, pady=62)
# Labers y entrys

lblIp1 = Label(marco, text="", fg="white", bg="#202020", font=('Arial', 10, 'bold')).grid(
    column=5, row=2, padx=27, pady=27)

lblIp1 = Label(marco, text="IP servidor:", fg="white", bg="#202020", font=('Arial', 10, 'bold')).grid(
    column=5, row=4, padx=0, pady=2)
txtIp1 = Entry(marco, textvariable=ipserver1, bg="#202020", fg="white", highlightbackground="black",
               highlightcolor="#77dd77", highlightthickness=2, width=3, font=('Arial', 12, 'bold'))
txtIp1.grid(column=6, row=4)

lblIp1 = Label(marco, text=".", fg="white", bg="#202020", font=('Arial', 10, 'bold')).grid(
    column=7, row=4)
txtIp2 = Entry(marco, textvariable=ipserver2, bg="#202020", fg="white", highlightbackground="black",
               highlightcolor="#77dd77", highlightthickness=2, width=3, font=('Arial', 12, 'bold'))
txtIp2.grid(column=8, row=4)

lblIp1 = Label(marco, text=".", fg="white", bg="#202020", font=('Arial', 10, 'bold')).grid(
    column=9, row=4, padx=2, pady=2)

txtIp3 = Entry(marco, textvariable=ipserver3, bg="#202020", fg="white", highlightbackground="black",
               highlightcolor="#77dd77", highlightthickness=2, width=3, font=('Arial', 12, 'bold'))
txtIp3.grid(column=10, row=4)

lblIp1 = Label(marco, text=".", fg="white", bg="#202020", font=('Arial', 10, 'bold')).grid(
    column=11, row=4, padx=2, pady=2)

txtIp4 = Entry(marco, textvariable=ipserver4, bg="#202020", fg="white", highlightbackground="black",
               highlightcolor="#77dd77", highlightthickness=2, width=3, font=('Arial', 12, 'bold'))
txtIp4.grid(column=12, row=4)

# variable = pickle.load(open("variableStoringFile.dat", "rb"))
# print(variable)


# boton de guardar

btnNuevo = Button(marco, text="Guardar ", compound=tk.RIGHT, activebackground='#bdbfbf', bg='#202020',
                  fg='white',
                  font=('Arial', 10, 'bold'), command=lambda: nuevo())
btnNuevo.grid(column=13, row=4, padx=30)


# Funciones del menu
def info():
    MessageBox.showinfo("Información del programa!", "Versión beta 0.0.3")
    # mese.config(bg='pink', font=('times', 16, 'italic'))


def salir():
    resultado = MessageBox.askquestion("Salir", "¿Está seguro que desea salir de esta ventana?")
    if resultado == "yes":
        ventana.quit()


def validar():
    return len(ipserver1.get()) and len(ipserver2.get())


def limpiar():
    ipserver1.set("")
    ipserver2.set("")


def character_limit(ipserver1):
    if len(ipserver1.get()) > 0:
        ipserver1.set(ipserver1.get()[:3])


ipserver1.trace("w", lambda *args: character_limit(ipserver1))
ipserver2.trace("w", lambda *args: character_limit(ipserver2))
ipserver3.trace("w", lambda *args: character_limit(ipserver3))
ipserver4.trace("w", lambda *args: character_limit(ipserver4))

def nuevo():
    # resultado = MessageBox.askquestion("Alerta!", "¿Está seguro que desea registra este usuario?")
    # if resultado == "yes":
    # if validar():
    direccionip = ipserver1.get() + "." + ipserver2.get() + "." + ipserver3.get() + "." + ipserver4.get()
    # varible = ipserver2.get()
    print(direccionip)
    # sql = "insert into usuario (nombre_user, pass_user, estado) values(%s,%s,%s)"
    # db.cursor.execute(sql, val)
    # db.miconexion.commit()
    # limpiar()
    # Load the variable
    pickle.dump(direccionip, open("variabledatos.dat", "wb"))
    # print(nombres.get())




#lblipat = Label(marco, text="IP ACUTAL: "+variable, fg="white", bg="#202020", font=('Arial', 10, 'bold')).grid(
#    column=8, row=5, padx=10, pady=10)

ventana.mainloop()

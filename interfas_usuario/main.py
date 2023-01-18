import tkinter as tk
from tkinter import *
from tkinter import messagebox as MessageBox
from tkinter import ttk
import os
from comnexion import *

ventana = tk.Tk()
ventana.title("Ventana de usurios")
ventana.config(bg='#202020')
ventana.geometry("800x600")



# ícono de la ventana.
icono = tk.PhotoImage(file="iconos/logot2.png")
ventana.iconphoto(True, icono)

db = DataBase()  # intacia de la conexion de la base de datos
modificar = False
dni = StringVar()  # esta enlazodo con labers y entri dni
sexo = StringVar()
nombres = StringVar()
apellidos = StringVar()

#menu
menubar = Menu(ventana)
ventana.config(menu=menubar)
#lista de opciones
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Nuevo")
filemenu.add_command(label="Abrir")
filemenu.add_command(label="Guardar")
filemenu.add_command(label="Cerrar")
filemenu.add_separator()
filemenu.add_command(label="Salir", command=lambda: salir() )

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Cortar")
editmenu.add_command(label="Copiar")
editmenu.add_command(label="Pegar")

usermenu = Menu(menubar, tearoff=0)
usermenu.add_command(label="Registro Usuario", command=lambda: ven_regis_user())

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Ayuda")
helpmenu.add_separator()
helpmenu.add_command(label="Acerca de...", command=lambda: info() )
#sub-Menu
menubar.add_cascade(label="Archivo", menu=filemenu)
menubar.add_cascade(label="Editar", menu=editmenu)
menubar.add_cascade(label="Usurio", menu=usermenu)
menubar.add_cascade(label="Ayuda", menu=helpmenu)

def ven_regis_user():
    os.system("resgistro_userios\\regis_user.py")
# funicon de seleconar estudiantes para modificar
def seleccionarClik(event):
    id = tvEstudiantes.selection()[0]
    print(id)
    if int(id) > 0:
        dni.set(tvEstudiantes.item(id, "values")[1])
        sexo.set(tvEstudiantes.item(id, "values")[2])
        nombres.set(tvEstudiantes.item(id, "values")[3])
        apellidos.set(tvEstudiantes.item(id, "values")[4])


marco = LabelFrame(ventana, text="Formulario de gestion de Estudiantes", fg="white")
marco.config(bg='#202020')
marco.place(x=60, y=60, width=650, height=450)

# Labers y entrys
lblDni = Label(marco, text="DNI:", fg="white", bg="#202020").grid(column=2, row=0, padx=5, pady=5)
txtDni = Entry(marco, textvariable=dni, bg="#202020", fg="white", highlightbackground="black", highlightcolor="#77dd77",
               highlightthickness=2, width=23)
txtDni.grid(column=3, row=0)

lblSexo = Label(marco, text="Sexo:", fg="white", bg="#202020").grid(column=2, row=1, padx=5, pady=5)
txtSexo = ttk.Combobox(marco, values=["M", "F"], textvariable=sexo, width=23)
txtSexo.grid(column=3, row=1)
txtSexo.current(0)

# color del combobox de sexo de estudiantes
style = ttk.Style()
style.theme_use('clam')
style.configure("TCombobox", fieldbackground="white" )

lblNombres = Label(marco, text="Nombres:", fg="white", bg="#202020").grid(column=5, row=0, padx=5, pady=5)
txtNombres = Entry(marco, textvariable=nombres, bg="#202020", fg="white", highlightbackground="black",
                   highlightcolor="#77dd77", highlightthickness=2, width=29)
txtNombres.grid(column=6, row=0)

lblapellidos = Label(marco, text="Apellidos:", fg="white", bg="#202020").grid(column=5, row=1, padx=5, pady=5)
txtapellidos = Entry(marco, textvariable=apellidos, bg="#202020", fg="white", highlightbackground="black",
                     highlightcolor="#77dd77", highlightthickness=2, width=29)
txtapellidos.grid(column=6, row=1)

lblMensaje = Label(marco, text="Aqui van los mensajes", fg="green", font=('Lucida Sans', 10, 'bold'))
lblMensaje.grid(column=3, row=2, columnspan=4)

# Tema de treeview de las tablas de los estudiates
style = ttk.Style(ventana)
style.theme_use("clam")
style.configure("Treeview", background="#202020", fieldbackground="#202020", foreground="white")

# Tabla de la lisa de estuadiantes
tvEstudiantes = ttk.Treeview(marco, selectmode=NONE)
tvEstudiantes.grid(column=3, row=3, columnspan=4, padx=5)
tvEstudiantes["columns"] = ("ID", "DNI", "SEXO", "NOMBRES", "APELLIDOS",)
tvEstudiantes.column("#0", width=0, stretch=NO)
tvEstudiantes.column("ID", width=50, anchor=CENTER)
tvEstudiantes.column("DNI", width=90, anchor=CENTER)
tvEstudiantes.column("SEXO", width=90, anchor=CENTER)
tvEstudiantes.column("NOMBRES", width=160, anchor=CENTER)
tvEstudiantes.column("APELLIDOS", width=160, anchor=CENTER)
tvEstudiantes.heading("#0", text="")
tvEstudiantes.heading("ID", text="ID", anchor=CENTER)
tvEstudiantes.heading("DNI", text="DNI", anchor=CENTER)
tvEstudiantes.heading("SEXO", text="SEXO", anchor=CENTER)
tvEstudiantes.heading("NOMBRES", text="NOMBRES", anchor=CENTER)
tvEstudiantes.heading("APELLIDOS", text="APELLIDOS", anchor=CENTER)
tvEstudiantes.bind("<<TreeviewSelect>>", seleccionarClik, )
# Botones de accionn

#btnEliminar = Button(marco, text="Eliminar", activebackground='#bdbfbf', bg='#202020', fg='white',
                     #font=('Arial', 10, 'bold'), command=lambda: eliminar())
#btnEliminar.grid(column=3, row=4)

#icono de los botones de accion del programa
img_boton = tk.PhotoImage(file="iconos/eliminar.png",width=20, height=20)

btnEliminar = Button(marco, text="Eliminar ",image=img_boton, compound=tk.RIGHT, activebackground='#bdbfbf', bg='#202020', fg='white',
                      font=('Arial', 10, 'bold'), command=lambda: eliminar2())
btnEliminar.grid(column=3, row=4)

img_boton2 = tk.PhotoImage(file="iconos/guadar.png",width=20, height=20)
btnNuevo = Button(marco, text="Guardar ",image=img_boton2,compound=tk.RIGHT, activebackground='#bdbfbf', bg='#202020', fg='white',
                  font=('Arial', 10, 'bold'), command=lambda: nuevo())
btnNuevo.grid(column=5, row=4)

img_boton3 = tk.PhotoImage(file="iconos/seleccionar.png",width=20, height=20)
btnModificar = Button(marco, text="Seleccionar ",image=img_boton3,compound=tk.RIGHT, activebackground='#bdbfbf', bg='#202020', fg='white',
                      font=('Arial', 10, 'bold'), command=lambda: actualizar())
btnModificar.grid(column=6, row=4)



# Funciones del menu
def info():
    MessageBox.showinfo("Información del programa!", "Versión beta 0.0.3")
    #mese.config(bg='pink', font=('times', 16, 'italic'))
def salir():
    resultado = MessageBox.askquestion("Salir","¿Está seguro que desea salir de esta ventana?")
    if resultado == "yes":
        ventana.quit()

#funciones de los botones
def modificarFalse():
    global modificar
    modificar = False
    tvEstudiantes.config(selectmode=NONE)
    btnNuevo.config(text="Guardar")
    btnModificar.config(text="Seleccionar")
    btnEliminar.config(state=DISABLED)
    print("hola mundo")


def modificarTrue():
    global modificar
    modificar = True

    tvEstudiantes.config(selectmode=BROWSE)
    btnModificar.config(text="Modificar")
    btnNuevo.config(text="Nuevo")
    btnEliminar.config(state=NORMAL)
    print("adios mundo")


def validar():
    return len(dni.get()) and len(nombres.get()) and len(apellidos.get())


def limpiar():
    dni.set("")
    nombres.set("")
    apellidos.set("")


def vaciar_tabla():
    filas = tvEstudiantes.get_children()
    for fila in filas:
        tvEstudiantes.delete(fila)


def llenar_tabla():
    vaciar_tabla()
    sql = "SELECT * FROM estudiantes WHERE estado='A'"
    db.cursor.execute(sql)
    filas = db.cursor.fetchall()
    for fila in filas:
        id = fila[0]
        tvEstudiantes.insert("", END, id, text=id, values=fila)


#def eliminar():
    #id = tvEstudiantes.selection()[0]
    #if int(id) > 0:
        #sql = "delete from estudiantes where id=" + id
        #db.cursor.execute(sql)
        #db.miconexion.commit()
        #tvEstudiantes.delete(id)
        #lblMensaje.config(text="Se a eliminado el registro correctamente")
    #else:
        #lblMensaje.config(text="Selecione un registro para eliminar")


# en elimanar hay un error cuando ledas al botos eliminar y no has selecionada nada no aparece el mensaje


def nuevo():
    if modificar == False:
        if validar():
            val = (dni.get(), sexo.get(), nombres.get(), apellidos.get(), "A")
            sql = "insert into estudiantes (dni, sexo, nombre, apellido, estado) values(%s,%s,%s,%s,%s)"
            db.cursor.execute(sql, val)
            db.miconexion.commit()
            lblMensaje.config(text="Se a guardo un registro correctamente", fg="green")
            llenar_tabla()
            limpiar()
        else:
            lblMensaje.config(text="Los campos no deben esta vacíos", fg="red")
    else:
        modificarFalse()
        limpiar()


def actualizar():
    if modificar == True:
        if validar():
            id = tvEstudiantes.selection()[0]
            val = (dni.get(), sexo.get(), nombres.get(), apellidos.get())
            sql = "update estudiantes set dni=%s, sexo=%s, nombre=%s, apellido=%s where id=" + id
            db.cursor.execute(sql, val)
            db.miconexion.commit()
            lblMensaje.config(text="Se a actualizado un registro correctamente", fg="green")
            llenar_tabla()
            limpiar()
        else:
            lblMensaje.config(text="Los campos no deben estar vacíos", fg="red")
    else:
        modificarTrue()


def eliminar2():
    id = tvEstudiantes.selection()[0]
    resultado = MessageBox.askquestion("Eliminar", "¿Está seguro que desea Eliminar este Estudiante?")
    if resultado == "yes":
        if int(id) > 0:
            # val = ('I')
            # print(val)
            sql = "update estudiantes set estado='I' where id=" + id
            db.cursor.execute(sql)
            db.miconexion.commit()
            lblMensaje.config(text="Se a eliminado el registro correctamente")
            llenar_tabla()
        else:
            lblMensaje.config(text="Seleccione un registro para eliminar")


llenar_tabla()
ventana.mainloop()

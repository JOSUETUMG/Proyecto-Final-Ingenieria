from tkinter import Tk, Label, Button, Entry, messagebox, ttk, Canvas
from tkinter import PhotoImage
import os
import algoritmo_archivos.base_datos as base_datos
import algoritmo
import sqlite3

#Ventana principal
def ventana_clientes():
    ventana_clientes = Tk()
    ventana_clientes.title("Clientes")
    ventana_clientes.geometry("1100x700+100+0")
    ventana_clientes.resizable(False, False)

    #Canvas de fondo con degradado
    canvas_bg = Canvas(ventana_clientes, width=1100, height=700)
    canvas_bg.pack(fill="both", expand=True)

    #Crear el degradado
    for i in range(700):
        ratio = i / 700
        color = '#%02x%02x%02x' % (
            int(45 + ratio * (149 - 45)),
            int(106 + ratio * (213 - 106)),
            int(79 + ratio * (178 - 79))
        )
        canvas_bg.create_rectangle(0, i, 1100, i + 1, fill=color, outline=color)

    #Frame para los campos de entrada
    frame_campos = ttk.Frame(ventana_clientes, padding="10")
    frame_campos.place(x=415, y=40)
    
    #Campos de entrada para la informacion del cliente
    Label(frame_campos, text="Código:", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=5, sticky="e")
    codigo_entry = Entry(frame_campos)
    codigo_entry.grid(row=0, column=1, padx=10, pady=5)
    Label(frame_campos, text="Nombre:", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=5, sticky="e")
    nombre_entry = Entry(frame_campos)
    nombre_entry.grid(row=1, column=1, padx=10, pady=5)
    Label(frame_campos, text="Dirección:", font=("Arial", 12)).grid(row=2, column=0, padx=10, pady=5, sticky="e")
    direccion_entry = Entry(frame_campos)
    direccion_entry.grid(row=2, column=1, padx=10, pady=5)
    
    #Frame para los botones de acciones
    frame_botones = ttk.Frame(ventana_clientes, padding="10")
    frame_botones.place(x=295, y=185)
    
    #Boton para agregar cliente
    ruta_imagen1 = os.path.join("algoritmo_archivos", "iconos", "agregar.png")
    agregar_img = PhotoImage(file=ruta_imagen1)
    boton_agregar = Button(frame_botones, text=" Agregar Cliente", command=lambda: agregar_cliente(codigo_entry, nombre_entry, direccion_entry, tree))
    boton_agregar.config(bg="#FEFBEA", bd=10, relief="raised", font=("Helvetica", 9, "bold"), image=agregar_img, compound="left")
    boton_agregar.grid(row=0, column=0, padx=10, pady=10)
    
    #Boton para actualizar cliente
    ruta_imagen2 = os.path.join("algoritmo_archivos", "iconos", "actualizar.png")
    actualizar_img = PhotoImage(file=ruta_imagen2)
    boton_actualizar = Button(frame_botones, text=" Actualizar Cliente", command=lambda: actualizar_cliente(codigo_entry, nombre_entry, direccion_entry, tree))
    boton_actualizar.config(bg="#FEFBEA", bd=10, relief="raised", font=("Helvetica", 9, "bold"), image=actualizar_img, compound="left")
    boton_actualizar.grid(row=0, column=1, padx=10, pady=10)
    
    #Boton para eliminar cliente
    ruta_imagen3 = os.path.join("algoritmo_archivos", "iconos", "eliminar.png")
    eliminar_img = PhotoImage(file=ruta_imagen3)
    boton_eliminar = Button(frame_botones, text="Eliminar Cliente", command=lambda: eliminar_cliente(tree))
    boton_eliminar.config(bg="#FEFBEA", bd=10, relief="raised", font=("Helvetica", 9, "bold"), image=eliminar_img, compound="left")
    boton_eliminar.grid(row=0, column=2, padx=10, pady=10)
    
    #Tabla para mostrar los clientes
    columns = ("codigo", "nombre", "direccion")
    tree = ttk.Treeview(ventana_clientes, columns=columns, show="headings")
    tree.heading("codigo", text="Código")
    tree.heading("nombre", text="Nombre")
    tree.heading("direccion", text="Dirección")
    tree.column("codigo", anchor="center", width=100)
    tree.column("nombre", anchor="center", width=150)
    tree.column("direccion", anchor="center", width=200)
    tree.place(x=250, y=290, width=600, height=300)
    
    #Funcion para cargar datos desde la base de datos
    def cargar_datos():
        for row in base_datos.listar_clientes_bd():
            tree.insert("", "end", values=row)
    cargar_datos()

    #Boton para regresar
    def regresar_algoritmo():
        ventana_clientes.destroy()
        algoritmo.abrir_ventana()
    ruta_imagen4 = os.path.join("algoritmo_archivos", "iconos", "regresar_24.png")
    regresar_img = PhotoImage(file=ruta_imagen4)
    boton_regresar = Button(ventana_clientes, text="  REGRESAR", command=regresar_algoritmo)
    boton_regresar.config(bg="#FEFBEA", bd=10, relief="raised", font=("Helvetica", 9, "bold"), image=regresar_img, compound="left")
    boton_regresar.place(x=50, y=600)
    
    ventana_clientes.mainloop()

#Funcion para agregar cliente
def agregar_cliente(codigo_entry, nombre_entry, direccion_entry, tree):
    codigo = codigo_entry.get()
    nombre = nombre_entry.get()
    direccion = direccion_entry.get()

    if not codigo or not nombre or not direccion:
        messagebox.showwarning("Advertencia", "Por favor, complete todos los campos")
        return

    try:
        base_datos.agregar_cliente_bd(codigo, nombre, direccion)
        tree.insert("", "end", values=(codigo, nombre, direccion))
        messagebox.showinfo("Éxito", "Cliente agregado exitosamente")
        codigo_entry.delete(0, 'end')
        nombre_entry.delete(0, 'end')
        direccion_entry.delete(0, 'end')
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "El código del cliente ya existe")

#Funcion para actualizar cliente
def actualizar_cliente(codigo_entry, nombre_entry, direccion_entry, tree):
    selected_item = tree.selection()
    if selected_item:
        item = tree.item(selected_item)
        codigo = codigo_entry.get()
        nombre = nombre_entry.get()
        direccion = direccion_entry.get()

        if not codigo or not nombre or not direccion:
            messagebox.showwarning("Advertencia", "Por favor, complete todos los campos")
            return

        try:
            base_datos.actualizar_cliente_bd(codigo, nombre, direccion)
            tree.item(selected_item, values=(codigo, nombre, direccion))
            messagebox.showinfo("Éxito", "Cliente actualizado exitosamente")
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "No se pudo actualizar el cliente")

#Funcion para eliminar cliente
def eliminar_cliente(tree):
    selected_item = tree.selection()
    if selected_item:
        item = tree.item(selected_item)
        codigo = item['values'][0]
        respuesta = messagebox.askyesno("Confirmación", "¿Estás seguro de que deseas eliminar este cliente?")
        if respuesta:
            base_datos.eliminar_cliente_bd(codigo)
            tree.delete(selected_item)
            messagebox.showinfo("Éxito", "Cliente eliminado exitosamente")
        else:
            messagebox.showinfo("Cancelado", "Eliminación cancelada")
    else:
        messagebox.showwarning("Advertencia", "Por favor, seleccione un cliente para eliminar")


#Bloqueo para la pantalla principal
if __name__ == "__main__":
    ventana_clientes()

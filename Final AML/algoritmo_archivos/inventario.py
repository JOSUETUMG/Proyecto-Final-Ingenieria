from tkinter import Tk, Label, Button, Entry, messagebox, ttk, Canvas
from tkinter import PhotoImage
import os
import algoritmo
import sqlite3

#Conexion a la base de datos
conn = sqlite3.connect('ventas.db')
c = conn.cursor()

#Crear lista de productos
c.execute('''CREATE TABLE IF NOT EXISTS productos
             (codigo TEXT PRIMARY KEY, nombre TEXT, existencia INTEGER, proveedor TEXT, precio REAL)''')

conn.commit()

#Ventana principal
def ventana_inventario():
    ventana_inventario = Tk()
    ventana_inventario.title("Inventario")
    ventana_inventario.geometry("1100x700+100+0")
    ventana_inventario.resizable(False, False)
    
    canvas_bg = Canvas(ventana_inventario, width=1100, height=700)
    canvas_bg.pack(fill="both", expand=True)

    # Crear el degradado
    for i in range(700):
        ratio = i / 700
        color = '#%02x%02x%02x' % (
            int(45 + ratio * (149 - 45)),
            int(106 + ratio * (213 - 106)),
            int(79 + ratio * (178 - 79))
        )
        canvas_bg.create_rectangle(0, i, 1100, i + 1, fill=color, outline=color)

   

    #Frame para los campos de entrada
    frame_campos = ttk.Frame(ventana_inventario, padding="10")
    frame_campos.place(x=415, y=40)

    #Campos de entrada para la informacion del producto
    Label(frame_campos, text="Código:", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=5, sticky="e")
    codigo_entry = Entry(frame_campos)
    codigo_entry.grid(row=0, column=1, padx=10, pady=5)

    Label(frame_campos, text="Nombre:", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=5, sticky="e")
    nombre_entry = Entry(frame_campos)
    nombre_entry.grid(row=1, column=1, padx=10, pady=5)

    Label(frame_campos, text="Existencia:", font=("Arial", 12)).grid(row=2, column=0, padx=10, pady=5, sticky="e")
    existencia_entry = Entry(frame_campos)
    existencia_entry.grid(row=2, column=1, padx=10, pady=5)

    Label(frame_campos, text="Proveedor:", font=("Arial", 12)).grid(row=3, column=0, padx=10, pady=5, sticky="e")
    proveedor_entry = Entry(frame_campos)
    proveedor_entry.grid(row=3, column=1, padx=10, pady=5)

    Label(frame_campos, text="Precio:", font=("Arial", 12)).grid(row=4, column=0, padx=10, pady=5, sticky="e")
    precio_entry = Entry(frame_campos)
    precio_entry.grid(row=4, column=1, padx=10, pady=5)

    #Frame para los botones de acciones
    frame_botones = ttk.Frame(ventana_inventario, padding="10")
    frame_botones.place(x=260, y=250)

    #Boton para agregar producto
    ruta_imagen1 = os.path.join("algoritmo_archivos", "iconos", "agregar.png")
    agregar_img = PhotoImage(file=ruta_imagen1)
    boton_agregar = Button(frame_botones, text=" Agregar Producto", command=lambda: agregar_producto(codigo_entry, nombre_entry, existencia_entry, proveedor_entry, precio_entry, tree))
    boton_agregar.config(bg="#FEFBEA", bd=10, relief="raised", font=("Helvetica", 9, "bold"), image=agregar_img, compound="left")
    boton_agregar.grid(row=0, column=0, padx=10, pady=10)

    #Boton para actualizar producto
    ruta_imagen2 = os.path.join("algoritmo_archivos", "iconos", "actualizar.png")
    actualizar_img = PhotoImage(file=ruta_imagen2)
    boton_actualizar = Button(frame_botones, text=" Actualizar Producto", command=lambda: actualizar_producto(codigo_entry, nombre_entry, existencia_entry, proveedor_entry, precio_entry, tree))
    boton_actualizar.config(bg="#FEFBEA", bd=10, relief="raised", font=("Helvetica", 9, "bold"), image=actualizar_img, compound="left")
    boton_actualizar.grid(row=0, column=1, padx=10, pady=10)

    #Boton para eliminar producto
    ruta_imagen3 = os.path.join("algoritmo_archivos", "iconos", "eliminar.png")
    eliminar_img = PhotoImage(file=ruta_imagen3)
    boton_eliminar = Button(frame_botones, text=" Eliminar Producto", command=lambda: eliminar_producto(tree))
    boton_eliminar.config(bg="#FEFBEA", bd=10, relief="raised", font=("Helvetica", 9, "bold"), image=eliminar_img, compound="left")
    boton_eliminar.grid(row=0, column=2, padx=10, pady=10)

    #Tabla para mostrar los productos
    columns = ("codigo", "nombre", "existencia", "proveedor", "precio")
    tree = ttk.Treeview(ventana_inventario, columns=columns, show="headings")
    tree.heading("codigo", text="Código")
    tree.heading("nombre", text="Nombre")
    tree.heading("existencia", text="Existencia")
    tree.heading("proveedor", text="Proveedor")
    tree.heading("precio", text="Precio")
    tree.column("codigo", anchor="center", width=100)
    tree.column("nombre", anchor="center", width=150)
    tree.column("existencia", anchor="center", width=100)
    tree.column("proveedor", anchor="center", width=150)
    tree.column("precio", anchor="center", width=100)
    tree.place(x=250, y=360, width=600, height=300)

    #Funcion para cargar datos desde la base de datos
    def cargar_datos():
        for row in listar_productos_bd():
            tree.insert("", "end", values=row)

    cargar_datos()

    #Boton para regresar
    def regresar_algoritmo():
        ventana_inventario.destroy()
        algoritmo.abrir_ventana()

    ruta_imagen4 = os.path.join("algoritmo_archivos", "iconos", "regresar_24.png")
    regresar_img = PhotoImage(file=ruta_imagen4)
    boton_regresar = Button(ventana_inventario, text="  REGRESAR", command=regresar_algoritmo)
    boton_regresar.config(bg="#FEFBEA", bd=10, relief="raised", font=("Helvetica", 9, "bold"), image=regresar_img, compound="left")
    boton_regresar.place(x=50, y=600)

    ventana_inventario.mainloop()

#Funcion para agregar producto
def agregar_producto(codigo_entry, nombre_entry, existencia_entry, proveedor_entry, precio_entry, tree):
    codigo = codigo_entry.get()
    nombre = nombre_entry.get()
    existencia = existencia_entry.get()
    proveedor = proveedor_entry.get()
    precio = precio_entry.get()

    if not codigo or not nombre or not existencia or not proveedor or not precio:
        messagebox.showwarning("Advertencia", "Por favor, complete todos los campos")
        return

    try:
        existencia = int(existencia)
        precio = float(precio)
    except ValueError:
        messagebox.showwarning("Advertencia", "Existencia debe ser un número entero y Precio debe ser un número decimal")
        return

    try:
        agregar_producto_bd(codigo, nombre, existencia, proveedor, precio)
        tree.insert("", "end", values=(codigo, nombre, existencia, proveedor, f"Q.{precio:.2f}"))
        messagebox.showinfo("Éxito", "Producto agregado exitosamente")
        codigo_entry.delete(0, 'end')
        nombre_entry.delete(0, 'end')
        existencia_entry.delete(0, 'end')
        proveedor_entry.delete(0, 'end')
        precio_entry.delete(0, 'end')
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "El código del producto ya existe")

#Fuoncin para actualizar producto
def actualizar_producto(codigo_entry, nombre_entry, existencia_entry, proveedor_entry, precio_entry, tree):
    selected_item = tree.selection()
    if selected_item:
        item = tree.item(selected_item)
        codigo = codigo_entry.get()
        nombre = nombre_entry.get()
        existencia = existencia_entry.get()
        proveedor = proveedor_entry.get()
        precio = precio_entry.get()

        if not codigo or not nombre or not existencia or not proveedor or not precio:
            messagebox.showwarning("Advertencia", "Por favor, complete todos los campos")
            return

        try:
            existencia = int(existencia)
            precio = float(precio)
        except ValueError:
            messagebox.showwarning("Advertencia", "Existencia debe ser un número entero y Precio debe ser un número decimal")
            return

        actualizar_producto_bd(codigo, nombre, existencia, proveedor, precio)
        tree.item(selected_item, values=(codigo, nombre, existencia, proveedor, f"Q.{precio:.2f}"))
        messagebox.showinfo("Éxito", "Producto actualizado exitosamente")
    else:
        messagebox.showwarning("Advertencia", "Por favor, seleccione un producto para actualizar")

#Funcion para eliminar producto
def eliminar_producto(tree):
    selected_item = tree.selection()
    if selected_item:
        item = tree.item(selected_item)
        codigo = item['values'][0]
        respuesta = messagebox.askyesno("Confirmación", "¿Estás seguro de que deseas eliminar este producto?")
        if respuesta:
            eliminar_producto_bd(codigo)
            tree.delete(selected_item)
            messagebox.showinfo("Éxito", "Producto eliminado exitosamente")
        else:
            messagebox.showinfo("Cancelado", "Eliminación cancelada")
    else:
        messagebox.showwarning("Advertencia", "Por favor, seleccione un producto para eliminar")


#Funcion para listar productos desde la base de datos
def listar_productos_bd():
    c.execute("SELECT * FROM productos")
    return c.fetchall()

#Funcion para agregar producto a la base de datos
def agregar_producto_bd(codigo, nombre, existencia, proveedor, precio):
    c.execute("INSERT INTO productos VALUES (?, ?, ?, ?, ?)", (codigo, nombre, existencia, proveedor, precio))
    conn.commit()

#Funcion para actualizar producto en la base de datos
def actualizar_producto_bd(codigo, nombre, existencia, proveedor, precio):
    c.execute("UPDATE productos SET nombre=?, existencia=?, proveedor=?, precio=? WHERE codigo=?", (nombre, existencia, proveedor, precio, codigo))
    conn.commit()

#Funcion para eliminar producto de la base de datos
def eliminar_producto_bd(codigo):
    c.execute("DELETE FROM productos WHERE codigo=?", (codigo,))
    conn.commit()

#Bloqueo para la pantalla principal
if __name__ == "__main__":
    ventana_inventario()


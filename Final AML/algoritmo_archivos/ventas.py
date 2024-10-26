from tkinter import Tk, Label, Button, Entry, messagebox, ttk, simpledialog, Toplevel, Canvas
from tkinter import PhotoImage
import os
import algoritmo_archivos.base_datos as base_datos
import algoritmo
import sqlite3
import algoritmo_archivos.crear_venta as crear_venta
from datetime import datetime

#Ventana principal
def ventana_ventas():
    ventana_ventas = Tk()
    ventana_ventas.title("Ventas")
    ventana_ventas.geometry("1100x700+100+0")
    ventana_ventas.resizable(False, False)
    
    canvas_bg = Canvas(ventana_ventas, width=1100, height=700)
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
    frame_campos = ttk.Frame(ventana_ventas, padding="10")
    frame_campos.place(x=350, y=40)

    #Campos de entrada para la informacion de la venta
    Label(frame_campos, text="Código o Nombre de Producto:", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=5, sticky="e")
    producto_entry = Entry(frame_campos)
    producto_entry.grid(row=0, column=1, padx=10, pady=5)

    #Boton para buscar producto y mostrar informacion

    ruta_imagen1 = os.path.join("algoritmo_archivos", "iconos", "buscar.png")
    buscar_img = PhotoImage(file=ruta_imagen1)
    boton_buscar = Button(frame_campos, text=" Buscar Producto", command=lambda: buscar_producto(producto_entry, tree, stock_label))
    boton_buscar.config(bg="#FEFBEA", bd=10, relief="raised", font=("Helvetica", 12, "bold"), image=buscar_img, compound="left")
    boton_buscar.grid(row=1, column=0, columnspan=2, pady=10)

    #Label para mostrar el stock actual
    stock_label = Label(frame_campos, text="Stock: ", font=("Helvetica", 12, "bold"))
    stock_label.grid(row=2, column=0, columnspan=2, pady=10)




    #Tabla para mostrar las ventas
    columns = ("codigo_producto", "producto", "existencias", "precio_total")
    tree = ttk.Treeview(ventana_ventas, columns=columns, show="headings")
    tree.heading("codigo_producto", text="Código de Producto")
    tree.heading("producto", text="Producto")
    tree.heading("existencias", text="Existencias")
    tree.heading("precio_total", text="Precio Total")
    tree.column("codigo_producto", anchor="center", width=150)
    tree.column("producto", anchor="center", width=150)
    tree.column("existencias", anchor="center", width=100)
    tree.column("precio_total", anchor="center", width=100)
    tree.place(x=300, y=250)



    #Frame para los botones de acciones adicionales
    frame_botones_acciones = ttk.Frame(ventana_ventas, padding="10")
    frame_botones_acciones.place(x=280, y=500)

    #Boton para editar productos

    ruta_imagen2 = os.path.join("algoritmo_archivos", "iconos", "editar.png")
    editar_img = PhotoImage(file=ruta_imagen2)
    boton_editar = Button(frame_botones_acciones, text=" Editar Producto", command=lambda: editar_producto(tree))
    boton_editar.config(bg="#FEFBEA", bd=10, relief="raised", font=("Helvetica", 12, "bold"), image=editar_img, compound="left")
    boton_editar.grid(row=0, column=0, padx=10, pady=10)

    #Boton para eliminar producto

    ruta_imagen3 = os.path.join("algoritmo_archivos", "iconos", "eliminar.png")
    eliminar_img = PhotoImage(file=ruta_imagen3)
    boton_eliminar = Button(frame_botones_acciones, text=" Eliminar Producto", command=lambda: eliminar_producto(tree))
    boton_eliminar.config(bg="#FEFBEA", bd=10, relief="raised", font=("Helvetica", 12, "bold"), image=eliminar_img, compound="left")
    boton_eliminar.grid(row=0, column=1, padx=10, pady=10)

    #Boton para pagar
    ruta_imagen5 = os.path.join("algoritmo_archivos", "iconos", "pagar.png")
    pagar_img = PhotoImage(file=ruta_imagen5)
    boton_pagar = Button(frame_botones_acciones, text=" Pagar", command=lambda: ventana_pago(tree))
    boton_pagar.config(bg="#FEFBEA", bd=10, relief="raised", font=("Helvetica", 12, "bold"), image=pagar_img, compound="left")
    boton_pagar.grid(row=0, column=2, padx=10, pady=10)




    #Boton para regresar
    def regresar_algoritmo():
        ventana_ventas.destroy()
        algoritmo.abrir_ventana()

    ruta_imagen4 = os.path.join("algoritmo_archivos", "iconos", "regresar_24.png")
    regresar_img = PhotoImage(file=ruta_imagen4)
    boton_regresar = Button(ventana_ventas, text="  REGRESAR", command=regresar_algoritmo)
    boton_regresar.config(bg="#FEFBEA", bd=10, relief="raised", font=("Helvetica", 9, "bold"), image=regresar_img, compound="left")
    boton_regresar.place(x=40, y=550)

    ventana_ventas.mainloop()

#Funcion para buscar producto y mostrar informacion
def buscar_producto(producto_entry, tree, stock_label):
    producto_input = producto_entry.get()
    producto = base_datos.obtener_producto_por_codigo(producto_input) or base_datos.obtener_producto_por_nombre(producto_input)

    if producto:
        stock_label.config(text=f"Stock: {producto[2]}")
        cantidad = simpledialog.askinteger("Cantidad", "Ingrese la cantidad de productos:")
        if cantidad and cantidad <= producto[2]:
            total = cantidad * producto[4]
            tree.insert("", "end", values=(producto[0], producto[1], cantidad, f"Q.{total:.2f}"))
            messagebox.showinfo("Información del Producto", f"Código: {producto[0]}\nProducto: {producto[1]}\nExistencias: {producto[2]}\nPrecio Unitario: Q.{producto[4]:.2f}\nCantidad: {cantidad}\nPrecio Total: Q.{total:.2f}")
        else:
            messagebox.showwarning("Advertencia", "No hay suficiente existencia del producto")
    else:
        messagebox.showwarning("Advertencia", "Producto no encontrado")

#Funcion para editar producto en la lista
def editar_producto(tree):
    selected_item = tree.selection()
    if selected_item:
        item = tree.item(selected_item)
        codigo_producto = item['values'][0]
        nueva_cantidad = simpledialog.askinteger("Editar Existencias", "Ingrese la nueva cantidad de existencias:")
        if nueva_cantidad is not None:
            precio_unitario = float(item['values'][3][2:])
            nuevo_total = nueva_cantidad * precio_unitario
            tree.item(selected_item, values=(codigo_producto, item['values'][1], nueva_cantidad, f"Q.{nuevo_total:.2f}"))
            messagebox.showinfo("Éxito", "Producto editado exitosamente")
        else:
            messagebox.showwarning("Advertencia", "Cantidad no válida")
    else:
        messagebox.showwarning("Advertencia", "Por favor seleccione un producto para editar")

#Funcion para eliminar producto de la lista
def eliminar_producto(tree):
    selected_item = tree.selection()
    if selected_item:
        respuesta = messagebox.askyesno("Confirmación", "¿Estás seguro de que deseas eliminar este producto?")
        if respuesta:
            tree.delete(selected_item)
            messagebox.showinfo("Éxito", "Producto eliminado exitosamente")
        else:
            messagebox.showinfo("Cancelado", "Eliminación cancelada")
    else:
        messagebox.showinfo("Información", "Por favor seleccione un producto para eliminar")

total = 0.0

#Funcion para calcular el total de la compra
def calcular_total(tree):
    global total
    total = 0.0
    for child in tree.get_children():
        total += float(tree.item(child)["values"][3][2:])
    return total

#Funcion para mostrar la ventana de pago
def ventana_pago(tree):
    global total
    total = calcular_total(tree)
    ventana_pago = Toplevel()
    ventana_pago.title("Pago")
    ventana_pago.geometry("400x400")
    ventana_pago.resizable(False, False)
    ventana_pago.configure(bg="SkyBlue3")

    #Centrar la ventana en la pantalla
    ventana_pago.update_idletasks()
    width = ventana_pago.winfo_width()
    height = ventana_pago.winfo_height()
    x = (ventana_pago.winfo_screenwidth() // 2) - (width // 2)
    y = (ventana_pago.winfo_screenheight() // 2) - (height // 2)
    ventana_pago.geometry(f'{width}x{height}+{x}+{y}')

    Label(ventana_pago, text=f"Total: Q{total:.2f}", font=("Arial", 14), bg="SkyBlue3").pack(pady=10)

    Label(ventana_pago, text="Ingrese su pago:", font=("Arial", 12), bg="SkyBlue3").pack(pady=5)
    pago_entry = Entry(ventana_pago, font=("Arial", 12))
    pago_entry.pack(pady=5)

    resultado_label = Label(ventana_pago, text="", font=("Arial", 12), bg="SkyBlue3")
    resultado_label.pack(pady=10)

    def calcular_cambio():
        global pago
        global total
        try:
            pago = float(pago_entry.get())
            if pago < total:
                resultado_label.config(text=f"Faltan Q{total - pago:.2f}")
            else:
                resultado_label.config(text=f"Su cambio es Q{pago - total:.2f}")
        except ValueError:
            resultado_label.config(text="Monto no válido")

    Button(ventana_pago, text="Calcular Cambio", command=calcular_cambio, bg="SkyBlue4", bd=10, relief="raised", font=("Arial", 9, "bold")).pack(pady=10)

    def generar_venta():
        global total
        global pago
        if pago < total:
            messagebox.showinfo("Error","El pago no es suficiente")
            ventana_pago.focus_force()
            return
        while True:
            cliente_input = simpledialog.askstring("Datos del Cliente", "Ingrese el código o nombre del cliente:")
            
            if cliente_input:
                cliente = base_datos.obtener_cliente_por_codigo(cliente_input) or base_datos.obtener_cliente_por_nombre(cliente_input)
                if cliente:
                    codigo_cliente, nombre_cliente, direccion_cliente = cliente
                    crear_venta.generar_factura(tree, codigo_cliente, nombre_cliente, direccion_cliente)
                    
                    for child in tree.get_children():
                        item = tree.item(child)
                        codigo_producto = item["values"][0]
                        producto = item["values"][1]
                        cantidad = item["values"][2]
                        total = float(item["values"][3][2:])
                        fecha_actual = datetime.now().strftime("%d-%m-%Y")

                        base_datos.agregar_venta_bd(codigo_producto, codigo_cliente, cantidad, total, nombre_cliente, fecha_actual, producto)

                    messagebox.showinfo("Éxito", "Compra generada exitosamente y factura guardada en la carpeta 'compras'")
                    actualizar_inventario(tree)
                    break
                else:
                    messagebox.showwarning("Advertencia", "Cliente no encontrado")
            else:    
                messagebox.showwarning("Advertencia", "Debe ingresar el código o nombre del cliente")

    Button(ventana_pago, text="Generar Venta", command=generar_venta, bg="SkyBlue4", bd=10, relief="raised", font=("Arial", 9, "bold")).pack(pady=10)

    #Funcion para actualizar el inventario
    def actualizar_inventario(tree):
        for child in tree.get_children():
            item = tree.item(child)
            codigo_producto = item["values"][0]
            cantidad_vendida = item["values"][2]
            producto = base_datos.obtener_producto_por_codigo(codigo_producto)
            if producto:
                nueva_existencia = producto[2] - cantidad_vendida
                base_datos.actualizar_existencia_producto(codigo_producto, nueva_existencia)

#Bloqueo para la pantalla principal
if __name__ == "__main__":
    ventana_ventas()


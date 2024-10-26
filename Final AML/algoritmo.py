from tkinter import Tk, Label, Button, Canvas
import principal
from tkinter import PhotoImage
import os
from PIL import Image, ImageTk
from algoritmo_archivos.inventario import ventana_inventario
from algoritmo_archivos.clientes import ventana_clientes
from algoritmo_archivos.ventas import ventana_ventas
from algoritmo_archivos.reporte import ventana_reporte

#Ventana algoritmo
def abrir_ventana():
    ventana_algoritmo = Tk()
    ventana_algoritmo.title("Algoritmos")
    ventana_algoritmo.geometry("850x600+200+50")
    ventana_algoritmo.resizable(False, False)
    

    canvas = Canvas(ventana_algoritmo, width=850, height=600)
    canvas.pack()

    for i in range(600):
        ratio = i / 600
        color = '#%02x%02x%02x' % (
            int(45 + ratio * (149 - 45)),
            int(106 + ratio * (213 - 106)),
            int(79 + ratio * (178 - 79))
        )
        canvas.create_rectangle(0, i, 850, i+1, fill=color, outline=color)

    #Boton para abrir el inventario
    def abrir_ventana_inventario():
        ventana_algoritmo.destroy()
        ventana_inventario()

    ruta_imagen2 = os.path.join("algoritmo_archivos", "iconos", "inventario.png")
    inventario_img = PhotoImage(file=ruta_imagen2)
    boton_inventario = Button(ventana_algoritmo, text=" INVENTARIO", command=abrir_ventana_inventario)
    boton_inventario.config(bg="#FEFBEA", bd=10, relief="raised", font=("Helvetica", 12, "bold"), image=inventario_img, compound="left")
    boton_inventario.place(x=100, y=150)
 
    #Boton para abrir el control de clientes
    def abrir_ventana_clientes():
        ventana_algoritmo.destroy()
        ventana_clientes()

    ruta_imagen3 = os.path.join("algoritmo_archivos", "iconos", "clientes.png")
    clientes_img = PhotoImage(file=ruta_imagen3)
    boton_clientes = Button(ventana_algoritmo, text=" CLIENTES", command=abrir_ventana_clientes)
    boton_clientes.config(bg="#FEFBEA", bd=10, relief="raised", font=("Helvetica", 14, "bold"), image=clientes_img, compound="left")
    boton_clientes.place(x=100, y=250)

    #Boton para abrir el control de ventas
    def abrir_ventana_ventas():
        ventana_algoritmo.destroy()
        ventana_ventas()

    ruta_imagen1 = os.path.join("algoritmo_archivos", "iconos", "carrito.png")
    carrito_img = PhotoImage(file=ruta_imagen1)
    boton_ventas = Button(ventana_algoritmo, text=" VENTAS", command=abrir_ventana_ventas)
    boton_ventas.config(bg="#FEFBEA", bd=10, relief="raised", font=("Helvetica", 14, "bold"), image=carrito_img, compound="left")
    boton_ventas.place(x=100,y=450)

    #Boton para regresar al menu principal
    def regresar_menu_principal():
        ventana_algoritmo.destroy()
        principal.abrir_ventana_principal()

    ruta_imagen4 = os.path.join("algoritmo_archivos", "iconos", "regresar_24.png")
    regresar_img = PhotoImage(file=ruta_imagen4)
    boton_regresar = Button(ventana_algoritmo, text="  REGRESAR", command=regresar_menu_principal)
    boton_regresar.config(bg="#FEFBEA", bd=10, relief="raised", font=("Helvetica", 14, "bold"), image=regresar_img, compound="left")
    boton_regresar.place(x=100,y=50)

    #Boton para el reporte
    def abrir_ventana_reporte():
        ventana_algoritmo.destroy()
        ventana_reporte()

    ruta_imagen5 = os.path.join("algoritmo_archivos", "iconos", "reporte.png")
    reporte_img = PhotoImage(file=ruta_imagen5)
    boton_regresar = Button(ventana_algoritmo, text="  REPORTE", command=abrir_ventana_reporte)
    boton_regresar.config(bg="#FEFBEA", bd=10, relief="raised", font=("Helvetica", 14, "bold"), image=reporte_img, compound="left")
    boton_regresar.place(x=100, y=350)

    #Logo
    ruta_logo = os.path.join("algoritmo_archivos", "iconos", "logo.jpg")
    logo_img = Image.open(ruta_logo)
    logo_img = logo_img.resize((200, 200), Image.LANCZOS)
    logo_img = ImageTk.PhotoImage(logo_img)
    logo_label = Label(ventana_algoritmo, image=logo_img)
    logo_label.image = logo_img 
    logo_label.place(x=400, y=150)


    ventana_algoritmo.mainloop()

if __name__ == "__main__":
    abrir_ventana()

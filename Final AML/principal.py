from tkinter import Tk, Label, Button
from PIL import Image, ImageTk
from fractions import Fraction
import algoritmo, matematica_discreta, algebra_lineal

#Ventana principal
def abrir_ventana_principal():
    ventana_principal = Tk()
    ventana_principal.title("PROYECTO")
    ventana_principal.geometry("850x600+200+50")
    ventana_principal.resizable(False, False)
    ventana_principal.configure(bg="SkyBlue3")

    #Imagen de fondo
    imagen = Image.open("fondo_main.jpg")
    imagen = imagen.resize((850, 600), Image.LANCZOS)
    imagen_fondo = ImageTk.PhotoImage(imagen)
    fondo_label = Label(ventana_principal, image=imagen_fondo)
    fondo_label.place(x=0, y=0, relwidth=1, relheight=1)

    #Titulo 
    titulo = Label(ventana_principal, text="MENU PRINCIPAL")
    titulo.config(bg="SkyBlue4", font=("Arial", 20, "bold"))
    titulo.place(x=315, y=50) 

    #Boton para el proyecto de algoritmo
    def abrir_ventana_algoritmo():
        ventana_principal.destroy()
        algoritmo.abrir_ventana()

    boton_algoritmo = Button(ventana_principal, text="ALGORITMOS", command=abrir_ventana_algoritmo)
    boton_algoritmo.config(bg="SkyBlue4", bd=10, relief="raised", font=("Arial", 15, "bold"))
    boton_algoritmo.place(x=350, y=150)  

    #Boton para el proyecto de matematica discreta
    def abrir_ventana_matematica_discreta():
        ventana_principal.destroy()
        matematica_discreta.abrir_ventana()

    boton_matematica_discreta = Button(ventana_principal, text="MATEMATICA DISCRETA", command=abrir_ventana_matematica_discreta)
    boton_matematica_discreta.config(bg="SkyBlue4", bd=10, relief="raised", font=("Arial", 15, "bold"))
    boton_matematica_discreta.place(x=300, y=250)  

    #Boton para el proyecto de algebra lineal
    def abrir_ventana_algebra_lineal():
        ventana_principal.destroy()
        algebra_lineal.abrir_ventana()

    boton_algebra_lineal = Button(ventana_principal, text="ALGEBRA LINEAL", command=abrir_ventana_algebra_lineal)
    boton_algebra_lineal.config(bg="SkyBlue4", bd=10, relief="raised", font=("Arial", 15, "bold"))
    boton_algebra_lineal.place(x=340, y=350)  

    ventana_principal.mainloop()

#Bloqueo para la pantalla principal
if __name__ == "__main__":
    abrir_ventana_principal()
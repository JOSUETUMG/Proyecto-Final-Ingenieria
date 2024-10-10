from tkinter import Tk, Label, Button
import principal

#Ventana algoritmo
def abrir_ventana():
    ventana_algoritmo = Tk()
    ventana_algoritmo.title("Algoritmos")
    ventana_algoritmo.geometry("850x600+200+50")
    ventana_algoritmo.resizable(False, False)
    ventana_algoritmo.configure(bg="SkyBlue3")

#Compañero trabajen aqui todo el codigo por favor :)

    #Boton para regresar al menu principal
    def regresar_menu_principal():
        ventana_algoritmo.destroy()
        principal.abrir_ventana_principal()

    boton_regresar = Button(ventana_algoritmo, text="REGRESAR AL MENU PRINCIPAL", command=regresar_menu_principal)
    boton_regresar.config(bg="SkyBlue4", bd=5, relief="raised", font=("Arial", 5, "bold"))
    boton_regresar.place(x=10, y=10)

    ventana_algoritmo.mainloop()




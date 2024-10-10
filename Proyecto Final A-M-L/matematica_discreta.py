from tkinter import Tk, Label, Button
import principal

#Ventana matematica discreta
def abrir_ventana():
    ventana_matematica_discreta = Tk()
    ventana_matematica_discreta.title("Matematica Discreta")
    ventana_matematica_discreta.geometry("850x600+200+50")
    ventana_matematica_discreta.resizable(False, False)
    ventana_matematica_discreta.configure(bg="SkyBlue3")

#Compañero trabajen aqui todo el codigo por favor :)

#Boton para regresar al menu principal
    def regresar_menu_principal():
        ventana_matematica_discreta.destroy()
        principal.abrir_ventana_principal()

    boton_regresar = Button(ventana_matematica_discreta, text="REGRESAR AL MENU PRINCIPAL", command=regresar_menu_principal)
    boton_regresar.config(bg="SkyBlue4", bd=10, relief="raised", font=("Arial", 15, "bold"))
    boton_regresar.place(x=300, y=500)


    ventana_matematica_discreta.mainloop()
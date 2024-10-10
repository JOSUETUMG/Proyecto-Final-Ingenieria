from tkinter import Tk, Label, Button
import principal

#Ventana algrebra lineal
def abrir_ventana():
    ventana_algebra_lineal = Tk()
    ventana_algebra_lineal.title("Algebra Lineal")
    ventana_algebra_lineal.geometry("850x600+200+50")
    ventana_algebra_lineal.resizable(False, False)
    ventana_algebra_lineal.configure(bg="SkyBlue3")
    
#Compañero trabajen aqui todo el codigo por favor :)

 #Boton para regresar al menu principal
    def regresar_menu_principal():
        ventana_algebra_lineal.destroy()
        principal.abrir_ventana_principal()

    boton_regresar = Button(ventana_algebra_lineal, text="REGRESAR AL MENU PRINCIPAL", command=regresar_menu_principal)
    boton_regresar.config(bg="SkyBlue4", bd=10, relief="raised", font=("Arial", 15, "bold"))
    boton_regresar.place(x=300, y=500)




    ventana_algebra_lineal.mainloop()
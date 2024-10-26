from tkinter import Tk, Button
import principal 
import algebra_lineal_archivos.algebra_inversa_matriz as algebra_inversa_matriz
import algebra_lineal_archivos.algebra_multi_matrices as algebra_multi_matrices
import algebra_lineal_archivos.algebra_sistema_ecuaciones as algebra_sistema_ecuaciones

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

    boton_regresar = Button(ventana_algebra_lineal, text="<< Menú principal", command=regresar_menu_principal)
    boton_regresar.config(bg="SkyBlue4", bd=10, relief="raised", font=("Arial", 9, "bold"))
    boton_regresar.place(x=20, y=20)

    #Boton para inversa de matriz
    def abrir_inversa_matriz():
        ventana_algebra_lineal.destroy()
        algebra_inversa_matriz.abrir_ventana()

    boton_inversa_matriz = Button(ventana_algebra_lineal, text="Encontrar Inversa de Matriz", command=abrir_inversa_matriz)
    boton_inversa_matriz.config(bg="SkyBlue4", bd=10, relief="raised", font=("Arial", 15, "bold"))
    boton_inversa_matriz.place(x=280, y=150)  

    #Boton para multiplicación de matrices
    def abrir_multi_matrices():
        ventana_algebra_lineal.destroy()
        algebra_multi_matrices.abrir_ventana()

    boton_inversa_matriz = Button(ventana_algebra_lineal, text="Multiplicación de matrices", command=abrir_multi_matrices)
    boton_inversa_matriz.config(bg="SkyBlue4", bd=10, relief="raised", font=("Arial", 15, "bold"))
    boton_inversa_matriz.place(x=290, y=250)

    #Boton para resolver sistemas de ecuaciones
    def abrir_sistema_ecuaciones():
        ventana_algebra_lineal.destroy()
        algebra_sistema_ecuaciones.abrir_ventana()

    boton_sistema_ecuaciones = Button(ventana_algebra_lineal, text="Sistemas de ecuaciones", command=abrir_sistema_ecuaciones)
    boton_sistema_ecuaciones.config(bg="SkyBlue4", bd=10, relief="raised", font=("Arial", 15, "bold"))
    boton_sistema_ecuaciones.place(x=296, y=350)

    ventana_algebra_lineal.mainloop()
from tkinter import Tk, Label, Button, Entry, messagebox
from math import factorial
from PIL import Image, ImageTk
import principal

#Ventana matematica discreta
def abrir_ventana():
    ventana_matematica_discreta = Tk()
    ventana_matematica_discreta.title("Matemática Discreta")
    ventana_matematica_discreta.geometry("850x600+200+50")
    ventana_matematica_discreta.resizable(False, False)
    ventana_matematica_discreta.configure(bg="SkyBlue3")
    mostrar_menu(ventana_matematica_discreta)
    ventana_matematica_discreta.mainloop()


#Funciones para calculos matematicos
def permutaciones_sin_repeticion(n, r):
    return factorial(n) // factorial(n - r)
def permutaciones_con_repeticion(n, r):
    return n ** r
def combinaciones_sin_repeticion(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))
def combinaciones_con_repeticion(n, r):
    return factorial(n + r - 1) // (factorial(r) * factorial(n - 1))


#Funcion para calcular el resultado
def calcular_operacion(tipo_operacion, entry_n, entry_r, result_label):
    try:
        n = int(entry_n.get())
        r = int(entry_r.get())
        if tipo_operacion == "Permutaciones sin repetición":
            resultado = permutaciones_sin_repeticion(n, r)
        elif tipo_operacion == "Permutaciones con repetición":
            resultado = permutaciones_con_repeticion(n, r)
        elif tipo_operacion == "Combinaciones sin repetición":
            resultado = combinaciones_sin_repeticion(n, r)
        elif tipo_operacion == "Combinaciones con repetición":
            resultado = combinaciones_con_repeticion(n, r)
        result_label.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese números válidos.")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {str(e)}")


#Funcion para mostrar los campos de entrada en la misma ventana
def mostrar_entrada(ventana, operacion):
    for widget in ventana.winfo_children():
        widget.destroy()


    Label(ventana, text=operacion, font=("Arial", 14, "bold")).pack(pady=10)
    
    Label(ventana, text="Ingrese el valor de n:").pack()
    entry_n = Entry(ventana)
    entry_n.pack(pady=5)

    Label(ventana, text="Ingrese el valor de r:").pack()
    entry_r = Entry(ventana)
    entry_r.pack(pady=5)

    #Etiqueta para mostrar el resultado
    result_label = Label(ventana, text="", font=("Arial", 12))
    result_label.pack(pady=10)

    #Boton para calcular y mostrar resultado
    Button(ventana, text="Calcular", bg="darkblue", fg="white",
           command=lambda: calcular_operacion(operacion, entry_n, entry_r, result_label)).pack(pady=10)

    #Boton para regresar al menu de selección de operaciones
    Button(ventana, text="Regresar al Menú de Operaciones", command=lambda: mostrar_menu(ventana),
           bg="gray", fg="white", width=30).pack(pady=10)

#Funcion para mostrar el menu de operaciones
def mostrar_menu(ventana):
    #Limpiar la ventana principal para mostrar el menu de operaciones
    for widget in ventana.winfo_children():
        widget.destroy()

    Label(ventana, text="Seleccione una Operación", font=("Arial", 14, "bold")).pack(pady=10)

    #Botones de operacion más pequeños y con colores distintivos
    permutacion_sin_repeticion = Button(ventana, text="Permutaciones sin repetición", bg="lightblue", fg="black", command=lambda: mostrar_entrada(ventana, "Permutaciones sin repetición"), width=30).pack(pady=5)
    permutacion_con_repeticion = Button(ventana, text="Permutaciones con repetición", bg="lightgreen", fg="black", command=lambda: mostrar_entrada(ventana, "Permutaciones con repetición"), width=30).pack(pady=5)
    combinaciones_sin_repeticion = Button(ventana, text="Combinaciones sin repetición", bg="lightcoral", fg="black", command=lambda: mostrar_entrada(ventana, "Combinaciones sin repetición"), width=30).pack(pady=5)
    combinaciones_con_repeticion = Button(ventana, text="Combinaciones con repetición", bg="lightyellow", fg="black", command=lambda: mostrar_entrada(ventana, "Combinaciones con repetición"), width=30).pack(pady=5)
    
    #Boton para regresar al menu principal
    Button(ventana, text="Regresar", command=lambda: regresar_menu_principal(ventana), bg="gray", fg="white", width=10).pack(pady=20)

#Funcion para regresar al menu principal
def regresar_menu_principal(ventana):
    ventana.destroy()
    principal.abrir_ventana_principal()


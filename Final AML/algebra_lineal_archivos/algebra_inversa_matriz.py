from tkinter import Tk, Label, Button, Radiobutton, IntVar, Entry
from fractions import Fraction
import numpy as np
import algebra_lineal

# Abrir ventana de encontrar matriz inversa
def abrir_ventana():
    ventana_inversa_matriz = Tk()
    ventana_inversa_matriz.title("Encontrar matriz inversa")
    ventana_inversa_matriz.geometry("850x600+200+50")
    ventana_inversa_matriz.resizable(False, False)
    ventana_inversa_matriz.configure(bg="SkyBlue3")

    # Botón para regresar a ventana algebra lineal
    def regresar_ventana_algebra():
        ventana_inversa_matriz.destroy()
        algebra_lineal.abrir_ventana()

    boton_regresar = Button(ventana_inversa_matriz, text="<< Algebra Lineal", command=regresar_ventana_algebra)
    boton_regresar.config(bg="SkyBlue4", bd=10, relief="raised", font=("Arial", 9, "bold"))
    boton_regresar.place(x=20, y=20)

    # Variable para almacenar la opción seleccionada
    opcion = IntVar()
    opcion.set(2)  # Valor por defecto

    # Array para guardar las entradas
    entradas = []
    determinante = 0
    matriz = []

    # Función para crear los espacios de entrada según la opción seleccionada
    def crear_entradas():
        nonlocal entradas
        # Quitar todas las entradas anteriores
        for widget in ventana_inversa_matriz.winfo_children():
            if isinstance(widget, Entry):
                widget.destroy()
        
        entradas = []
        tamanomatriz = opcion.get()
        for i in range(tamanomatriz):
            fila = []
            for j in range(tamanomatriz):
                entrada = Entry(ventana_inversa_matriz, width=5, justify='center')
                entrada.place(x=350 + j*50, y=120 + i*50)
                fila.append(entrada)
            entradas.append(fila)

    # Función para calcular el determinante
    def calcular_determinante():
        nonlocal determinante
        nonlocal matriz
        try:
            tamanomatriz = opcion.get()
            matriz = []
            for i in range(tamanomatriz):
                fila = []
                for j in range(tamanomatriz):
                    valor = entradas[i][j].get()
                    if valor == "":
                        raise ValueError("Campo vacío")
                    fila.append(float(Fraction(valor)))
                matriz.append(fila)
            matriz = np.array(matriz)
            determinante = np.linalg.det(matriz)
            if determinante == 0:
                resultado_label.config(text="Determinante de la matriz es 0. No tiene inversa")
        except ValueError as e:
            if str(e) == "Campo vacío":
                resultado_label.config(text="Error: Asegúrate de que todas las entradas están llenas.")
            else:
                resultado_label.config(text="Error: Asegúrate de ingresar solo números o fracciones válidas.")

    # Texto de elige el tamaño de la matriz
    label = Label(ventana_inversa_matriz, text="Elige el tamaño de la matriz:", bg="SkyBlue3", font=("Arial", 12))
    label.place(x=175, y=30)

    # Botones de radio para elegir el tamaño de la matriz
    radio_2x2 = Radiobutton(ventana_inversa_matriz, text="2x2", variable=opcion, value=2, command=crear_entradas, bg="SkyBlue3")
    radio_2x2.place(x=375, y=30)

    radio_3x3 = Radiobutton(ventana_inversa_matriz, text="3x3", variable=opcion, value=3, command=crear_entradas, bg="SkyBlue3")
    radio_3x3.place(x=425, y=30)

    radio_4x4 = Radiobutton(ventana_inversa_matriz, text="4x4", variable=opcion, value=4, command=crear_entradas, bg="SkyBlue3")
    radio_4x4.place(x=475, y=30)

    # Crear entradas por defecto
    crear_entradas()

    def matriz_inversa():
        if determinante != 0:
            inversa = np.linalg.inv(matriz)
            inversa_str = "\n".join(["\t".join([str(Fraction(num).limit_denominator()) for num in fila]) for fila in inversa])
            resultado_label.config(text=f"Matriz Inversa:\n{inversa_str}")

    def ejecutar():
        calcular_determinante()
        if determinante != 0:
            matriz_inversa()
    # Botón para encontrar matriz inversa
    inversa_button = Button(ventana_inversa_matriz, text="Encontrar Matriz Inversa", command=ejecutar)
    inversa_button.place(x=375, y=340)

    # Etiqueta para mostrar el resultado
    resultado_label = Label(ventana_inversa_matriz, bg="SkyBlue3", font=("Arial", 12))
    resultado_label.place(x=310, y=400)

    ventana_inversa_matriz.mainloop()
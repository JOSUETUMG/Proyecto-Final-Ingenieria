from tkinter import Tk, Label, Button, Radiobutton, IntVar, Entry
from fractions import Fraction
import numpy as np
import algebra_lineal

# Ventana multiplicación de matrices
def abrir_ventana():
    ventana_multi_matrices = Tk()
    ventana_multi_matrices.title("Multiplicar matrices")
    ventana_multi_matrices.geometry("850x600+200+50")
    ventana_multi_matrices.resizable(False, False)
    ventana_multi_matrices.configure(bg="SkyBlue3")

    # Botón para regresar a ventana algebra lineal
    def regresar_ventana_algebra():
        ventana_multi_matrices.destroy()
        algebra_lineal.abrir_ventana()

    # Variable para almacenar la opción seleccionada
    opcion = IntVar()
    opcion.set(2)  # Valor por defecto

    entradas1 = []
    entradas2 = []
    matriz1 = []
    matriz2 = []
    matriz_resultado = []

    # Función para crear los espacios de entrada según la opción seleccionada
    def crear_entradas():
        nonlocal entradas1, entradas2
        # Quitar todas las entradas anteriores
        for widget in ventana_multi_matrices.winfo_children():
            if isinstance(widget, Entry):
                widget.destroy()
                
        entradas1 = []
        entradas2 = []
        tamanomatriz = opcion.get()
        for i in range(tamanomatriz):
            fila1 = []
            fila2 = []
            for j in range(tamanomatriz):
                entrada1 = Entry(ventana_multi_matrices, width=5, justify='center')
                entrada1.place(x=175 + j*50, y=120 + i*50)
                fila1.append(entrada1)
                
                entrada2 = Entry(ventana_multi_matrices, width=5, justify='center')
                entrada2.place(x=475 + j*50, y=120 + i*50)
                fila2.append(entrada2)
                
            entradas1.append(fila1)
            entradas2.append(fila2)
    
    crear_entradas()

    def entradas_a_matriz():
        nonlocal matriz1, matriz2
        try:
            tamanomatriz = opcion.get()
            matriz1 = []
            matriz2 = []

            for i in range(tamanomatriz):
                fila1 = []
                fila2 = []
                
                for j in range(tamanomatriz):
                    valor1 = entradas1[i][j].get()
                    if valor1 == "":
                        raise ValueError("Campo vacío")
                    fila1.append(float(Fraction(valor1)))
                    
                    valor2 = entradas2[i][j].get()
                    if valor2 == "":
                        raise ValueError("Campo vacío")
                    fila2.append(float(Fraction(valor2)))
                
                matriz1.append(fila1)
                matriz2.append(fila2)

            matriz1 = np.array(matriz1)
            matriz2 = np.array(matriz2)
        
        except ValueError as e:
            if str(e) == "Campo vacío":
                resultado_label.config(text="Error: Asegúrate de que todas las entradas están llenas.")
            else:
                resultado_label.config(text="Error: Asegúrate de ingresar solo números o fracciones válidas.")

    def multiplicar():
        nonlocal matriz_resultado
        entradas_a_matriz()
        matriz_resultado = np.dot(matriz1, matriz2)
        resultado_str = "\n".join(["\t".join([str(Fraction(num).limit_denominator()) for num in fila]) for fila in matriz_resultado])
        resultado_label.config(text=f"Matriz resultado:\n{resultado_str}")

    # Texto de elige el tamaño de la matriz
    label = Label(ventana_multi_matrices, text="Elige el tamaño de la matriz:", bg="SkyBlue3", font=("Arial", 12))
    label.place(x=175, y=30)

    # Botones de radio para elegir el tamaño de la matriz
    radio_2x2 = Radiobutton(ventana_multi_matrices, text="2x2", variable=opcion, value=2, command=crear_entradas, bg="SkyBlue3")
    radio_2x2.place(x=375, y=30)

    radio_3x3 = Radiobutton(ventana_multi_matrices, text="3x3", variable=opcion, value=3, command=crear_entradas, bg="SkyBlue3")
    radio_3x3.place(x=425, y=30)

    radio_4x4 = Radiobutton(ventana_multi_matrices, text="4x4", variable=opcion, value=4, command=crear_entradas, bg="SkyBlue3")
    radio_4x4.place(x=475, y=30)

    boton_regresar = Button(ventana_multi_matrices, text="<< Algebra Lineal", command=regresar_ventana_algebra)
    boton_regresar.config(bg="SkyBlue4", bd=10, relief="raised", font=("Arial", 9, "bold"))
    boton_regresar.place(x=20, y=20)

    # Botón para realizar la multiplicación
    multiplicar_button = Button(ventana_multi_matrices, text="Multiplicar Matrices", command=multiplicar)
    multiplicar_button.place(x=375, y=340)

    # Etiqueta para mostrar el resultado
    resultado_label = Label(ventana_multi_matrices, bg="SkyBlue3", font=("Arial", 12))
    resultado_label.place(x=310, y=400)

    ventana_multi_matrices.mainloop()
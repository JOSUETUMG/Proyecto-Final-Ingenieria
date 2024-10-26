from tkinter import Tk, Label, Button, Radiobutton, IntVar, Entry
from fractions import Fraction
import numpy as np
import algebra_lineal
import matplotlib.pyplot as plt

# Ventana sistemas de ecuaciones
def abrir_ventana():
    ventana_sistemas = Tk()
    ventana_sistemas.title("Sistemas de Ecuaciones")
    ventana_sistemas.geometry("850x700+200+0")
    ventana_sistemas.resizable(False, False)
    ventana_sistemas.configure(bg="SkyBlue3")

    # Botón para regresar a ventana algebra lineal
    def regresar_ventana_algebra():
        ventana_sistemas.destroy()
        algebra_lineal.abrir_ventana()

    # Variable para almacenar la opción seleccionada
    opcion = IntVar()
    opcion.set(2)  # Valor por defecto

    metodo = IntVar()
    metodo.set(1)  # Valor por defecto

    entradas = []
    etiquetas_fijas = []

    # Función para crear los espacios de entrada según la opción seleccionada
    def crear_entradas():
        nonlocal entradas
        for widget in ventana_sistemas.winfo_children():
            if isinstance(widget, Entry) or (isinstance(widget, Label) and widget not in etiquetas_fijas):
                widget.destroy()
            resultado_label.config(text='')

        entradas = []
        tamanomatriz = opcion.get()
        for i in range(tamanomatriz):
            fila = []
            for j in range(tamanomatriz):
                entrada = Entry(ventana_sistemas, width=5, justify='center')
                entrada.place(x=175 + j*50, y=120 + i*50)
                fila.append(entrada)
            entradas.append(fila)
            # Campo para el término independiente
            resultado = Entry(ventana_sistemas, width=5, justify='center')
            resultado.place(x=175 + tamanomatriz*50 + 50, y=120 + i*50)
            fila.append(resultado)

        # Crear etiquetas para las variables
        for j in range(tamanomatriz):
            etiqueta_variable = Label(ventana_sistemas, text=f"x{j+1}", bg="SkyBlue3", font=("Arial", 12))
            etiqueta_variable.place(x=175 + j*50, y=90)
        
        # Crear etiquetas para los signos "="
        for i in range(tamanomatriz):
            etiqueta_igual = Label(ventana_sistemas, text="=", bg="SkyBlue3", font=("Arial", 12))
            etiqueta_igual.place(x=175 + tamanomatriz*50, y=120 + i*50)

    crear_entradas()

    def resolver_sistema():
        nonlocal entradas
        try:
            tamanomatriz = opcion.get()
            matriz = []
            resultados = []
            for i in range(tamanomatriz):
                fila = []
                for j in range(tamanomatriz):
                    valor = entradas[i][j].get()
                    if valor == "":
                        raise ValueError("Campo vacío")
                    fila.append(float(Fraction(valor)))

                resultados.append(float(Fraction(entradas[i][-1].get())))  # Término independiente
                matriz.append(fila)

            matriz = np.array(matriz)
            resultados = np.array(resultados)
            
            # Variables para almacenar soluciones
            soluciones = []
            procedimiento = ""
            metodo_usado = ""

            if metodo.get() == 1:  # Gauss-Jordan
                det = np.linalg.det(matriz) #Calcula determinante
                matriz_aumentada = np.column_stack((matriz, resultados)) #Agregar los elementos del array Resultados como columna a Matriz
                procedimiento += "Matriz aumentada inicial:\n" + str(matriz_aumentada) + "\n\n"
                if det == 0:
                    resultado_label.config(text="El sistema no tiene solución única (determinante es 0).")
                    return
                soluciones = np.linalg.solve(matriz, resultados)  # Resuelve sistema de ecuaciones
                metodo_usado = "Gauss-Jordan"
            
            elif metodo.get() == 2:  # Regla de Cramer
                det = round(np.linalg.det(matriz), 2) #Calcula determinante
                procedimiento += "Determinante de la matriz:\n" + str(det) + "\n\n"
                if det == 0:
                    resultado_label.config(text="El sistema no tiene solución única (determinante es 0).")
                    return
                soluciones = [round(np.linalg.det(np.column_stack((matriz[:, :i], resultados, matriz[:, i+1:]))) / det, 2) for i in range(tamanomatriz)]
                metodo_usado = "Regla de Cramer"

            # Convertir y redondear soluciones para ambos métodos
            soluciones_fraccion = [Fraction(sol).limit_denominator() for sol in soluciones]
            soluciones_redondeadas = [round(sol, 2) for sol in soluciones]

            # Formatear soluciones para mostrar
            resultado_str = "\n".join([
                f"x{index+1} = {fraccion} ≈ {decimal}"
                for index, (fraccion, decimal) in enumerate(zip(soluciones_fraccion, soluciones_redondeadas))
            ])

            # Mostrar resultado en la etiqueta
            resultado_label.config(text=f"Soluciones del sistema usando {metodo_usado}:\n{resultado_str}\n\n{procedimiento}")

        except ValueError as e:
            if str(e) == "Campo vacío":
                resultado_label.config(text="Error: Asegúrate de que todas las entradas están llenas.")
            else:
                resultado_label.config(text="Error: Asegúrate de ingresar solo números o fracciones válidas.")

    def generar_grafica():
        tamanomatriz = opcion.get()

        if tamanomatriz == 2:
            try:
                # Extraer valores de los Entry
                a1, b1, c1 = float(entradas[0][0].get()), float(entradas[0][1].get()), float(entradas[0][2].get())
                a2, b2, c2 = float(entradas[1][0].get()), float(entradas[1][1].get()), float(entradas[1][2].get())

                # Definir las ecuaciones
                def eq1(x):
                    return (c1 - a1 * x) / b1

                def eq2(x):
                    return (c2 - a2 * x) / b2

                # Crear un rango de valores para x
                valores_x = np.linspace(-10, 10, 400)

                # Generar los valores correspondientes de y para ambas ecuaciones
                valores_y_eq1 = eq1(valores_x)
                valores_y_eq2 = eq2(valores_x)

                # Crear la gráfica
                plt.figure(figsize=(10, 8))
                plt.plot(valores_x, valores_y_eq1, label=f'{a1}x + {b1}y = {c1}', color='blue')
                plt.plot(valores_x, valores_y_eq2, label=f'{a2}x + {b2}y = {c2}', color='red')

                # Añadir etiquetas y título
                plt.xlabel('x')
                plt.ylabel('y')
                plt.axhline(0, color='black', linewidth=0.5)
                plt.axvline(0, color='black', linewidth=0.5)
                plt.grid(color='gray', linestyle='--', linewidth=0.5)
                plt.legend()
                plt.title('Sistema de Ecuaciones Lineales 2x2')

                # Mostrar la gráfica
                plt.show()

            except ValueError:
                resultado_label.config(text="Error: Asegúrate de que las entradas sean válidas para el sistema 2x2.")

        elif tamanomatriz == 3:
            try:
                # Extraer valores de los Entry
                a1, b1, c1, d1 = float(entradas[0][0].get()), float(entradas[0][1].get()), float(entradas[0][2].get()), float(entradas[0][3].get())
                a2, b2, c2, d2 = float(entradas[1][0].get()), float(entradas[1][1].get()), float(entradas[1][2].get()), float(entradas[1][3].get())
                a3, b3, c3, d3 = float(entradas[2][0].get()), float(entradas[2][1].get()), float(entradas[2][2].get()), float(entradas[2][3].get())

                # Crear la gráfica 3D
                fig = plt.figure()
                ax = fig.add_subplot(111, projection='3d')

                # Crear un rango de valores para x y y
                valores_x = np.linspace(-10, 10, 400)
                valores_y = np.linspace(-10, 10, 400)
                x, y = np.meshgrid(valores_x, valores_y)

                # Generar los valores correspondientes de z para las ecuaciones
                valores_z_eq1 = (d1 - a1 * x - b1 * y) / c1
                valores_z_eq2 = (d2 - a2 * x - b2 * y) / c2
                valores_z_eq3 = (d3 - a3 * x - b3 * y) / c3

                # Graficar las ecuaciones
                ax.plot(x, y, valores_z_eq1, color='blue', alpha=0.5, label=f'{a1}x + {b1}y + {c1}z = {d1}')
                ax.plot(x, y, valores_z_eq2, color='red', alpha=0.5, label=f'{a2}x + {b2}y + {c2}z = {d2}')
                ax.plot(x, y, valores_z_eq3, color='yellow', alpha=0.5, label=f'{a3}x + {b3}y + {c3}z = {d3}')

                # Añadir etiquetas y título
                ax.set_xlabel('x')
                ax.set_ylabel('y')
                ax.set_zlabel('z')
                plt.title('Sistema de Ecuaciones Lineales 3x3')

                # Mostrar la gráfica
                plt.show()

            except ValueError:
                resultado_label.config(text="Error: Asegúrate de que las entradas sean válidas para el sistema 3x3.")

    # Texto de elige el tamaño de la matriz
    label_tamano = Label(ventana_sistemas, text="Elige el tamaño del sistema:", bg="SkyBlue3", font=("Arial", 12))
    label_tamano.place(x=175, y=30)
    etiquetas_fijas.append(label_tamano)

    # Botones de radio para elegir el tamaño del sistema
    radio_2x2 = Radiobutton(ventana_sistemas, text="2x2", variable=opcion, value=2, command=crear_entradas, bg="SkyBlue3")
    radio_2x2.place(x=375, y=30)

    radio_3x3 = Radiobutton(ventana_sistemas, text="3x3", variable=opcion, value=3, command=crear_entradas, bg="SkyBlue3")
    radio_3x3.place(x=425, y=30)

    radio_4x4 = Radiobutton(ventana_sistemas, text="4x4", variable=opcion, value=4, command=crear_entradas, bg="SkyBlue3")
    radio_4x4.place(x=475, y=30)

    # Texto de elige el método
    label_metodo = Label(ventana_sistemas, text="Elige el método de resolución:", bg="SkyBlue3", font=("Arial", 12))
    label_metodo.place(x=175, y=60)
    etiquetas_fijas.append(label_metodo)

    # Botones de radio para elegir el método de resolución
    radio_gauss = Radiobutton(ventana_sistemas, text="Gauss-Jordan", variable=metodo, value=1, command=crear_entradas, bg="SkyBlue3")
    radio_gauss.place(x=375, y=60)

    radio_cramer = Radiobutton(ventana_sistemas, text="Regla de Cramer", variable=metodo, value=2, command=crear_entradas, bg="SkyBlue3")
    radio_cramer.place(x=475, y=60)

    # Botón para regresar a ventana algebra lineal
    boton_regresar = Button(ventana_sistemas, text="<< Algebra Lineal", command=regresar_ventana_algebra)
    boton_regresar.config(bg="SkyBlue4", bd=10, relief="raised", font=("Arial", 9, "bold"))
    boton_regresar.place(x=20, y=20)

    # Botón para resolver el sistema
    resolver_button = Button(ventana_sistemas, text="Resolver", command=resolver_sistema)
    resolver_button.place(x=375, y=340)

    # Botón para generar gráfica
    boton_grafica = Button(ventana_sistemas, text="Generar Gráfica", command=generar_grafica)
    boton_grafica.config(bg="SkyBlue4", bd=10, relief="raised", font=("Arial", 9, "bold"))
    boton_grafica.place(x=550, y=185)

    # Etiqueta para mostrar el resultado
    resultado_label = Label(ventana_sistemas, bg="SkyBlue3", font=("Arial", 12))
    resultado_label.place(x=310, y=400)
    etiquetas_fijas.append(resultado_label)

    ventana_sistemas.mainloop()
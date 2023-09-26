import tkinter as tk
from tkinter import ttk

# Función para encontrar la raíz por el método de bisección
def biseccion(a, b, tol, max_iter):
    resultado = []

    fa = funcion(a)
    fb = funcion(b)

    if fa * fb >= 0:
        return "La función no cumple con el teorema de Bolzano."

    iteracion = 1
    while (b - a) / 2.0 > tol and iteracion <= max_iter:
        c = (a + b) / 2.0
        fc = funcion(c)

        resultado.append(f"Iteración {iteracion}: a = {a}, b = {b}, c = {c}, f(c) = {fc}")

        if fc == 0.0:
            break
        elif fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc

        iteracion += 1

    resultado.append(f"Resultado final: Raíz aproximada = {c}")

    return resultado

# Función que representa la función f(x) que deseas encontrar la raíz
def funcion(x):
    return x**3 - 4*x**2 + 7*x - 3

# Crear una ventana para mostrar los resultados
root = tk.Tk()
root.title("Método de Bisección")
root.geometry("400x400")

# Crear un cuadro de texto para mostrar los resultados
resultado_text = tk.Text(root, wrap=tk.WORD)
resultado_text.pack()

# Calcular la raíz por el método de bisección
a = 0.5
b = 2.5
tolerancia = 0.00000000000000001
max_iteraciones = 20
resultados = biseccion(a, b, tolerancia, max_iteraciones)

# Mostrar los resultados en el cuadro de texto
for resultado in resultados:
    resultado_text.insert(tk.END, resultado + "\n")

root.mainloop()

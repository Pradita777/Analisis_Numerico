import tkinter as tk

# Funciones que queremos ejecutar
def funcion1():
    resultado_label.config(text="Función 1 ejecutada")

def funcion2():
    resultado_label.config(text="Función 2 ejecutada")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Interfaz Gráfica para Ejecutar Funciones")

# Crear etiquetas
titulo_label = tk.Label(ventana, text="Elija una función para ejecutar:")
titulo_label.pack()

resultado_label = tk.Label(ventana, text="")
resultado_label.pack()

# Botones para ejecutar funciones
boton_funcion1 = tk.Button(ventana, text="Función 1", command=funcion1)
boton_funcion1.pack()

boton_funcion2 = tk.Button(ventana, text="Función 2", command=funcion2)
boton_funcion2.pack()

# Iniciar el bucle principal de la aplicación
ventana.mainloop()

import tkinter as tk
from tkinter import ttk
import Biseccion

# Funciones para encontrar la raíz de una función
def metodo1():
    a = 0.5
    b = 2.5
    tolerancia = 0.0001
    max_iteraciones = 20

    resultados = Biseccion.biseccion(a, b, tolerancia, max_iteraciones)
    for resultado in resultados:
        print(resultado)
    pass

def metodo2():
    # Aquí puedes implementar el método 2
    pass

def metodo3():
    # Aquí puedes implementar el método 3
    pass

# Crear una ventana principal
root = tk.Tk()
root.title("Encontrar Raíz de una Función")
root.geometry("800x600")

# Configurar la barra de menú
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Crear un menú desplegable en la barra de menú
metodos_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Métodos", menu=metodos_menu)

# Agregar opciones al menú desplegable
metodos_menu.add_command(label="Método 1", command=metodo1)
metodos_menu.add_command(label="Método 2", command=metodo2)
metodos_menu.add_command(label="Método 3", command=metodo3)

# Crear un marco para cada ventana de método
metodo1_frame = ttk.Frame(root)
metodo2_frame = ttk.Frame(root)
metodo3_frame = ttk.Frame(root)

# Función para cambiar entre ventanas de método
def cambiar_ventana(ventana):
    metodo1_frame.pack_forget()
    metodo2_frame.pack_forget()
    metodo3_frame.pack_forget()
    
    ventana.pack()

# Botones para cambiar entre ventanas de método
btn_metodo1 = ttk.Button(root, text="Método 1", command=lambda: cambiar_ventana(metodo1_frame))
btn_metodo2 = ttk.Button(root, text="Método 2", command=lambda: cambiar_ventana(metodo2_frame))
btn_metodo3 = ttk.Button(root, text="Método 3", command=lambda: cambiar_ventana(metodo3_frame))

btn_metodo1.pack()
btn_metodo2.pack()
btn_metodo3.pack()

# Mostrar la ventana principal
cambiar_ventana(metodo1_frame)
root.mainloop()


from root_finder import RootFinder
import tkinter as tk

class RootFinderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Raíces")
        
        # Crear instancia de la clase RootFinder
        self.root_finder = RootFinder()

        # Crear un menú desplegable para seleccionar el método
        self.method_label = tk.Label(root, text="Selecciona un método:")
        self.method_label.pack(anchor='w')  # Alinea a la izquierda

        # Crear botones para cada método
        self.bisection_button = tk.Button(root, text="Bisección", command=self.show_bisection_interface)
        self.bisection_button.pack(anchor='w', padx=10, pady=5)  # Alinea a la izquierda

        self.newton_button = tk.Button(root, text="Newton-Raphson", command=self.show_newton_interface)
        self.newton_button.pack(anchor='w', padx=10, pady=5)  # Alinea a la izquierda

        # Otros widgets...
        # Agrega widgets para ingresar los parámetros según el método seleccionado

    def show_bisection_interface(self):
        self.func_label = tk.Label(root, text="Función:")
        self.func_label.pack(anchor='w')  # Alinea a la izquierda

        self.func_entry = tk.Entry(root, width=40)
        self.func_entry.pack(anchor='w', padx=10, pady=5)  # Alinea a la izquierda

        # Etiquetas y cuadros de texto para los puntos iniciales, tolerancia e iteraciones
        self.a_label = tk.Label(root, text="Punto inicial izquierdo (a):")
        self.a_label.pack(anchor='w')

        self.a_entry = tk.Entry(root)
        self.a_entry.pack(anchor='w', padx=10, pady=5)

        self.b_label = tk.Label(root, text="Punto inicial derecho (b):")
        self.b_label.pack(anchor='w')

        self.b_entry = tk.Entry(root)
        self.b_entry.pack(anchor='w', padx=10, pady=5)

        self.tolerancia_label = tk.Label(root, text="Tolerancia:")
        self.tolerancia_label.pack(anchor='w')

        self.tolerancia_entry = tk.Entry(root)
        self.tolerancia_entry.pack(anchor='w', padx=10, pady=5)

        self.iteraciones_label = tk.Label(root, text="Iteraciones máximas:")
        self.iteraciones_label.pack(anchor='w')

        self.iteraciones_entry = tk.Entry(root)
        self.iteraciones_entry.pack(anchor='w', padx=10, pady=5)

        # Botón para calcular la raíz utilizando el método de bisección
        self.calcular_button = tk.Button(root, text="Calcular Raíz por Bisección", command=self.calcular_biseccion)
        self.calcular_button.pack(anchor='w', padx=10, pady=10)

        # Etiqueta para mostrar el resultado
        self.resultado_label = tk.Label(root, text="")
        self.resultado_label.pack(anchor='w', padx=10, pady=5)

    def calcular_biseccion(self):
        # Obtener los valores ingresados por el usuario
        funcion_str = self.func_entry.get()
        a = float(self.a_entry.get())
        b = float(self.b_entry.get())
        tolerancia = float(self.tolerancia_entry.get())
        max_iteraciones = int(self.iteraciones_entry.get())

        # Implementar el cálculo de la raíz utilizando el método de bisección
        try:
            # Evaluar la función y realizar el cálculo de la raíz aquí
            # A continuación, mostramos un mensaje de ejemplo
            resultado = f"Aproximación de la raíz por bisección: {a + b / 2:.6f}"
            self.resultado_label.config(text=resultado)
        except Exception as e:
            self.resultado_label.config(text=f"Error: {str(e)}")

    def show_newton_interface(self):
        pass
        # Aquí debes implementar la interfaz para el método de Newton-Raphson
        # Puedes crear nuevos widgets específicos para este método y ocultar/mostrar widgets según sea necesario


if __name__ == "__main__":
    root = tk.Tk()
    app = RootFinderApp(root)
    root.mainloop()

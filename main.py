from tkinter import Tk
from interfaz_grafica import CalculatorApp

def main():
    """Función principal que inicializa la aplicación de la calculadora."""

    root = Tk()
    app = CalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    """Punto de entrada del programa."""
    
    main()

from tkinter import Label, Entry, Button
from calculator import Calculator

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")
        
        self.calculator = Calculator()

        self.label = Label(root, text="Ingrese la operación:")
        self.label.pack()

        self.entry = Entry(root)
        self.entry.pack()

        self.result_label = Label(root, text="")
        self.result_label.pack()

        self.calculate_button = Button(root, text="Calcular", command=self.calculate)
        self.calculate_button.pack()

    def calculate(self):
        operation = self.entry.get()
        try:
            result = self.calculator.calculate(operation)
            if result is not None:
                self.result_label.config(text=f"El resultado es: {result}")
            else:
                self.result_label.config(text="Operación inválida")
        except Exception as e:
            self.result_label.config(text=f"Error: {e}")
from abc import ABC, abstractmethod

class Operation(ABC):
    @abstractmethod
    def execute(self):
        """Ejecuta la operación y devuelve el resultado."""

        pass

class Addition(Operation):
    def __init__(self, num1, num2):
        """Inicializa la operación de suma con los números a sumar."""

        self.num1 = num1
        self.num2 = num2

    def execute(self):
        """Realiza la suma de los números y devuelve el resultado."""

        return self.num1 + self.num2

class Subtraction(Operation):
    def __init__(self, num1, num2):
        """Inicializa la operación de resta con los números a restar."""

        self.num1 = num1
        self.num2 = num2

    def execute(self):
        """Realiza la resta de los números y devuelve el resultado."""

        return self.num1 - self.num2

class Multiplication(Operation):
    def __init__(self, num1, num2):
        """Inicializa la operación de multiplicación con los números a multiplicar."""

        self.num1 = num1
        self.num2 = num2

    def execute(self):
        """Realiza la multiplicación de los números y devuelve el resultado."""

        return self.num1 * self.num2

class Division(Operation):
    def __init__(self, num1, num2):
        """Inicializa la operación de división con los números a dividir."""

        self.num1 = num1
        self.num2 = num2

    def execute(self):
        """Realiza la división de los números y devuelve el resultado."""

        if self.num2 == 0:
            raise ZeroDivisionError("No se puede dividir por cero")
        return self.num1 / self.num2

# Patrón estructural: Factory Method
class OperationFactory:
    def create_operation(self, operator, num1, num2):
        """Crea una instancia de la operación correspondiente según el operador dado."""
        
        if operator == '+':
            return Addition(num1, num2)
        elif operator == '-':
            return Subtraction(num1, num2)
        elif operator == '*':
            return Multiplication(num1, num2)
        elif operator == '/':
            return Division(num1, num2)
        else:
            raise ValueError("Operador no válido")

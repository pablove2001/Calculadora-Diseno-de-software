from abc import ABC, abstractmethod

class Operation(ABC):
    @abstractmethod
    def execute(self, num1, num2):
        """Ejecuta la operación y devuelve el resultado."""

        pass

class Addition(Operation):
    def execute(self, num1, num2):
        """Realiza la suma de los números y devuelve el resultado."""

        return num1 + num2

class Subtraction(Operation):
    def execute(self, num1, num2):
        """Realiza la resta de los números y devuelve el resultado."""

        return num1 - num2

class Multiplication(Operation):
    def execute(self, num1, num2):
        """Realiza la multiplicación de los números y devuelve el resultado."""

        return num1 * num2

class Division(Operation):
    def execute(self, num1, num2):
        """Realiza la división de los números y devuelve el resultado."""

        if num2 == 0:
            raise ZeroDivisionError("No se puede dividir por cero")
        return num1 / num2

# Patrón creacional: Factory Method
class OperationFactory:
    def get_operation_instance(self, operator):
        """Crea una instancia de la operación correspondiente según el operador dado."""
        
        if operator == '+':
            return Addition()
        elif operator == '-':
            return Subtraction()
        elif operator == '*':
            return Multiplication()
        elif operator == '/':
            return Division()
        else:
            raise ValueError("Operador no válido")

from abc import ABC, abstractmethod

class Operation(ABC):
    @abstractmethod
    def execute(self):
        pass

class Addition(Operation):
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def execute(self):
        return self.num1 + self.num2

class Subtraction(Operation):
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def execute(self):
        return self.num1 - self.num2

class Multiplication(Operation):
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def execute(self):
        return self.num1 * self.num2

class Division(Operation):
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def execute(self):
        if self.num2 == 0:
            raise ZeroDivisionError("No se puede dividir por cero")
        return self.num1 / self.num2

# Patrón estructural: Factory Method
class OperationFactory:
    def create_operation(self, operator, num1, num2):
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

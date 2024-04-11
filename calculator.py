from operation import OperationFactory

class Calculator:
    def __init__(self):
        """Inicializa la calculadora con una fábrica de operaciones."""
        self.operation_factory = OperationFactory()

    def calculate(self, operation_str):
        """Calcula el resultado de la operación ingresada por el usuario."""
        try:
            parts = operation_str.split()
            num1 = float(parts[0])
            num2 = float(parts[2])
            operator = parts[1]
            operation = self.operation_factory.create_operation(operator)
            return operation.execute(num1, num2)
        except (ValueError, IndexError, ZeroDivisionError) as e:
            print(f"Error al calcular: {e}")
            return None

from operation import OperationFactory

class Calculator:
    def __init__(self):
        self.operation_factory = OperationFactory()

    def run(self):
        while True:
            operation = input("Ingrese la operación a realizar (e.g., '2 + 2'): ")
            if operation.lower() == 'exit':
                break
            result = self.calculate(operation)
            print(f"El resultado es: {result}")

    def calculate(self, operation_str):
        try:
            parts = operation_str.split()
            num1 = float(parts[0])
            num2 = float(parts[2])
            operator = parts[1]
            operation = self.operation_factory.create_operation(operator, num1, num2)
            return operation.execute()
        except (ValueError, IndexError, ZeroDivisionError) as e:
            print(f"Error al calcular: {e}")
            return None

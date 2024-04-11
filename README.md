# Calculadora-Diseno-de-software

## Descripción del proyecto

Este es el entregable del proyecto final de la materia Diseño de Software. En este proyecto se realizó un código de Python con el propósito de cumplir con la mayoría de los puntos de la rúbrica y haciéndolo lo más sencillo posible.

El objetivo del código es mostrar una interfaz grafica en la cual puedas meter una operación con utilizando un solo operador (+, -, \* y /) y el programa debe de identificar los dos números y el operador, para cuando seleccionen el botón calcular pueda realizar la operación adecuada.

La estructura del código se divide en 4 archivos. El archivo main.py se encarga de correr inicialmente el programa para despues llamar a la interfaz gráfica. El archivo interfaz_grafica.py contiene el código de la interfaz grafica y se encarga de llamar a la clase Calcular, a la cual le pasa la entrada de texto. El archivo calculator.py se encarga de recibir la operación (“2 + 2”), separar los dos números y el signo mediante los espacios y despues llama a al método get_operation_instance() de la clase OperationFactory el cual retorna una instancia de una clase que se encarga de recibir los dos valores numéricos y retornar un resultado. Por ultimo se encuentra el archivo operation.py el cual contiene la clase con el método “Factory Method” y las otras clases implementadas para el funcionamiento de las operaciones.

## Integrantes del equipo

- Pablo Vergara Escoto 734178

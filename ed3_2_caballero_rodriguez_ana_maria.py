"""
Este es un módulo que implementa una calculadora científica.
Contiene operaciones matemáticas como suma, resta, multiplicación, división,
y funciones avanzadas como logaritmo, seno, coseno, tangente, etc.

Este archivo también configura un logger para registrar eventos importantes
y errores en las operaciones realizadas.
"""
import math
import logging
import sys

# Configuración del logging para escribir tanto en archivo como en consola
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# Configurar el logger
logger = logging.getLogger('CalculadoraCientifica')
logger.setLevel(logging.INFO)

# Handler para archivo
FILE_HANDLER = logging.FileHandler('calculadora.log')
FILE_HANDLER.setFormatter(formatter)

# Handler para consola
CONSOLE_HANDLER = logging.StreamHandler(sys.stdout)
CONSOLE_HANDLER.setFormatter(formatter)

# Añadir ambos handlers al logger
logger.addHandler(FILE_HANDLER)
logger.addHandler(CONSOLE_HANDLER)

class CalculadoraCientifica:
    """Clase que implementa operaciones científicas básicas y avanzadas"""

    def __init__(self):
        logger.info("Iniciando calculadora científica")

    @staticmethod
    def validar_numeros(*args):
        """Valida que los argumentos sean números"""
        for num in args:
            if not isinstance(num, (int, float)):
                raise TypeError(f"Se esperaba un número, se recibió {type(num)}")

    def sumar(self, a, b):
        """Suma dos números"""
        self.validar_numeros(a, b)
        logger.info("Sumando %d + %d", a, b)
        return a + b

    def restar(self, a, b):
        """Resta dos números"""
        self.validar_numeros(a, b)
        logger.info("Restando %d - %d", a, b)
        return a - b

    def multiplicar(self, a, b):
        """Multiplica dos números"""
        self.validar_numeros(a, b)
        logger.info("Multiplicando %d * %d", a, b)
        return a * b

    def dividir(self, a, b):
        """Divide dos números"""
        self.validar_numeros(a, b)
        if b == 0:
            logger.error("Intento de división por cero")
            raise ValueError("No se puede dividir por cero")
        logger.info("Dividiendo %d / %d", a, b)
        return a / b

    def potencia(self, base, exponente):
        """Calcula la potencia de un número"""
        self.validar_numeros(base, exponente)
        logger.info("Calculando %d ^ %d", base, exponente)
        return math.pow(base, exponente)

    def raiz_cuadrada(self, numero):
        """Calcula la raíz cuadrada de un número"""
        self.validar_numeros(numero)
        if numero < 0:
            logger.error("Intento de calcular raíz cuadrada de número negativo: %d", numero)
            raise ValueError("No se puede calcular la raíz cuadrada de un número negativo")
        logger.info("Calculando raíz cuadrada de %d", numero)
        return math.sqrt(numero)

    def logaritmo_natural(self, numero):
        """Calcula el logaritmo natural de un número"""
        self.validar_numeros(numero)
        if numero <= 0:
            logger.error("Intento de calcular logaritmo de número no positivo: %d", numero)
            raise ValueError("No se puede calcular el logaritmo de un número menor o igual a cero")
        logger.info("Calculando logaritmo natural de %d", numero)
        return math.log(numero)

    def logaritmo_base_10(self, numero):
        """Calcula el logaritmo en base 10 de un número"""
        self.validar_numeros(numero)
        if numero <= 0:
            logger.error("Intento de calcular logaritmo base 10 de número no positivo: %d", numero)
            raise ValueError("No se puede calcular el logaritmo de un número menor o igual a cero")
        logger.info("Calculando logaritmo base 10 de %d", numero)
        return math.log10(numero)

    def seno(self, angulo):
        """Calcula el seno de un ángulo en radianes"""
        self.validar_numeros(angulo)
        logger.info("Calculando seno de %f radianes", angulo)
        return math.sin(angulo)

    def coseno(self, angulo):
        """Calcula el coseno de un ángulo en radianes"""
        self.validar_numeros(angulo)
        logger.info("Calculando coseno de %f radianes", angulo)
        return math.cos(angulo)

    def tangente(self, angulo):
        """Calcula la tangente de un ángulo en radianes"""
        self.validar_numeros(angulo)
        logger.info("Calculando tangente de %f radianes", angulo)
        return math.tan(angulo)
def main():
    """Punto de entrada del programa"""
    calc = CalculadoraCientifica()

    try:
        # Solicitar dos números al usuario
        print("\n=== Calculadora Científica ===")
        a = float(input("Introduce el primer número: "))
        b = float(input("Introduce el segundo número: "))

        # Realizar operaciones y mostrar resultados
        print("\n=== Resultados de las Operaciones ===")
        print(f"Suma: {calc.sumar(a, b)}")
        print(f"Resta: {calc.restar(a, b)}")
        print(f"Multiplicación: {calc.multiplicar(a, b)}")
        try:
            print(f"División: {calc.dividir(a, b)}")
        except ValueError as e:
            print(f"División: Error - {e}")

        print(f"Potencia ({a} ^ {b}): {calc.potencia(a, b)}")
        print(f"Raíz Cuadrada del primer número ({a}): {calc.raiz_cuadrada(a)}")
        print(f"Logaritmo Natural del primer número ({a}): {calc.logaritmo_natural(a)}")
        print(f"Logaritmo Base 10 del primer número ({a}): {calc.logaritmo_base_10(a)}")
        print(f"Seno del primer número ({a}): {calc.seno(a)}")
        print(f"Coseno del primer número ({a}): {calc.coseno(a)}")
        print(f"Tangente del primer número ({a}): {calc.tangente(a)}")

    except ValueError as error:
        logger.error("Error de valor: %s", str(error))
        print(f"Error de valor: {error}")
    except TypeError as error:
        logger.error("Error de tipo: %s", str(error))
        print(f"Error de tipo: {error}")
    except Exception as error:  # pylint: disable=broad-except
        logger.error("Error inesperado: %s", str(error))
        print(f"Error inesperado: {error}")


if __name__ == "__main__":
    main()

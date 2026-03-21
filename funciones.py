def calcular_area_circulo(radio):
    """
    Calcula el area de un circulo.

    Args:
        radio (float): Radio del circulo.

    Returns:
        float: Area calculada con la formula pi * r^2.
    """
    pi = 3.1416
    return pi * radio ** 2

radio = float(input("Ingresa el radio del circulo: "))
area = calcular_area_circulo(radio)
print("El area del circulo es:", area)


def calcular_factorial(n):
    factorial = 1

    for i in range(1, n + 1):
        factorial = factorial * i

    return factorial

numero = int(input("Ingresa un numero: "))
print("El factorial es:", calcular_factorial(numero))


def primeros_fibonacci(n):
    serie = []
    a, b = 0, 1

    for i in range(n):
        serie.append(a)
        a, b = b, a + b

    return serie

numero = int(input("Ingresa la cantidad de numeros Fibonacci: "))
print(primeros_fibonacci(numero))


def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

grados = float(input("Ingresa los grados Celsius: "))
print("Grados Fahrenheit:", celsius_a_fahrenheit(grados))


def es_primo(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

numero = int(input("Ingresa un numero: "))
print(es_primo(numero))


def maximo_lista(lista):
    if len(lista) == 0:
        return None

    maximo = lista[0]

    for numero in lista:
        if numero > maximo:
            maximo = numero

    return maximo

numeros = [3, 8, 2, 15, 6]
print("El maximo es:", maximo_lista(numeros))

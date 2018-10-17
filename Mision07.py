# Autor Humberto Carrillo Gómez
# Descripción: Este programa despliega un menú con diversas funciones que utilizan el ciclo while.


def dividir(dividendo, divisor):         # Recibe un dividendo y un divisor y calcula el resultado y el cociente
    d1 = dividendo
    cociente = 0

    while dividendo >= divisor:
        dividendo = dividendo - divisor
        cociente = cociente + 1

    print('%d / %d = %d, sobra %d' % (d1, divisor, cociente, dividendo))


def encontrarMayor ():   # Devuelve el numéro mayor de una lista de números.

    mayor = 0
    valor = int(input("Teclea un número [Teclea -1 para salir]: "))
    if valor == -1:
        print('No hay valor mayor')
    else:
        while valor != -1:
            numero = int(input("Teclea una serie de números para encontrar el mayor: "))
            if numero > mayor:
                mayor = numero
            if numero == -1:
                break
        print('El mayor es: ', mayor)


def menu ():                           # Despliega un menu con las opciones que puede elegir el usuario
    print("Misión 07", "Ciclos While")
    print("Autor:", "Humberto Carrillo Gómez")
    print("Marícula:", "A01377246")
    print("1.", "Calcular divisiones")
    print("2.", "Encontrar el mayor")
    print("3.", "Salir")
    opcion = int(input("Teclea tu opción: "))
    print("")
    return opcion


def main():        # Función principal: Resuelve el problema
    opcion = menu()
    while opcion != 3:
        if opcion == 1:
            dividir(190, 50)              # En el paréntesis se teclean el dividendo y el divisor.
        if opcion == 2:
            encontrarMayor()
        if opcion != 1 and opcion != 2 and opcion != 3:
            print('Error', ',' 'Teclea 1, 2 o 3')
        print('')
        print('')
        opcion = menu()
    if opcion == 3:
        print("Gracias por utilizar este programa, regresa pronto.")


main()  # Llamada a la función principal

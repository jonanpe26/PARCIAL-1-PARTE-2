def mcd(a, b):
    if b == 0:
        return a
    return mcd(b, a % b)

def repetir(c, n):
    if n <= 0:
        return ""
    return c + repetir(c, n - 1)

def contar(cadena, letra, i=0):
    if i == len(cadena):
        return 0
    suma = 1 if cadena[i] == letra else 0
    return suma + contar(cadena, letra, i + 1)



def menu():
    while True:
        print("1. calcular el MCD de dos numeros")
        print("2. crear una cadena repetida N veces")
        print("3. contar cuantas veces aparece una letra en una cadena")
        print("4. convertir un numero decimal a binario")
        print("5. calcular cuantos digitos tienen un numero")
        print("6. salir")
        op =

        match case:

            case 1:
                a=int(input("ingrese el valor del primer numero"))
                b=int(input("ingrese el valor del segundo numero"))


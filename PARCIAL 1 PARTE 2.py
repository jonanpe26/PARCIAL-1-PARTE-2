def mcd(a,b):
    if b==0:
        return a
    return mcd(b,a%b)

def repetir(c,n):
    if n<=0:
        return ""
    return c + repetir(c,n-1)

def contar(cadena,letra,i=0):
    if i==len(cadena):
        return 0
    suma=1 if cadena[i]==letra else 0
    return suma+contar(cadena,letra,i+1)

def binario(n):
    if n==0:
        return ""
    return binario(n//2)+str(n%2)

def calcular(n):
    if n <0:
        n =-n
    if n < 10:
        return 1
    return 1+calcular(n//10)


def menu():
    while True:
        print("1. calcular el MCD de dos numeros")
        print("2. crear una cadena repetida N veces")
        print("3. contar cuantas veces aparece una letra en una cadena")
        print("4. convertir un numero decimal a binario")
        print("5. calcular cuantos digitos tienen un numero")
        print("6. salir")
        op = int(input("ingrese opcion"))

        match op:

            case 1:
                a=int(input("ingrese el valor del primer numero"))
                b=int(input("ingrese el valor del segundo numero"))
                print(f"el MCD es{mcd}")

            case 2:
                palabra=int(input("ingrese la palabra"))
                veces=int(input("repetir cuantas veces"))
                print(f"resultado{repetir}")

            case 3:
                cadena=input("ingrese la palabra")
                letra=input("ingrese la letra que ")
                print(f"La letra {letra} aparece {contar} veces")

            case 4:
                decimal=int(input("ingrese el numero en decimal"))
                print(f"el numero {decimal} a binario es {binario}")

            case 5:
                numero=int(input("ingrese el numero"))
                print(f"el numero tiene {calcular} digitos")
            case 6:
                print("saliendo")
                break
        case_:
            print("Opcion invalida")


print()




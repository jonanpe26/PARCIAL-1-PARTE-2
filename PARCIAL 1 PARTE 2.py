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

while True:
        print("1. calcular el MCD de dos numeros")
        print("2. crear una cadena repetida N veces")
        print("3. contar cuantas veces aparece una letra en una cadena")
        print("4. convertir un numero decimal a binario")
        print("5. calcular cuantos digitos tienen un numero")
        print("6. salir")
        op = input("opcion")

        match op:
            case "1":
                a= int(input("ingres primer numero"))
                b=int(input("ingrese segundo numero"))
                print("MCD:", mcd(a, b))
            case "2":
                cadena = input("ingrese el texto")
                numero = int(input("cuantas veces"))
                print("Resultad", repetir(cadena, numero))
            case "3":
                cadena = input("ingrese le texto")
                letra = input("que letra desea contar")
                print("la letra aparece", contar(cadena, letra))
            case "4":
                n=int(input("ingres numero decimal"))
                if n==0:
                    print("binario 0")
                else:
                    print("Binario",binario(n))
            case "5":
                n = int(input("ingres numero"))
                print("digitos", calcular(n))
            case "6":
                print("saliendo")
                break
            case _:
                print("error")

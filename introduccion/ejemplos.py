def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    return a // b

def datosSumar():
    firstVal = int(input("Escoja un numero: "))
    secondVal = int(input("Escoja un numero: "))
    resultado = suma(firstVal, secondVal)
    return resultado

def datosRestar():
    firstVal = int(input("Escoja un numero: "))
    secondVal = int(input("Escoja un numero: "))
    resultado = resta(firstVal, secondVal)
    return resultado

def datosMultiplicar():
    firstVal = int(input("Escoja un numero: "))
    secondVal = int(input("Escoja un numero: "))
    resultado = multiplicacion(firstVal, secondVal)
    return resultado

def datosDividir():
    firstVal = int(input("Escoja un numero: "))
    secondVal = int(input("Escoja un numero: "))
    resultado = division(firstVal, secondVal)
    return resultado
#-----------------------------------------------------#





while True:
    print("1. para Sumar")
    print("2. para Restar")
    print("3. para Multiplicar")
    print("4. para Dividir")
    print("5. para Salir")
    calculo = int(input("Escoja que operacion desea realizar: "))
    match calculo:
        case 1:
            print(datosSumar())
        case 2:
            print(datosRestar())
        case 3:
            print(datosMultiplicar())
        case 4:
            print(datosDividir())
        case 5:
            break
        case _:
            print("Numero introducido no valido")
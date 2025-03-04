#calculadora 
def sumar(x,y):
    return x+y
def restar(x,y):
    return x-y
def multiplicar(x,y):
    return x*y
def dividir(x,y):
    if y == 0:
        return "Error: División por cero"
    else:
        return x/y
while True:
    v1 = float(input("Numero 1: "))
    v2 = float(input("Numero 2: "))
    x = sumar(v1,v2)
    print(f"La suma es: {x}")
    x = restar(v1,v2)
    print(f"La resta es: {x}") 
    x = multiplicar(v1,v2)
    print(f"La multuplicacion es: {x}")
    x = dividir(v1,v2)
    print(f"La division es: {x}")
num = 1
while num != 77:
    num = float(input("Ingrese un valor: "))
    
    if num > 0:
        print(f"{num} es mayor a 0")
    elif num < 0:
        print(f"{num} es menor a 0")
    else:
        print(f"{num} es igual a 0")
#Fernando, mayor o igual a dos numeros

num1 = float(input("Ingrese un numero: "))
num2 = float(input("Ingrese otro numero: "))

if num1 > num2:
    print(f"{num1} es mayor a {num2}")
    #par o impar
    if num1 % 2 == 0:
        print("es par")
    else:
        print("es impar")
elif num1 > num2:
    print(f"{num2} es mayor a {num1}")
    #par o impar
    if num2 % 2 == 0:
        print("es par")
    else:
        print("es impar")

else:
    print("Los numeros son iguales")
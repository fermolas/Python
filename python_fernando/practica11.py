#Fernando, user y admin
#Ejercicios prácticos sobre bucles N°6
#cuadrado y triangulo
for x in range(4):
    print("* " * 4)

#trinagulo
for x  in range(1,5):
    print("* " * x)
    
#borde
m = 5 #el for no toma 5
for x in range(m):
    if x == 0 or x == m-1:
        print("**********")
    else:
        print("*        *")
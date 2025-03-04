calificaciones = [2,5,5,4.5,1]
nombre = ["Moises","Camila","Fernanda","Pablo","Tania"]
lista_variada = [True, 10.5, "abc",[0,1,1]]

print("Estudiante: ", nombre[2])
print("Calificaion: ", calificaciones[-2])
print("lista dentro de otra ", lista_variada[3][0])
print("Imprimir un rango o slice ",nombre[1:3]) 
print(lista_variada)

#agregar elementos a una lista
nombre.append("Anibal")
print(nombre)
#remover elementps de una lista
nombre.remove("Pablo")
print(nombre)
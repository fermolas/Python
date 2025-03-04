#Función que detecta si un número es primo
import math
def esPrimo(num):
 for i in range(3,int(math.sqrt(num))+1,2):
  if num%i==0:
   return False
 return True
def listaPrimos(limite):
 print(2)
 for j in range(3,limite+1,2):
  if esPrimo(j):
   print(j)
listaPrimos(100)
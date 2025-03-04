from practica16 import Calculadora
#Calculadora Cientifica
class CalculadoraCientifica(Calculadora):

        def __init__(self):
            super()
        
        def factorial(self):
            factorial = 1
            for x in range(1, self.numero1 + 1):
                factorial = factorial * x
            return factorial
    
if __name__ == "__main__":
    casioFx = CalculadoraCientifica()
    casioFx.setNumeros(5,2)
    print(casioFx.factorial())
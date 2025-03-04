class Pokemon:
    #Definiion de un Pokemon
    #atributos
    nombre = None
    habilidad = None
    tipo = None
    #contructor
    def __init__(self, n, h, t):
        self.nombre = n
        self.habilidad = h
        self.tipo = t
    #metodos
    def verNombre(self):
        return self.nombre
    
    def atacar(self):
        print(f"{self.nombre} ataco")
    
    def defenderse(self):
        print(f"{self.nombre} se defendio")
        
if __name__  == "__main__":
    picachu1 = Pokemon("Picachu", "Trueno","Electrico")
    picachu1.atacar()
    picachu1.defenderse()
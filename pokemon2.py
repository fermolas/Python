class Pokemon:
    def __init__(self, nombre, tipo, nivel=1):
        """Constructor de la clase"""
        self.nombre = nombre
        self.tipo = tipo
        self.nivel = nivel
        self.vida = nivel * 10  # Vida basada en el nivel

    def atacar(self, otro_pokemon):
        """Método para atacar a otro Pokémon"""
        daño = self.nivel * 2  # Daño basado en el nivel
        otro_pokemon.vida -= daño
        print(f"{self.nombre} ataca a {otro_pokemon.nombre} y le quita {daño} puntos de vida.")
    
    def subir_nivel(self):
        """Método para subir de nivel"""
        self.nivel += 1
        self.vida += 10
        print(f"{self.nombre} ha subido al nivel {self.nivel}.")

    def __str__(self):
        """Representación en cadena del Pokémon"""
        return f"{self.nombre} (Tipo: {self.tipo}, Nivel: {self.nivel}, Vida: {self.vida})"

# Ejemplo de uso
pikachu = Pokemon("Pikachu", "Eléctrico", 5)
charmander = Pokemon("Charmander", "Fuego", 3)

print(pikachu)
print(charmander)

pikachu.atacar(charmander)
print(charmander)

charmander.subir_nivel()
print(charmander)

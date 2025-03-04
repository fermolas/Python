import random

class Pokemon:
    def __init__(self, nombre, vida, ataque):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque

    def atacar(self, otro_pokemon):
        dano = random.randint(self.ataque - 5, self.ataque + 5)
        otro_pokemon.vida -= dano
        print(f"{self.nombre} ataca a {otro_pokemon.nombre} causando {dano} de daño.")
        if otro_pokemon.vida <= 0:
            print(f"{otro_pokemon.nombre} ha sido derrotado!")
        else:
            print(f"Vida restante de {otro_pokemon.nombre}: {otro_pokemon.vida}")

# Crear Pokémon
pikachu = Pokemon("Pikachu", 100, 20)
charmander = Pokemon("Charmander", 100, 18)

# Simulación de batalla
print("¡Comienza la batalla!")
while pikachu.vida > 0 and charmander.vida > 0:
    pikachu.atacar(charmander)
    if charmander.vida > 0:
        charmander.atacar(pikachu)
    print("-")

print("La batalla ha terminado!")

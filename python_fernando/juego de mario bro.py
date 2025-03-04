import pygame
import sys

# Inicializar Pygame
pygame.init()

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

# Configuración de la pantalla
ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Super Mario Bros - Pygame")

# Reloj para controlar la velocidad del juego
reloj = pygame.time.Clock()

# Clase para el jugador (Mario)
class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))  # Red for Mario
        self.rect = self.image.get_rect()
        self.rect.center = (100, 500)
        self.velocidad = 5
        self.gravedad = 0.5
        self.velocidad_y = 0

    def actualizar(self):
        keys = pygame.key.get_pressed()

        # Movimiento horizontal
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.velocidad
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.velocidad
        
        # Movimiento vertical (salto)
        self.velocidad_y += self.gravedad
        self.rect.y += self.velocidad_y

        # Colisiones con el suelo (asumimos que el suelo está en la parte inferior de la pantalla)
        if self.rect.bottom >= ALTO:
            self.rect.bottom = ALTO
            self.velocidad_y = 0

    def saltar(self):
        if self.rect.bottom == ALTO:
            self.velocidad_y = -10  # Fuerza del salto

# Crear el jugador
jugador = Jugador()
todos_los_sprites = pygame.sprite.Group()
todos_los_sprites.add(jugador)

# Bucle principal del juego
while True:
    pantalla.fill(BLANCO)

    # Manejo de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:  # Tecla para saltar
                jugador.saltar()

    # Actualizar todos los sprites
    todos_los_sprites.update()

    # Dibujar todos los sprites
    todos_los_sprites.draw(pantalla)

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar la velocidad de fotogramas
    reloj.tick(60)
    
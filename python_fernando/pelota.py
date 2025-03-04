import pygame
import sys

# Inicializamos Pygame
pygame.init()

# Definimos las dimensiones de la ventana
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pelota en movimiento")

# Definimos los colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Definimos las propiedades de la pelota
ball_radius = 20
ball_x = width // 2
ball_y = height // 2
ball_speed_x = 3
ball_speed_y = 3

# Bucle principal
while True:
    # Detectamos eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Movemos la pelota
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Colisiones con los bordes de la pantalla
    if ball_x - ball_radius <= 0 or ball_x + ball_radius >= width:
        ball_speed_x = -ball_speed_x
    if ball_y - ball_radius <= 0 or ball_y + ball_radius >= height:
        ball_speed_y = -ball_speed_y

    # Rellenamos la pantalla con negro
    screen.fill(BLACK)

    # Dibujamos la pelota
    pygame.draw.circle(screen, WHITE, (ball_x, ball_y), ball_radius)

    # Actualizamos la pantalla
    pygame.display.flip()

    # Controlamos la velocidad de actualización
    pygame.time.Clock().tick(60)

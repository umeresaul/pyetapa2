import pygame
import sys
import random

# Inicializa Pygame
pygame.init()

# Establece las dimensiones de la ventana
ventana = pygame.display.set_mode((800, 600))

# Establece el título de la ventana
pygame.display.set_caption("Juego de la Viborita")

# Define los colores
negro = (0, 0, 0)
blanco = (255, 255, 255)
rojo = (255, 0, 0)

# Define la viborita y su dirección inicial
viborita = [(200, 200), (220, 200), (240, 200)]
direccion = "DERECHA"

# Define la manzana y su posición inicial
manzana = (400, 300)

# Bucle principal del juego
while True:
    # Maneja los eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_UP and direccion != "ABAJO":
                direccion = "ARRIBA"
            elif evento.key == pygame.K_DOWN and direccion != "ARRIBA":
                direccion = "ABAJO"
            elif evento.key == pygame.K_LEFT and direccion != "DERECHA":
                direccion = "IZQUIERDA"
            elif evento.key == pygame.K_RIGHT and direccion != "IZQUIERDA":
                direccion = "DERECHA"

    # Mueve la viborita
    cabeza = viborita[-1]
    if direccion == "ARRIBA":
        nueva_cabeza = (cabeza[0], cabeza[1] - 20)
    elif direccion == "ABAJO":
        nueva_cabeza = (cabeza[0], cabeza[1] + 20)
    elif direccion == "IZQUIERDA":
        nueva_cabeza = (cabeza[0] - 20, cabeza[1])
    elif direccion == "DERECHA":
        nueva_cabeza = (cabeza[0] + 20, cabeza[1])
    viborita.append(nueva_cabeza)

    # Verifica si la viborita se ha comido a sí misma
    if nueva_cabeza in viborita[:-1]:
        pygame.quit()
        sys.exit()

    # Verifica si la viborita ha comido la manzana
    if nueva_cabeza == manzana:
        manzana = (random.randint(0, 780), random.randint(0, 580))
    else:
        viborita.pop(0)

    # Dibuja la ventana
    ventana.fill(negro)
    for pos in viborita:
        pygame.draw.rect(ventana, blanco, pygame.Rect(pos[0], pos[1], 20, 20))
    pygame.draw.rect(ventana, rojo, pygame.Rect(manzana[0], manzana[1], 20, 20))
    pygame.display.update()

    # Limita la velocidad del juego
    pygame.time.delay(100)
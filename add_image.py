import pygame

pygame.init()

screen = pygame.display.set_mode((1000, 1000))

surface = pygame.image.load('./Apple Fruit Ninja.png')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.blit(surface, (500, 500))

    pygame.display.update()

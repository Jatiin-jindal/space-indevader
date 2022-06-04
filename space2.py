import pygame
pygame.init()

window = pygame.display.set_mode((800 , 600))
background = pygame.image.load("space_indevader1/background.png")

while True:
    window.blit(background,(0 , 0))
    for event in pygame.event.get():
        if event.type == pygame.quit:
            window.quit()

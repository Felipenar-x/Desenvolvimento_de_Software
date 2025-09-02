import pygame
from sys import exit

pygame.display.set_caption("Loading Screen Example")
clock = pygame.time.Clock()
tela = pygame.display.set_mode((600, 800))
pygame.init()


barra = pygame.Surface((500,50))
barra.fill((255, 255, 255))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    # dar um update nos elementos e desenhar na tela
    tela.blit(barra, (50, 150))


    pygame.display.update()
    clock.tick(60)


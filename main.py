import pygame
from jogo import Jogo 

# Inicializando o jogo
pygame.init()
jogo = Jogo()

running = True
while running:
    for event in pygame.event.get():
        running = jogo.processar_eventos(event)
    
    jogo.desenhar_tela()

pygame.quit()

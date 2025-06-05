import pygame

# Inicializando pygame
pygame.init()

# Definições de tela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo Matemático")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Fonte
font = pygame.font.Font(None, 36)

# Sons
pygame.mixer.init()
correct_sound = pygame.mixer.Sound("game/assets/correct.wav")  # Som de acerto
wrong_sound = pygame.mixer.Sound("game/assets/wrong.wav")  # Som de erro

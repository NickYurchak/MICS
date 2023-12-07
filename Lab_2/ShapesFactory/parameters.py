import pygame
import random
from shape import Shape

# Ініціалізація Pygame
pygame.init()

# Розміри вікна
WINDOW_WIDTH = 1264
WINDOW_HEIGHT = 768

# Колір фону
BACKGROUND_COLOR = (255, 255, 255)

# Колір фігур
SHAPE_COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]

# Ініціалізація вікна
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Генерація абстрактної картини")
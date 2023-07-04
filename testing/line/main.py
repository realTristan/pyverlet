from testing.config import draw_background, SCREEN
from objects.line import Line
import pygame

# Initialize pygame
pygame.init()

# Window Title
pygame.display.set_caption("pyverlet")

# Create a new line
line = Line((100, 100), 100, 30, 4)

# Game Loop
while 1:
    draw_background()
    line.draw(SCREEN)
    pygame.display.flip()


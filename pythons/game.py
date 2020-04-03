import pygame

pygame.init()
win = pygame.display.set_mode((500, 500))

f1 = pygame.font.Font(None, 36)
text1 = f1.render('Hello Привет', 1, (180, 0, 0))

run = True
while run:
    pygame.time.delay(100)
import pygame

pygame.init()
win = pygame.display.set_mode((500, 500))

myfont = pygame.font.SysFont("Comic Sans MS", 30)
textsurface = myfont.render("Some Text", False, (0, 0, 0))

run = True
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win.fill((255, 255, 255))
    pygame.display.flip()

pygame.quit()
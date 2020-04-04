import pygame

pygame.init()
win = pygame.display.set_mode((500, 500))

pygame.font.init()

def draw_text(surface, text, size, x, y):
    font = pygame.font.SysFont("Comic Sans MS", size)
    text_surface = font.render(text, True, (255, 255, 255))
    surface.blit(text_surface, (x, y))

run = True
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    draw_text(win, "Some Text", 30, 0, 0)
    pygame.display.flip()

pygame.quit()


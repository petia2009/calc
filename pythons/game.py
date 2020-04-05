import pygame

pygame.init()
win = pygame.display.set_mode((500, 500))

pygame.font.init()

texte = ""

x = 0

def enter_nuber(lenght):
    if lenght == "0":
        x = 0
    if lenght == "1":
        x = 10
    if lenght == "2":
        x = 20
    if lenght == "3":
        x = 30
    if lenght == "4":
        x = 40
    if lenght == "5":
        x = 50
    if lenght == "6":
        x = 60
    if lenght == "7":
        x = 70
    if lenght == "8":
        x = 80
    if lenght == "9":
        x = 90

def draw_text(surface, text, size, x, y):
    font = pygame.font.SysFont("Comic Sans MS", size)
    text_surface = font.render(text, True, (255, 255, 255))
    surface.blit(text_surface, (x, y))

run = True
while run:
    pygame.time.delay(100)
    draw_text(win, "you can't enter number > 9", 20, 0, 0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_0]:
        enter_nuber("0")
        draw_text(win, texte + "0", 30, x, 30)

    if keys[pygame.K_1]:
        enter_nuber("1")
        draw_text(win, texte + "1", 30, x, 30)

    if keys[pygame.K_2]:
        enter_nuber("2")
        draw_text(win, texte + "2", 30, x, 30)

    if keys[pygame.K_3]:
        enter_nuber("3")
        draw_text(win, texte + "3", 30, x, 30)

    if keys[pygame.K_4]:
        enter_nuber("4")
        draw_text(win, texte + "4", 30, x, 30)

    if keys[pygame.K_5]:
        enter_nuber("5")
        draw_text(win, texte + "5", 30, x, 30)

    if keys[pygame.K_6]:
        enter_nuber("6")
        draw_text(win, texte + "6", 30, x, 30)

    if keys[pygame.K_7]:
        enter_nuber("7")
        draw_text(win, texte + "7", 30, x, 30)

    if keys[pygame.K_8]:
        enter_nuber("8")
        draw_text(win, texte + "8", 30, x, 30)

    if keys[pygame.K_9]:
        enter_nuber("9")
        draw_text(win, texte + "9", 30, x, 30)


    pygame.display.flip()

pygame.quit()
import pygame

pygame.init()

window = pygame.display.set_mode([700, 500])
clock = pygame.time.Clock()

game = True
background_img = pygame.image.load("background2.png")
background_img = pygame.transform.scale(background_img, [700, 500])

player1_img = pygame.image.load("cyborg.png")
player1_img = pygame.transform.scale(player1_img, [50, 50])
player1_x = 120
player1_y = 40




text = pygame.font.Font(None, 30).render("Text", True, [0,0,0])
text_n2 = pygame.font.Font(None, 30).render("level", True, [20,0,30])
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
            pygame.quit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        player1_x += 5
    if keys[pygame.K_e]:
        player1_y += 5
    if keys[pygame.K_r]:
        player1_x -= 5
    if keys[pygame.K_t]:
        player1_y -= 5

    window.fill([123, 123, 123])
    window.blit(background_img, [0, 0])
    window.blit(player1_img, [player1_x, player1_y])
    window.blit(text, [20, 20])
    window.blit(text_n2, [20,50])
    pygame.display.flip()
    clock.tick(60)
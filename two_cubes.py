import pygame
import sys

pygame.init()

screen =pygame.display.set_mode((1360, 766))
pygame.display.toggle_fullscreen()

SCR = (0, 0, 0)
PLR = (250, 0, 0)
PLR2 = (0, 0, 250)

player = pygame.Rect(650, 350, 50, 50)
player2 = pygame.Rect(650, 200, 50, 50)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player.x -= 1
    if keys[pygame.K_d]:
        player.x += 1
    if keys[pygame.K_w]:
        player.y -= 1
    if keys[pygame.K_s]:
        player.y += 1
    if keys[pygame.K_LEFT]:
        player2.x -= 1
    if keys[pygame.K_RIGHT]:
        player2.x += 1
    if keys[pygame.K_UP]:
        player2.y -= 1
    if keys[pygame.K_DOWN]:
        player2.y += 1
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit()
    if keys[pygame.K_b]:
        PLR = (0, 0, 250)
    if keys[pygame.K_r]:
        PLR = (250, 0, 0)
    if keys[pygame.K_g]:
        PLR = (0, 250, 0)
    if keys[pygame.K_x]:
        PLR2 = (0, 0, 250)
    if keys[pygame.K_c]:
        PLR2 = (250, 0, 0)
    if keys[pygame.K_v]:
        PLR2 = (0, 250, 0)


    screen.fill(SCR)
    pygame.draw.rect(screen, PLR, player)
    pygame.draw.rect(screen, PLR2, player2)
    pygame.display.flip()

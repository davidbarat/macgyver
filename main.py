import pygame
from resources import create_dazzle
from resources import init

pygame.init()
go = True
clock = pygame.time.Clock()


# Main
while go:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            go = False

    init()
    create_dazzle()

    class macgyver:
        # mac_position = (450, 300)
        # mac_pic = pygame.image.load("resources/MacGyver.png").convert()
        # screen.blit(mac_pic, mac_position)

        def move(self):
            return 'move'

    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

pygame.quit()

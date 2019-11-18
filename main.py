import pygame
from resources import create_dazzle
pygame.init()

carryOn = True

clock = pygame.time.Clock()

# Main
while carryOn:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False

        class macgyver:
            position = ()

            def move(self):
                return 'move'

    create_dazzle()

    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

pygame.quit()

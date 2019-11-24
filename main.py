import pygame
import resources
from resources import create_dazzle
from resources import init

pygame.init()
go = True
clock = pygame.time.Clock()

init()
create_dazzle()


# Main
while go:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            go = False

    class macgyver:
        resources.mac_position

        def move(self):
            return 'move'

    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

pygame.quit()

import pygame
pygame.init()


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (49, 31, 222)


# Open a new window
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("MacGyver dazzle")


# The loop will carry on until the user exit the game
carryOn = True

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

# Main
while carryOn:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False

        class macgyver:
            position = ()


            def move(self):
                return 'move'

        # creating dazzle

        pygame.draw.line(screen, BLUE, [0, 0], [100, 100], 5)

        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(60)

pygame.quit()

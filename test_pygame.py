import pygame
pygame.init()


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (49, 31, 222)
width_line = 3

# Open a new window
size = (850, 650)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("MacGyver dazzle")

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

        # creating dazzle
        pygame.draw.rect(screen, WHITE, [50, 50, 750, 550], 1)
        pygame.draw.line(screen, BLUE, [100, 50], [100, 150], width_line)
        pygame.draw.line(screen, BLUE, [100, 150], [150, 150], width_line)
        pygame.draw.line(screen, BLUE, [150, 150], [150, 200], width_line)
        pygame.draw.line(screen, BLUE, [150, 200], [100, 200], width_line)
        pygame.draw.line(screen, BLUE, [100, 200], [100, 250], width_line)


        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(60)

pygame.quit()

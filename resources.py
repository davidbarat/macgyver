import pygame


WHITE = (255, 255, 255)
BLUE = (49, 31, 222)
width_line = 3

# create a window
size = (850, 650)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("MacGyver dazzle")

def create_dazzle():
    # creating dazzle
    pygame.draw.rect(screen, WHITE, [50, 50, 750, 550], 1)
    pygame.draw.line(screen, BLUE, [100, 50], [100, 150], width_line)
    pygame.draw.line(screen, BLUE, [100, 150], [150, 150], width_line)
    pygame.draw.line(screen, BLUE, [150, 150], [150, 200], width_line)
    pygame.draw.line(screen, BLUE, [150, 200], [100, 200], width_line)
    pygame.draw.line(screen, BLUE, [100, 200], [100, 250], width_line)
    pygame.draw.line(screen, BLUE, [50, 300], [150, 300], width_line)
    pygame.draw.line(screen, BLUE, [150, 300], [150, 250], width_line)
    pygame.draw.line(screen, BLUE, [150, 250], [200, 250], width_line)
    pygame.draw.line(screen, BLUE, [200, 250], [200, 100], width_line)
    pygame.draw.line(screen, BLUE, [200, 100], [300, 100], width_line)
    pygame.draw.line(screen, BLUE, [300, 100], [300, 350], width_line)
    pygame.draw.line(screen, BLUE, [300, 350], [200, 350], width_line)
    pygame.draw.line(screen, BLUE, [200, 350], [200, 400], width_line)
    pygame.draw.line(screen, BLUE, [150, 350], [150, 450], width_line)
    pygame.draw.line(screen, BLUE, [100, 400], [100, 500], width_line)
    pygame.draw.line(screen, BLUE, [100, 500], [200, 500], width_line)
    pygame.draw.line(screen, BLUE, [100, 550], [150, 550], width_line)
    pygame.draw.line(screen, BLUE, [150, 550], [150, 600], width_line)
    pygame.draw.line(screen, BLUE, [200, 600], [200, 550], width_line)
    pygame.draw.line(screen, BLUE, [200, 550], [350, 550], width_line)
    pygame.draw.line(screen, BLUE, [250, 150], [250, 300], width_line)
    pygame.draw.line(screen, BLUE, [250, 300], [200, 300], width_line)
    pygame.draw.line(screen, BLUE, [400, 600], [400, 500], width_line)
    pygame.draw.line(screen, BLUE, [400, 500], [500, 500], width_line)
    pygame.draw.line(screen, BLUE, [550, 600], [550, 550], width_line)
    pygame.draw.line(screen, BLUE, [550, 550], [750, 550], width_line)
    pygame.draw.line(screen, BLUE, [750, 550], [750, 400], width_line)
    pygame.draw.line(screen, BLUE, [550, 500], [700, 500], width_line)
    pygame.draw.line(screen, BLUE, [700, 500], [700, 350], width_line)
    pygame.draw.line(screen, BLUE, [700, 350], [800, 350], width_line)
    pygame.draw.line(screen, BLUE, [400, 350], [400, 400], width_line)
    pygame.draw.rect(screen, BLUE, [450, 350, 50, 50], width_line)
    pygame.draw.line(screen, BLUE, [550, 350], [550, 400], width_line)
    pygame.draw.line(screen, BLUE, [550, 300], [550, 250], width_line)











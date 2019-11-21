import pygame


white = (255, 255, 255)
blue = (49, 31, 222)
width_line = 3
initial_pos = (0, 0)


def init():

    # create window
    pygame.display.set_caption("MacGyver dazzle")
    global size
    global screen
    size = (850, 650)
    screen = pygame.display.set_mode(size)
    mac_position = (450, 300)
    mac_pic = pygame.image.load("resources/MacGyver.png").convert()
    keeper_position = (150, 600)
    keeper_pic = pygame.image.load("resources/Gardien.png").convert()
    screen.blit(mac_pic, mac_position)
    screen.blit(keeper_pic, keeper_position)


def create_dazzle():

    # creating dazzle
    file = open('lab.txt', 'r')
    rock_width = 0
    while 1:
        char = file.read(1)
        print(char)

        if not char:
            break
        if char == 'x':
            print(rock_width)
            rock_position = (rock_width, 200)
            rock_pic = pygame.image.load("resources/rock.png").convert()
            screen.blit(rock_pic, rock_position)
            rock_width += 50

    file.close()

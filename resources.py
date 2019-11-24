import pygame


def init():

    # create window
    pygame.display.set_caption("MacGyver dazzle")
    global size
    global screen
    size = (850, 650)
    screen = pygame.display.set_mode(size)


def create_dazzle():

    # creating dazzle
    file = open('lab.txt', 'r')
    cursor_width = 0
    cursor_height = 0
    while 1:
        char = file.read(1)

        if not char:
            break
        if char == 'x':
            cursor_position = (cursor_width, cursor_height)
            rock_pic = pygame.image.load("resources/rock.png").convert()
            screen.blit(rock_pic, cursor_position)
            cursor_width += 50

        if char == 'M':
            global mac_position
            cursor_position = (cursor_width, cursor_height)
            mac_position = cursor_position
            mac_pic = pygame.image.load("resources/MacGyver.png").convert()
            screen.blit(mac_pic, cursor_position)
            cursor_width += 50

        if char == 'G':
            cursor_position = (cursor_width, cursor_height)
            badguy_pic = pygame.image.load("resources/Gardien.png").convert()
            screen.blit(badguy_pic, cursor_position)
            cursor_width += 50

        if char == '.':
            cursor_position = (cursor_width, cursor_height)
            floor_pic = pygame.image.load("resources/floor.png").convert()
            screen.blit(floor_pic, cursor_position)
            cursor_width += 50

        if char == '\n':
            cursor_width = 0
            cursor_height += 50

    file.close()

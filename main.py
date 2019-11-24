import pygame
import resources
# from resources import create_dazzle
# from resources import init_screen

pygame.init()
go = True
clock = pygame.time.Clock()

# init_screen()
# create_dazzle()


class dazzle():

    def __init__(self):
        print('init dazzle')

    def init_screen(self):

        # create window
        pygame.display.set_caption("MacGyver dazzle")
        global size
        global screen
        size = (850, 650)
        screen = pygame.display.set_mode(size)

    def create_dazzle(self):

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
                rock_pic = pygame.image.load(
                    "resources/rock.png").convert()
                screen.blit(rock_pic, cursor_position)
                cursor_width += 50

            if char == 'M':
                global mac_position
                cursor_position = (cursor_width, cursor_height)
                mac_position = cursor_position
                mac_pic = pygame.image.load(
                    "resources/MacGyver.png").convert()
                screen.blit(mac_pic, cursor_position)
                cursor_width += 50

            if char == 'G':
                cursor_position = (cursor_width, cursor_height)
                badguy_pic = pygame.image.load(
                    "resources/Gardien.png").convert()
                screen.blit(badguy_pic, cursor_position)
                cursor_width += 50

            if char == '.':
                cursor_position = (cursor_width, cursor_height)
                floor_pic = pygame.image.load(
                    "resources/floor.png").convert()
                screen.blit(floor_pic, cursor_position)
                cursor_width += 50

            if char == '\n':
                cursor_width = 0
                cursor_height += 50

        file.close()


class character(dazzle):

    def __init__(self):
        print('init class character')

    def move(self, direction):
        if direction == 'down':
            mac_initial_position = mac_position
            mac_initial_position_list = list(mac_position)
            print(mac_initial_position_list)
            rock_pic = pygame.image.load(
                "resources/floor.png").convert()
            screen.blit(rock_pic, mac_initial_position)
            new_mac_position_list = [x + 50 for x in mac_initial_position_list[:2]]
            print(new_mac_position_list)
            mac_pic = pygame.image.load(
                "resources/MacGyver.png").convert()
            screen.blit(mac_pic, tuple(new_mac_position_list))


mydazzle = dazzle()
mydazzle.init_screen()
mydazzle.create_dazzle()

# Main
while go:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            go = False
        if event.type == pygame.KEYDOWN:
            print('hello keydown')
            # key = keydown
            macgyver = character()
            macgyver.move('down')

    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

pygame.quit()

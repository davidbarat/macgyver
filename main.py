import pygame
# import resources
# from resources import create_dazzle
# from resources import init_screen

pygame.init()
go = True
clock = pygame.time.Clock()


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

    def get_limit_dazzle(self):

        file = open('resources/lab.txt', 'r')
        numberofline = 0
        for line in file:
            numberofline += 1

        numberofline -= 1  # we start at coord (0,0)
        return numberofline * 50

    def create_dazzle(self):

        # creating dazzle
        file = open('resources/lab.txt', 'r')
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
    flag = 0

    def __init__(self):
        # global mac_initial_position_list
        self.mac_initial_position_list = list(mac_position)
        # self.mac_final_position = []
        # self.mac_initial_width = 0
        # self.mac_initial_eight = 0

    def move(self, direction):
        global mac_initial_position_list
        global mac_final_position
        if direction == 'down':
            if not self.flag:
                print(self.flag)
                print(mac_position)
                print(self.mac_initial_position_list)
                self.mac_initial_position_width = self.mac_initial_position_list[0]
                self.mac_initial_position_eight = self.mac_initial_position_list[1]
                self.rock_pic = pygame.image.load(
                    "resources/floor.png").convert()
                screen.blit(self.rock_pic, self.mac_initial_position_list)
                self.mac_initial_position_eight += 50
                self.mac_pic = pygame.image.load(
                    "resources/MacGyver.png").convert()
                screen.blit(self.mac_pic, (
                    self.mac_initial_position_width,
                    self.mac_initial_position_eight))
                self.mac_final_position = [self.mac_initial_position_width,
                                           self.mac_initial_position_eight]
                self.flag += 1

            else:
                self.mac_initial_position_width = self.mac_final_position[0]
                self.mac_initial_position_eight = self.mac_final_position[1]
                # print(mac_initial_position)
                print(height_limit)
                print(self.mac_initial_position_eight)
                if self.mac_initial_position_eight >= height_limit:
                    print('no move')
                else:
                    self.rock_pic = pygame.image.load(
                        "resources/floor.png").convert()
                    screen.blit(self.rock_pic, (
                        self.mac_initial_position_width,
                        self.mac_initial_position_eight))
                    self.mac_initial_position_eight += 50
                    mac_pic = pygame.image.load(
                        "resources/MacGyver.png").convert()
                    screen.blit(mac_pic, (
                        self.mac_initial_position_width,
                        self.mac_initial_position_eight))
                    self.mac_final_position = [self.mac_initial_position_width,
                                               self.mac_initial_position_eight]
                    self.flag += 1


mydazzle = dazzle()
mydazzle.init_screen()
mydazzle.create_dazzle()
height_limit = mydazzle.get_limit_dazzle()
macgyver = character()

# Main
while go:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            go = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                macgyver.move('down')

    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

pygame.quit()

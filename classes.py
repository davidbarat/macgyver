import pygame
import random


class maze():
    # mac_position = []

    def __init__(self):

        print('init maze')
        self.list_position_rock = []
        self.mac_position = []
        # self.size = 0
        # self.screen = 0

    def init_screen(self):

        # create window
        pygame.display.set_caption("MacGyver maze")
        self.size = (900, 850)
        self.screen = pygame.display.set_mode(self.size)

    def get_limit_maze(self):

        # file = open('resources/lab.txt', 'r')
        with open('resources/lab.txt') as file:
            numberofline = 0
            for line in file:
                numberofline += 1
            numberofline -= 1  # we start at coord (0,0)
            return numberofline * 50

    def create_maze(self):

        # creating maze
        # file = open('resources/lab.txt', 'r')
        cursor_width = 0
        cursor_height = 0
        with open('resources/lab.txt') as file:
            while 1:
                char = file.read(1)

                if not char:
                    break
                if char == 'x':
                    cursor_position = (cursor_width, cursor_height)
                    rock_pic = pygame.image.load(
                        "resources/rock.png").convert()
                    self.screen.blit(rock_pic, cursor_position)
                    self.list_position_rock.append((cursor_width,
                                                    cursor_height))
                    cursor_width += 50

                if char == 'M':
                    cursor_position = [cursor_width, cursor_height]
                    self.mac_position = [cursor_width, cursor_height]
                    mac_pic = pygame.image.load(
                        "resources/MacGyver.png").convert()
                    self.screen.blit(mac_pic, cursor_position)
                    cursor_width += 50

                if char == 'G':
                    cursor_position = (cursor_width, cursor_height)
                    badguy_pic = pygame.image.load(
                        "resources/Gardien.png").convert()
                    self.screen.blit(badguy_pic, cursor_position)
                    cursor_width += 50

                if char == '.':
                    cursor_position = (cursor_width, cursor_height)
                    floor_pic = pygame.image.load(
                        "resources/floor.png").convert()
                    self.screen.blit(floor_pic, cursor_position)
                    cursor_width += 50

                if char == '\n':
                    cursor_width = 0
                    cursor_height += 50

            # print(self.list_position_rock)
            # file.close()
            # return self.list_position_rock, self.mac_position
            return self.list_position_rock


class character():

    def __init__(self):
        print('class character')
        # 15 sprites by 50 pixels
        self.width_limit = 14 * 50
        self.height_limit = 14 * 50
        self.width_min = 0
        self.height_min = 0
        self.count_object = 0
        # self.mac_final_position = maze.mac_position

    def check_wall(self, direction, list_rock, mac_position):
        self.mac_final_position = mac_position
        if direction == 'down':
            self.mac_initial_position_width = self.mac_final_position[0]
            self.mac_initial_position_eight = self.mac_final_position[1]
            self.test_position_rock = (self.mac_initial_position_width,
                                       self.mac_initial_position_eight + 50)
            # print(self.test_position_rock)

        if direction == 'up':
            self.mac_initial_position_width = self.mac_final_position[0]
            self.mac_initial_position_eight = self.mac_final_position[1]
            self.test_position_rock = (self.mac_initial_position_width,
                                       self.mac_initial_position_eight - 50)
            # print(self.test_position_rock)

        if direction == 'right':
            self.mac_initial_position_width = self.mac_final_position[0]
            self.mac_initial_position_eight = self.mac_final_position[1]
            self.test_position_rock = (self.mac_initial_position_width + 50,
                                       self.mac_initial_position_eight)
            # print(self.test_position_rock)

        if direction == 'left':
            self.mac_initial_position_width = self.mac_final_position[0]
            self.mac_initial_position_eight = self.mac_final_position[1]
            self.test_position_rock = (self.mac_initial_position_width - 50,
                                       self.mac_initial_position_eight)
            # print(self.test_position_rock)

        if (self.test_position_rock) in list_rock:
            return True
        else:
            return False


    def move(self, direction, mac_position, screen, list_position_object_coord):

        # self.mac_initial_position_list = list(mac_position)
        # print(self.mac_initial_position_list)
        # self.mac_initial_position_list = list(mac_position)
        print(self.mac_final_position)
        self.mac_initial_position_width = self.mac_final_position[0]
        self.mac_initial_position_eight = self.mac_final_position[1]
        print(self.mac_initial_position_width, self.mac_initial_position_eight)
        # self.mac_initial_position_width = mac_position[0]
        # self.mac_initial_position_eight = mac_position[1]
        print('move')
        # next move
        if direction == 'down':
            self.mac_initial_position_eight += 50
        if direction == 'up':
            self.mac_initial_position_eight -= 50
        if direction == 'right':
            self.mac_initial_position_width += 50
        if direction == 'left':
            self.mac_initial_position_width -= 50
        # print(self.width_limit)
        # print(self.height_limit)
        print(self.mac_initial_position_width)
        print(self.mac_initial_position_eight)
        if not (self.mac_initial_position_width > self.width_limit or self.mac_initial_position_eight > self.height_limit or self.mac_initial_position_width < self.width_min or self.mac_initial_position_eight < self.height_min):
            print('je peux mover')
            self.rock_pic = pygame.image.load(
                "resources/floor.png").convert()
            screen.blit(self.rock_pic, self.mac_final_position)
            self.mac_pic = pygame.image.load(
                "resources/MacGyver.png").convert()
            screen.blit(self.mac_pic, (
                        self.mac_initial_position_width,
                        self.mac_initial_position_eight))
            # print(mac_position)
            del self.mac_final_position
            self.mac_final_position = [self.mac_initial_position_width,
                                       self.mac_initial_position_eight]
            """ mac_position = [self.mac_initial_position_width,
                            self.mac_initial_position_eight]"""
            # print(list_position_object_coord)
            # print(self.mac_final_position)
            # print(list_position_object_coord)
            # self.coord_x_mac = self.mac_final_position[0]
            # self.coord_y_mac = self.mac_final_position[1]
            self.list_coord_mac = [(self.mac_final_position[0],
                                    self.mac_final_position[1])]

            print("compare position mac pos object")
            print(list_position_object_coord)
            print(self.list_coord_mac)
            for idx, i in enumerate(list_position_object_coord):
                if list(i) == self.mac_final_position:
                    """ attention count, il incremente mm qd
                    objet est déja récupéré"""
                    self.count_object += 1
                    self.font = pygame.font.SysFont('Comic Sans MS', 30)
                    self.color = (132, 0, 140)
                    self.text = self.font.render("Inventory", True, self.color)
                    # screen.blit(self.text, (775, 0))
                    if idx == 0:
                        self.object_pic = pygame.image.load(
                            "resources/ether.png").convert()
                        screen.blit(self.object_pic, (800, 50))
                    elif idx == 1:
                        self.object_pic = pygame.image.load(
                            "resources/aiguille.png").convert()
                        screen.blit(self.object_pic, (800, 150))
                    elif idx == 2:
                        self.object_pic = pygame.image.load(
                            "resources/tube.png").convert()
                        screen.blit(self.object_pic, (800, 250))

            return self.mac_final_position


class object():

    def __init__(self):

        # self.file = open('resources/lab.txt', 'r')
        self.object_height = 0
        self.object_width = 0
        self.list_position_object = []

    def get_position(self):

        with open('resources/lab.txt') as self.file:
            for char in self.file.read():
                if char == '.':
                    self.object_width += 50
                    self.list_position_object.append((self.object_width,
                                                      self.object_height))
                if char == '\n':
                    self.object_height += 50
                    self.object_width = 0

            self.final_position_object = random.sample(
                self.list_position_object, 3)
            # print(self.final_position_object)
            return(self.final_position_object)

    def print_pic(self, t_object, position_coord, screen):
        if t_object == 'tube':
            self.object_pic = pygame.image.load(
                "resources/tube.png").convert()
            screen.blit(self.object_pic, position_coord)
            # list_position_object_coord.append(position_coord)
        if t_object == 'aiguille':
            self.object_pic = pygame.image.load(
                "resources/aiguille.png").convert()
            screen.blit(self.object_pic, position_coord)
            # list_position_object_coord.append(position_coord)
        if t_object == 'ether':
            self.object_pic = pygame.image.load(
                "resources/ether.png").convert()
            screen.blit(self.object_pic, position_coord)
            # list_position_object_coord.append(position_coord)
        # print(list_position_object_coord)

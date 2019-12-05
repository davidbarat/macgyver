import pygame
import random


pygame.init()
go = True
clock = pygame.time.Clock()
list_object = ['ether', 'aiguille', 'tube']
picked_object = []
list_position_object_coord = []
# 15 sprites by 50 pixels
width_limit = 14 * 50
height_limit = 15 * 50
width_min = 0
height_min = 0


class dazzle():

    def __init__(self):

        print('init dazzle')
        self.list_position_rock = []

    def init_screen(self):

        # create window
        pygame.display.set_caption("MacGyver dazzle")
        global size
        global screen
        size = (900, 850)
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
                self.list_position_rock.append((cursor_width,
                                                cursor_height))
                cursor_width += 50

            if char == 'M':
                # global mac_position
                # self.mac_position
                cursor_position = (cursor_width, cursor_height)
                self.mac_position = cursor_position
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

        # print(self.list_position_rock)
        file.close()
        return self.list_position_rock, self.mac_position


class character():

    def __init__(self):
        print('class character')
        self.mac_final_position = mac_position

    def check_wall(self, direction, list_rock, mac_position):
        if direction == 'down':
            self.mac_initial_position_width = self.mac_final_position[0]
            self.mac_initial_position_eight = self.mac_final_position[1]
            self.test_position_rock = (self.mac_initial_position_width,
                                       self.mac_initial_position_eight + 50)
            print(self.test_position_rock)
            # check next position is a rock position
            if (self.test_position_rock) in list_rock:
                return True
            else:
                return False

        if direction == 'up':
            self.mac_initial_position_width = self.mac_final_position[0]
            self.mac_initial_position_eight = self.mac_final_position[1]
            self.test_position_rock = (self.mac_initial_position_width,
                                       self.mac_initial_position_eight - 50)
            print(self.test_position_rock)
            # check next position is a rock position
            if (self.test_position_rock) in list_rock:
                return True
            else:
                return False

        if direction == 'right':
            self.mac_initial_position_width = self.mac_final_position[0]
            self.mac_initial_position_eight = self.mac_final_position[1]
            self.test_position_rock = (self.mac_initial_position_width + 50,
                                       self.mac_initial_position_eight)
            print(self.test_position_rock)
            # check next position is a rock position
            if (self.test_position_rock) in list_rock:
                return True
            else:
                return False

        if direction == 'left':
            self.mac_initial_position_width = self.mac_final_position[0]
            self.mac_initial_position_eight = self.mac_final_position[1]
            self.test_position_rock = (self.mac_initial_position_width - 50,
                                       self.mac_initial_position_eight)
            print(self.test_position_rock)
            # check next position is a rock position
            if (self.test_position_rock) in list_rock:
                return True
            else:
                return False

    def move(self, direction, mac_position):
        self.mac_initial_position_list = list(mac_position)
        self.mac_initial_position_width = self.mac_final_position[0]
        self.mac_initial_position_eight = self.mac_final_position[1]
        # next move
        if direction == 'down':
            self.mac_initial_position_eight += 50
        if direction == 'up':
            self.mac_initial_position_eight -= 50
        if direction == 'right':
            self.mac_initial_position_width += 50
        if direction == 'left':
            self.mac_initial_position_width -= 50
        print(width_limit)
        print(height_limit)
        if not (self.mac_initial_position_width > width_limit or self.mac_initial_position_eight > height_limit or self.mac_initial_position_width < width_min or self.mac_initial_position_eight < height_min):
            self.rock_pic = pygame.image.load(
                "resources/floor.png").convert()
            screen.blit(self.rock_pic, self.mac_final_position)
            self.mac_pic = pygame.image.load(
                "resources/MacGyver.png").convert()
            screen.blit(self.mac_pic, (
                        self.mac_initial_position_width,
                        self.mac_initial_position_eight))
            # print(mac_position)
            self.mac_final_position = [self.mac_initial_position_width,
                                       self.mac_initial_position_eight]
            print(list_position_object_coord)
            print(self.mac_final_position)

            if list(self.mac_final_position) in list_position_object_coord:
                print('good')
                self.object_pic = pygame.image.load(
                    "resources/tube.png").convert()
                screen.blit(self.object_pic, (800, 50))
        # print(self.mac_final_position)


class object():

    def __init__(self):

        self.file = open('resources/lab.txt', 'r')
        self.object_height = 0
        self.object_width = 0
        self.list_position_object = []

    def get_position(self):

        for char in self.file.read():
            # print(char)
            if char == '.':
                self.object_width += 50
                self.list_position_object.append((self.object_width,
                                                  self.object_height))
            if char == '\n':
                self.object_height += 50
                self.object_width = 0

        self.final_position_object = random.choice(self.list_position_object)
        return(self.final_position_object)

    def print_pic(self, t_object, position_coord):
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


mydazzle = dazzle()
mydazzle.init_screen()
list_rock, mac_position = mydazzle.create_dazzle()

# item get position
for item in list_object:
    item_object = object()
    position_item = item_object.get_position()
    print(position_item)
    item_object.print_pic(item, position_item)
    list_position_object_coord.append(position_item)

macgyver = character()

# Main
while go:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            go = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                if not macgyver.check_wall('down', list_rock, mac_position):
                    macgyver.move('down', mac_position)
            if event.key == pygame.K_UP:
                if not macgyver.check_wall('up', list_rock, mac_position):
                    macgyver.move('up', mac_position)
            if event.key == pygame.K_RIGHT:
                if not macgyver.check_wall('right', list_rock, mac_position):
                    macgyver.move('right', mac_position)
            if event.key == pygame.K_LEFT:
                if not macgyver.check_wall('left', list_rock, mac_position):
                    macgyver.move('left', mac_position)

    pygame.display.flip()

    # Limit to 60 frames per second
    clock.tick(60)

pygame.quit()

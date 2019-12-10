import pygame
from classes import character
from classes import object
from classes import maze


pygame.init()
go = True
clock = pygame.time.Clock()
list_object = ['ether', 'aiguille', 'tube']
picked_object = []
list_position_object_coord = []

my_maze = maze()
my_maze.init_screen()
list_rock = my_maze.create_maze()
print('list rock')
print(list_rock)
position_keeper = my_maze.position_keeper
print(position_keeper)

for item in list_object:
    item_object = object()

position_item = item_object.get_position()
# print(position_item)

for idx, item in enumerate(list_object):
    item_object.print_pic(item, position_item[idx], my_maze.screen)
    list_position_object_coord = position_item

# print(list_position_object_coord)
macgyver = character()
count_object = macgyver.count_object

# Main
while go:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            go = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                # new_position_mac = my_maze.mac_position
                if not macgyver.check_wall('down',
                                           list_rock, my_maze.mac_position):
                    new_position_mac = macgyver.move('down',
                                                     my_maze.mac_position,
                                                     my_maze.screen,
                                                     list_position_object_coord
                                                     )
                else:
                    new_position_mac = my_maze.mac_position

            elif event.key == pygame.K_UP:
                if not macgyver.check_wall('up',
                                           list_rock, my_maze.mac_position):
                    new_position_mac = macgyver.move('up',
                                                     my_maze.mac_position,
                                                     my_maze.screen,
                                                     list_position_object_coord
                                                     )
                else:
                    new_position_mac = my_maze.mac_position

            elif event.key == pygame.K_RIGHT:
                if not macgyver.check_wall('right',
                                           list_rock, my_maze.mac_position):
                    new_position_mac = macgyver.move('right',
                                                     my_maze.mac_position,
                                                     my_maze.screen,
                                                     list_position_object_coord
                                                     )
                else:
                    new_position_mac = my_maze.mac_position

            elif event.key == pygame.K_LEFT:
                # print('left')
                if not macgyver.check_wall('left',
                                           list_rock, my_maze.mac_position):
                    # print('left')
                    new_position_mac = macgyver.move('left',
                                                     my_maze.mac_position,
                                                     my_maze.screen,
                                                     list_position_object_coord
                                                     )
                else:
                    new_position_mac = my_maze.mac_position
            if macgyver.check_win(new_position_mac,
                                  position_keeper,
                                  macgyver.count_object, my_maze.screen):
                print('c est win')

            my_maze.mac_position = new_position_mac
            print('count object ', macgyver.count_object)

    pygame.display.flip()

    # Limit to 60 frames per second
    clock.tick(60)

pygame.quit()

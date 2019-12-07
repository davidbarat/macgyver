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
# list_rock, mac_position = my_maze.create_maze()
list_rock = my_maze.create_maze()
# print('position de mac')
print(my_maze.mac_position)
david = my_maze.mac_position
print(david)
# item get position
for item in list_object:
    item_object = object()
    position_item = item_object.get_position()
    print(position_item)
    item_object.print_pic(item, position_item, my_maze.screen)
    list_position_object_coord.append(position_item)

macgyver = character()

# Main
while go:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            go = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                if not macgyver.check_wall('down',
                                           list_rock, my_maze.mac_position):
                    new_position_mac = macgyver.move('down',
                                                     my_maze.mac_position,
                                                     my_maze.screen,
                                                     list_position_object_coord
                                                     )
            if event.key == pygame.K_UP:
                if not macgyver.check_wall('up',
                                           list_rock, my_maze.mac_position):
                    new_position_mac = macgyver.move('up',
                                                     my_maze.mac_position,
                                                     my_maze.screen,
                                                     list_position_object_coord
                                                     )
            if event.key == pygame.K_RIGHT:
                if not macgyver.check_wall('right',
                                           list_rock, my_maze.mac_position):
                    new_position_mac = macgyver.move('right',
                                                     my_maze.mac_position,
                                                     my_maze.screen,
                                                     list_position_object_coord
                                                     )
            if event.key == pygame.K_LEFT:
                if not macgyver.check_wall('left',
                                           list_rock, my_maze.mac_position):
                    new_position_mac = macgyver.move('left',
                                                     my_maze.mac_position,
                                                     my_maze.screen,
                                                     list_position_object_coord
                                                     )
            my_maze.mac_position = new_position_mac

    pygame.display.flip()

    # Limit to 60 frames per second
    clock.tick(60)

pygame.quit()

from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file =  "maps/test_line.txt" 
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt" 
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

# Start tansverse test code
opposite = {'n': 's', 's': 'n', 'e':'w', 'w': 'e'}
def travel(visited = set(), path):
    #set up place to get closest room with open direction (where we haven't explored yet)
    nearest = []
    #starts in this room
    room = player.current_room
    for direction in room.get_exits():
        player.travel(direction)
        if room in visited:
            player.travel(opposite[direction])
        else:
            room = player.current_room






# soltion round 1
# opposite = {'n': 's', 's': 'n', 'e':'w', 'w': 'e'}


# def traverse(room, visited = None):
#     if visited is None:
#         visited = set()

#     # create a path list
#     path = []
#     room = player.current_room

#     # Go through possible directions
#     for direction in room.get_exits():
#         player.travel(direction)
#         room = player.current_room

#         # if room is visited
#         if room in visited:
#             player.travel(opposite[direction])
#             # else add room to visited and direction to path
#         else:
#             visited.add(room)
#             path.append(direction)
#             #recursivly call function again on this room and add to path
#             path += traverse(room, visited)
#             player.travel(opposite[direction])
#             path.append(opposite[direction])
#     return path
                
# traversal_path = traverse(player.current_room)

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")

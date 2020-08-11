from room import Room
from player import Player
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
name = input('please input your player name: ')
player = Player(name, room['outside'])

# Write a loop that:
while True:

    print(f'{player} You are in {player.current_room.name} {player.current_room.description} !')
    player_input = input(
        f'Please choose which direction you would like to go \n [s] for SOUTH \n [n] for NORTH \n [e] for EAST \n [w] for WEST \n [q] to QUIT GAME \n :')

    if player_input == 'q':
        print("Thank you for playing")
        break
    if player_input == 's':
        player = Player(name, room['foyer'])
        print(f' {name} are now in {player.current_room}')
        break
    else:
        print("You cannot go in that direction, please choose another direction")

        #
        # If the user enters a cardinal direction, attempt to move to the room there.
        # Print an error message if the movement isn't allowed.
        #
        # If the user enters "q", quit the game.

from room import Room
from player import Player
from item import Item
# Declare all the rooms



item_list = {
    'cheeseburger': Item("cheeseburger", "Now thats a tasty burger"),
    'lizzo': Item("Lizzo", "Why a man great til he gotta be great"),
    'dumble_dore': Item("Dumble_dore", "Dumble dore the wizard"),
    'kimmy': Item("kimmy_shmidt", "Unbreakable! Females are strong as hell!"),
    'jian_yang': Item("jian_yang", "Erich Bachman this is your mom"),
}



room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [item_list['cheeseburger']]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",[item_list['lizzo'], item_list['dumble_dore']]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",[item_list['kimmy']]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",[item_list['kimmy']]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",[item_list['jian_yang']]),
}




# Link rooms together

room['outside'].n_to = room['foyer'] #goes from outside to foyer
room['foyer'].s_to = room['outside'] #goes from foyer to outside
room['foyer'].n_to = room['overlook'] #goes from the foyer to the overlook
room['foyer'].e_to = room['narrow']   #goes from the foyer to the narrow
room['overlook'].s_to = room['foyer'] #goes from the overlook to the foyer 
room['narrow'].w_to = room['foyer']   #goes from the narrow to the foyer
room['narrow'].n_to = room['treasure'] #goes from the narrow to the treasure
room['treasure'].s_to = room['narrow'] #goes from the treasure to the narrow

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
name = input('please input your player name: ')
player = Player(name, room['outside'])

# Write a loop that:
while True:
    for item in player.location.items:
        print(item)
    # print(f'{player} You are in {player.location.name} {player.location.description}!')
    location = input(
        f'Please choose which direction you would like to go \n [s] for SOUTH \n [n] for NORTH \n [e] for EAST \n [w] for WEST \n [q] to QUIT GAME \n :')

    if location == 'q':
        print('thank you for playing')
        break
    elif location == 'n':
        if hasattr(player.location, 'n_to'):
            player.location = player.location.n_to
    elif location == 's':
        if hasattr(player.location, 's_to'):
            player.location = player.location.s_to
        else:
            print('you cannot go there')
    elif location == 'w':
        if hasattr(player.location, 'w_to'):
            player.location = player.location.w_to
        else:
            print('you cannot go there')
    elif location == 'e':
        if hasattr(player.location, 'e_to'):
            player.location = player.location.e_to
        else:
            print('you cannot go there')                
    else:
        print('you cannot go there')

        #
        # If the user enters a cardinal direction, attempt to move to the room there.
        # Print an error message if the movement isn't allowed.
        #
        # If the user enters "q", quit the game.

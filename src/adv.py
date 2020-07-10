from room import Room
from player import Player
from item import Item

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


items = {
    "sword": Item("Sword", "A cool sword"),
    "grail": Item("The Holy Grail", "You chose... wisely"),
    "flask": Item("Ye Flask", "Better than some stupid Grail")
}

room["foyer"].add_item(items["sword"])
room["overlook"].add_item(items["flask"])
room["treasure"].add_item(items["grail"])
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
name = input("What is your name?\n")
player = Player(name, room["outside"])

valid_directions = ('n', 's', 'e', 'w')

# Write a loop that:
while True:
    # * Prints the current room name
    current_room = player.current_room
    print("\nCurrent Location:", current_room.name)

    # * Prints the current description (the textwrap module might be useful here).
    description = current_room.description
    # print(textwrap.wrap(description, 70))
    print(f"{description}\n")

    # * Waits for user input and decides what to do.
    direction = input("What would you like to do? \n").strip().lower().split()
    
    #
    # If the user enters a cardinal direction, attempt to move to the room there.
    
    ###### if direction == "n":
    ######     player.current_room = current_room.n_to

    ###### elif direction == "s":
    ######     player.current_room = current_room.s_to

    ###### elif direction == "w":
    ######     player.current_room = current_room.w_to

    ###### elif direction == "e":
    ######     player.current_room = current_room.e_to
    
    if direction[0].startswith(valid_directions):
        player.move(direction[0])
    # Print an error message if the movement isn't allowed.
    #
    # If the user enters "q", quit the game.
    
    elif direction[0].startswith("i"):
        current_room.list_items()
        print()
        player.list_items()

    ### direction = "take sword"
    elif direction[0].startswith("t"):
        item = items[direction[1]]
        if item in current_room.items:
            player.take_item(item)
            current_room.remove_item(item)
            item.on_take()
        elif item not in current_room.items:
            print(f"\n      There is no {item.name} in this room")


    elif direction[0].startswith("d"):
        item = items[direction[1]]
        if item in player.items:
            player.drop_item(item)
            current_room.add_item(item)
            item.on_drop()
        elif item not in current_room.items:
            print(f"\n      You are not carrying a {item.name}")
    
    elif direction[0].startswith("q"):
        break

#! python3
"""
Text adventure by Karl Weir

Here is a small adventure game I decided to make after reading
Mark Z. Danielewski's fantastic book, House of Leaves. 



The rooms in the game are numbered linearly. The player starts 
in room 1 then finds their way to room 2 ect. The players position
in each room is determined by XY coordinates. 

         Room 1

             0 1 2
             _ _ _
        0   |_|V|_|  0  Key:
   Y    1   |_|_|_|  1  @ = Player position
        2   |_|@|_|  2  V = Exit

             0 1 2 


               X

The position of the player is based on the room they are in, their X
coordinate and their Y coordinate respectively. Therefore in the 
above example the players position would be '112'.

              Room 2

            0 1 2 3 4
            _ _ _ _ _       
       0   |_|V|_|_|_|   0
       1   |_|_|_|_|_|   1
   Y   2   |_|_|_|_|_|   2
       3   |_|_|_|_|_|   3
       4   |_|_|@|_|_|   4

            0 1 2 3 4

And in this example the player position would be '224'. 



These constant variables are used because if I mistype them, Python will 
immediately throw up an error message since no variable with the typo
name will exist. If we mistyped the strings, the bugs that it produces would
be harder to find.
"""
SCREEN_WIDTH = 80

"""
The game world data is stored in a dictionary (which itself has dictionaries
and lists). Each dictionary value inside the world variable is a different
position in the game world. The key is a string of a coordinate (i.e '402')
that is the reference name of the location.

The value is another dictionary, which has keys 'desc', 'north', 'south',
'east', 'west', 'up', 'down', 'shop', and 'ground'. We use the constant
variables (e.g. DESC, NORTH, etc.) instead of strings in case we make
typos.

DESC is a text description of the area. GROUND is a list of items that are
on the ground in this area. The directions (NORTH, SOUTH, UP, etc.) are the
areas the exist in the direction.
"""

from world_data import (
    DESC, NORTH, SOUTH, EAST, WEST, UP, DOWN, NORTHDESC, SOUTHDESC,
    EASTDESC, WESTDESC, UPDESC, DOWNDESC, GROUND, SHOP, GROUNDDESC,
    SHORTDESC, LONGDESC, TAKEABLE, EDIBLE, OPENABLE, DESCWORDS,
    worldPositions, worldItems
)
"""
These variables track where the player is and what is in their inventory.
The value in the location variable will always be a key in the world variable
and the value in the inventory list will always be a key in the worldItems
variable.
"""

location = '112' # Start position ie 1 = room 1, 1 = X coordinate 1, 2 = Y coordinate 2.
inventory = [] # Start with blank inventory
playerHealth = 150
playerSanity = 1000
showExitDescriptions = True

import cmd, textwrap, time

def displayLocation(loc):
    """A helper function for displaying an area's description and exits."""

    # Print the room's description (using textwrap.wrap())
    print()
    print('\n'.join(textwrap.wrap(worldPositions[loc][DESC], SCREEN_WIDTH)))
    #print(location) #uncomment to see room IDs as you enter them

    # Print all the items on the ground.
    if len(worldPositions[loc][GROUND]) > 0:
        print()
        for item in worldPositions[loc][GROUND]:
            print(worldItems[item][GROUNDDESC])

    # Print all the 'positions' around the player
    exits = []
    # This part of the function checks which directions are in the array 'worldPositions'
    for direction in (NORTH, SOUTH, EAST, WEST, UP, DOWN): 
        if direction in worldPositions[loc].keys():
            exits.append(direction.title())
    print()
    # Print a description for each direction around the player
    print('=' * 50)
    if showExitDescriptions:
            for direction in (NORTH, SOUTH, EAST, WEST, UP, DOWN,):
                if direction in worldPositions[location]:
                    print('%s: %s' % (direction.title(), worldPositions[location][direction][1])) #Insert [1] after [direction to not print out room IDs]
    print('=' * 50)
def moveDirection(direction):
    """ A helper function that changes the location of the player."""
    global location

    if direction in worldPositions[location]:
        print()
        print('You move to the %s.' % direction)
        location = worldPositions[location][direction][0]
        displayLocation(location)
    else:
        print('Grey ash walls stop you from going further')

def getAllDescWords(itemList):
    """Returns a list of "description words" for each item named in itemList."""
    itemList = list(set(itemList)) # make itemList unique
    descWords = []
    for item in itemList:
        descWords.extend(worldItems[item][DESCWORDS])
    return list(set(descWords))

def getAllFirstDescWords(itemList):
    """Returns a list of the first "description word" in the list of
    description words for each item named in itemList."""
    itemList = list(set(itemList)) # make itemList unique
    descWords = []
    for item in itemList:
        descWords.append(worldItems[item][DESCWORDS][0])
    return list(set(descWords))

def getFirstItemMatchingDesc(desc, itemList):
    itemList = list(set(itemList)) # make itemList unique
    for item in itemList:
        if desc in worldItems[item][DESCWORDS]:
            return item
    return None

def getAllItemsMatchingDesc(desc, itemList):
    itemList = list(set(itemList)) # make itemList unique
    matchingItems = []
    for item in itemList:
        if desc in worldItems[item][DESCWORDS]:
            matchingItems.append(item)
    return matchingItems

class TextAdventureCmd(cmd.Cmd):
    prompt = '\n> '

    # The default() method is called when none of the other do_*() command methods match.
    def default(self, arg):
        print('I do not understand that command. Type "help" for a list of commands.')

    # A very simple "quit" command to terminate the program:
    def do_quit(self, arg):
        """Quit the game."""
        return True # this exits the Cmd application loop in TextAdventureCmd.cmdloop()


    # These direction commands have a long (i.e. north) and show (i.e. n) form.
    # Since the code is basically the same, I put it in the moveDirection()
    # function.
    def do_north(self, arg):
        """Go to the area to the north, if possible."""
        moveDirection('north')

    def do_south(self, arg):
        """Go to the area to the south, if possible."""
        moveDirection('south')

    def do_east(self, arg):
        """Go to the area to the east, if possible."""
        moveDirection('east')

    def do_west(self, arg):
        """Go to the area to the west, if possible."""
        moveDirection('west')

    def do_up(self, arg):
        """Go to the area upwards, if possible."""
        moveDirection('up')

    def do_down(self, arg):
        """Go to the area downwards, if possible."""
        moveDirection('down')

    # Since the code is the exact same, we can just copy the
    # methods with shortened names:
    do_n = do_north
    do_s = do_south
    do_e = do_east
    do_w = do_west
    do_u = do_up
    do_d = do_down

    def do_info(self, arg):
        """Display players current Health Points and Sanity."""
        print()
        print('Health: %i' % (playerHealth))
        if (playerHealth > 100):
            print('You\'re in good physical health.')
        else :
            print(' - You don\'t look so good. Find food and eat to replenish HP.')
        print('Sanity: %i' % (playerSanity))

    def do_exits(self, arg):
        """Toggle showing full exit descriptions or brief exit descriptions. Brief exit descriptions are basically hard mode."""
        global showExitDescriptions
        showExitDescriptions = not showExitDescriptions
        if showExitDescriptions:
            print('Showing full exit descriptions.')
        else:
            print('Showing brief exit descriptions.')

    
    def do_inventory(self, arg):
        """Display a list of the items in your possession."""

        if len(inventory) == 0:
            print('Inventory:\n  (nothing)')
            return

        # first get a count of each distinct item in the inventory
        itemCount = {}
        for item in inventory:
            if item in itemCount.keys():
                itemCount[item] += 1
            else:
                itemCount[item] = 1

        # get a list of inventory items with duplicates removed:
        print('Inventory:')
        for item in set(inventory):
            if itemCount[item] > 1:
                print('  %s (%s)' % (item, itemCount[item]))
            else:
                print('  ' + item)

    do_inv = do_inventory
    

    def do_take(self, arg):
        """"take <item> - Take an item on the ground."""

        # put this value in a more suitably named variable
        itemToTake = arg.lower()

        if itemToTake == '':
            print('Take what? Type "look" to see the items on the ground here.')
            return

        cantTake = False

        # get the item name that the player's command describes
        for item in getAllItemsMatchingDesc(itemToTake, worldPositions[location][GROUND]):
            if worldItems[item].get(TAKEABLE, True) == False:
                cantTake = True
                continue # there may be other items named this that you can take, so we continue checking
            print('You take %s.' % (worldItems[item][SHORTDESC]))
            worldPositions[location][GROUND].remove(item) # remove from the ground
            inventory.append(item) # add to inventory
            return

        if cantTake:
            print('You cannot take "%s".' % (itemToTake))
        else:
            print('That is not on the ground.')


    def do_drop(self, arg):
        """"drop <item> - Drop an item from your inventory onto the ground."""

        # put this value in a more suitably named variable
        itemToDrop = arg.lower()

        # get a list of all "description words" for each item in the inventory
        invDescWords = getAllDescWords(inventory)

        # find out if the player doesn't have that item
        if itemToDrop not in invDescWords:
            print('You do not have "%s" in your inventory.' % (itemToDrop))
            return

        # get the item name that the player's command describes
        item = getFirstItemMatchingDesc(itemToDrop, inventory)
        if item != None:
            print('You drop %s.' % (worldItems[item][SHORTDESC]))
            inventory.remove(item) # remove from inventory
            worldPositions[location][GROUND].append(item) # add to the ground


    def complete_take(self, text, line, begidx, endidx):
        possibleItems = []
        text = text.lower()

        # if the user has only typed "take" but no item name:
        if not text:
            return getAllFirstDescWords(worldPositions[location][GROUND])

        # otherwise, get a list of all "description words" for ground items matching the command text so far:
        for item in list(set(worldPositions[location][GROUND])):
            for descWord in worldItems[item][DESCWORDS]:
                if descWord.startswith(text) and worldItems[item].get(TAKEABLE, True):
                    possibleItems.append(descWord)

        return list(set(possibleItems)) # make list unique


    def complete_drop(self, text, line, begidx, endidx):
        possibleItems = []
        itemToDrop = text.lower()

        # get a list of all "description words" for each item in the inventory
        invDescWords = getAllDescWords(inventory)

        for descWord in invDescWords:
            if line.startswith('drop %s' % (descWord)):
                return [] # command is complete

        # if the user has only typed "drop" but no item name:
        if itemToDrop == '':
            return getAllFirstDescWords(inventory)

        # otherwise, get a list of all "description words" for inventory items matching the command text so far:
        for descWord in invDescWords:
            if descWord.startswith(text):
                possibleItems.append(descWord)

        return list(set(possibleItems)) # make list unique


    def do_look(self, arg):
        """Look at an item, direction, or the area:
"look" - display the current area's description
"look <direction>" - display the description of the area in that direction
"look exits" - display the description of all adjacent areas
"look <item>" - display the description of an item on the ground or in your inventory"""

        lookingAt = arg.lower()
        if lookingAt == '':
            # "look" will re-print the area description
            displayLocation(location)
            return

        if lookingAt == 'exits':
            for direction in (NORTH, SOUTH, EAST, WEST, UP, DOWN):
                if direction in worldPositions[location]:
                    print('%s: %s' % (direction.title(), worldPositions[location][direction][1]))
            return

        if lookingAt in ('north', 'west', 'east', 'south', 'up', 'down', 'n', 'w', 'e', 's', 'u', 'd'):
            if lookingAt.startswith('n') and NORTH in worldPositions[location]:
                print(worldPositions[location][NORTH][1])
            elif lookingAt.startswith('w') and WEST in worldPositions[location]:
                print(worldPositions[location][WEST][1])
            elif lookingAt.startswith('e') and EAST in worldPositions[location]:
                print(worldPositions[location][EAST][1])
            elif lookingAt.startswith('s') and SOUTH in worldPositions[location]:
                print(worldPositions[location][SOUTH][1])
            elif lookingAt.startswith('u') and UP in worldPositions[location]:
                print(worldPositions[location][UP][1])
            elif lookingAt.startswith('d') and DOWN in worldPositions[location]:
                print(worldPositions[location][DOWN][1])
            else:
                print('There is nothing in that direction.')
            return

        # see if the item being looked at is on the ground at this location
        item = getFirstItemMatchingDesc(lookingAt, worldPositions[location][GROUND])
        if item != None:
            print('\n'.join(textwrap.wrap(worldItems[item][LONGDESC], SCREEN_WIDTH)))
            return

        # see if the item being looked at is in the inventory
        item = getFirstItemMatchingDesc(lookingAt, inventory)
        if item != None:
            print('\n'.join(textwrap.wrap(worldItems[item][LONGDESC], SCREEN_WIDTH)))
            return

        print('You do not see that nearby.')


    def complete_look(self, text, line, begidx, endidx):
        possibleItems = []
        lookingAt = text.lower()

        # get a list of all "description words" for each item in the inventory
        invDescWords = getAllDescWords(inventory)
        groundDescWords = getAllDescWords(worldPositions[location][GROUND])
        shopDescWords = getAllDescWords(worldPositions[location].get(SHOP, []))

        for descWord in invDescWords + groundDescWords + shopDescWords + [NORTH, SOUTH, EAST, WEST, UP, DOWN]:
            if line.startswith('look %s' % (descWord)):
                return [] # command is complete

        # if the user has only typed "look" but no item name, show all items on ground, shop and directions:
        if lookingAt == '':
            possibleItems.extend(getAllFirstDescWords(worldPositions[location][GROUND]))
            possibleItems.extend(getAllFirstDescWords(worldPositions[location].get(SHOP, [])))
            for direction in (NORTH, SOUTH, EAST, WEST, UP, DOWN):
                if direction in worldPositions[location]:
                    possibleItems.append(direction)
            return list(set(possibleItems)) # make list unique

        # otherwise, get a list of all "description words" for ground items matching the command text so far:
        for descWord in groundDescWords:
            if descWord.startswith(lookingAt):
                possibleItems.append(descWord)

        # otherwise, get a list of all "description words" for items for sale at the shop (if this is one):
        for descWord in shopDescWords:
            if descWord.startswith(lookingAt):
                possibleItems.append(descWord)

        # check for matching directions
        for direction in (NORTH, SOUTH, EAST, WEST, UP, DOWN):
            if direction.startswith(lookingAt):
                possibleItems.append(direction)

        # get a list of all "description words" for inventory items matching the command text so far:
        for descWord in invDescWords:
            if descWord.startswith(lookingAt):
                possibleItems.append(descWord)

        return list(set(possibleItems)) # make list unique

    def do_eat(self, arg):
        """"eat <item>" - eat an item in your inventory."""
        global playerHealth
        itemToEat = arg.lower()

        if itemToEat == '':
            print('Eat what? Type "inventory" or "inv" to see your inventory.')
            return

        cantEat = False

        for item in getAllItemsMatchingDesc(itemToEat, inventory):
            if worldItems[item].get(EDIBLE, False) == False:
                cantEat = True
                continue # there may be other items named this that you can eat, so we continue checking
            # NOTE - If you wanted to implement hunger levels, here is where
            # you would add code that changes the player's hunger level.

            playerHealth += 25
            print('You eat %s' % (worldItems[item][SHORTDESC]))
            inventory.remove(item)
            return

        if cantEat:
            print('You cannot eat that.')
        else:
            print('You do not have "%s". Type "inventory" or "inv" to see your inventory.' % (itemToEat))


    def complete_eat(self, text, line, begidx, endidx):
        itemToEat = text.lower()
        possibleItems = []

        # if the user has only typed "eat" but no item name:
        if itemToEat == '':
            return getAllFirstDescWords(inventory)

        # otherwise, get a list of all "description words" for edible inventory items matching the command text so far:
        for item in list(set(inventory)):
            for descWord in worldItems[item][DESCWORDS]:
                if descWord.startswith(text) and worldItems[item].get(EDIBLE, False):
                    possibleItems.append(descWord)

        return list(set(possibleItems)) # make list unique


if __name__ == '__main__':
    print()
    print()
    print('                                     @@@@     ')
    print('                                   @@@@@@@@   ')
    print('                                  @@@@@@@@@@  ')
    print('                                   @@@@@@@@   ')
    print('                                     @@@@     ')
    print('                                      ||      ')
    print('                                      ||      ')
    print('                                      ||      ')
    print('                                 A S H T R E E')
    print('                                 =============')
    print()
    time.sleep(1)
    print('(Type "help" for commands.)')
    print()
    time.sleep(1)
    print('\n'.join(textwrap.wrap('The door leading back slams closed behind you, you scramble at the handle but the door won\'t let you go back. You slump to the ground and bury your face into your hands, somehow trying to stop the darkness suffocating you. Panic sets in... A few moments later your heart begins to slow. You bring your hands from your face to out in front of you and watch them disappear into the dark. The only sound you can hear is your footsteps echoing back. You seem to be in a relatively small room.', SCREEN_WIDTH)))
    print()
    time.sleep(3)
    displayLocation(location)
    TextAdventureCmd().cmdloop()
    print('Thanks for playing!')

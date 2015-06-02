#! usr/bin/python3
# A couple of functions. The first displays the contents of a dictionary (in this case a typical
# fantasy game inventory). The second takes a list of any size and adds it to the inventory.

import pprint

def displayInventory(inventory):

	pprint.pprint("Inventory:")
	item_total = 0

	for k, v in inventory.items():
		pprint.pprint(str(v) + ' ' + k)
		item_total += v

	pprint.pprint('Total number of items: ' + str(item_total))

def addToInventory(inventory, addedItems):

	# Counter variable for while loop
	itemSelectedInList = 0

	# While loop executes the same number of times as there are indexes in any list passed to the function
	while itemSelectedInList < len(addedItems):

		# If the lists index value (Loot Item) is not already within the inventory; add it with a default value of 1
		if addedItems[itemSelectedInList] not in inventory:
			inventory.setdefault(addedItems[itemSelectedInList], 1)

			# Increase counter variable for while loop by 1
			itemSelectedInList += 1
			continue

		# If list value already exists as a dictionary key; increase its value by 1
		else:
			inventory[addedItems[itemSelectedInList]] += 1

			# Increase counter variable for while loop by 1
			itemSelectedInList += 1
			continue

	return inventory

# Different sets of inventories
inv = {'arrow': 12, 'gold coin': 42, 'rope': 1, 'torch': 6, 'dagger': 1}

# Different sets of Loot
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'ruby']
skeletonLoot = ['gold coin', 'gold coin', 'gold coin', 'bone meal']
goblinLoot = ['healing potion', 'gold coin']


# To prove that function can work with any loot list and update dynamically.
displayInventory(inv)
addToInventory(inv, goblinLoot)
displayInventory(inv)
addToInventory(inv, skeletonLoot)
displayInventory(inv)
addToInventory(inv, dragonLoot)
displayInventory(inv)


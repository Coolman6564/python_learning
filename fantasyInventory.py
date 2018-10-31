def display_inventory(player_inventory):
    """This function displays a players current inventory."""
    total_items = 0
    print("Inventory: ")
    for key, value in player_inventory.items():
        total_items += int(value)
        print(str(value) + ": " + str(key.title()))
    print("Total number of inventory items: " + str(total_items))


def add_to_inventory(player_inventory, added_items):
    """This function adds items found to the players existing inventory."""
    # For each new piece of loot...
    for new_loot_piece in added_items:
        if new_loot_piece in player_inventory:
            # if the loot already existed in inventory, increment it's count
            player_inventory[new_loot_piece] += 1
        else:
            # If the loot was not already in the inventory, create a new piece of loot
            # in the inventory and se it's default value to 1.
            player_inventory.setdefault(new_loot_piece, 1)

    return player_inventory


inventory = {'rope': 1,
             'torch': 6,
             'gold coin': 42,
             'dagger': 1,
             'arrow': 12}

dragon_loot = {'gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', 'dragon meat'}

new_inventory = add_to_inventory(inventory, dragon_loot)
display_inventory(new_inventory)

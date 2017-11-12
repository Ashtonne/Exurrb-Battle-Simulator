import csv
import os
import sys
from entity import Player
from entity import Enemy
from entity import Item


# loads instances of players, enemys, or items into memory
def instanceLoader(entityType, entityName):

    # ensure csv file exists
    if os.path.isfile("entity_data/" + entityType + ".csv" == False):
        print("{} data does not exist. Please restart and create a new {} data file.".format(entityType.capitalize(), entityType.capitalize()))
        sys.exit(2)    
    
    with open("entity_data/" + entityType + ".csv", "r") as file:
        reader = csv.reader(file, delimiter=',')
        # search every first value until name is found
        for name in reader:
            if entityName == name[0]:
                # create a new entity with values found in csv file
                if entityType == "player":
                    # intialize a player with some default values
                    player = Player(entityName, "tmp", 0, 0, 0, 0, 0)
                    
                    # open up class types file and search for players class
                    with open("entity_data/class_types.csv", "r") as classTypeFile:
                        classReader = csv.reader(classTypeFile, delimiter=',')
                        print("checkpoint")
                        for row in classReader:
                            # if class type is equal to players class type
                            if row[0] == name[1]:
                                
                                # add items to players inventory
                                for item in row:
                                    if item != name[1] and itemCheck(item):
                                        player.addItem(item)
                                        print("{} found".format(item))
                    return True
                        
                elif entityType == "enemy":
                    #enemy = Enemy(row[0], row[1], row[2])
                    return True
                        
                elif entityType == "item":
                    #item = Item(row[0], row[1], row[2], row[3])
                    return True
                        
                else:
                    print("Entity type not found.")
    return False
    
def itemCheck(item):

    # check to see if item is in clothing
    with open("items/clothing.csv", "r") as clothingItems:
        reader = csv.reader(clothingItems)
        
        for row in reader:
            if row[0] == item:
                return True

    # check to see if item is in magic            
    with open("items/magic.csv", "r") as magicItems:
        reader = csv.reader(magicItems)
        
        for row in reader:
            if row[0] == item:
                return True

    # check to see if item is in melee        
    with open("items/melee.csv", "r") as meleeItems:
        reader = csv.reader(meleeItems)
        
        for row in reader:
            if row[0] == item:
                return True

    # check to see if item is in miscellaneous            
    with open("items/miscellaneous.csv", "r") as miscellaneousItems:
        reader = csv.reader(miscellaneousItems)
        
        for row in reader:
            if row[0] == item:
                return True

    # check to see if item is in ranged            
    with open("items/ranged.csv", "r") as rangedItems:
        reader = csv.reader(rangedItems)
        
        for row in reader:
            if row[0] == item:
                return True

    print("Item {} not found. It will not be added to the current player's inventory.".format(item))
    
    # item not found            
    return False
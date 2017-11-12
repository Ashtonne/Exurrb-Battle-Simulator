import os
import sys
import csv
from entity import Player
from entity import Enemy
from entity import Item


# loads instances of players, enemys, or items into memory
def instanceLoader(entityType, entityName):
    
    if entityType == "item":
        
        # check if item exists
        if itemCheck(entityName, "ITEMFOUND"):
            
            # open file where item is located
            with open(itemCheck(entityName, "ITEMLOCATION"), "r") as file:
                reader = csv.reader(file, delimiter=',')
                
                # search each row to find item
                for row in reader:
                    if row[0] == entityName:
                        item = Item(entityName, row[1], row[2], row[3], row[4], row[5], row[6])
                        return item
        else:
            print("{} does not exist".format(entityName))
            sys.exit(2)
                    
    # ensure csv file exists
    if os.path.isfile("entity_data/" + entityType + ".csv" == False):
        print("{} data does not exist. Please restart and create a new {} data file.".format(entityType.capitalize(), entityType.capitalize()))
        sys.exit(3)    
    
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
                                    if item != name[1] and itemCheck(item, "ITEMFOUND"):
                                        player.addItem(item)
                                        print("{} found".format(item))
                    #TODO add item benifits to player
                    
                    # return initialized player
                    return player
                        
                elif entityType == "enemy":
                    # intialize an enemy with values found in row
                    enemy = Enemy(entityName, name[1], name[2])
                    
                    # return initialized enemy
                    return enemy
                       
                else:
                    print("Entity type not found.")
    return False
    
    
def itemCheck(item, returnOption):

    if searchFile("items/clothing", item, returnOption):
        return searchFile("items/clothing", item, returnOption)
        
    elif searchFile("items/magic", item, returnOption):
        return searchFile("items/magic", item, returnOption)
        
    elif searchFile("items/melee", item, returnOption):
        return searchFile("items/melee", item, returnOption)
        
    elif searchFile("items/ranged", item, returnOption):
        return searchFile("items/ranged", item, returnOption)
        
        
# search files for a target value
def searchFile(directory, target, returnOption):
    # open file in specified mode
    with open(directory, "r") as file:
        reader = csv.reader(file)
        
        # search file row by row
        for row in reader:
            if row[0] == target:
                if returnOption == "ITEMLOCATION":
                    return directory
                elif returnOption == "ITEMFOUND":
                    return True
                else:
                    print("invalid function parameter")
                    return False
                    
    print("{} not found".format(target))
    return False
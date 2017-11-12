import sys
import csv
import os
from random import randint
from entity import Player
from entity import Enemy
from entity import Item


# dice roll function
def rollDice(diceSides):
    diceRoll = randint(0, diceSides)
    return diceRoll

# loads instances of players, enemys, or items into memory
def instanceLoader(entityType, entityName):

    # ensure csv file exists
    if(os.path.isfile("entity_data/" + entityType + ".csv") == False):
        print("{} data does not exist. Please restart and create a new {}.".format(entityType.capitalize(), entityType.capitalize()))
        sys.exit(2)    

    with open("entity_data/" + entityType + ".csv", "r") as file:

        reader = csv.reader(file, delimiter=',')
        # search every first value until name is found
        for row in reader:
            if entityName == row[0]:
                # create a new entity with values found in csv file
                if entityType == "player":
                    player = Player(row[0], row[1])
                    return True
                        
                elif entityType == "enemy":
                    enemy = Enemy(row[0], row[1], row[2])
                    return True
                        
                elif entityType == "item":
                    item = Item(row[0], row[1], row[2], row[3])
                    return True
                        
                else:
                    print("Entity type not found.")
    return False
 
     
# TODO battle player function
# TODO battle enemy function
# TODO colors for all the outputs
# TODO context strings stored in lists, but imported from files
# TODO implement item functionality
# TODO create battle log
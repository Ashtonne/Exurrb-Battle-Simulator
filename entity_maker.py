import os.path
import csv
import sys
from ui_helpers import getUserInput


# https://docs.python.org/3.1/library/csv.html

# entitys are players and enemies
def makeEntity():
    
    # clearscreen
    print(chr(27) + "[2J") 
    
    print("Choose an option, 0 to exit")
    print("1) Create new Player(s)")
    print("2) Create new Enemy(s) ")
    choice = input("Choice: ")
    
    choice = getUserInput(['1', '2'], choice)
    
    if choice == '1':
        entityChoice = "player"
    else:
        entityChoice = "enemy"
        
    # ensure csv file exists
    if(os.path.isfile("entity_data/" + entityChoice + ".csv") == False):
        file = open("entity_data/" + entityChoice + ".csv", "w+")
        # close file because file may already exist next time around
        file.close() 
    
    #TODO allow deletion of a player
    #TODO list all players functionality
    
    amount = None
    
    # pester user until they provide a valid integer
    while amount == None:
        try:
            amount = int(input("How many? "))
        except ValueError:
            print("{} is not a valid amount".format(amount))
            
    # open csv file and write to it
    with open("entity_data/" + entityChoice + ".csv", "w", newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
    
        for i in range(amount):
            # add one to i because most people dont start counting from 0
            name = input("{} {}'s Name: ".format(entityChoice.capitalize(), i+1))
            classType = input("{} {}'s Class: ".format(entityChoice.capitalize(), i+1))
            
            # write given data to the csv file
            writer.writerow([name, classType])
            
    file.close()
    
    

def makeItem():
    
    # ensure csv file exists
    if(os.path.isfile("entity_data/item.csv") == False):
        file = open("entity_data/item.csv", "w+")
        # close file because file may already exist next time around
        file.close() 
        
    amount = None
    
    # pester user until they provide a valid integer
    while amount == None:
        try:
            amount = int(input("Items to create: "))
        except ValueError:
            print("{} is not a valid amount".format(amount))
    
    # open csv file and write to it
    with open("entity_data/item.csv", "w", newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
    
        for i in range(amount):
            # add one to i because most people dont start counting from 0
            name = input("Item {}'s Name: ".format(i+1))
            itemType = input("Item {}'s Type (Ranged, Melee, Magic): ".format(i+1))
            tier = int(input("Item {}'s Tier (1-4): ".format(i+1)))
            durability = int(input("Item {}'s Durability (x amount of uses): ".format(i+1)))
            
            # write given data to the csv file
            writer.writerow([name, itemType, tier, durability])
            
    file.close()
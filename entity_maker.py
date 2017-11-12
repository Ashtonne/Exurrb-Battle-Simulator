import os.path
import csv
import sys
from ui_helpers import getUserInput


# entitys are players and enemies
def makeEntity():
    
    # clearscreen
    print(chr(27) + "[2J") 
    
    print("Specify which entity you would like to create:")
    print("1) Create new Player(s)")
    print("2) Create new Enemy(s) ")
    print("0) Exit")
    
    choice = input("Choice: ")
    
    choice = getUserInput(['1', '2'], choice)
    
    if choice == '1':
        entityChoice = "player"
    else:
        entityChoice = "enemy"
        
    # ensure csv file exists
    if(os.path.isfile("entity_data/" + entityChoice + ".csv") == False):
        file = open("entity_data/" + entityChoice + ".csv", "w+")
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
    with open("entity_data/" + entityChoice + ".csv", "a", newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
    
        for i in range(amount):
            # add one to i because most people dont start counting from 0
            name = input("{} {}'s Name: ".format(entityChoice.capitalize(), i+1))
            classType = input("{} {}'s Class: ".format(entityChoice.capitalize(), i+1))
            
            # write given data to the csv file
            writer.writerow([name, classType])
            
    file.close()
    
    

def makeItem():
    
    # clearscreen
    print(chr(27) + "[2J")     
    
    print("Choose an item type:")
    print("1) Create new Melee Item(s)")
    print("2) Create new Ranged Item(s) ")
    print("3) Create new Magic Item(s) ")
    print("4) Create new Clothing Item(s) ")
    print("0) Exit")
    
    choice = input("Choice: ")
    getUserInput(['1', '2', '3', '4'], choice)
    
    if choice == '1':
        itemType = "melee"
    elif choice == '2':
        itemType = "ranged"    
    elif choice == '3':
        itemType = "magic"
    elif choice == '4':
        itemType = "clothing"        
        
    # ensure csv file exists
    if(os.path.isfile("items/" + itemType + ".csv") == False):
        file = open("items/" + itemType + ".csv")
        file.close() 
        
    amount = None
    
    # pester user until they provide a valid integer
    while amount == None:
        try:
            amount = int(input("Items to create (low amount reccomended): "))
        except ValueError:
            print("{} is not a valid amount".format(amount))
    
    # open csv file and write to it
    with open("items/" + itemType + ".csv", "a", newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC)
    
        for i in range(amount):
            # get item info from user
            name = input("Item {}'s Name: ".format(i+1))
            tier = int(input("Item {}'s Tier (1-4): ".format(i+1)))
            durability = int(input("Item {}'s Durability (x amount of uses): ".format(i+1)))
            weight = int(input("Item {}'s Weight (x pounds): ".format(i+1)))
            strengthAdr = int(input("Item {}'s Strength Bonus: ".format(i+1)))
            enduranceAdr = int(input("Item {}'s Endurance Bonus: ".format(i+1)))
            agilityAdr = int(input("Item {}'s Agility Bonus: ".format(i+1)))
            
            # write given data to the csv file
            writer.writerow([name, tier, durability, weight, strengthAdr, enduranceAdr, agilityAdr])

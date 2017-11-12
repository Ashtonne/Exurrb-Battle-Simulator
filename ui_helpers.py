import sys

def menu():
    
    # TODO colors to make everything look nice 
    print("Choose an option, 0 to exit")
    print("1) Battle against an enemy")
    print("2) Battle a fellow adventurer")
    print("3) Add a player, enemy, or item")

    return

def getUserInput(acceptedInputs, choice):
    
    while choice not in acceptedInputs:
    # TODO colors to make everything look nice
        if choice == '0':
            print("Exiting...")
            sys.exit(0)
            
        print("-------------------------")    
        print("{} is not a valid option".format(choice))

        choice = input("Choice: ")
    
    return choice
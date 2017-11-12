import sys
from entity_maker import makeEntity
from entity_maker import makeItem
from ui_helpers import menu
from ui_helpers import getUserInput


def main():

    # check if user has python 3
    if sys.version_info[0] < 3:
        print("You must have python 3 installed!")
        print("If you have python 3 installed, try running with: python3 Exurrb-Battle-Simulator.py if your using the command line")
        sys.exit(1)
      
    while True:
        
        # clearscreen
        print(chr(27) + "[2J")  
        
        menu()
        option = input("Choice: ")  
        
        option = getUserInput(['1', '2', '3'], option)    
        
        if option == '1':
            print("placeholder")
            break
        elif option == '2':
            print("placeholder")
            break
        else:
            # clearscreen
            print(chr(27) + "[2J") 
    
            print("Choose and option below:")
            print("1) Create new Enemy or Player")
            print("2) Create new Item")
            print("0) Exit")
            
            choice = input("Choice: ")
    
            choice = getUserInput(['1', '2'], choice)
            
            if choice == '1':
                makeEntity()
            else:
                makeItem()
    sys.exit(0)
            
    
    
if __name__ == "__main__":
    main()
import sys
from entity_maker import makeEntity
from entity_maker import makeItem
from ui_helpers import menu
from ui_helpers import getUserInput
from simulator import instanceLoader

def main():

    # check if user has python 3
    if sys.version_info[0] < 3:
        print("You must have python 3 installed!")
        print("If you have python 3 installed, try running with: python3 exurrb_battle_sim.py if your using the command line")
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
    
            print("Choose an option, 0 to exit")
            print("1) Create new Player(s)")
            print("2) Create new Enemy(s) ")
            choice = input("Choice: ")
    
            choice = getUserInput(['1', '2'], choice)
        
    sys.exit(0)
            
    
    
if __name__ == "__main__":
    main()
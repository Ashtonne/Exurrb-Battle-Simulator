class Player:
    
    def __init__(self, name, classType, weight, strength, perception, endurance, agility):
        self.inventory = []
        self.name = name
        self.classType = classType
        self.weight = weight
        self.strength = strength
        self.perception = perception
        self.endurance = endurance
        self.agility = agility
        
    def addItem(self, item):
        self.inventory.append(item)
    
    # private copy of addItem method for player
    addItem = addItem
    
class Enemy:
    
    def __init__(self, name, size, armourClass):
        self.name = name
        self.size = size
        self.armourClass = armourClass


class Item:
    
    def __init__(self, name, tier, durability, weight, strengthAdr, perceptionAdr, enduranceAdr, agilityAdr):
        self.name = name
        self.tier = tier # 1, 2, 3, 4  (1 being the best)
        self.durability = durability # x amount of hits
        self.weight = weight # x amount of pounds
        self.strengthAdr = strengthAdr
        self.enduranceAdr = enduranceAdr
        self.agilityAdr = agilityAdr

        
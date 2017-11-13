class Player:
    
    def __init__(self, name, classType, weight, strength, endurance, agility):
        self.inventory = []
        self.name = name
        self.classType = classType
        self.weight = weight
        self.strength = strength
        self.endurance = endurance
        self.agility = agility
        
    # add an item to players inventory
    def addItem(self, item):
        self.inventory.append(item)
    
    # apply stats to player 
    def applyStats(self, weight, strength, endurance, agility):
        self.weight += int(weight)
        self.strength += int(strength)
        self.endurance += int(endurance)
        self.agility += int(agility)
        
    # return players an item in player's inventory
    def getItem(self, itemPlace):
        return self.inventory[itemPlace]
    
    # returns size of player's inventory
    def inventorySize(self):
        return len(self.inventory)
    
class Enemy:
    
    def __init__(self, name, size, armourClass):
        self.name = name
        self.size = size
        self.armourClass = armourClass


class Item:
    
    def __init__(self, name, tier, durability, weight, strengthAdr, enduranceAdr, agilityAdr):
        self.name = name
        self.tier = tier # 1, 2, 3, 4  (1 being the best)
        self.durability = durability # x amount of hits
        self.weight = weight # x amount of pounds
        self.strengthAdr = strengthAdr
        self.enduranceAdr = enduranceAdr
        self.agilityAdr = agilityAdr

        
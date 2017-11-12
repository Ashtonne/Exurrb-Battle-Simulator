class Player:
    
    def __init__(self, name, classType, weight, strength, perception, endurance, agility):
        self.items = set()
        self.name = name
        self.classType = classType
        self.weight = weight
        self.strength = strength
        self.perception = perception
        self.endurance = endurance
        self.agility = agility
        
        
class Enemy:
    
    def __init__(self, name, size, armourClass):
        self.items = set()
        self.name = name
        self.size = size
        self.armourClass = armourClass


class Item:
    
    def __init__(self, name, itemType, tier, durability, weight, strengthAdr, perceptionAdr, enduranceAdr, agilityAdr):
        self.name = name
        self.itemType = itemType # Ranged, Melee, Magic
        self.tier = tier # 1, 2, 3, 4  (1 being the best)
        self.durability = durability # 1-X amount of hits
        self.weight = weight
        self.perceptionAdr = perceptionAdr
        self.enduranceAdr = enduranceAdr
        self.agilityAdr = agilityAdr

        
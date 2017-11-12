class Player:
    
    def __init__(self, name, classType):
        self.items = set()
        self.name = name
        self.classType = classType
        
        
class Enemy:
    
    def __init__(self, name, size, armourClass):
        self.items = set()
        self.name = name
        self.size = size
        self.armourClass = armourClass

class Item:
    
    def __init__(self, name, itemType, tier, durability):
        self.name = name
        self.itemType = itemType # Ranged, Melee, Magic
        self.tier = tier # 1, 2, 3, 4  (1 being the best)
        self.durability = durability # 1-X amount of hits
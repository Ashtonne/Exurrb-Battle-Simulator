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
 
     
# TODO battle player function
# TODO battle enemy function
# TODO colors for all the outputs
# TODO implement item functionality
# TODO create battle log
# TODO create class functionality and item assigning
# TODO implement special abilities with conditons
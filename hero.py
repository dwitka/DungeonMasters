from tile import *
from room import *


class Hero(Tile):
    '''A class representing the hero venturing into the dungeon.
    Heroes have the following attributes: a name, a list of items,
    hit points, strength, gold, and a viewing radius. Heroes
    inherit the visible boolean from Tile.'''

    def __init__(self, name, bonuses=(0, 0, 0)):
        '''(Hero, str, list) -> NoneType
        Create a new hero with name name,
        an empty list of items and bonuses to
        hp, strength, gold and radius as specified
        in bonuses'''
        
        if name == 'Rogue':
            bonuses = (0, -1, 1)
        elif name == 'Barbarian':
            bonuses = (2, 0, 0)
        else:
            bonuses = (-2, -1, 2)

        self.name = name
        self.items = []
        self.hp = 10 + bonuses[0]
        self.strength = 3 + bonuses[1]
        self.radius = 1 + bonuses[2]
        Tile.__init__(self, True)

    def symbol(self):
        '''(Hero) -> str
        Return the map representation symbol of Hero: O.'''

        #return "\u263b"
        return "O"

    def __str__(self):
        '''(Item) -> str
        Return the Hero's name.'''

        return "{}\nHP:{:2d} STR:{:2d} RAD:{:2d}\n".format(
                    self.name, self.hp, self.strength, self.radius)

    def take(self, item):
        '''ADD SIGNATURE HERE
        Add item to hero's items
        and update their stats as a result.'''

        
        self.hp = self.hp + int(item[-5])
        
        self.strength = self.strength + int(item[-4])
        self.radius = self.radius + int(item[-3])
        self.items.append(str(item[0]))


    def fight(self, baddie):
        '''ADD SIGNATURE HERE -> str
        Fight baddie and return the outcome of the
        battle in string format.'''
        print(baddie)
        while self.hp > 0 and int(baddie[1]) > 0:
            self.hp = self.hp - int(baddie[2])
            baddie[1] = int(baddie[1]) - self.strength
            
        # Baddie strikes first
        # Until one opponent is dead
            # attacker deals damage equal to their strength
            # attacker and defender alternate
        if self.hp <= 0:
            print("Killed by", (baddie[0]))
        else:
            print("Defeated", (baddie[0]))

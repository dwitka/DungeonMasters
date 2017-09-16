from hero import *
from room import *
from screen import *

NORTH = 0
SOUTH = 1
EAST = 2
WEST = 3
CENTRE = 4

class Game:
    '''The controller class that keeps track of the current room
    the hero is in, the screen it should display to, etc. '''

    def __init__(self, mapname, hero):
        '''(Game, str) -> NoneType
        Create a new Game given the name of an initial room
        to load. mapname excludes extension.'''

        self.current_room = self.load(mapname)
        self.hero = Hero(str(hero))
        
        # start hero in position 4 (center)
        # corresponding to Room.locations[4]
        self.current_room.add_hero(self.hero, CENTRE)

    def game_over(self):
        '''(Game) -> NoneType
        Return True iff hero's hit points are 0 or less.'''

        return self.hero.hp <= 0

    def load(self, mapname):
        '''(Game, str) -> Room
        Append .map to mapname and open corresponding file.
        Create a new Room with appropriately placed walls.
        Precondition: file is a valid map format file.'''

        if mapname == "None":
            return
        mapfile = open(mapname + ".map", "r")
        walls = []
        items = []
        monsters = []
        row = 0
        assert mapfile.readline() == "MAPSTART\n"
        currline = mapfile.readline()
        while currline != "MAPFINISH\n":
            for col in range(len(currline)):
                if currline[col] == 'X':
                    walls.append((row, col))
            currline = mapfile.readline()
            row += 1

        #begin populating with items
        assert mapfile.readline() == "ITEMS\n"
        currline = mapfile.readline()
        while currline != "MONSTERS\n":
            # ADD ITEM PARSING CODE HERE
            bob = currline.strip()
            bob = bob.split(',')
            items.append(bob)
            currline = mapfile.readline()
            
        #begin populating with monsters
        #assert mapfile.readline() == "MONSTERS\n"
        currline = mapfile.readline()
        while currline != "ENDFILE":
            joe = currline.strip()
            joe = joe.split(',')
            monsters.append(joe)
            currline = mapfile.readline()
        mapfile.close()
        
        #create Room
        room = Room(self, walls, items, monsters)

        # PROCESS .links FILES HERE

        return room

    def move_hero(self, x, y):
        '''(Game, int, int)
        Send a move command from the GameScreen to the current room
        to move the hero x tiles to the right and y tiles down.'''

        self.current_room.move_hero(x, y)


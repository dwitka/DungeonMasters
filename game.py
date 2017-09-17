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
        # start hero in position 4 (CENTER)
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
        #Lists for all the different Tiles
        walls = []
        items = []
        monsters = []
        doors = []

        #Parse the file and load the Lists
        row = 0
        assert mapfile.readline() == "MAPSTART\n"
        current_line = mapfile.readline()
        while current_line != "MAPFINISH\n":
            for col in range(len(current_line)):
                #If Tile is a Wall add it to walls list
                if current_line[col] == 'X':
                    walls.append((row, col))
                #If Tile is a Door add it to doors list   
                if current_line[col] == 'D':
                    doors.append((row, col))
            current_line = mapfile.readline()
            row = row + 1

        #Begin populating items List with items
        assert mapfile.readline() == "ITEMS\n"
        current_line = mapfile.readline()
        while current_line != "MONSTERS\n":
            # ADD ITEM PARSING CODE HERE
            strip_line = current_line.strip()
            split_list = strip_line.split(',')
            items.append(split_list)
            current_line = mapfile.readline()
            
        #Begin populating monsters List with monsters
        current_line = mapfile.readline()
        while current_line != "ENDFILE":
            strip_line = current_line.strip()
            split_list = strip_line.split(',')
            monsters.append(split_list)
            current_line = mapfile.readline()
        mapfile.close()
        
        #Create Room
        room = Room(self, walls, items, monsters, doors, mapname)
        return room


    def move_hero(self, x, y):
        '''(Game, int, int)
        Send a move command from the GameScreen to the current room
        to move the hero x tiles to the right and y tiles down.'''
        self.current_room.move_hero(x, y)


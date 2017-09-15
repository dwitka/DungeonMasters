from tile import *
from math import floor, ceil
from game import *
from hero import *

ROWS = 11
COLS = 21


class Room:
    '''A class representing one of several interconnected
    Rooms that constitute the game.'''
    
    def __init__(self, game, walls, items, monsters):
        '''(Room, Game, list) -> NoneType
        Create a new Room that belongs to game game.
        Add walls at all coordinates specified as tuples (x, y) in walls.'''
        
        self.game = game
        self.rows = ROWS
        self.cols = COLS
        self.items = items
        self.monsters = monsters

        #populate the entire grid with empty tiles first
        self.grid = [[Tile() for q in list(range(self.cols))]
            for z in list(range(self.rows))]

        #add walls as specified by the map file
        for i, j in walls:
            self.grid[i][j] = Wall()
            
        for item in items:
            i = int(item[-2])
            j = int(item[-1])
            self.grid[i][j] = Item()
            
        for item in monsters:
            i = int(item[-2])
            j = int(item[-1])
            self.grid[i][j] = Monster()

        self.status = ""

        #specify where hero should appear if he is coming from
        #each direction: 0 - north, 1 - south, 2 - east, 3 - west
        # 4 - center

        self.locations = [(self.rows - 2, ceil(self.cols // 2)),
                        (1, ceil(self.cols // 2)),
                        (ceil(self.rows // 2), 1),
                        (ceil(self.rows // 2), self.cols - 2),
                        (ceil(self.rows // 2), ceil(self.cols // 2))]

    def update_visibility(self):
        '''(Room) -> NoneType
        Update what the hero has uncovered given his new position.'''
        
        L = []
        for i in range(self.hero.radius):
            L.append(i)
            L.append(-i)
        L.append(self.hero.radius)
        L.append(-self.hero.radius)
        L.remove(0)
        
        for i in L:
            for j in L:
                if i == 0 and j == 0:
                    pass
                elif not self.in_grid((self.hero_x + i), (self.hero_y + j)):
                    pass
                elif type(self.grid[self.hero_x + i][self.hero_y + j]) == Wall:
                    self.add(Wall(True), self.hero_x + i, self.hero_y + j)
                elif type(self.grid[self.hero_x + i][self.hero_y + j]) == Item:
                    self.add(Item(True), self.hero_x + i, self.hero_y + j)
                elif type(self.grid[self.hero_x + i][self.hero_y + j]) == Monster:
                    self.add(Monster(True), self.hero_x + i, self.hero_y + j)
                else:
                    self.grid[self.hero_x + i][self.hero_y + j] = Tile(True)

    def add_hero(self, hero, where):
        '''(Room, Hero, int) -> NoneType
        Add hero hero to the room, placing him
        as specified in self.locations[where].'''

        self.hero_x, self.hero_y = self.locations[where]
        self.hero = hero
        self.grid[self.hero_x][self.hero_y] = self.hero
        self.update_visibility()

    def add(self, obj, x, y):
        '''(Room, Tile, int, int) -> NoneType
        Add Tile object obj to the room at (x, y).'''

        self.grid[x][y] = obj

    def in_grid(self, x, y):
        '''(Room, int, int) -> bool
        Return True iff coordinates (x,y) fall within the room's grid.'''

        return x >= 0 and x < self.rows and y >= 0 and y < self.cols

    def move_hero(self, x, y):
        '''(Room, int, int) -> NoneType
        Move hero to new location +x and +y from current location.
        If the new location is impenetrable, do not update hero location.'''

        newx = self.hero_x + x
        newy = self.hero_y + y
        if not self.in_grid(newx, newy) or type(self.grid[newx][newy]) == Wall:
            return

        # DOOR CODE GOES HERE

        else:
            self.resolve(newx, newy)
        self.update_visibility()

    def resolve(self, x, y):
        '''(Room, int, int) -> NoneType
        Resolve an encounter between a penetrable Tile and a hero.
        '''

        #Replace space hero left with a new blank Tile
        self.grid[self.hero_x][self.hero_y] = Tile(True)

        # ITEM AND MONSTER CODE GOES HERE
        for item in self.items:
            if self.hero_x == int(item[-2]) and self.hero_y == int(item[-1]):
                q = self.items.index(item)
                k = self.items.pop(q)
                self.hero.take(k)
                print("Picked up!!!", (str(item[0])))
                
                
        for item in self.monsters:
            if self.hero_x == int(item[-2]) and self.hero_y == int(item[-1]):
                q = self.monsters.index(item)
                k = self.monsters.pop(q)
                self.hero.fight(k)
                print("Fight!!!")
                
                
                
                
                '''
                self.hero.hp = self.hero.hp + int(item[-5])
                if int(item[-5]) != 0:
                    print("Picked up!!!", (str(item[0])))
                self.hero.strength = self.hero.strength + int(item[-4])
                self.hero.radius = self.hero.radius + int(item[-3])
                self.items.remove(item)'''
        

        self.status = ""

        #update hero location
        self.hero_x = x
        self.hero_y = y
        self.grid[x][y] = self.hero

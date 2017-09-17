class Tile:
    '''Anything that takes up one square tile on the map.
    The default tile is empty space.'''

    def __init__(self, vis=False):
        '''(Tile, bool, bool) -> NoneType
        Construct a new tile. If penetrate is True,
        the tile can be stepped on by the Hero.
        self.visible is set to True once the Hero
        has uncovered that tile.'''

        self.visible = vis

    def symbol(self):
        '''(Tile) -> str
        Return the map representation symbol for Tile.'''

        return " "


class Wall:
    '''A subclass of Tile that represents an impassable wall.'''

    def __init__(self, vis=False):
        '''(Wall) -> NoneType
        Construct an impenetrable Tile'''
        self.visible = vis
        #Tile.__init__(self)

    def symbol(self):
        '''(Wall) -> str
        Return the map representation symbol for Wall: X.'''

        #return "\u2588"
        return "X"

class Door:
    '''A subclass of Tile that represents an impassable wall.'''

    def __init__(self, vis=False):
        '''(Wall) -> NoneType
        Construct an impenetrable Tile'''
        self.visible = vis
        #Tile.__init__(self)

    def symbol(self):
        '''(Wall) -> str
        Return the map representation symbol for Wall: X.'''

        #return "\u2588"
        return "D"
    
class Item:
    '''A subclass of Tile that represents a retrievable item.'''

    def __init__(self, vis=False):
        '''(Item) -> NoneType
        Construct an impenetrable Tile'''
        self.visible = vis
        #Tile.__init__(self)

    def symbol(self):
        '''(Item) -> str
        Return the map representation symbol for Wall: X.'''

        return "I"
    
class Monster:
    '''A subclass of Tile that represents an Enemy.'''

    def __init__(self, vis=False):
        '''(Monster) -> NoneType
        Construct an impenetrable Tile'''
        self.visible = vis
        #Tile.__init__(self)

    def symbol(self):
        '''(Monster) -> str
        Return the map representation symbol for Wall: X.'''

        return "M"

class Door:
    '''A subclass of Tile that represents a Door.'''

    def __init__(self, vis=False):
        '''(Door) -> NoneType
        Construct an impenetrable Tile'''
        self.visible = vis
        #Tile.__init__(self)

    def symbol(self):
        '''(Door) -> str
        Return the map representation symbol for Door: D.'''

        return "D"

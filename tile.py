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

    def symbol(self):
        '''(Wall) -> str
        Return the map representation symbol for Wall: X.'''
        #You can also use unicode characters "\u2588"
        return "X"


class Door:
    '''A subclass of Tile that represents a rotating door.'''
    def __init__(self, vis=False):
        '''(Wall) -> NoneType
        Construct an rotating Door Tile'''
        self.visible = vis

    def symbol(self):
        '''(Wall) -> str
        Return the map representation symbol for Door: D.'''
        return "D"


class Item:
    '''A subclass of Tile that represents a retrievable item.'''
    def __init__(self, vis=False):
        '''(Item) -> NoneType
        Construct a retrievable Item Tile'''
        self.visible = vis

    def symbol(self):
        '''(Item) -> str
        Return the map representation symbol for Item: I.'''
        return "I"

  
class Monster:
    '''A subclass of Tile that represents a dangerous monster.'''
    def __init__(self, vis=False):
        '''(Monster) -> NoneType
        Construct an dangerous Monster Tile'''
        self.visible = vis

    def symbol(self):
        '''(Monster) -> str
        Return the map representation symbol for Monster: M.'''
        return "M"


from game import *


class GameScreen:
    '''Display the current state of a game in a text-based format.
    This class is fully implemented and needs no
    additional work from students.'''

    def initialize_game(self):
        '''(GameScreen) -> NoneType
        Initialize new game with new user-selected hero class
        and starting room files.'''
        hero = None
        #Get the text input and choose the hero
        while hero is None:
            c = input("Select hero type:\n(R)ogue (M)age (B)arbarian\n")
            c = c.lower()
            if c == 'r':
                hero = 'Rogue'
            elif c == 'm':
                hero = 'Mage'
            elif c == 'b':
                hero = 'Barbarian'
        #Initialize game with hero
        self.game = Game("rooms/dungeonroom", hero)


    def play(self):
        '''(Game) -> NoneType
        The main game loop.'''
        exit = False
        while not exit:
            print(self)
            if self.game.game_over():
                break
            c = input("Next: ")
            if c in ['q', 'x']:
                print("Thanks for playing!")
                exit = True
            #Text input to control hero's movements
            elif c == 'w':  # UP
                self.game.move_hero(-1, 0)
            elif c == 's':  # DOWN
                self.game.move_hero(1, 0)
            elif c == 'a':  # LEFT
                self.game.move_hero(0, -1)
            elif c == 'd':  # RIGHT
                self.game.move_hero(0, 1)
            elif c == 'r':
                ## RESTART GAME
                self.initialize_game()
            else:
                pass


    def __str__(self):
        '''(GameScreen) -> NoneType
        Return a string representing the current room.
        Include the game's Hero string represetation and a
        status message from the last action taken.'''
        room = self.game.current_room
        room_string = ""
        #Render a GAME OVER screen with text mostly centered
        #In the space of the room in which the character died.
        if self.game.game_over():
            #Top row
            room_string += "X" * (2 + room.cols) + "\n"
            #Empty rows above GAME OVER
            for i in list(range(floor((room.rows - 2) / 2))):
                room_string += "X" + " " * room.cols + "X\n"
            #GAME OVER rows
            room_string += ("X" + " " * floor((room.cols - 4) / 2) +
                "GAME" + " " * ceil((room.cols - 4) / 2) + "X\n")
            room_string += ("X" + " " * floor((room.cols - 4) / 2) +
                "OVER" + " " * ceil((room.cols - 4) / 2) + "X\n")
            #Empty rows below GAME OVER
            for i in list(range(ceil((room.rows - 2) / 2))):
                room_string += "X" + " " * room.cols + "X\n"
            #Bottom row
            room_string += "X" * (2 + room.cols) + "\n"
        else:
            for row in range(room.rows):
                for column in room.grid[row]:
                    if column is not None:
                        if column.visible:
                            room_string += column.symbol()
                        else:
                            #This is the symbol for 'not yet explored' : ?
                            room_string += "?"
                room_string += "\n"
        #Hero representation
        room_string += str(self.game.hero)
        #Last status message
        room_string += room.status
        return room_string
    
#Start the game 
if __name__ == '__main__':
    game_screen = GameScreen()
    game_screen.initialize_game()
    game_screen.play()


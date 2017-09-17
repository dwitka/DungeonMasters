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
        while hero is None:
            inputText = input("Select hero type:\n(R)ogue (M)age (B)arbarian\n")
            inputText = inputText.lower()
            if inputText == 'r':
                hero = 'Rogue'
            elif inputText == 'm':
                hero = 'Mage'
            elif inputText == 'b':
                hero = 'Barbarian'

        self.game = Game("rooms/startroom", hero)

    def play(self):
        '''(Game) -> NoneType
        The main game loop.'''
        exit = False
        while not exit:
            print(self)
            if self.game.game_over():
                break
            inputText = input("Next: ")
            if inputText in ['q', 'x']:
                print("Thanks for playing!")
                exit = True
            elif inputText == 'w':  # UP
                self.game.move_hero(-1, 0)
            elif inputText == 's':  # DOWN
                self.game.move_hero(1, 0)
            elif inputText == 'a':  # LEFT
                self.game.move_hero(0, -1)
            elif inputText == 'd':  # RIGHT
                self.game.move_hero(0, 1)
            elif inputText == 'r':
                ## RESTART GAME
                self.initialize_game()
            else:
                pass

    def __str__(self):
        '''(GameScreen) -> String
        Return a string representing the current room.
        Include the game's Hero string represetation and a
        status message from the last action taken.'''
        room = self.game.current_room
        currentRoom = ""

        if self.game.game_over():
            #render a GAME OVER screen with text mostly centered
            #in the space of the room in which the character died.

            #top row
            currentRoom += "X" * (2 + room.cols) + "\n"
            #empty rows above GAME OVER
            for i in list(range(floor((room.rows - 2) / 2))):
                currentRoom += "X" + " " * room.cols + "X\n"
            # GAME OVER rows
            currentRoom += ("X" + " " * floor((room.cols - 4) / 2) +
                "GAME" + " " * ceil((room.cols - 4) / 2) + "X\n")
            currentRoom += ("X" + " " * floor((room.cols - 4) / 2) +
                "OVER" + " " * ceil((room.cols - 4) / 2) + "X\n")
            #empty rows below GAME OVER
            for i in list(range(ceil((room.rows - 2) / 2))):
                currentRoom += "X" + " " * room.cols + "X\n"
            #bottom row
            currentRoom += "X" * (2 + room.cols) + "\n"
        else:
            for index_i in range(room.rows):
                for index_j in room.grid[index_i]:
                    if index_j is not None:
                        if index_j.visible:
                            currentRoom += index_j.symbol()
                        else:
                            #This is the symbol for 'not yet explored' : ?
                            currentRoom += "?"
                currentRoom += "\n"
        #hero representation
        currentRoom += str(self.game.hero)
        #last status message
        currentRoom += room.status
        return currentRoom

if __name__ == '__main__':
    gs = GameScreen()
    gs.initialize_game()
    gs.play()


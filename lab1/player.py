class Player:

    # Init the player with their color
    def __init__(self, color):
        self.color = color

    # Get the next move from this player given the current board
    def getMove(self, board):
        print("SHOULD BE OVERRIDEN")
        toRet = (0,0)
        return toRet

# Class representing
class AIPlayer(Player):

    def getMove(self, board):
        print("AI PLAYER MOVE")
        toRet = (0, 0)
        return toRet

# Player class to allow for a human to play the game from the terminal
class HumanPlayer(Player):

    def getMove(self, board):
        print("HUMAN PLAYER")
        toRet = (0, 0)
        return toRet

from lab1.board import Color, Board
from lab1.player import HumanPlayer, AIPlayer
from lab1.game import Game

print(' --------------------- ')
print('| WELCOME TO OTHELLO! |')
print(' --------------------- ')

human_color = None
ai_color = None
valid_input = False
while not valid_input:
    input_color = input('Choose your color: (b or w)\n')
    if input_color == 'b':
        human_color = Color.BLACK
        ai_color = Color.WHITE
        valid_input = True
    elif input_color == 'w':
        human_color = Color.WHITE
        ai_color = Color.BLACK
        valid_input = True
    else:
        print('Invalid input')
        continue

time_limit = None
level = None
valid_input = False
while not valid_input:
    input_limit = input('Choose a time limit for the AI: (int value in seconds)\n')
    try:
        time_limit = int(input_limit)
    except ValueError:
        print('Invalid input')
        continue
    else:
        valid_input = True

    if time_limit < 7:
        level = 2
    elif time_limit < 90:
        level = 3
    else:
        level = 4

player_b = None
player_w = None
if human_color == Color.WHITE:
    player_b = AIPlayer(ai_color, level)
    player_w = HumanPlayer(human_color)
else:
    player_w = AIPlayer(ai_color, level)
    player_b = HumanPlayer(human_color)


game = Game(player_w, player_b)
game.start()

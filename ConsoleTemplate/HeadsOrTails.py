from MyGameEngine import GameBoard
from random import randint
from curses import KEY_RIGHT, KEY_LEFT, KEY_DOWN

class Coin(object):
    def __init__(self, window):
        self.window = window
        self.x = int(MAX_X/2)
        self.y = int(MAX_Y/2)
        self.flips = 50

        flip = randint(0,100)
        if flip < 50:
            self.value = '@'
        else:
            self.value = '%'

    def render(self):
        self.window.addstr(self.y, self.x, self.value)

    def update(self):
        if self.flips > 0:
            if self.value == '@':
                self.value = '%'
            else:
                self.value = '@'
            self.window.addstr(self.y, self.x, self.value)
            self.flips -= 1
        else:
            game_text.coin_result(self)




    def update_direction(self, direction):
        return


class TheGame(object):
    def __init__(self,window):
        self.window = window
        self.choice = ''
        self.result = False
        self.done = 30

    def render(self):
        self.window.addstr(1, int(MAX_X/2)-7, 'Heads or Tails?')
        self.window.addstr(5, int(MAX_X/2)-10, 'Heads')
        self.window.addstr(5, int(MAX_X/2)+10, 'Tails')

        if self.choice == 'Heads':
            self.window.addstr(5, int(MAX_X/2)-12, 'X')
        elif self.choice == 'Tails':
            self.window.addstr(5, int(MAX_X/2)+8, 'X')


        if self.result:
            self.window.addstr(8, int(MAX_X / 2)-2, self.result_value)

            if self.result_value == self.choice:
                self.window.addstr(3, int(MAX_X / 2)-4, 'You Win!')
            else:
                self.window.addstr(3, int(MAX_X / 2)-4, 'You Lose!')



    def update(self):
        if self.result:
            if self.done == 0:
                game.stop_game()
            else:
                self.done -= 1


    def update_direction(self, direction):
        if direction == KEY_LEFT:
            self.choice = 'Heads'
        elif direction == KEY_RIGHT:
            self.choice = 'Tails'
        elif direction == KEY_DOWN:
            coin = Coin(self.window)
            game.add_game_object(coin)


    def coin_result(self,coin):
        if coin.value == '@':
            self.result_value = 'Heads'
        else:
            self.result_value= 'Tails'
        self.result = True






WIDTH = 50
HEIGHT = 20
MAX_X = WIDTH - 2
MAX_Y = HEIGHT - 2


def run_game():
    global game
    game = GameBoard(WIDTH, HEIGHT)
    window = game.get_window()

    global game_text
    game_text = TheGame(window)

    game.add_game_object(game_text)

    game.start()


if __name__ == '__main__':
    run_game()

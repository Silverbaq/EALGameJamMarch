from MyGameEngine import GameBoard

from curses import KEY_RIGHT, KEY_LEFT, KEY_DOWN, KEY_UP

class GameElement(object):

    def __init__(self, window):
        self.window = window
        self.x = int(MAX_X/2)
        self.y = int(MAX_Y/2)
        self.shape = '1001001010101011'
        self.timer = 30

    def render(self):
        self.window.addstr(self.y, self.x-8, self.shape)

    def update(self):
        self.timer -= 1
        if self.timer == 0:
            self.shape = 'You Win!!!'
        elif self.timer == -50:
            game.stop_game()


    def update_direction(self, direction):
        if direction == KEY_RIGHT:
            if self.x < MAX_X - 3:
                self.x += 2
        elif direction == KEY_LEFT:
            if self.x > 3:
                self.x -= 2



WIDTH = 50
HEIGHT = 20
MAX_X = WIDTH - 2
MAX_Y = HEIGHT - 2


def run_game():
    global game
    game = GameBoard(WIDTH, HEIGHT)
    window = game.get_window()

    element = GameElement(window)
    game.add_game_object(element)

    game.start()


if __name__ == '__main__':
    run_game()

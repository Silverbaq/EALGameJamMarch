from MyGameEngine import GameBoard
from random import randint
from curses import KEY_RIGHT, KEY_LEFT, KEY_DOWN, KEY_UP


class Rain(object):

    def __init__(self, window, char='|'):
        self.x = randint(1, MAX_X)
        self.y = 1
        self.char = char
        self.window = window

    def move_down(self):
        self.y += 1
        if self.y > MAX_Y:
            game.remove_game_object(self)
            player.colited(self)

    def render(self):
        self.window.addstr(self.y, self.x, self.char)

    def update(self):
        self.move_down()

    def update_direction(self, direction):
        return


class Cloud(object):

    def __init__(self, window):
        self.window = window
        self.timer = 0

    def spawn(self):
        rain = Rain(self.window)
        game.add_game_object(rain)

    def update(self):
        if self.timer == 0:
            self.spawn()
            self.timer = randint(1, 10)
        else:
            self.timer -= 1

    def render(self):
        return

    def update_direction(self, direction):
        return


class PlayerPad(object):

    def __init__(self, window):
        self.window = window
        self.x = 5
        self.y = MAX_Y
        self.shape = '_____'
        self.points = 0
        self.hits = 10

    @property
    def score(self):
        return 'Score: {}'.format(self.points)

    @property
    def lives(self):
        l = '1'* self.hits
        return 'Lives: {}'.format(l)

    def render(self):
        self.window.addstr(self.y, self.x - 2, self.shape)
        self.window.addstr(0,0, self.lives)
        self.window.addstr(0,int(MAX_X/2)-4, self.score)

    def update(self):
        return

    def lose_life(self):
        self.hits -= 1
        if self.hits == 0:
            game.stop_game()

    def gain_points(self):
        self.points += 10

    def colited(self, rain):
        if rain.x in [self.x - 2, self.x - 1, self.x, self.x + 1, self.x + 2]:
            self.gain_points()
        else:
            self.lose_life()

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

    cloud = Cloud(window)
    game.add_game_object(cloud)

    global player
    player = PlayerPad(window)
    game.add_game_object(player)

    game.start()


if __name__ == '__main__':
    run_game()

from MyGameEngine import GameBoard
from curses import KEY_RIGHT, KEY_LEFT, KEY_DOWN, KEY_UP, KEY_ENTER
import datetime


class BoardValues(object):
    spacer = (2, 1)
    card_size = (7, 7)
    offset = (3, 1)
    rows = 2
    cols = 4

    def __init__(self):
        self.current_row = 0
        self.current_col = 0


class SelectedMarker(object):
    def __init__(self, window, geometry):
        self.window = window
        self.geo = geometry

    def render(self):
        x = self.geo.card_size[0] * self.geo.current_col \
            + self.geo.spacer[0] * self.geo.current_col \
            + self.geo.offset[0] - 1
        y = (self.geo.card_size[1] + 1) * self.geo.current_row + \
            self.geo.spacer[1] * self.geo.current_row \
            + self.geo.offset[1]
        self.window.addstr(y, x, 'Y')
        return

    def update(self):
        return

    def update_direction(self, direction):
        return

    def reset(self):
        return


class Card(object):
    def __init__(self, window, row, col, geometry):
        self.card_size = geometry.card_size
        self.window = window
        self.row = row
        self.col = col
        self.geo = geometry
        self.turned = False

    def set_turned(self, state):
        self.turned = state

    def is_turned(self):
        return self.turned

    def get_pos(self):
        return self.row, self.col

    def render_back(self):
        for c in range(self.card_size[0]):
            for r in range(self.card_size[1]):
                x = self.geo.card_size[0] * self.col \
                    + self.geo.spacer[0] * self.col \
                    + self.geo.offset[0] + c
                y = self.geo.card_size[1] * self.row + \
                    self.geo.spacer[1] * self.row \
                    + self.geo.offset[1] + r
                self.window.addstr(y, x, 'X')

    def render_front(self):
        for c in range(self.card_size[0]):
            for r in range(self.card_size[1]):
                x = self.geo.card_size[0] * self.col \
                    + self.geo.spacer[0] * self.col \
                    + self.geo.offset[0] + c
                y = self.geo.card_size[1] * self.row + \
                    self.geo.spacer[1] * self.row \
                    + self.geo.offset[1] + r
                self.window.addstr(y, x, '0')

    def render(self):
        if self.turned:
            self.render_back()
        else:
            self.render_front()

    def update(self):
        return

    def update_direction(self, direction):
        if direction == 10:  # enter key
            if (self.geo.current_row == self.row) and (self.geo.current_col == self.col):
                self.turned = not self.turned

        return

    def reset(self):
        return


class Board(object):
    def __init__(self, window, geometry):
        self.card_size = (5, 5)
        self.window = window
        self.rows = geometry.rows
        self.cols = geometry.cols

        self.geo = geometry
        self.cards = []

        for i in range(self.rows):
            for j in range(self.cols):
                self.cards.append(Card(window, i, j, self.geo))

        self.is_waiting = False
        self.wait_until_time = datetime.datetime.now()

    def get_card_number(self, row, col):
        return row * self.rows + col

    def render(self):
        for card in self.cards:
            card.render()

    def update(self):
        if self.is_waiting:
            if datetime.datetime.now() > self.wait_until_time:
                for c in self.cards:
                    c.set_turned(False)
                self.is_waiting = False
        return

    def update_direction(self, direction):
        row, col = self.geo.current_row, self.geo.current_col
        if direction == KEY_LEFT:
            self.geo.current_col = (col - 1) % self.geo.cols
            return

        if direction == KEY_RIGHT:
            self.geo.current_col = (col + 1) % self.geo.cols
            return

        if direction == KEY_UP:
            self.geo.current_row = (row - 1) % self.geo.rows
            return

        if direction == KEY_DOWN:
            self.geo.current_row = (row + 1) % self.geo.rows
            return

        if not self.is_waiting:
            for c in self.cards:
                c.update_direction(direction)

            if direction == 10:  # enter key
                self.check_turned()
        return

    def check_turned(self):
        sum_turned = sum(1 for c in self.cards if c.is_turned())
        if sum_turned > 1:
            self.set_wait_state()

    def set_wait_state(self):
        self.is_waiting = True
        self.wait_until_time = datetime.timedelta(seconds=2) + datetime.datetime.now()

    def reset(self):
        return


def run_game(width, height):
    global game
    game = GameBoard(width, height)
    window = game.get_window()

    bv = BoardValues()
    game.add_game_object(Board(window, bv))
    game.add_game_object(SelectedMarker(window, bv))

    game.start()


if __name__ == '__main__':
    run_game(45, 20)

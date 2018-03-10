from MyGameEngine import GameBoard
from curses import KEY_RIGHT, KEY_LEFT, KEY_DOWN, KEY_UP, KEY_ENTER
import datetime
import random


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
    def __init__(self, window, row, col, geometry, card_type):
        self._window = window
        self._row = row
        self._col = col
        self._geo = geometry
        self._show_front = False
        self._disabled = False
        self._card_type = str(card_type)

    @property
    def card_type(self):
        return self._card_type

    def set_show_front(self, state):
        if self.is_disabled():
            self._show_front = False
            return

        self._show_front = state

    def is_show_front(self):
        return self._show_front

    def is_disabled(self):
        return self._disabled

    def set_disabled(self, state):
        self._disabled = state

    def render_back(self):
        for c in range(self._geo.card_size[0]):
            for r in range(self._geo.card_size[1]):
                x = self._geo.card_size[0] * self._col \
                    + self._geo.spacer[0] * self._col \
                    + self._geo.offset[0] + c
                y = self._geo.card_size[1] * self._row + \
                    self._geo.spacer[1] * self._row \
                    + self._geo.offset[1] + r
                self._window.addstr(y, x, 'X')

    def render_front(self):
        for c in range(self._geo.card_size[0]):
            for r in range(self._geo.card_size[1]):
                x = self._geo.card_size[0] * self._col \
                    + self._geo.spacer[0] * self._col \
                    + self._geo.offset[0] + c
                y = self._geo.card_size[1] * self._row + \
                    self._geo.spacer[1] * self._row \
                    + self._geo.offset[1] + r
                self._window.addstr(y, x, self._card_type)

    def render(self):
        if self._disabled:
            return

        if not self.is_show_front():
            self.render_back()
        else:
            self.render_front()

    def update(self):
        return

    def update_direction(self, direction):
        if direction == 10:  # enter key
            if (self._geo.current_row == self._row) and (self._geo.current_col == self._col):
                self._show_front = not self.is_show_front()

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
        self.init_cards(window)

        self.is_waiting = False
        self.wait_until_time = datetime.datetime.now()

    def init_cards(self, window):
        card_array = []
        for i in range((self.cols * self.rows) // 2):
            card_array.append(i)
            card_array.append(i)
        random.shuffle(card_array)

        for i in range(self.rows):
            for j in range(self.cols):
                self.cards.append(Card(window, i, j, self.geo,
                                       card_array[self.get_card_number(i, j)]))

    def get_card_number(self, row, col):
        return row * self.cols + col

    def render(self):
        for card in self.cards:
            card.render()

    def update(self):
        if self.is_waiting:
            if datetime.datetime.now() > self.wait_until_time:
                self.is_waiting = False
                self.compare_turned()
                for c in self.cards:
                    c.set_show_front(False)
        return

    def compare_turned(self):
        turned = None
        for c in self.cards:
            if c.is_show_front():
                if not turned:
                    turned = c
                else:
                    if turned.card_type == c.card_type:
                        c.set_disabled(True)
                        c.set_show_front(True)
                        turned.set_disabled(True)
                        turned.set_show_front(True)

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
        sum_turned = sum(1 for c in self.cards if c.is_show_front())
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

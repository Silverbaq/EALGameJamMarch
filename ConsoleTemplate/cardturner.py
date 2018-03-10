from MyGameEngine import GameBoard
from curses import KEY_RIGHT, KEY_LEFT, KEY_DOWN, KEY_UP


class BoardValues(object):
    spacer = (2, 1)
    card_size = (6, 7)
    offset = (3, 1)
    rows = 2
    cols = 3


class SelectedMarker(object):
    def __init__(self, window, geometry):
        self.window = window
        self.geo = geometry
        self.row = 0
        self.col = 0

    def get_pos(self):
        return self.row, self.col

    def set_pos(self, row, col):
        self.row = row
        self.col = col

    def render(self):
        x = self.geo.card_size[0] * self.col \
            + self.geo.spacer[0] * self.col \
            + self.geo.offset[0] - 1
        y = (self.geo.card_size[1] + 1) * self.row + \
            self.geo.spacer[1] * self.row \
            + self.geo.offset[1]
        self.window.addstr(y, x, 'Y')
        return

    def update(self):
        return

    def update_direction(self, direction):
        if direction == KEY_LEFT:
            self.col = (self.col - 1) % (self.geo.cols)
            return

        if direction == KEY_RIGHT:
            self.col = (self.col + 1) % (self.geo.cols)
            return

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

    def get_pos(self):
        return self.row, self.col

    def render(self):
        for c in range(self.card_size[0]):
            for r in range(self.card_size[1]):
                x = self.geo.card_size[0] * self.col \
                    + self.geo.spacer[0] * self.col \
                    + self.geo.offset[0] + c
                y = self.geo.card_size[1] * self.row + \
                    self.geo.spacer[1] * self.row \
                    + self.geo.offset[1] + r
                self.window.addstr(y, x, 'X')

    def update(self):
        return

    def update_direction(self, direction):
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

        self.current_card = self.get_card_number(0, 0)

    def get_card_number(self, row, col):
        return row * self.rows + col

    def render(self):
        for card in self.cards:
            card.render()

    def update(self):
        return

    def update_direction(self, direction):
        #        if direction == KEY_LEFT:
        #            r, c = self.cards[self.current_card].get
        #            pos()
        #
        return

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

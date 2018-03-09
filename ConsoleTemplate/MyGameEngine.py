'''
    Simple game engine
'''

import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_DOWN, KEY_UP
from threading import Thread


class GameBoard(object):
    game_objects = []
    game_running = False

    def __init__(self, width=35, height=20, timeout=100):
        curses.initscr()
        self.window = curses.newwin(height, width, 0, 0)
        self.window.timeout(timeout)
        self.window.keypad(1)
        curses.noecho()
        curses.curs_set(0)
        self.window.border(0)

    def get_window(self):
        return self.window

    def update_game(self):
        self.game_running = True
        while self.game_running:
            self.window.clear()
            self.window.border(0)

            # Update view
            for element in self.game_objects:
                element.render()  # Every game object needs a render() function

            # Update game events
            event = self.window.getch()

            if event in [KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT]:
                for element in self.game_objects:
                    element.update_object(event)  # Every game element needs a "update_object"

            if not self.game_running:  # terminate game
                break
        curses.endwin()

    def start(self):
        Thread(target=self.update_game).start()

    def add_game_object(self, obj):
        self.game_objects.append(obj)

    def remove_game_object(self, obj):
        self.game_objects.remove(obj)

    def stop_game(self):
        self.game_running = False

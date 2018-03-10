# Import the necessary packages
from cursesmenu import *
from cursesmenu.items import *

menu = CursesMenu("Games Menu", "Choose a title")

snake_item = CommandItem("Snake",  "python TestSnake.py")
rain_of_war_item = CommandItem("Rain of war", "python RainOfWar.py")

menu.append_item(snake_item)
menu.append_item(rain_of_war_item)
menu.show()
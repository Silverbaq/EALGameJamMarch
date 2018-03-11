# Import the necessary packages
from cursesmenu import *
from cursesmenu.items import *

menu = CursesMenu("Games Menu", "Choose a title")

snake_item = CommandItem("Snake",  "python TestSnake.py")
rain_of_war_item = CommandItem("Rain of war", "python RainOfWar.py")
uwin_item = CommandItem("You win", "python UWin.py")
ulose_item = CommandItem("You lose", "python ULose.py")
hort_item = CommandItem("Heads or Tails", "python HeadsOrTails.py")
guess_item = CommandItem("Guess it", "python GuessIt.py")

menu.append_item(snake_item)
menu.append_item(rain_of_war_item)
menu.append_item(uwin_item)
menu.append_item(ulose_item)
menu.append_item(hort_item)
menu.append_item(guess_item)
menu.show()
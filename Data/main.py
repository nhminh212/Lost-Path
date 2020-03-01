from . import setup, tools
from .States import main_menu, load_screen, level_1
from . import Constants as c


def Main():
    # Add states to control here.
    run_it = tools.Control(setup.Title)
    state_dict = { c.main_menu: main_menu.Menu(),
                  c.load_screen: load_screen.LoadScreen(),
                  c.game_over: load_screen.GameOver(),
                  c.level1: level_1.Level1()}

    run_it.setup_states(state_dict, c.main_menu)
    run_it.main()
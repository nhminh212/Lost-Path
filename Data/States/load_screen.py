from .. import setup, tools
from .. import Constants as c
# from .. Components import game_sound
from .. Components import info


class LoadScreen(tools._State):
    def __init__(self):
        tools._State.__init__(self)

    def startup(self, current_time, persist):
        self.start_time = current_time
        self.persist = persist
        self.game_info = self.persist
        self.next = self.set_next_state()

        info_state = self.set_overhead_info_state()

        self.overhead_info = info.OverheadInfo(self.game_info, info_state)
        # self.sound_manager = game_sound.Sound(self.overhead_info)


    def set_next_state(self):
        # Sets the next state
        return c.level1

    def set_overhead_info_state(self):
        # sets the state to send to the overhead info object"""
        return c.load_screen


    def update(self, surface, keys, current_time):
        # Updates the loading screen
        if (current_time - self.start_time) < 2400:
            surface.fill(c.black)
            self.overhead_info.update(self.game_info)
            self.overhead_info.draw(surface)

        elif (current_time - self.start_time) < 2600:
            surface.fill(c.black)

        else:
            self.done = True


class GameOver(LoadScreen):
    # A loading screen with Game Over
    def __init__(self):
        super(GameOver, self).__init__()

    def set_next_state(self):
        # Sets next state
        return c.main_menu

    def set_overhead_info_state(self):
        # sets the state to send to the overhead info object
        return c.game_over

    def update(self, surface, keys, current_time):
        self.current_time = current_time
        # self.sound_manager.update(self.persist, None)

        if (self.current_time - self.start_time) < 7000:
            surface.fill(c.black)
            self.overhead_info.update(self.game_info)
            self.overhead_info.draw(surface)
        elif (self.current_time - self.start_time) < 7200:
            surface.fill(c.black)
        else:
            self.done = True


class TimeOut(LoadScreen):
    # Loading Screen with Time Out
    def __init__(self):
        super(TimeOut, self).__init__()

    def set_next_state(self):
        # Sets next state
        if self.persist[c.lives] == 0:
            return c.game_over
        else:
            return c.load_screen

    def update(self, surface, keys, current_time):
        self.current_time = current_time

        if (self.current_time - self.start_time) < 2400:
            surface.fill(c.black)
            self.overhead_info.update(self.game_info)
            self.overhead_info.draw(surface)
        else:
            self.done = True
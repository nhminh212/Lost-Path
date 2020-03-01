import pygame as pg
from .. import setup
from .. import Constants as c

class Sound(object):
    # Handles all sound for the game
    def __init__(self, overhead_info):
        # Initialize the class
        self.sfx_dict = setup.SFX
        self.music_dict = setup.MUSIC
        self.overhead_info = overhead_info
        self.game_info = overhead_info.game_info
        self.set_music_mixer()



    def set_music_mixer(self):
        # Sets music for level
        if self.overhead_info.state == c.level1:
            pg.mixer.music.load(self.music_dict['world_theme'])
            pg.mixer.music.play()
        elif self.overhead_info.state == c.game_over:
            pg.mixer.music.load(self.music_dict['game_over'])
            pg.mixer.music.play()
            self.state = c.game_over


    def update(self, game_info, billy):
        # Updates sound object with game info
        self.game_info = game_info
        self.billy = billy
        self.handle_state()

    def  handle_state(self):
        # Handles the state of the sound object
        if self.billy.dead:
            self.play_music('death', c.billy_dead)

        elif self.state == c.billy_dead:
            pass
        elif self.state == c.game_over:
            pass

    def play_music(self, key, state):
        # Plays new music
        pg.mixer.music.load(self.music_dict[key])
        pg.mixer.music.play()
        self.state = state

    def stop_music(self):
        # Stops playback
        pg.mixer.music.stop()




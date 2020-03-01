import os
import pygame as pg
from . import tools
from . import Constants as c

Title = c.Title

os.environ['SDL_VIDEO_CENTERED'] = '1'
pg.init()
pg.event.set_allowed([pg.KEYDOWN, pg.KEYUP, pg.QUIT])
pg.display.set_caption(c.Title)
screen = pg.display.set_mode(c.screen_size)
screen_rect = screen.get_rect()

GFX = tools.load_all_gfx(os.path.join("Resources", "graphics"))
# MUSIC = tools.load_all_sfx(os.path.join("Resources", "Music"))
# SFX = tools.load_all_sfx(os.path.join("Resources","sound"))
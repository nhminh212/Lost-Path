import pygame as pg
from .. import setup
from .. import Constants as c


class Invisible(pg.sprite.Sprite):
    def __init__(self, x, y, w, h, name):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w, h)).convert()
        # self.image.fill(c.blue_hat)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.state = None
        self.name = name




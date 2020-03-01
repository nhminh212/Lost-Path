import pygame as pg
from Data import Constants as c


class Platform(pg.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w, h)).convert()
        # self.image.fill(c.red)
        self.image.set_colorkey(c.black)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.state = None

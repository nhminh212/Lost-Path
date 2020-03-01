import pygame as pg
from .. import Constants as c


class Checkpoint(pg.sprite.Sprite):
    # Invisible sprite used to add enemies, special boxes
    # and trigger sliding down the flag pole
    def __init__(self, x, name, y=c.ground_height - 220, width=100, height=100):
        super(Checkpoint, self).__init__()
        self.image = pg.Surface((width, height))
        # self.image.fill(c.black)
        self.image.set_colorkey(c.black)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.name = name

import pygame as pg
from .. import setup
from .. import Constants as c


class Food(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.sprite_sheet = setup.GFX['drumstick']
        self.image = self.sprite_sheet
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y - 5
        self.gravity = 1
        self.y_vel = -15
        self.initial_height = self.rect.bottom - 5

    def get_image(self, x, y, w, h):
        # Get image
        image = pg.Surface([w, h]).convert()
        rect = image.get_rect()

        image.set_colorkey(c.black)
        image = pg.transform.scale(image, (30, 40))

        return image

    def update(self, game_info, viewport):
        # update food's behavior
        self.current_time = game_info[c.current_time]
        self.viewport = viewport

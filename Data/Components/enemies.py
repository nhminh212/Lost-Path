import pygame as pg
from .. import setup
from .. import Constants as c


class Enemies(pg.sprite.Sprite):
    # Base class of all enemies
    def __init__(self):
        pg.sprite.Sprite.__init__(self)

    def setup_enemies(self, x, y, direction, name, setup_frames):
        # Set up various values for enemies
        self.sprite_sheet = setup.GFX['spritesheet']
        self.frames = []
        self.frame_index = 0
        self.animated_timer = 0
        self.death_timer = 0
        self.gravity = 1.5
        self.state = c.walk

        self.name = name
        self.direction = direction
        setup_frames()

        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.bottom = y
        self.set_velocity()

    def set_velocity(self):
        # Sets velocity vector based on direction
        if self.direction == c.left:
            self.x_vel = -2
        else:
            self.x_vel = 2

        self.y_vel = 0

    def get_image(self, x, y, w, h):
        # Get image frames from the sprite sheet
        image = pg.Surface([w, h]).convert()
        rect = image.get_rect()

        image.blit(self.sprite_sheet, (0, 0), (x, y, w, h))
        image.set_colorkey(c.black)

        image = pg.transform.scale(image,
                                   (int(rect.w * c.size_multiplier),
                                    int(rect.h * c.size_multiplier)))
        return image

    def handle_state(self):
        # Enemies behavior based on state
        if self.state == c.walk:
            self.walking()
        elif self.state == c.fall:
            self.falling()

    def walking(self):
        # Moving state
        if (self.current_time - self.animated_timer) > 125:
            if self.direction == c.left:
                self.frame_index = 0
                if self.frame_index == 0:
                    self.frame_index += 1
                elif self.frame_index == 1:
                    self.frame_index = 0
            else:
                self.frame_index = 2
                if self.frame_index == 2:
                    self.frame_index += 1
                elif self.frame_index == 3:
                    self.frame_index = 2
            self.animated_timer = self.current_time

    def falling(self):
        # For when it falls off a ledge
        if self.y_vel < 10:
            self.y_vel += self.gravity

    def jumped_on(self):
        # Placeholder for when the enemy is stomped on
        pass

    def animation(self):
        # Switching between two frames
        self.image = self.frames[self.frame_index]

    def update(self, game_info, *args):
        # Update enemy behavior
        self.current_time = game_info[c.current_time]
        self.handle_state()
        self.animation()


class dog(Enemies):
    def __init__(self, y=c.ground_height, x=0, direction=c.left, name='dog'):
        Enemies.__init__(self)
        self.setup_enemies(x, y, direction, name, self.setup_frames)


    def setup_frames(self):
        # Put the images frames in a list to be animated

        self.frames.append(self.get_image(5432, 3059, 573, 392))  # Left 1
        self.frames.append(self.get_image(9, 3059, 561, 414))  # Left 2

        self.frames.append(self.get_image(2764, 3059, 573, 392))  # Right 1
        self.frames.append(self.get_image(3868, 1534, 560, 414))  # Right 2

    def get_image(self, x, y, w, h):
        # extract image from sprite sheet
        image = pg.Surface([w, h], pg.SRCALPHA)
        rect = image.get_rect()

        image.blit(self.sprite_sheet, (0, 0), (x, y, w, h))
        image = pg.transform.scale(image,
                                   (int(rect.w * c.size_multiplier),
                                    int(rect.h * c.size_multiplier)))
        return image


class bird(Enemies):
    def __init__(self, y=c.ground_height, x=0, direction=c.left, name='bird'):
        Enemies.__init__(self)
        self.setup_enemies(x, y, direction, name, self.setup_frames)

    def setup_frames(self):
        # Put the images frames in a list to be animated

        self.frames.append(self.get_image(5802, 4537, 671, 343))  # Left
        self.frames.append(self.get_image(5802, 4537, 671, 343))  # Left
        self.frames.append(self.get_image(4330, 4537, 671, 343))  # Right
        self.frames.append(self.get_image(4330, 4537, 671, 343))  # Right

    def get_image(self, x, y, w, h):
        # extract image from sprite sheet
        image = pg.Surface([w, h], pg.SRCALPHA)
        rect = image.get_rect()

        image.blit(self.sprite_sheet, (0, 0), (x, y, w, h))
        image = pg.transform.scale(image,
                                   (int(rect.w * c.size_multiplier),
                                    int(rect.h * c.size_multiplier)))
        return image


class rock(Enemies):
    def __init__(self, y=50, x=1639, direction=None, name='cloud'):
        Enemies.__init__(self)
        self.setup_enemies(x, y, direction, name, self.setup_frames)

    def setup_frames(self):
        self.frames.append((self.get_image(0, 1408, 590, 579)))
        self.frames.append((self.get_image(0, 1408, 590, 579)))
        self.frames.append((self.get_image(0, 1408, 590, 579)))
        self.frames.append((self.get_image(0, 1408, 590, 579)))
        self.frames.append((self.get_image(0, 1408, 590, 579)))

    def get_image(self, x, y, w, h):
        # extract image from sprite sheet
        image = pg.Surface([w, h], pg.SRCALPHA)

        image.blit(setup.GFX['trap'], (0, 0), (x, y, w, h))
        image = pg.transform.scale(image,
                                       (100, 100))
        return image
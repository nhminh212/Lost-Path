import pygame as pg
from .. import setup, tools
from .. import Constants as c
from ..Components import info, billy


class Menu(tools._State):
    def __init__(self):
        # Initialize the state
        tools._State.__init__(self)
        persist = {c.lives: 3,
                   c.current_time: 0.0,
                   c.level_state: None,
                   c.camera_start_x: 0,
                   c.billy_dead: False}
        self.startup(0.0, persist)

    def startup(self, current_time, persist):
        # Called every time the game's state becomes this one.  Initializes
        # certain values
        self.next = c.load_screen
        self.persist = persist
        self.game_info = persist
        self.overhead_info = info.OverheadInfo(self.game_info, c.main_menu)

        self.sprite_sheet = setup.GFX['title_screen']
        self.setup_background()
        self.setup_billy()
        self.setup_cursor()

    def setup_cursor(self):
        # Creates the cursor to select main menu option
        self.cursor = pg.sprite.Sprite()
        dest = (450, 400)
        self.cursor.image, self.cursor.rect = self.get_image(1, 0, 44, 74,
                                                             dest, setup.GFX['sprite'])
        self.cursor.image = pg.transform.scale(self.cursor.image, (30, 40))
        self.cursor.state = c.new_game

    def setup_billy(self):
        # Place Billy at the beginning of the level
        self.billy = billy.Billy()
        self.billy.rect.x = 110
        self.billy.rect.bottom = c.ground_height

    def setup_background(self):
        # Setup the background image to blit
        self.background = setup.GFX['black']
        self.background_rect = self.background.get_rect()
        self.background = pg.transform.scale(self.background,
                                             (int(self.background_rect.w * c.background_multiplier),
                                              int(self.background_rect.h * c.background_multiplier)))

        self.viewport = setup.screen.get_rect(bottom=setup.screen_rect.bottom)

        self.image_dict = setup.GFX['label']
        self.image_dict = pg.transform.scale(self.image_dict, (700, 400))

    def get_image(self, x, y, w, h, dest, sprite_sheet):
        # Return images and rects to blit onto the screen
        image = pg.Surface([w, h])
        rect = image.get_rect()

        image.blit(sprite_sheet, (0, 0), (x, y, w, h))
        if sprite_sheet == setup.GFX['title_screen']:
            image.set_colorkey((255, 0, 255))
            image = pg.transform.scale(image,
                                       (int(rect.w * c.size_multiplier),
                                        int(rect.h * c.size_multiplier)))

        else:
            image.set_colorkey(c.black)
            image = pg.transform.scale(image,
                                       (int(rect.w * 3),
                                        int(rect.h * 3)))

        rect = image.get_rect()
        rect.x = dest[0]
        rect.y = dest[1]
        return (image, rect)

    def update(self, surface, keys, current_time):
        # Updates the state every refresh
        self.current_time = current_time
        self.game_info[c.current_time] = self.current_time
        self.update_cursor(keys)
        self.overhead_info.update(self.game_info)

        surface.blit(self.background, self.viewport, self.viewport)
        surface.blit(self.image_dict, (280, 60))
        surface.blit(self.billy.image, self.billy.rect)
        surface.blit(self.cursor.image, self.cursor.rect)
        self.overhead_info.draw(surface)

    def update_cursor(self, keys):
        # Update the position of the cursor
        input_list = [pg.K_RETURN]

        if self.cursor.state == c.new_game:
            self.cursor.rect.y = 460
            if keys[pg.K_DOWN]:
                self.cursor.state = c.cont
            for input in input_list:
                if keys[input]:
                    self.reset_game_info()
                    self.done = True
        elif self.cursor.state == c.cont:
            self.cursor.rect.y = 530
            if keys[pg.K_UP]:
                self.cursor.state = c.new_game
            elif keys[pg.K_DOWN]:
                self.cursor.state = c.helps
        elif self.cursor.state == c.helps:
            self.cursor.rect.y = 600
            if keys[pg.K_UP]:
                self.cursor.state = c.cont
            elif keys[pg.K_DOWN]:
                self.cursor.state = c.quit_game
        elif self.cursor.state == c.quit_game:
            self.cursor.rect.y = 670
            if keys[pg.K_UP]:
                self.cursor.state = c.helps

    def reset_game_info(self):
        # Resets the game info in case of a Game Over and restart
        self.game_info[c.lives] = 3
        self.game_info[c.current_time] = 0.0
        self.game_info[c.level_state] = None

        self.persist = self.game_info

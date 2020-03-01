import pygame as pg
import os
from .. import setup
from .. import Constants as c


class Character(pg.sprite.Sprite):
# Parent class for all characters used for the overhead level info
    def __init__(self, image):
        super(Character, self).__init__()
        self.image = image
        self.rect = self.image.get_rect()


class OverheadInfo(object):
# Class for level information like score, coin total,
# and time remaining
    def __init__(self, game_info, state):
        self.sprite_sheet = setup.GFX['text_images']
        self.current_time = 0
        self.total_lives = game_info[c.lives]
        self.state = state
        self.game_info = game_info

        self.create_image_dict()
        self.create_info_labels()
        self.create_load_screen_labels()
        self.create_billy_image()
        self.create_game_over_label()
        self.create_main_menu_labels()

    def create_image_dict(self):
        # Creates the initial images for the score
        self.image_dict = {}
        image_list = []

        image_list.append(self.get_image(3, 230, 7, 7))
        image_list.append(self.get_image(12, 230, 7, 7))
        image_list.append(self.get_image(19, 230, 7, 7))
        image_list.append(self.get_image(27, 230, 7, 7))
        image_list.append(self.get_image(35, 230, 7, 7))
        image_list.append(self.get_image(43, 230, 7, 7))
        image_list.append(self.get_image(51, 230, 7, 7))
        image_list.append(self.get_image(59, 230, 7, 7))
        image_list.append(self.get_image(67, 230, 7, 7))
        image_list.append(self.get_image(75, 230, 7, 7))

        image_list.append(self.get_image(83, 230, 7, 7))
        image_list.append(self.get_image(91, 230, 7, 7))
        image_list.append(self.get_image(99, 230, 7, 7))
        image_list.append(self.get_image(107, 230, 7, 7))
        image_list.append(self.get_image(115, 230, 7, 7))
        image_list.append(self.get_image(123, 230, 7, 7))
        image_list.append(self.get_image(3, 238, 7, 7))
        image_list.append(self.get_image(11, 238, 7, 7))
        image_list.append(self.get_image(20, 238, 7, 7))
        image_list.append(self.get_image(27, 238, 7, 7))
        image_list.append(self.get_image(35, 238, 7, 7))
        image_list.append(self.get_image(44, 238, 7, 7))
        image_list.append(self.get_image(51, 238, 7, 7))
        image_list.append(self.get_image(59, 238, 7, 7))
        image_list.append(self.get_image(67, 238, 7, 7))
        image_list.append(self.get_image(75, 238, 7, 7))
        image_list.append(self.get_image(83, 238, 7, 7))
        image_list.append(self.get_image(91, 238, 7, 7))
        image_list.append(self.get_image(99, 238, 7, 7))
        image_list.append(self.get_image(108, 238, 7, 7))
        image_list.append(self.get_image(115, 238, 7, 7))
        image_list.append(self.get_image(123, 238, 7, 7))
        image_list.append(self.get_image(3, 246, 7, 7))
        image_list.append(self.get_image(11, 246, 7, 7))
        image_list.append(self.get_image(20, 246, 7, 7))
        image_list.append(self.get_image(27, 246, 7, 7))
        image_list.append(self.get_image(48, 248, 7, 7))

        image_list.append(self.get_image(68, 249, 6, 2))
        image_list.append(self.get_image(75, 247, 6, 6))

        character_string = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ -*'

        for character, image in zip(character_string, image_list):
            self.image_dict[character] = image

    def get_image(self, x, y, w, h):
        # Extract image from sprite sheet
        image = pg.Surface([w, h])
        rect = image.get_rect()

        image.blit(self.sprite_sheet, (0, 0), (x, y, w, h))
        image.set_colorkey((92, 148, 252))
        image = pg.transform.scale(image,
                                   (int(rect.w*2.9),
                                    int(rect.h*2.9)))
        return image

    def create_info_labels(self):
        # Create the labels that describe each info
        self.billy_label = []


        self.create_label(self.billy_label, 'LOST PATH', 75, 30)

        self.label_list = [self.billy_label]

    def create_load_screen_labels(self):
        # Create labels for the center info of a load screen
        world_label = []
        number_label = []

        self.create_label(world_label, 'LEVEL', 490, 300)
        self.create_label(number_label, '1', 630, 300)

        self.center_labels = [world_label, number_label]

    def create_label(self, label_list, string, x, y):
        # Create a label (World, Time, Billy)
        for letter in string:
            label_list.append(Character(self.image_dict[letter]))

        self.set_label_rects(label_list, x, y)

    def set_label_rects(self, label_list, x, y):
        # Set a location of each individual character
        for i, letter in enumerate(label_list):
            letter.rect.x = x + ((letter.rect.w + 3) * i)
            letter.rect.y = y
            if letter.image == self.image_dict['-']:
                letter.rect.y += 7
                letter.rect.x += 2

    def create_billy_image(self):
        # Get Billy image
        self.life_times_image = self.get_image(75, 247, 6, 6)
        self.life_times_rect = self.life_times_image.get_rect(center=(578, 465))
        self.life_total_label = []
        self.create_label(self.life_total_label, str(self.total_lives), 620, 455)

        self.sprite_sheet = setup.GFX['spritesheet']
        self.billy_image = self.get_image(7, 0, 421, 706)
        self.billy_image = pg.transform.scale(self.billy_image,(43, 50))
        self.billy_rect = self.billy_image.get_rect(center=(505, 455))

    def create_game_over_label(self):
        # Create the label for the GAME OVER screen
        game_label = []
        over_label = []

        self.create_label(game_label, 'GAME', 280, 300)
        self.create_label(over_label, 'OVER', 400, 300)

        self.game_over_label = [game_label, over_label]

    def create_main_menu_labels(self):
        # Create labels for the main menu screen
        new_game = []
        cont = []
        helps = []
        quit_game = []

        self.create_label(new_game, 'NEW GAME', 500, 470)
        self.create_label(cont, 'CONTINUE', 500, 540)
        self.create_label(helps, 'HELP', 500, 610)
        self.create_label(quit_game, 'QUIT GAME', 500, 680)

        self.main_menu_labels = [new_game, cont, helps, quit_game]

    def update(self, level_info, billy = None):
        # Updates all overhead info
        self.billy = billy

    def draw(self, surface):
        # Draws overhead info based on state
        if self.state == c.main_menu:
            self.draw_main_menu_info(surface)
        elif self.state == c.load_screen:
            self.draw_loading_screen_info(surface)
        elif self.state == c.level1:
            self.draw_level_screen_info(surface)
        elif self.state == c.game_over:
            self.draw_game_over_screen_info(surface)
        elif self.state == c.end_of_level:
            self.draw_level_screen_info(surface)
        else:
            pass

    def draw_main_menu_info(self, surface):
        # Draw info for main menu
        for label in self.main_menu_labels:
            for letter in label:
                surface.blit(letter.image, letter.rect)

        for label in self.label_list:
            for letter in label:
                surface.blit(letter.image, letter.rect)

    def draw_loading_screen_info(self, surface):
        # Draw info for loading screen
        for word in self.center_labels:
            for letter in word:
                surface.blit(letter.image, letter.rect)

        for word in self.life_total_label:
            surface.blit(word.image, word.rect)

        surface.blit(self.billy_image, self.billy_rect)
        surface.blit(self.life_times_image, self.life_times_rect)

        for label in self.label_list:
            for letter in label:
                surface.blit(letter.image, letter.rect)

    def draw_level_screen_info(self, surface):
        # Draws info during regular game play
        for label in self.label_list:
            for letter in label:
                surface.blit(letter.image, letter.rect)

    def draw_game_over_screen_info(self, surface):
        # Draws info when game over
        for word in self.game_over_label:
            for letter in word:
                surface.blit(letter.image, letter.rect)

        for label in self.label_list:
            for letter in label:
                surface.blit(letter.image, letter.rect)
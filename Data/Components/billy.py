import pygame as pg
from Data import setup, tools
import platform
from .. import Constants as c


class Billy(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.sprite_sheet = setup.GFX['spritesheet']  # import Billy Sprite

        self.setup_timers()
        self.setup_state_booleans()
        self.setup_forces()
        self.setup_counter()
        self.load_images_from_sheets()

        self.state = c.walk
        self.image = self.right_frames[self.frame_index]
        self.rect = self.image.get_rect()
        self.mask = pg.mask.from_surface(self.image)

        self.key_timer = 0

    def setup_timers(self):
        # Animation timers
        self.walking_timer = 0
        self.death_timer = 0
        self.transition_timer = 0
        self.checkpoint_timer = 0

    def setup_state_booleans(self):
        # Booleans for each states
        self.facing_right = True
        self.allow_jump = True
        self.dead = False
        self.hit = False
        self.pass_level1 = False
        self.in_transition_state = False
        self.pass_level1 = False

    def setup_forces(self):
        # forces for movements
        self.x_vel = 0
        self.y_vel = 0
        self.max_x_vel = c.max_walk_speed
        self.max_y_vel = c.max_y_vel
        self.jump_vel = c.jump_vel
        self.x_accel = c.walk_accel
        self.gravity = c.gravity

    def setup_counter(self):
        # hold important values
        self.frame_index = 0

    def load_images_from_sheets(self):
        # Extract Billy images from sprite sheets
        self.right_frames = []
        self.left_frames = []

        self.right = []
        self.left = []
        self.right.append(self.get_image(7, 0, 421, 706))  # Right standing [0]
        self.right.append(self.get_image(1259, 8, 435, 688))  # Right walking 1 [1]
        self.right.append(self.get_image(4050, 5, 511, 695))  # Right walking 2 [2]
        self.right.append(self.get_image(4159, 3057, 443, 650))  # Right jump [3]
        self.right.append(self.get_image(2514, 19, 702, 412))  # Right death [4]
        self.right.append(self.get_image(4, 7384, 564, 691))  # Right death 1 [5]
        self.right.append(self.get_image(2984, 5847, 721, 489))  # Right death 2 [6]

        self.left.append(self.get_image(7, 1535, 425, 705))  # Left standing [0]
        self.left.append(self.get_image(1255, 1533, 439, 693))  # Left walking 1 [1]
        self.left.append(self.get_image(2525, 1530, 511, 695))  # Left walking 2 [2]
        self.left.append(self.get_image(5388, 7, 443, 650))  # Left jump [3]
        self.left.append(self.get_image(5814, 4544, 702, 412))  # Left death [4]
        self.left.append(self.get_image(6079, 5854, 564, 592))  # Left death [5]
        self.left.append(self.get_image(4534, 5847, 712, 489))  # Left death [6]

        self.normal_frames = [self.right, self.left]
        self.right_frames = self.normal_frames[0]
        self.left_frames = self.normal_frames[1]

    def get_image(self, x, y, w, h):
        # extract image from sprite sheet
        image = pg.Surface([w, h], pg.SRCALPHA)
        rect = image.get_rect()

        image.blit(self.sprite_sheet, (0, 0), (x, y, w, h))
        image = pg.transform.scale(image,
                                   (int(rect.w * c.size_multiplier),
                                    int(rect.h * c.size_multiplier)))
        return image

    def update(self, keys, game_info):
        # Update Billy's animations once per frame
        self.current_time = game_info[c.current_time]
        self.handle_state(keys)
        self.animation()

    def handle_state(self, keys):
        # Billy's behavior based on states
        if self.state == c.stand:
            self.standing(keys)
        elif self.state == c.walk:
            self.walking(keys)
        elif self.state == c.jump:
            self.jumping(keys)
        elif self.state == c.fall:
            self.falling(keys)
        elif self.state == c.death_jump:
            self.jumping_to_death()

    def standing(self, keys):
        # Billy's standing state
        self.check_to_allow_jump(keys)

        self.frame_index = 0
        self.x_vel = 0
        self.y_vel = 0

        if keys[tools.keybinding['left']]:
            self.facing_right = False
            self.state = c.walk
        elif keys[tools.keybinding['right']]:
            self.facing_right = True
            self.state = c.walk
        elif keys[tools.keybinding['jump']]:
            if self.allow_jump:
                self.state = c.jump
                self.y_vel = c.jump_vel
        else:
            self.state = c.stand

    def check_to_allow_jump(self, keys):
        # Check jump
        if not keys[tools.keybinding['jump']]:
            self.allow_jump = True

    def walking(self, keys):
        # Check walking state
        self.check_to_allow_jump(keys)

        if self.frame_index == 0:
            self.frame_index += 1
            self.walking_timer = self.current_time
        else:
            if (self.current_time - self.walking_timer >
                    self.calculate_animation_speed()):
                if self.frame_index < 2:
                    self.frame_index += 1
                else:
                    self.frame_index = 1

                self.walking_timer = self.current_time

        if keys[tools.keybinding['jump']]:
            if self.allow_jump:
                self.state = c.jump
                if self.x_vel > 4.5 or self.x_vel < -4.5:
                    self.y_vel = c.jump_vel - .5
                else:
                    self.y_vel = c.jump_vel

        if keys[tools.keybinding['left']]:
            self.facing_right = False
            self.x_accel = c.walk_accel

            if self.x_vel > (self.max_x_vel * -1):
                self.x_vel -= self.x_accel
                if self.x_vel > -0.5:
                    self.x_vel = -0.5
                elif self.x_vel < (self.max_x_vel * -1):
                    self.x_vel += self.x_accel

        elif keys[tools.keybinding['right']]:
            self.facing_right = True
            self.x_accel = c.walk_accel

            if self.x_vel < self.max_x_vel:
                self.x_vel += self.x_accel
                if self.x_vel < 0.5:
                    self.x_vel = 0.5
            elif self.x_vel > self.max_x_vel:
                self.x_vel -= self.x_accel

        else:
            if self.facing_right:
                if self.x_vel > 0:
                    self.x_vel -= self.x_accel
                else:
                    self.x_vel = 0
                    self.state = c.stand
            else:
                if self.x_vel < 0:
                    self.x_vel += self.x_accel
                else:
                    self.x_vel = 0
                    self.state = c.stand

    def calculate_animation_speed(self):
        # Walk animation related to x_vel
        if self.x_vel == 0:
            animation_speed = 130
        elif self.x_vel > 0:
            animation_speed = 130 - (self.x_vel * (13))
        else:
            animation_speed = 130 - (self.x_vel * (13) * -1)

        return animation_speed

    def jumping(self, keys):
        # Jump states
        self.allow_jump = False
        self.frame_index = 3
        self.gravity = c.jump_gravity
        self.y_vel += self.gravity

        if self.y_vel >= 0 and self.y_vel < self.max_y_vel:
            self.gravity = c.gravity
            self.state = c.fall

        if keys[tools.keybinding['left']]:
            if self.x_vel > (self.max_x_vel * -1):
                self.x_vel -= self.x_accel

        elif keys[tools.keybinding['right']]:
            if self.x_vel < self.max_x_vel:
                self.x_vel += self.x_accel

        if not keys[tools.keybinding['jump']]:
            self.gravity = c.gravity
            self.state = c.fall

    def falling(self, keys):
        # Fall states
        if self.y_vel < c.max_y_vel:
            self.y_vel += self.gravity

        if keys[tools.keybinding['left']]:
            if self.x_vel > (self.max_x_vel * - 1):
                self.x_vel -= self.x_accel

        elif keys[tools.keybinding['right']]:
            if self.x_vel < self.max_x_vel:
                self.x_vel += self.x_accel

    def jumping_to_death(self):
        # Called when Billy is in a DEATH_JUMP state"""
        if self.death_timer == 0:
            self.death_timer = self.current_time
        elif (self.current_time - self.death_timer) > 500:
            self.rect.y += self.y_vel
            self.y_vel += self.gravity
        self.frame_index = 4
        if self.facing_right:
            self.image = self.right_frames[self.frame_index]
        else:
            self.image = self.left_frames[self.frame_index]
        if self.frame_index < 6:
            self.frame_index += 1
        else:
            self.frame_index = 6

    def start_death_jump(self, game_info):
        # Used to put Mario in a DEATH_JUMP state
        self.dead = True
        game_info[c.billy_dead] = True
        self.y_vel = -11
        self.gravity = .5
        self.frame_index = 3
        if self.facing_right:
            self.image = self.right_frames[self.frame_index]
        else:
            self.image = self.left_frames[self.frame_index]
        self.state = c.death_jump
        self.in_transition_state = True


    def timer_between_these_two_times(self, start_time, end_time):
        # Check timer with action
        if start_time <= (self.current_time - self.transition_timer) < end_time:
            return True

    def adjust_rect(self):
        # Make sure new Rect has the same bottom and left location as previous Rect
        x = self.rect.x
        bottom = self.rect.bottom
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.bottom = bottom

    def animation(self):
        if self.facing_right:
            self.image = self.right_frames[self.frame_index]
        else:
            self.image = self.left_frames[self.frame_index]

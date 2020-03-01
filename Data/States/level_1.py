import pygame as pg
from .. import setup, tools
from .. import Constants as c
# from .. import game_sound
from ..Components import billy
from ..Components import platforms
from ..Components import enemies
from ..Components import checkpoint
from ..Components import info
from ..Components import invisible_trap


class Level1(tools._State):
    def __init__(self):
        tools._State.__init__(self)

    def startup(self, current_time, persist):
        # Called when the State object is created
        self.game_info = persist
        self.persist = self.game_info
        self.game_info[c.current_time] = current_time
        self.game_info[c.level_state] = c.not_frozen
        self.game_info[c.billy_dead] = False

        self.state = c.not_frozen
        self.death_timer = 0

        self.overhead_info_display = info.OverheadInfo(self.game_info, c.level1)
        # self.sound_manager = game_sound.Sound(self.overhead_info_display)

        self.setup_background()
        self.setup_ground()
        self.setup_bricks()
        self.setup_steps()
        self.setup_invisible_trap()
        self.setup_food()
        self.setup_enemies()
        self.setup_billy()
        self.setup_checkpoints()
        self.setup_spritegroups()

    def setup_background(self):
        # set background image, rect and scale
        self.background = setup.GFX['background']
        self.back_rect = self.background.get_rect()
        self.background = pg.transform.scale(self.background,
                                             (int(self.back_rect.w * c.background_multiplier),
                                              int(self.back_rect.h * c.background_multiplier)))
        self.back_rect = self.background.get_rect()
        w = self.back_rect.w
        h = self.back_rect.h

        self.level = pg.Surface((w, h)).convert()
        self.level_rect = self.level.get_rect()
        self.viewport = setup.screen.get_rect(bottom=self.level_rect.bottom)
        self.viewport.x = self.game_info[c.camera_start_x]

    def setup_ground(self):
        # Create rectangles over top of the ground for sprites to walk on
        ground_rect1 = platforms.Platform(0, c.ground_height, 912, 90)
        ground_rect2 = platforms.Platform(1179, c.ground_height, 419, 90)
        ground_rect3 = platforms.Platform(1864, c.ground_height, 2083, 90)
        ground_rect4 = platforms.Platform(4172, c.ground_height, 2900, 90)
        ground_rect5 = platforms.Platform(7620, c.ground_height, 2920, 90)

        self.ground_group = pg.sprite.Group(ground_rect1,
                                            ground_rect2,
                                            ground_rect3,
                                            ground_rect4,
                                            ground_rect5)

    def setup_bricks(self):
        # Creates all the bricks for the level.

        brick1 = platforms.Platform(508, 392, 317, 71)
        brick2 = platforms.Platform(3235, 380, 825, 71)
        brick3 = platforms.Platform(4495, 510, 126, 71)
        # brick4 = platforms.Platform(6473, 475, 101, 71)
        brick5 = platforms.Platform(8216, 470, 825, 71)

        self.brick_group = pg.sprite.Group(brick1, brick2,
                                           brick3,  # brick4,
                                           brick5)

    def setup_steps(self):
        # Create collideable rects for all the steps

        step1 = platforms.Platform(1438, 490, 160, 400)
        step2 = platforms.Platform(2422, 510, 160, 400)
        step3 = platforms.Platform(2968, 620, 103, 170)
        step4 = platforms.Platform(6086, 650, 131, 100)
        step5 = platforms.Platform(6742, 653, 132, 82)
        step6 = platforms.Platform(6875, 555, 132, 170)
        step7 = platforms.Platform(7003, 470, 127, 400)
        step8 = platforms.Platform(7623, 470, 127, 400)
        step9 = platforms.Platform(7751, 555, 132, 170)
        step10 = platforms.Platform(7883, 653, 127, 82)

        self.step_group = pg.sprite.Group(step1, step2,
                                          step3, step4,
                                          step5, step6,
                                          step7, step8,
                                          step9, step10)

    def setup_invisible_trap(self):
        # Create traps that only appear when interact

        # First trap (spike)
        trap1 = invisible_trap.Invisible(508, 463, 32, 30, 'spike1')
        # trap2 = invisible_trap.Invisible(540, 463, 32, 30, 'spike1')
        # trap3 = invisible_trap.Invisible(572, 463, 32, 30, 'spike1')
        # trap4 = invisible_trap.Invisible(604, 463, 32, 30, 'spike1')
        # trap5 = invisible_trap.Invisible(636, 463, 32, 30, 'spike1')
        # trap6 = invisible_trap.Invisible(668, 463, 32, 30, 'spike1')
        # trap7 = invisible_trap.Invisible(700, 463, 32, 30, 'spike1')
        # trap8 = invisible_trap.Invisible(732, 463, 32, 30, 'spike1')
        # trap9 = invisible_trap.Invisible(764, 463, 32, 30, 'spike1')
        # trap10 = invisible_trap.Invisible(796, 463, 29, 30, 'spike1')
        #
        # # Second trap (spike)
        # trap11 = invisible_trap.Invisible(1278, c.ground_height - 30, 32, 30, 'spike')
        # trap12 = invisible_trap.Invisible(1310, c.ground_height - 30, 32, 30, 'spike')
        # trap13 = invisible_trap.Invisible(1342, c.ground_height - 30, 32, 30, 'spike')
        # trap14 = invisible_trap.Invisible(1374, c.ground_height - 30, 32, 30, 'spike')
        # trap15 = invisible_trap.Invisible(1406, c.ground_height - 30, 32, 30, 'spike')
        #
        # # Third trap (cloud)
        # trap16 = invisible_trap.Invisible(1638, 50, 180, 120, 'cloud')
        #
        # # Fourth trap (hole)
        # trap17 = invisible_trap.Invisible(1598, c.ground_height - 30, 266, 120, 'hole')
        #
        # # Fifth trap (spike)
        # trap18 = invisible_trap.Invisible(2068, c.ground_height - 30, 32, 30, 'spike')
        # trap19 = invisible_trap.Invisible(2100, c.ground_height - 30, 32, 30, 'spike')
        # trap20 = invisible_trap.Invisible(2132, c.ground_height - 30, 32, 30, 'spike')
        # trap21 = invisible_trap.Invisible(2164, c.ground_height - 30, 32, 30, 'spike')
        # trap22 = invisible_trap.Invisible(2196, c.ground_height - 30, 32, 30, 'spike')
        # trap23 = invisible_trap.Invisible(2228, c.ground_height - 30, 32, 30, 'spike')
        #
        # # Sixth trap (rock)
        # trap24 = invisible_trap.Invisible(2422, 240, 160, 200, 'check')
        # trap25 = invisible_trap.Invisible(2422, -158, 160, 160, 'rock')
        #
        # # Seventh trap (flag)
        # trap26 = invisible_trap.Invisible(2968, 492, 103, 125, 'flag')
        #
        # # Eighth trap (rock)
        # trap27 = invisible_trap.Invisible(3235, 202, 160, 180, 'check')
        # trap28 = invisible_trap.Invisible(3235, -158, 160, 160, 'rock')
        #
        # trap29 = invisible_trap.Invisible(3395, 202, 160, 180, 'check')
        # trap30 = invisible_trap.Invisible(3395, -158, 160, 160, 'rock')
        #
        # trap31 = invisible_trap.Invisible(3555, 202, 160, 180, 'check')
        # trap32 = invisible_trap.Invisible(3555, -158, 160, 160, 'rock')
        #
        # trap33 = invisible_trap.Invisible(3715, 202, 160, 180, 'check')
        # trap34 = invisible_trap.Invisible(3715, -158, 160, 160, 'rock')
        #
        # trap35 = invisible_trap.Invisible(3875, 202, 160, 180, 'check')
        # trap36 = invisible_trap.Invisible(3875, -158, 160, 160, 'rock')
        #
        # # Ninth trap (spike)
        # trap37 = invisible_trap.Invisible(3335, 451, 65, 95, 'spike1')
        # trap38 = invisible_trap.Invisible(3400, 451, 65, 95, 'spike1')
        # trap39 = invisible_trap.Invisible(3465, 451, 65, 95, 'spike1')
        # trap40 = invisible_trap.Invisible(3530, 451, 65, 95, 'spike1')
        # trap41 = invisible_trap.Invisible(3595, 451, 65, 95, 'spike1')
        # trap42 = invisible_trap.Invisible(3660, 451, 65, 95, 'spike1')
        # trap43 = invisible_trap.Invisible(3725, 451, 65, 95, 'spike1')
        # trap44 = invisible_trap.Invisible(3790, 451, 65, 95, 'spike1')
        #
        # # Tenth trap (cloud)
        # trap45 = invisible_trap.Invisible(4135, 152, 180, 120, 'cloud')
        #
        # # Eleventh trap (spike)
        # trap46 = invisible_trap.Invisible(4283, c.ground_height - 30, 32, 30, 'spike')
        # trap47 = invisible_trap.Invisible(4315, c.ground_height - 30, 32, 30, 'spike')
        # trap48 = invisible_trap.Invisible(4347, c.ground_height - 30, 32, 30, 'spike')
        # trap49 = invisible_trap.Invisible(4379, c.ground_height - 30, 32, 30, 'spike')
        # trap50 = invisible_trap.Invisible(4411, c.ground_height - 30, 32, 30, 'spike')
        # trap51 = invisible_trap.Invisible(4443, c.ground_height - 30, 32, 30, 'spike')
        #
        # # Twelfth trap (spike)
        # trap52 = invisible_trap.Invisible(4665, c.ground_height - 30, 32, 30, 'spike')
        # trap53 = invisible_trap.Invisible(4697, c.ground_height - 30, 32, 30, 'spike')
        # trap54 = invisible_trap.Invisible(4729, c.ground_height - 30, 32, 30, 'spike')
        # trap55 = invisible_trap.Invisible(4761, c.ground_height - 30, 32, 30, 'spike')
        # trap56 = invisible_trap.Invisible(4793, c.ground_height - 30, 32, 30, 'spike')
        # trap57 = invisible_trap.Invisible(4825, c.ground_height - 30, 32, 30, 'spike')
        #
        # # Thirteenth trap (cloud)
        # trap58 = invisible_trap.Invisible(5025, 340, 180, 120, 'cloud')
        # trap59 = invisible_trap.Invisible(5625, 340, 180, 120, 'cloud')
        #
        # # Fourteenth trap (rock)
        # trap60 = invisible_trap.Invisible(6086, 460, 131, 180, 'check')
        # trap61 = invisible_trap.Invisible(6086, -158, 131, 131, 'rock')
        #
        # # fifteenth trap (rock)
        # trap62 = invisible_trap.Invisible(7623, 270, 127, 180, 'check')
        # trap63 = invisible_trap.Invisible(7623, -158, 127, 127, 'rock')
        #
        # trap64 = invisible_trap.Invisible(7751, 355, 131, 180, 'check')
        # trap65 = invisible_trap.Invisible(7751, -158, 131, 131, 'rock')
        #
        # trap66 = invisible_trap.Invisible(7883, 453, 127, 180, 'check')
        # trap67 = invisible_trap.Invisible(7883, -158, 127, 127, 'rock')
        #
        # self.spike_group = pg.sprite.Group(trap11, trap12,
        #                                    trap13, trap14,
        #                                    trap15,
        #                                    trap17, trap18,
        #                                    trap19, trap20,
        #                                    trap21, trap22,
        #                                    trap23, trap26,
        #                                    trap46,
        #                                    trap47, trap48,
        #                                    trap49, trap50,
        #                                    trap51, trap52,
        #                                    trap53, trap54,
        #                                    trap55, trap56,
        #                                    trap57)
        # self.spike1_group = pg.sprite.Group(trap1, trap2,
        #                                     trap3, trap4,
        #                                     trap5, trap6,
        #                                     trap7, trap8,
        #                                     trap9, trap10,
        #                                     trap37, trap38,
        #                                     trap39, trap40,
        #                                     trap41, trap42,
        #                                     trap43, trap44)
        # self.cloud_group = pg.sprite.Group(trap16,
        #                                    trap45,
        #                                    trap58,
        #                                    trap59)
        # self.rock_group = pg.sprite.Group(trap25, trap28,
        #                                   trap30, trap32,
        #                                   trap34, trap36,
        #                                   trap61, trap63,
        #                                   trap65, trap67)
        # self.check_group = pg.sprite.Group(trap24, trap27,
        #                                    trap29, trap31,
        #                                    trap33, trap35,
        #                                    trap60, trap62,
        #                                    trap64, trap66)
        # self.trap_group = [self.spike_group,
        #                    self.spike1_group,
        #                    self.cloud_group,
        #                    self.rock_group,
        #                    self.check_group]

    def setup_food(self):
        pass

    def setup_enemies(self):
        # Creates all the enemies and stores them in a list of lists
        dog0 = enemies.dog()
        dog1 = enemies.dog(380)
        dog2 = enemies.dog()
        dog3 = enemies.dog()
        dog4 = enemies.dog()
        dog5 = enemies.dog()
        dog6 = enemies.dog()
        dog7 = enemies.dog()
        dog8 = enemies.dog()
        dog9 = enemies.dog()

        rock1 = enemies.rock()
        rock2 = enemies.rock()
        rock3 = enemies.rock()
        rock4 = enemies.rock()
        rock5 = enemies.rock()
        rock6 = enemies.rock()
        rock7 = enemies.rock()

        enemy_group1 = pg.sprite.Group(dog0)
        enemy_group2 = pg.sprite.Group(dog1)
        enemy_group3 = pg.sprite.Group(dog2)
        enemy_group4 = pg.sprite.Group(dog3)
        enemy_group5 = pg.sprite.Group(dog4)
        enemy_group6 = pg.sprite.Group(dog5)
        enemy_group7 = pg.sprite.Group(dog6)
        enemy_group8 = pg.sprite.Group(dog7)
        enemy_group9 = pg.sprite.Group(dog8)
        enemy_group10 = pg.sprite.Group(dog9)

        rock_group1 = pg.sprite.Group(rock1)
        rock_group2 = pg.sprite.Group(rock2)
        rock_group3 = pg.sprite.Group(rock3)
        rock_group4 = pg.sprite.Group(rock4)
        rock_group5 = pg.sprite.Group(rock5)
        rock_group6 = pg.sprite.Group(rock6)
        rock_group7 = pg.sprite.Group(rock7)
        self.enemy_group_list = [enemy_group1,
                                 enemy_group2,
                                 enemy_group3,
                                 enemy_group4,
                                 enemy_group5,
                                 enemy_group6,
                                 enemy_group7,
                                 rock_group1,
                                 enemy_group8,
                                 rock_group2,
                                 rock_group3,
                                 rock_group4, rock_group5,
                                 enemy_group9, rock_group6,
                                 enemy_group10, rock_group7]

    def setup_billy(self):
        # Set Billy starting point
        self.billy = billy.Billy()
        self.billy.rect.x = self.viewport.x + 110
        self.billy.rect.bottom = c.ground_height

    def setup_checkpoints(self):
        # Creates invisible checkpoints that when collided will trigger
        # the creation of enemies from the self.enemy_group_list
        check1 = checkpoint.Checkpoint(2020, "1")
        check2 = checkpoint.Checkpoint(2760, '2')
        check3 = checkpoint.Checkpoint(4660, '3')
        check4 = checkpoint.Checkpoint(4700, '4')
        check5 = checkpoint.Checkpoint(4740, '5')
        check6 = checkpoint.Checkpoint(5886, '6')
        check7 = checkpoint.Checkpoint(7951, '7')
        check8 = checkpoint.Checkpoint(580, '8', 490, 100, 100)
        check9 = checkpoint.Checkpoint(1223, '9', c.ground_height-190, 100, 100)
        check10 = checkpoint.Checkpoint(1639, '10', 50, 150, 120)
        check11 = checkpoint.Checkpoint(3283, '11', 210, 150, 120)
        check12 = checkpoint.Checkpoint(10354, '12', c.ground_height-60, 10, 60)
        check13 = checkpoint.Checkpoint(4295, '13')
        check14 = checkpoint.Checkpoint(3583, '14', 210, 150, 120)
        check15 = checkpoint.Checkpoint(5286, '15')
        check16 = checkpoint.Checkpoint(6473, '16', 505)
        check17 = checkpoint.Checkpoint(9000, '17')

        self.check_point_group = pg.sprite.Group(check1, check2,
                                                 check3, check4,
                                                 check5, check6,
                                                 check7, check8,
                                                 check9, check10,
                                                 check11, check12,
                                                 check13, check14,
                                                 check15, check16,
                                                 check17)

    def setup_spritegroups(self):
        # Sprite group value
        self.enemy_group = pg.sprite.Group()

        self.ground_step_group = pg.sprite.Group(self.ground_group,
                                                 self.step_group)
        self.billy_and_enemy_group = pg.sprite.Group(self.billy,
                                                     self.enemy_group)

    def update(self, surface, keys, current_time):
        # update the whole level with states
        self.game_info[c.current_time] = self.current_time = current_time
        self.handle_states(keys)
        self.blit_everything(surface)
        # self.sound_manager.update(self.game_info, self.billy)

    def handle_states(self, keys):
        # If the level is in a FROZEN state, only mario will update
        if self.state == c.frozen:
            self.update_during_transition_state(keys)
        elif self.state == c.not_frozen:
            self.update_all_sprites(keys)

    def update_during_transition_state(self, keys):
        # Update Billy's transition state when dies
        self.billy.update(keys, self.game_info)
        self.check_for_billy_death()
        self.overhead_info_display.update(self.game_info, self.billy)

    def check_if_billy_in_transition_state(self):
        # The level FREEZE when Billy is in transition state
        if self.billy.in_transition_state:
            self.game_info[c.level_state] = self.state = c.frozen
        elif self.billy.in_transition_state == False:
            if self.state == c.frozen:
                self.game_info[c.level_state] = self.state = c.not_frozen

    def update_all_sprites(self, keys):
        # Updates the location of all sprites on the screen
        self.billy.update(keys, self.game_info)
        self.check_points_check()
        self.enemy_group.update(self.game_info)
        self.brick_group.update(self)
        # self.coin_group.update(self.game_info, self.viewport)
        self.adjust_sprite_positions()
        self.check_if_billy_in_transition_state()
        self.check_for_billy_death()
        self.update_viewport()
        self.overhead_info_display.update(self.game_info, self.billy)

    def check_points_check(self):
        # Detect if checkpoint collision occurs, delete checkpoint,
        # add enemies to self.enemy_group
        checkpoint = pg.sprite.spritecollideany(self.billy,
                                                self.check_point_group)
        if checkpoint:
            checkpoint.kill()

            for i in range(1, 20):
                if checkpoint.name == str(i):
                    for index, enemy in enumerate(self.enemy_group_list[i - 1]):
                        enemy.rect.x = self.viewport.right + (index * 60)
                        if self.enemy_group_list[0]:
                            enemy.rect.center = checkpoint.rect.center
                    self.enemy_group.add(self.enemy_group_list[i - 1])
                self.billy_and_enemy_group.add(self.enemy_group)

        if self.billy.rect.x > 10452:
            self.state = c.pass_level1
            self.billy.kill()
            self.billy.state == c.stand
            self.billy.pass_level1 = True
            self.next = c.main_menu





    def adjust_sprite_positions(self):
        # Adjusts sprites by their x and y velocities and collisions
        self.adjust_billy_position()
        self.adjust_enemy_position()

    def adjust_billy_position(self):
        # Adjusts billy's position based on his x, y velocities and
        # potential collisions
        self.last_x_position = self.billy.rect.right
        self.billy.rect.x += round(self.billy.x_vel)
        self.check_billy_x_collisions()

        if self.billy.in_transition_state == False:
            self.billy.rect.y += round(self.billy.y_vel)
            self.check_billy_y_collisions()

        if self.billy.rect.x < (self.viewport.x + 5):
            self.billy.rect.x = (self.viewport.x + 5)

    def check_billy_x_collisions(self):
        # Check for collisions after billy is moved on the x axis
        platform = pg.sprite.spritecollideany(self.billy, self.ground_step_group)
        brick = pg.sprite.spritecollideany(self.billy, self.brick_group)
        enemy = pg.sprite.spritecollideany(self.billy, self.enemy_group)

        if brick:
            self.adjust_billy_for_x_collisions(brick)

        elif platform:
            self.adjust_billy_for_x_collisions(platform)

        elif enemy:
            self.billy.start_death_jump(self.game_info)
            self.state = c.frozen

    def adjust_billy_for_x_collisions(self, platform):
        # Puts Billy flush next to the platform after moving on the x axis
        if self.billy.rect.x < platform.rect.x:
            self.billy.rect.right = platform.rect.left
        else:
            self.billy.rect.left = platform.rect.right

        self.billy.x_vel = 0

    def check_billy_y_collisions(self):
        # Check for collisions after billy is moved on the x axis
        platform = pg.sprite.spritecollideany(self.billy, self.ground_step_group)
        brick = pg.sprite.spritecollideany(self.billy, self.brick_group)
        enemy = pg.sprite.spritecollideany(self.billy, self.enemy_group)

        if brick:
            self.adjust_billy_for_y_brick_collisions(brick)

        elif platform:
            self.adjust_billy_for_y_platform_collisions(platform)

        elif enemy:
            self.billy.start_death_jump(self.game_info)
            self.state = c.frozen

        self.test_if_billy_is_falling()

    def adjust_billy_for_y_brick_collisions(self, brick):
        # Billy collisions with bricks on the y-axis
        if self.billy.rect.y > brick.rect.y:
            self.billy.y_vel = 0
            self.billy.state = c.fall
        elif brick.rect.bottom > self.billy.rect.bottom:
            self.billy.y_vel = 0
            self.billy.rect.bottom = brick.rect.top
            self.billy.state = c.walk
        elif self.billy.rect.right == brick.rect.left:
            self.billy.x_vel = 0
            self.billy.y_vel = 0
            self.billy.state = c.fall
        elif self.billy.rect.left == brick.rect.right:
            self.billy.x_vel = 0
            self.billy.y_vel = 0
            self.billy.state = c.fall

    def adjust_billy_for_y_platform_collisions(self, platform):
        # Billy collisions with platform on the y-axis
        if platform.rect.bottom > self.billy.rect.bottom:
            self.billy.y_vel = 0
            self.billy.rect.bottom = platform.rect.top
            self.billy.state = c.walk
        elif platform.rect.top < self.billy.rect.top:
            self.billy.y_vel = 7
            self.billy.rect.top = platform.rect.bottom
            self.billy.state = c.fall

    def test_if_billy_is_falling(self):
        # Changes Billy to a FALL state if more than a pixel above a step,
        # ground, step or box
        self.billy.rect.y += 1
        test_collide_group = pg.sprite.Group(self.ground_step_group,
                                             self.brick_group)
        if pg.sprite.spritecollideany(self.billy, test_collide_group) is None:
            if self.billy.state != c.jump \
                    and self.billy.state != c.death_jump:
                self.billy.state = c.fall

        self.billy.rect.y -= 1

    def adjust_enemy_position(self):
        # Moves all enemies along the x, y axes and check for collisions
        for enemy in self.enemy_group:
            enemy.rect.x += enemy.x_vel
            self.check_enemy_x_collisions(enemy)

            enemy.rect.y += enemy.y_vel
            self.check_enemy_y_collisions(enemy)
            self.delete_if_off_screen(enemy)

    def check_enemy_x_collisions(self, enemy):
        # Enemy collisions along the x axis.  Removes enemy from enemy group
        # in order to check against all other enemies then adds it back.
        enemy.kill()

        platform = pg.sprite.spritecollideany(enemy, self.ground_step_group)
        enemy_platform = pg.sprite.spritecollideany(enemy, self.enemy_group)

        if platform:
            if enemy.direction == c.right:
                enemy.rect.right = platform.rect.left
                enemy.direction = c.left
                enemy.x_vel = -2

            elif enemy.direction == c.left:
                enemy.rect.left = platform.rect.right
                enemy.direction = c.right
                enemy.x_vel = 2


        elif enemy_platform:
            if enemy.direction == c.right:
                enemy.rect.right = enemy_platform.rect.left
                enemy.direction = c.left
                enemy_platform.direction = c.right
                enemy.x_vel = -2
                enemy_platform.x_vel = 2
            elif enemy.direction == c.left:
                enemy.rect.left = enemy_platform.rect.right
                enemy.direction = c.right
                enemy_platform.direction = c.left
                enemy.x_vel = 2
                enemy_platform.x_vel = -2

        self.enemy_group.add(enemy)
        self.billy_and_enemy_group.add(self.enemy_group)

    def check_enemy_y_collisions(self, enemy):
        # Enemy collisions on the y axis
        platform = pg.sprite.spritecollideany(enemy, self.ground_step_group)
        brick = pg.sprite.spritecollideany(enemy, self.brick_group)

        if platform:
            if enemy.rect.bottom > platform.rect.bottom:
                enemy.y_vel = 7
                enemy.rect.top = platform.rect.bottom
                enemy.state = c.fall
            elif enemy.rect.bottom < platform.rect.bottom:

                enemy.y_vel = 0
                enemy.rect.bottom = platform.rect.top
                enemy.state = c.walk

        elif brick:
            if enemy.rect.x > brick.rect.x:
                enemy.y_vel = 7
                enemy.rect.top = brick.rect.bottom
                enemy.state = c.fall
            else:
                enemy.y_vel = 0
                enemy.rect.bottom = brick.rect.top
                enemy.state = c.walk

        else:
            enemy.rect.y += 1
            test_group = pg.sprite.Group(self.ground_step_group,
                                         self.brick_group)
            if pg.sprite.spritecollideany(enemy, test_group) is None:
                if enemy.state != c.jump:
                    enemy.state = c.fall

            enemy.rect.y -= 1

    def check_if_falling(self, sprite, sprite_group):
        # Checks if sprite should enter a falling state
        sprite.rect.y += 1

        if pg.sprite.spritecollideany(sprite, sprite_group) is None:
            if sprite.state != c.jump:
                sprite.state = c.fall

        sprite.rect.y -= 1

    def delete_if_off_screen(self, enemy):
        # Removes enemy from sprite groups if 500 pixels left off the screen,
        # underneath the bottom of the screen, or right of the screen if shell
        if enemy.rect.x < (self.viewport.x - 300):
            enemy.kill()

        elif enemy.rect.y > self.viewport.bottom:
            enemy.kill()

    def check_for_billy_death(self):
        # Restarts the level if billy is dead
        if self.billy.rect.y > c.screen_height and not self.billy.pass_level1:
            self.billy.dead = True
            self.billy.x_vel = 0
            self.state = c.frozen
            self.game_info[c.billy_dead] = True
        if self.billy.dead:
            if self.death_timer == 0:
                self.death_timer = self.current_time
            elif (self.current_time - self.death_timer) > 3000:
                self.set_game_info_values()
                self.done = True

    def set_game_info_values(self):
        # sets the new game values after a player's death
        if self.billy.dead:
            self.persist[c.lives] -= 1

        if self.billy.dead == False:
            self.next = c.main_menu
            self.game_info[c.camera_start_x] = 0
        else:
            self.game_info[c.camera_start_x] == 0
            self.next = c.load_screen

    def update_viewport(self):
        # Change the view of the camera
        third = self.viewport.x + self.viewport.w // 3
        billy_center = self.billy.rect.centerx
        billy_right = self.billy.rect.right

        if self.billy.x_vel > 0 and billy_center >= third:
            mult = 0.5 if billy_right < self.viewport.centerx else 1
            new = self.viewport.x + mult * self.billy.x_vel
            highest = self.level_rect.w - self.viewport.w
            self.viewport.x = min(highest, new)

    def end_game(self):
        # End the game
        self.set_game_info_values()
        self.next = c.game_over
        # self.sound_manager.stop_music()
        self.done = True

    def blit_everything(self, surface):
        # Blit all sprites to the main surface
        self.level.blit(self.background, self.viewport, self.viewport)
        self.ground_group.draw(self.level)
        # self.food_group.draw(self.level)
        self.brick_group.draw(self.level)
        self.step_group.draw(self.level)
        self.check_point_group.draw(self.level)
        self.billy_and_enemy_group.draw(self.level)

        surface.blit(self.level, (0, 0), self.viewport)
        self.overhead_info_display.draw(surface)

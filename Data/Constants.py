import os

# game settings
screen_width = 1200
screen_height = 800
screen_size = (screen_width, screen_height)
Title = "Lost Path"
FPS = 70

# color definition
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue_hat = (75, 83, 164)
brown_shoe = (139, 94, 60)
brown_shoe_layer = (196, 154, 108)
pink_dot = (226, 142, 188)
red_shirt = (205, 32, 39)
green = (0, 255, 0)
green_grass = (177, 190, 17)
sky_blue = (39, 145, 251)
skin = (239, 212, 189)

# game value
x = 120
y = 760
billy_width = 104
billy_height = 166

size_multiplier = 0.192
brick_size_multiplier = 2.69
background_multiplier = 0.858
ground_height = screen_height - 90

# Billy states
stand = 'standing'
walk = 'walk'
jump = 'jump'
fall = 'fall'
hit = 'hit'
check = 'checkpoint'
left = 'left'
right = 'right'
jumped_on = 'jumped on'
death_jump = 'death jump'

# Movement property
walk_accel = .15
run_accel = 20

gravity = 1.01
jump_gravity = .31
jump_vel = -15
fast_jump_vel = -17.5
max_y_vel = 11

max_run_speed = 800
max_walk_speed = 6

# Game info directory key
coin_total = 'coin total'
score = 'score'
top_score = 'top score'
lives = 'lives'
current_time = 'current time'
level_state = 'level state'
camera_start_x = 'camera start x'
billy_dead = 'billy dead'

# Level state
frozen = 'frozen'
not_frozen = 'not frozen'
pass_level1 = 'pass level 1'

# overhead info state
main_menu = 'main menu'
load_screen = 'loading screen'
level1 = 'level'
game_over = 'game over'
end_of_level = 'end of level'

# main menu cursor state
new_game = 'new game'
cont = 'continue'
helps = 'help'
quit_game = 'quit game'


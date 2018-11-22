import random
from pico2d import *
import main_state
import game_world
import game_framework

class Ball:
    image = None

    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y, self.fall_speed = random.randint(0, 1800-1), random.randint(0, 1000), 0
        self.font = load_font('ENCR10B.TTF', 16)

    def get_bb(self):
        return self.x - main_state.boy.x - 10 + 640, self.y - main_state.boy.y - 10 + 300, self.x - main_state.boy.x + 10 + 640, self.y  - main_state.boy.y + 10 + 300

    def draw(self):

        self.image.draw(self.x - main_state.boy.x + 640, self.y - main_state.boy.y + 300)
        self.font.draw(self.x - main_state.boy.x, self.y - main_state.boy.y, '(%5d, %5d)' % (self.x - main_state.boy.x + 640, self.y - main_state.boy.y + 300), (255, 255, 0))
        #draw_rectangle(*self.get_bb())

    def update(self):
        self.y -= self.fall_speed * game_framework.frame_time


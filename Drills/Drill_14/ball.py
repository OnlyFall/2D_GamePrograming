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
        self.x, self.y, self.fall_speed = random.randint(-1600, 3200-1), random.randint(-600, 1200), 0

    def get_bb(self):
        return self.x - main_state.boy.x - 10, self.y - main_state.boy.y - 10, self.x - main_state.boy.x + 10, self.y - main_state.boy.y + 10

    def set_background(self, boy):
        self.center_object = boy
        self.cx, self.cy = self.x, self.y
        if boy.x_velocity > 0:
            self.cx = self.x + boy.x
            #self.cy = self.y - boy.y_velocity * game_framework.frame_time
        else:
            self.cx = self.x - boy.x
            #self.cy = self.y - boy.y_velocity * game_framework.frame_time

        if boy.y_velocity > 0:
            self.cy = self.y + boy.y
        else:
            self.cy = self.y - boy.y

    def draw(self):

        self.image.draw(self.x - main_state.boy.x, self.y - main_state.boy.y)
        #draw_rectangle(*self.get_bb())

    def update(self):
        self.y -= self.fall_speed * game_framework.frame_time


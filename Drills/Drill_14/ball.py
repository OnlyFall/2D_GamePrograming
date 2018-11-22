import random
from pico2d import *
import game_world
import game_framework

class Ball:
    image = None

    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y, self.fall_speed = random.randint(0, 1600-1), random.randint(0, 600), 0
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def set_background(self, boy):
        self.center_object = boy
        self.cx, self.cy = 0, 0
        if boy.x_velocity > 0:
            self.cx = self.x - boy.x_velocity * game_framework.frame_time
            self.cy = self.y - boy.y_velocity * game_framework.frame_time
        else:
            self.cx = self.x - boy.x_velocity * game_framework.frame_time
            self.cy = self.y - boy.y_velocity * game_framework.frame_time

    def draw(self):

        self.image.draw(self.cx, self.cy)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.y -= self.fall_speed * game_framework.frame_time


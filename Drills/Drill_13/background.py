import random

from pico2d import *


class FixedBackground:

    def __init__(self):
        self.image = load_image('futsal_court.png')
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.w = self.image.w
        self.h = self.image.h

    def set_center_object(self, boy):
        self.center_object = boy

    def draw(self):
        self.image.clip_draw_to_origin(self.window_left, self.window_bottom, self.canvas_width, self.canvas_height, 0, 0)

    def update(self):
        self.window_left = clamp(0, int(self.center_object.x) - self.canvas_width // 2, self.w - self.canvas_width)
        self.window_bottom = clamp(0, int(self.center_object.y) - self.canvas_height // 2, self.h - self.canvas_height)

    def handle_event(self, event):
        pass


class InfiniteBackground:


    def __init__(self):
        self.image = load_image('futsal_court.png')
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.w = self.image.w
        self.h = self.image.h

    def set_center_object(self, boy):
        self.center_object = boy


    def draw(self):
        self.image.clip_draw_to_origin(self.q3l, self.q3b, self.q3w, self.q3h, 0, 0)
        self.image.clip_draw_to_origin(self.q2l, self.q2b, self.q2w, self.q2h, 0, self.q3h)
        self.image.clip_draw_to_origin(self.q4l, self.q4b, self.q4w, self.q4h, self.q3w, 0)
        self.image.clip_draw_to_origin(self.q1l, self.q1b, self.q1w, self.q1h, self.q3w, self.q3h)

    def update(self):
        self.q3l = (int(self.center_object.x) - self.canvas_width // 2) % self.w
        self.q3b = (int(self.center_object.y) - self.canvas_height // 2) % self.h
        self.q3w = clamp(0, self.w - self.q3l, self.w)
        self.q3h = clamp(0, self.h - self.q3b, self.h)

        # quadrant 2
        self.q2l = self.q3l
        self.q2b = 0
        self.q2w = self.q3w
        self.q2h = self.canvas_height - self.q3h

        # quadrand 4
        self.q4l = 0
        self.q4b = self.q3h
        self.q4w = self.canvas_width - self.q3w
        self.q4h = self.q3h

        # quadrand 1
        self.q1l = 0
        self.q1b = 0
        self.q1w = self.q4w
        self.q1h = self.q2h


    def handle_event(self, event):
        pass






import random
import json
import os

from pico2d import *

import game_framework
import title_state
import pause_state
import pause_state_second


name = "MainState"

boy = None
grass = None
font = None
banana = None

count = 0
frame = 0

class Banana:
    def __init__(self):
        self.image = load_image('character\\temp\\sprite.png')
        self.x = 800
        self.y = 90

    def update(self):
        global count, frame
        count = (count + 1) % 30
        if count == 0:
            frame = (frame + 1) % 4

    def draw(self):
        self.image.clip_draw(0, frame * 150, 150, 150, self.x, self.y)



class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)



class Boy:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.image = load_image('run_animation.png')
        self.dir = 1

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir
        if self.x >= 800:
            self.dir = -1
        elif self.x <= 0:
            self.dir = 1

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)


def enter():
    global boy, grass, banana
    boy = Boy()
    grass = Grass()
    banana = Banana()


def exit():
    global boy, grass, banana
    del(boy)
    del(grass)
    del(banana)


def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.push_state(pause_state_second)
           # game_framework.push_state(pause_state)


def update():
    boy.update()
    banana.update()


def draw():
    clear_canvas()
    grass.draw()
    banana.draw()
    update_canvas()






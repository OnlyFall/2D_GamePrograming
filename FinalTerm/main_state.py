import random
import json
import os

from pico2d import *
import game_framework
import game_world

from Banana import Banana
from background import Back

name = "MainState"

banana = None
Die = None

def enter():
    global banana
    global Die

    back = Back()
    banana = Banana()
    game_world.add_object(back, 0)
    game_world.add_object(banana, 1)


def exit():
    game_world.clear()

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
                game_framework.quit()
        else:
            banana.handle_event(event)


def update():
    for game_object in game_world.all_objects():
        game_object.update()


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()







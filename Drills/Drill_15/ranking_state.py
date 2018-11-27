import random
import json
import pickle
import os

from pico2d import *
import game_framework
import game_world
import world_build_state
import json

Rank = []
name = "RankingState"

def enter():
    global Rank
    with open('Rank.json', 'r') as f:
        temp = json.load(f)

        k = temp["Rank"]
        Rank = k

    Rank.sort(reverse=True)

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
            game_framework.change_state(world_build_state)


def update():
    pass


font = None
def draw():
    clear_canvas()
    global font, Rank

    if font == None:
        font = load_font('ENCR10B.TTF', 20)


    if(len(Rank) < 10):
        for i in range(len(Rank)):
            font.draw(100, 500 - 30 * (i + 2), str(i + 1) + '# ( Time:  %3.4f' % (Rank[i]) + ')', (0, 0, 0))

    else:
        for i in range(10):
            font.draw(100, 500 - 30 * (i + 2), str(i + 1) + '# ( Time:  %3.4f'  % (Rank[i]) + ')', (0, 0, 0))



    update_canvas()






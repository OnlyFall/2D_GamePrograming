import random
import json
import pickle
import os

from pico2d import *
import game_framework
import game_world
from collections import  OrderedDict

import ranking_state
import world_build_state
import pickle
name = "MainState"

ZombieData = None

def collide(a, b):
    # fill here
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True

boy = None
twice_zombie = None

def enter():
    # game world is prepared already in world_build_state
    global boy
    global twice_zombie
    boy = world_build_state.get_boy()
    twice_zombie = world_build_state.returnZombie
    pass

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
        elif event.type == SDL_KEYDOWN and event.key == SDLK_s:
            game_world.save()
        else:
            boy.handle_event(event)

loadRank = []
tmpRank = []

def update():
    global twice_zombie
    global loadRank
    global tmpRank
    for game_object in game_world.all_objects():
        game_object.update()


    #블로그에서 찾은 방법!
    file_data = OrderedDict()


    for zombie_count in twice_zombie:
        if collide(boy, zombie_count):
            #tmpRank.clear()
            with open('Rank.json', 'r', encoding="utf-8") as f:
                loadRank = json.load(f)
            k = loadRank["Rank"]
            tmpRank = k

            save_time = (get_time() - boy.start_time)
            tmpRank.append(save_time)
            file_data["Rank"] = tmpRank

            #loadRank.append(save_time)

            with open('Rank.json', 'w', encoding="utf-8") as f:
                json.dump(file_data, f, ensure_ascii=False, indent="\t")
            game_framework.change_state(ranking_state)
            break

def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()







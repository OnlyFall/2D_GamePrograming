import random
import json
import os
import PIL.Image
from pico2d import *

import game_framework
import title_state
import pause_state
import pause_state_second


name = "MainState"

BackGround = None
font = None
banana = None
step = None
heart = None

img = None

left = False
right = False
up = False
down = False

count = 0
frame = 0

#충돌체크 이미지 로드
check = None

#점프를 위한 공간
jumpCount = 0
boolJumpCount = False

class HEART:
    def __init__(self):
        self.image = load_image('UI\\HEART\\Heart.png')

    def draw(self):
        self.image.draw(self.x, self.y)

class BG:
    def __init__(self):
        self.image = load_image('BG\\stage.png')

    def draw(self):
        self.image.clip_draw(0, 0, 1600, 800, 800, 400)

class STEP:
    def __init__(self):
        self.image = load_image('STEP\\PT_0005.png')

    def draw(self):
        self.image.clip_draw(0, 0, 1600, 800, 800, 400)

class Banana:
    def __init__(self):
        self.image = load_image('character\\temp\\sprite.png')
        self.x = 800
        self.y = 90

    def update(self):
        global img
        global count, frame
        global left, right, up, down
        global jumpCount

        count = (count + 1) % 10
        if count == 0:
            frame = (frame + 1) % 4

        if left == True:
            self.x -= 5
        if right == True:
            self.x += 5

        if(up == True):
            if jumpCount < 45:
                self. y += 5
                jumpCount += 1

            elif jumpCount == 45:
                if self.y > 90:
                    r, g, b, a = img.getpixel((self.x, self.y))

                    if (r, g, b) == (78, 201, 17) or (r, g, b) == (67, 119, 108) or (r, g, b) == (45, 132, 114) or (r, g, b) == (106, 150, 194) or (r, g, b) == (70, 106, 144) or (r, g, b) == (46, 79, 114) or (r, g, b) == (78, 163, 146):
                        jumpCount = 0
                        up = False

                    self.y -= 5

                else:
                    up = False
                    jumpCount = 0

        elif up == False:
            pass



    def draw(self):
        self.image.clip_draw(0, frame * 150, 150, 150, self.x, self.y)



def enter():
    global step, BackGround, banana, heart, img
    BackGround = BG()
    banana = Banana()
    step = STEP()
    heart = [HEART() for heart in range(5)]
    img = PIL.Image.open("STEP\\PT_0005.png")

def exit():
    global BackGround, banana, step
    del(BackGround)
    del(step)
    del(banana)


def pause():
    pass


def resume():
    pass



def handle_events():
    global left, right, up, down
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.push_state(pause_state_second)
        elif event.type == SDL_KEYDOWN:
            if(event.key == SDLK_LEFT):
                left = True
            elif(event.key == SDLK_RIGHT):
                right = True
            elif(event.key == SDLK_UP):
                if up == False:
                    up = True
            elif(event.key == SDLK_DOWN):
                down = True
        elif event.type == SDL_KEYUP:
            if (event.key == SDLK_LEFT):
                left = False
            elif (event.key == SDLK_RIGHT):
                right = False
           # game_framework.push_state(pause_state)

bananaCount = 0

def update():
    global bananaCount
    bananaCount = (bananaCount + 1) % 3
    if bananaCount == 0:
        banana.update()


def draw():
    clear_canvas()
    BackGround.draw()
    step.draw()
    banana.draw()
    update_canvas()






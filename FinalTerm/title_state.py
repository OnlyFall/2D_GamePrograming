import game_framework
import main_state
from pico2d import *


name = "TitleState"
BG = None
START = None
END = None
startSelect = 0

def enter():
    global BG, START, END
    BG = load_image("UI\\startBG.png")
    START = load_image('UI\\start.png')

def exit():
    global BG, START, END
    del(BG)
    del(START)
    del(END)


def handle_events():
    global startSelect
    events = get_events()
    for event in events:
        if(event.type == SDL_MOUSEMOTION):
            mouseX = event.x
            mouseY = 800 - event.y - 1
            if mouseX > (1200 / 2) - (129 / 2) and  mouseX < (1200 / 2) + (129 / 2) and mouseY < 300 + (25 / 2) and mouseY > 300 - (25 / 2):
                startSelect = 1
            else:
                startSelect = 0
        elif(event.type == SDL_MOUSEBUTTONDOWN):
            game_framework.change_state(main_state)

        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(main_state)


def draw():
    global startSelect
    handle_events()
    clear_canvas()
    BG.draw(600, 400)
    START.clip_draw(startSelect * 129, 0, 129, 25, 600, 300)
    update_canvas()


def update():
    pass


def pause():
    pass


def resume():
    pass







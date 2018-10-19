import game_framework
import main_state
from pico2d import *


name = "TitleState"
image = None


def enter():
    global image
    image = load_image("BG\\stage.png")

def exit():
    global image
    del(image)


mouseX, mouseY = 0,0
def handle_events():
    global mouseX, mouseY

    events = get_events()
    for event in events:

        if event.type == SDL_QUIT:
            game_framework.quit()

        if(event.type == SDL_MOUSEMOTION):
            mouseX = event.x
            mouseY = event.y

        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(main_state)


def draw():
    clear_canvas()
    image.draw(400, 300)
    update_canvas()


def update():
    pass


def pause():
    pass


def resume():
    pass







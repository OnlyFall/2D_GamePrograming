import game_framework
import main_state
from pico2d import *


name = "TitleState"
image = None


def enter():
    global image
    image = load_image('pause.png')


def exit():
    global image
    del(image)


def handle_events():
    events = get_events()

    for event in events:

        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(main_state)
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_p):
                game_framework.pop_state()

frame = 0
def draw():
    global frame

    clear_canvas()

    main_state.draw()
    if frame == 0:
        image.draw(400, 300)

    update_canvas()







def update():
    global frame
    frame = (frame + 1) % 2
    delay(0.4)

def pause():
    pass


def resume():
    pass







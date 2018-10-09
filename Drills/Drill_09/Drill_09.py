from pico2d import *

# Game object class here

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image(400, 30)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

# initialization code

# game main loop code

# finalization code
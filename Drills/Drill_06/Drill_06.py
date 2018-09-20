from pico2d import *
KPU_WIDTH, KPU_HEIGHT = 1280, 1024

def handle_events():
    global moveCheck
    events = get_events()

    for event in events:
        if event.type == SDL_MOUSEBUTTONDOWN
            endX = event.x - 25
            endY = KPU_HEIGHT - 1 - event.y + 26
            moveCheck = False
            


def moveingCharacter():


open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
stop = load_image('character.png')
hand = load_image('hand_arrow.png')

running = True
x = 800 // 2
frame = 0
endX, endY = 0


while running:
    moveingCharacter()
    handle_events()

close_canvas()


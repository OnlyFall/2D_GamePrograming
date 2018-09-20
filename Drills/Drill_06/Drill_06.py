from pico2d import *
KPU_WIDTH, KPU_HEIGHT = 1280, 1024

def handle_events():
    global moveCheck
    global endX, endY
    events = get_events()

    for event in events:
        if event.type == SDL_MOUSEBUTTONDOWN:
            endX = event.x - 25
            endY = KPU_HEIGHT - 1 - event.y + 26
            moveCheck = True

        elif event.type == SDL_MOUSEMOTION:
            mouseX = event.x
            mouseY = event.y


def characterDraw():
    pass

def moveingCharacter():
    global ch_x, ch_y
    global endX, endY
    global moveCheck

    moveX = (endX - ch_x) / 100
    moveY = (endY - ch_y) / 100

    count = 0

    while count < 100:
        ch_x += moveX
        ch_y += moveY
        characterDraw()
        handle_events()
        if moveCheck == True:
            count = 0
            moveX = (endX - ch_x) / 100
            moveY = (endY - ch_y) / 100
        hand.draw(mouseX, mouseY)






open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
stop = load_image('character.png')
hand = load_image('hand_arrow.png')

running = True
mouseX, mouseY = KPU_WIDTH / 2, KPU_HEIGHT / 2
frame = 0
ch_x, ch_y = KPU_WIDTH / 2, KPU_HEIGHT / 2
endX, endY = 0, 0
moveCheck = False

while running:
    moveingCharacter()
    handle_events()

close_canvas()


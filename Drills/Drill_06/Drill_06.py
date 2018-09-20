from pico2d import *
KPU_WIDTH, KPU_HEIGHT = 1280, 1024

def handle_events():
    global moveCheck
    global endX, endY
    global mouseX, mouseY
    global running
    events = get_events()

    for event in events:
        if event.type == SDL_MOUSEBUTTONDOWN:
            endX = event.x - 25
            endY = KPU_HEIGHT - 1 - event.y + 26
            moveCheck = True
            running = True

        elif event.type == SDL_MOUSEMOTION:
            mouseX = event.x
            mouseY = KPU_HEIGHT - 1 - event.y


def characterDraw(moveX):
    global mouseX, mouseY
    global ch_x, ch_y
    global frame
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    frame = (frame + 1) % 8

    if moveX > 0:
        character.clip_draw(frame * 100, 100 * 1, 100, 100, ch_x, ch_y)
    elif moveX < 0:
        character.clip_draw(frame * 100, 0, 100, 100, ch_x, ch_y)
    handle_events()
    hand.draw(mouseX, mouseY)

    update_canvas()

def moveingCharacter():
    global ch_x, ch_y
    global endX, endY
    global moveCheck
    global running
    moveX = (endX - ch_x) / 100
    moveY = (endY - ch_y) / 100

    count = 0

    while count < 100:
        clear_canvas()
        ch_x += moveX
        ch_y += moveY
        count += 1
        characterDraw(moveX)
        handle_events()
        if moveCheck == True:
            count = 0
            moveX = (endX - ch_x) / 100
            moveY = (endY - ch_y) / 100
            moveCheck = False
        update_canvas()
        running = False

def stopCharacter():
    global ch_x, ch_y

    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    stop.draw(ch_x, ch_y)
    handle_events()
    hand.draw(mouseX, mouseY)

    update_canvas()






open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
stop = load_image('character.png')
hand = load_image('hand_arrow.png')

hide_cursor()
running = False
mouseX, mouseY = KPU_WIDTH / 2, KPU_HEIGHT / 2
frame = 0
ch_x, ch_y = KPU_WIDTH / 2, KPU_HEIGHT / 2
moveX, moveY = KPU_WIDTH / 2, KPU_HEIGHT / 2
endX, endY = KPU_WIDTH / 2, KPU_HEIGHT / 2
moveCheck = False

while True:

    if running == True:
        moveingCharacter()
    elif running == False:
        stopCharacter()


close_canvas()


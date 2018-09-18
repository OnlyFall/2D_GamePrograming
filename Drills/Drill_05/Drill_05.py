from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('animation_sheet.png')


def move_first_to_second():
    startX, startY = 203, 535
    endX , endY = 132, 243
    frame = 0
    moveRangeX = (endX - startX) / 10
    moveRangeY = (endY - startY) / 10

    while startX > endX:
        clear_canvas_now()
        frame = (frame + 1) % 8
        if moveRangeX > 0:
            character.clip_draw(frame * 100, 100, 100, 100, startX, startY)
        elif moveRangeX < 0:
            character.clip_draw(frame * 100, 0, 100, 100, startX, startY)
        update_canvas()
        startX += moveRangeX
        startY += moveRangeY
        delay(0.01)


def move_second_to_third():
    pass

def move_third_to_fourth():
    pass

def move_fourth_to_fifth():
    pass

def move_fifth_to_sixth():
    pass

def move_sixth_to_seventh():
    pass

def move_seventh_to_eighth():
    pass

def move_eighth_to_nine():
    pass

def move_nine_to_tenth():
    pass

def move_tenth_to_first():
    pass


while True:
    move_first_to_second()
    move_second_to_third()
    move_third_to_fourth()
    move_fourth_to_fifth()
    move_fifth_to_sixth()
    move_sixth_to_seventh()
    move_seventh_to_eighth()
    move_eighth_to_nine()
    move_nine_to_tenth()
    move_tenth_to_first()

close_canvas()

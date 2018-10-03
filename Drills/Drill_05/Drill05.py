from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('animation_sheet.png')


def move_point_to_point(startX, startY, endX, endY):

    frame = 0
    moveRangeX = (endX - startX) / 10
    moveRangeY = (endY - startY) / 10
    count = 0

    while count < 10:
        clear_canvas_now()
        frame = (frame + 1) % 8
        if moveRangeX > 0:
            character.clip_draw(frame * 100, 100, 100, 100, startX, startY)
        elif moveRangeX < 0:
            character.clip_draw(frame * 100, 0, 100, 100, startX, startY)
        update_canvas()
        startX += moveRangeX
        startY += moveRangeY
        count+=1
        delay(0.01)




while True:
    move_point_to_point(203, 535, 132, 243)
    move_point_to_point(132, 243, 535, 470)
    move_point_to_point(535, 470, 477, 203)
    move_point_to_point(477, 203, 715, 136)
    move_point_to_point(715, 136, 316, 225)
    move_point_to_point(316, 225, 510, 92)
    move_point_to_point(510, 92, 692, 518)
    move_point_to_point(692, 518, 682, 336)
    move_point_to_point(682, 336, 712, 349)
    move_point_to_point(712, 349, 203, 535)
    #
close_canvas()

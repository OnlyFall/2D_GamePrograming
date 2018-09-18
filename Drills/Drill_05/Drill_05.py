from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')


def move_from_center_to_right():
    x, y = 800 // 2, 90
    while x < 800 - 25:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y);
        x += 2


def move_up():
    x, y = 800 - 25, 50 + 40
    while y < 600 - 50:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y);
        y += 2

def move_left():
    x, y = 800 - 25, 600 - 50
    while x > 0 + 25:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y);
        x -= 2

def move_down():
    pass

def move_left_to_center():
    pass

def make_rectangle():
   # move_from_center_to_right()
  #  move_up()
    move_left()
    move_down()
    move_left_to_center()

def make_circle():
    pass

while True:
    make_rectangle()
    make_circle()



    
close_canvas()

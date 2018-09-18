from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')


def move_from_center_to_right():
    pass

def move_up():
    pass

def move_left():
    pass

def move_down():
    pass

def move_left_to_center():
    pass

def make_rectangle():
    move_from_center_to_right()
    move_up()
    move_left()
    move_down()
    move_left_to_center()

def make_circle():
    pass

while True:
    make_rectangle()
    make_circle()



    
close_canvas()

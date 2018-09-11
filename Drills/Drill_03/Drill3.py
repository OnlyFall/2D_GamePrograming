from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')
x = 400
y = 90
change = 0
dir = 0
radian = 0

import math

while(True):
    clear_canvas_now()
    character.draw_now(x,y)
    grass.draw_now(400,30)
    if change == 0:
        if dir == 0:
            x+=1
            if x == 750:
                dir = 1
            if x == 400:
                change = 1
            
        elif dir == 1:
            y+=1
            if y == 510:
                dir = 2

        elif dir == 2:
            x -= 1
            if x == 50:
                dir = 3

        elif dir == 3:
            y -= 1
            
            if y == 90:
                dir = 0

    elif change == 1:
        x = math.sin(radian / 80) * 200 + 400
        y = -math.cos(radian / 80) * 200 + 300
        
        radian = radian + 3
        if radian == 360:
            radian = 0
            x = 400
            y = 90
            dir = 0
            change = 0
        
    
close_canvas()

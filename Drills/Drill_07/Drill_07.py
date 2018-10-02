
import random
from pico2d import *

WIDTH, HEIGHT = 1280, 1024


frame = 0
open_canvas(WIDTH, HEIGHT)
character = load_image('animation_sheet.png')
tempX = 0

def characterDraw(x, y):
    global frame
    global tempX
    clear_canvas()
    frame = (frame + 1) % 8
    if(tempX < x):
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    elif(tempX > x):
        character.clip_draw(frame * 100, 0 * 1, 100, 100, x, y)
    update_canvas()
    delay(0.01)

    tempX = x


def draw_line(p1, p2):
    global tempX

    if tempX == 0:
        tempX = p1[0]

    for i in range(0, 100 + 1, 1):
        t = i / 100
        x = (1 - t) * p1[0] + t * p2[0]
        y = (1 - t) * p1[1] + t * p2[1]
        characterDraw(x, y)



size = 20
points = [(random.randint(0, 1200), random.randint(0, 1000)) for i in range(size)]
n = 1
while True:
    draw_line(points[n - 1], points[n])
    n = (n + 1) % 20



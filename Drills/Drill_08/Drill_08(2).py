from pico2d import *
import turtle
import random

def draw_curve_3_points(p1, p2, p3):


    for i in range(0, 100, 2):
        t = i / 100
        x = (2*t**2 -3*t + 1)*p1[0] + (-4*t**2 + 4*t)*p2[0] + (2*t**2 -t)*p3[0]
        y = (2*t**2 -3*t + 1)*p1[1] + (-4*t**2 + 4*t)*p2[1] + (2*t**2 - t)*p3[1]


def draw_curve_4_points(p1, p2, p3, p4):


    # draw p1-p2
    for i in range(0, 50, 2):
        t = i / 100
        x = (2*t**2-3*t+1)*p1[0]+(-4*t**2+4*t)*p2[0]+(2*t**2-t)*p3[0]
        y = (2*t**2-3*t+1)*p1[1]+(-4*t**2+4*t)*p2[1]+(2*t**2-t)*p3[1]
        characterDraw((x,y))

    # draw p2-p3
    for i in range(0, 100, 2):
        t = i / 100
        x = ((-t**3 + 2*t**2 - t)*p1[0] + (3*t**3 - 5*t**2 + 2)*p2[0] + (-3*t**3 + 4*t**2 + t)*p3[0] + (t**3 - t**2)*p4[0])/2
        y = ((-t**3 + 2*t**2 - t)*p1[1] + (3*t**3 - 5*t**2 + 2)*p2[1] + (-3*t**3 + 4*t**2 + t)*p3[1] + (t**3 - t**2)*p4[1])/2
        characterDraw((x, y))

    # draw p3-p4
    for i in range(50, 100, 2):
        t = i / 100
        x = (2*t**2-3*t+1)*p2[0]+(-4*t**2+4*t)*p3[0]+(2*t**2-t)*p4[0]
        y = (2*t**2-3*t+1)*p2[1]+(-4*t**2+4*t)*p3[1]+(2*t**2-t)*p4[1]
        characterDraw((x,y))

def characterDraw(p):
    global frame
    global tempX

    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2 , KPU_HEIGHT // 2)
    frame = (frame + 1) % 8
    if tempX <= p[0]:
        character.clip_draw(frame * 100, 100 * 1, 100, 100, p[0], p[1])
    elif tempX > p[0]:
        character.clip_draw(frame * 100, 0 * 1, 100, 100, p[0], p[1])
    tempX = p[0]
    update_canvas()
    delay(0.01)


def characterStamp():
    pass

tempX = 0
frame = 0
KPU_WIDTH, KPU_HEIGHT = 1280, 1024
open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')

open_canvas(KPU_WIDTH, KPU_HEIGHT)
points = [(-350, 200), (400, 350), (300, -300), (-200, -200)]
while True:
    draw_curve_4_points(points[0], points[1], points[2],points[3])




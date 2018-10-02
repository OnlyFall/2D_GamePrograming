import turtle
import random
from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024
def stop():
    turtle.bye()


def prepare_turtle_canvas():
    turtle.setup(1024, 768)
    turtle.bgcolor(0.2, 0.2, 0.2)
    turtle.penup()
    turtle.hideturtle()
    turtle.shape('arrow')
    turtle.shapesize(2)
    turtle.pensize(5)
    turtle.color(1, 0, 0)
    turtle.speed(100)
    turtle.goto(-500, 0)
    turtle.pendown()
    turtle.goto(480, 0)
    turtle.stamp()
    turtle.penup()
    turtle.goto(0, -360)
    turtle.pendown()
    turtle.goto(0, 360)
    turtle.setheading(90)
    turtle.stamp()
    turtle.penup()
    turtle.home()

    turtle.shape('circle')
    turtle.pensize(1)
    turtle.color(0, 0, 0)
    turtle.speed(50)

    turtle.onkey(stop, 'Escape')
    turtle.listen()


def draw_big_point(p):
    turtle.goto(p)
    turtle.color(0.8, 0.9, 0)
    turtle.dot(15)
    turtle.write('     '+str(p))


def draw_point(p):
    turtle.goto(p)
    turtle.dot(5, random.random(), random.random(), random.random())


def draw_line_basic(p1, p2):
    pass

frame = 0
open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
tempX = 0

def characterDraw(x, y):
    global frame
    clear_canvas()
    frame = (frame + 1) % 8
    if(tempX < x):
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    elif(tempX > x):
        character.clip_draw(frame * 100, 0 * 1, 100, 100, x, y)
    update_canvas()
    delay(0.01)


def draw_line(p1, p2):
    global tempX

    if tempX == 0:
        tempX = p1[0]

    for i in range(0, 100 + 1, 1):
        t = i / 100
        x = (1 - t) * p1[0] + t * p2[0]
        y = (1 - t) * p1[1] + t * p2[1]
        characterDraw(x, y)


#prepare_turtle_canvas()
size = 20
points = [(random.randint(0, 1200), random.randint(0, 1000)) for i in range(size)]
n = 1
while True:
    draw_line(points[n - 1], points[n])


turtle.done()
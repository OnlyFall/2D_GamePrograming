from pico2d import *
import random

# Game object class here

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0,7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100 ,100, self.x, self.y)

class Small:
    def __init__(self):
        self.moveY = random.randint(1, 10)
        self.x, self.y = random.randint(100, 700), 500
        self.image = load_image('ball21x21.png')

    def draw(self):
        self.image.draw(self.x, self.y)

    def moveBall(self):
        if self.y - 11 > 30:
            self.y = self.y - self.moveY
        else:
            self.y = 40

class Big:
    def __init__(self):
        self.moveY = random.randint(1, 10)
        self.x, self.y = random.randint(100, 700), 500
        self.image = load_image('ball41x41.png')

    def draw(self):
        self.image.draw(self.x, self.y)

    def moveBall(self):
        if self.y - 22 > 30:
            self.y = self.y - self.moveY
        else:
            self.y = 40




def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

# initialization code
open_canvas()

smallBall = Small()
bigBall = Big()
smallBallCount = random.randint(1, 20)

bBall = [Small() for i in range(smallBallCount)]
sBall = [Big() for i in range(20 - smallBallCount)]

boy = Boy()
team = [Boy() for i in range(11)]
grass = Grass()

running = True
# game main loop code
while running:
    handle_events()

    for boy in team:
        boy.update()

    for smallBall in sBall:
        smallBall.moveBall()

    for bigBall in bBall:
        bigBall.moveBall()

    clear_canvas()
    grass.draw()

    for smallBall in sBall:
        smallBall.draw()

    for bigBall in bBall:
        bigBall.draw()

    for boy in team:
        boy.draw()

    update_canvas()

    delay(0.05)

# finalization code
close_canvas()
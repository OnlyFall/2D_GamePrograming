import game_framework
from pico2d import *
import math
import random

import game_world

# Boy Run Speed
PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)


# Boy Action Speed
# fill expressions correctly
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 6



# Boy Event
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, SLEEP_TIMER, SPACE, DIE, DOWN, END = range(9)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE
}


# Boy States

class IdleState:

    @staticmethod
    def enter(banana, event):
        banana.timer = get_time() - 0.9
        if event == RIGHT_DOWN:
            banana.velocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            banana.velocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            banana.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            banana.velocity += RUN_SPEED_PPS


    @staticmethod
    def exit(banana, event):
        if event == SPACE:
            banana.jumpRange = 0

    @staticmethod
    def do(banana):
        banana.frame = (banana.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 6

    @staticmethod
    def draw(banana):
        if banana.dir == 1:
            banana.image.opacify(1)
            banana.image.clip_draw(int(banana.frame) * 150, 150, 150, 150, banana.x, banana.y)
        else:
            banana.image.opacify(1)
            banana.image.clip_draw(int(banana.frame) * 150, 0, 150, 150, banana.x, banana.y)


class RunState:

    @staticmethod
    def enter(banana, event):
        if event == RIGHT_DOWN:
            banana.velocity += RUN_SPEED_PPS

        elif event == LEFT_DOWN:
            banana.velocity -= RUN_SPEED_PPS

        elif event == RIGHT_UP:
            banana.velocity -= RUN_SPEED_PPS

        elif event == LEFT_UP:
            banana.velocity += RUN_SPEED_PPS

        banana.dir = clamp(-1, banana.velocity, 1)

    @staticmethod
    def exit(banana, event):
        if event == SPACE:
            banana.jumpRange = 0

    @staticmethod
    def do(banana):
        banana.frame = (banana.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 6
        banana.x += banana.velocity * game_framework.frame_time
        banana.x = clamp(25, banana.x, 1600 - 25)

    @staticmethod
    def draw(banana):
        if banana.dir == 1:
            banana.image.opacify(1)
            banana.image.clip_draw(int(banana.frame) * 150, 150, 150, 150, banana.x, banana.y)
        else:
            banana.image.opacify(1)
            banana.image.clip_draw(int(banana.frame) * 150, 0, 150, 150, banana.x, banana.y)


class JumpUpState:

    @staticmethod
    def enter(banana, event):
        if event == RIGHT_DOWN:
            banana.velocity += RUN_SPEED_PPS

        elif event == LEFT_DOWN:
            banana.velocity -= RUN_SPEED_PPS

        elif event == RIGHT_UP:
            banana.velocity -= RUN_SPEED_PPS

        elif event == LEFT_UP:
            banana.velocity += RUN_SPEED_PPS

        banana.dir = clamp(-1, banana.velocity, 1)

    @staticmethod
    def exit(banana, event):
        pass

    @staticmethod
    def do(banana):
        banana.frame = (banana.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 6
        banana.x += banana.velocity * game_framework.frame_time
        if banana.dir == 1:
            banana.jumpRange += 150 * game_framework.frame_time
            banana.y += 150 * game_framework.frame_time
        else:
            banana.jumpRange += 150 *game_framework.frame_time
            banana.y += 150 * game_framework.frame_time

        banana.x = clamp(25, banana.x, 1600 - 25)

        if banana.jumpRange >= 150:
            banana.add_event(DOWN)


    @staticmethod
    def draw(banana):
        if banana.dir == 1:
            banana.image.opacify(1)
            banana.image.clip_draw(int(banana.frame) * 150, 150, 150, 150, banana.x, banana.y)
        else:
            banana.image.opacify(1)
            banana.image.clip_draw(int(banana.frame) * 150, 0, 150, 150, banana.x, banana.y)


class JumpDownState:

    @staticmethod
    def enter(banana, event):
        if event == RIGHT_DOWN:
            banana.velocity += RUN_SPEED_PPS

        elif event == LEFT_DOWN:
            banana.velocity -= RUN_SPEED_PPS

        elif event == RIGHT_UP:
            banana.velocity -= RUN_SPEED_PPS

        elif event == LEFT_UP:
            banana.velocity += RUN_SPEED_PPS

        banana.dir = clamp(-1, banana.velocity, 1)

    @staticmethod
    def exit(banana, event):
        pass

    @staticmethod
    def do(banana):
        banana.frame = (banana.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 6
        banana.x += banana.velocity * game_framework.frame_time
        if banana.dir == 1:
            banana.y -= 150 * game_framework.frame_time
        else:
            banana.y -= 150 * game_framework.frame_time

        banana.x = clamp(25, banana.x, 1600 - 25)

        if banana.y <= 90:
            banana.add_event(END)


    @staticmethod
    def draw(banana):
        if banana.dir == 1:
            banana.image.opacify(1)
            banana.image.clip_draw(int(banana.frame) * 150, 150, 150, 150, banana.x, banana.y)
        else:
            banana.image.opacify(1)
            banana.image.clip_draw(int(banana.frame) * 150, 0, 150, 150, banana.x, banana.y)

next_state_table = {
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState, SPACE: JumpUpState},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState, SPACE: JumpUpState},
    JumpUpState:{RIGHT_DOWN: JumpUpState, LEFT_DOWN: JumpUpState, RIGHT_UP: JumpUpState, LEFT_UP: JumpUpState, SPACE: JumpUpState, DOWN:JumpDownState},
    JumpDownState: {END: RunState,RIGHT_DOWN: JumpDownState, LEFT_DOWN: JumpDownState, RIGHT_UP: JumpDownState, LEFT_UP: JumpDownState, SPACE: JumpDownState}
}

class Banana:

    def __init__(self):
        self.x, self.y = 1600 // 2, 90
        self.jumpRange = 0
        self.opacifyValue = 1
        self.GhostX, self.GhostY = 0, 0
        self.rad = 0
        self.standup = 0
        # Boy is only once created, so instance image loading is fine
        self.image = load_image('character\\Banana\\totalBanana.png')
        self.dir = 1
        self.velocity = 0
        self.frame = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)


    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

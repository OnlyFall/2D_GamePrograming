import game_framework
from pico2d import *
from ball import Ball

import game_world

import game_framework
from pico2d import *

import game_world

# Boy Run Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Boy Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8



# Boy Event
RIGHTKEY_DOWN, LEFTKEY_DOWN, UPKEY_DOWN, DOWNKEY_DOWN, RIGHTKEY_UP, LEFTKEY_UP, UPKEY_UP, DOWNKEY_UP, SPACE = range(9)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHTKEY_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFTKEY_DOWN,
    (SDL_KEYDOWN, SDLK_UP): UPKEY_DOWN,
    (SDL_KEYDOWN, SDLK_DOWN): DOWNKEY_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHTKEY_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFTKEY_UP,
    (SDL_KEYUP, SDLK_UP): UPKEY_UP,
    (SDL_KEYUP, SDLK_DOWN): DOWNKEY_UP,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE
}


# Boy States

class WalkingState:

    @staticmethod
    def enter(boy, event):
        if event == RIGHTKEY_DOWN:
            boy.x_velocity += RUN_SPEED_PPS
        elif event == RIGHTKEY_UP:
            boy.x_velocity -= RUN_SPEED_PPS
        if event == LEFTKEY_DOWN:
            boy.x_velocity -= RUN_SPEED_PPS
        elif event == LEFTKEY_UP:
            boy.x_velocity += RUN_SPEED_PPS

        if event == UPKEY_DOWN:
            boy.y_velocity += RUN_SPEED_PPS
        elif event == UPKEY_UP:
            boy.y_velocity -= RUN_SPEED_PPS
        if event == DOWNKEY_DOWN:
            boy.y_velocity -= RUN_SPEED_PPS
        elif event == DOWNKEY_UP:
            boy.y_velocity += RUN_SPEED_PPS



    @staticmethod
    def exit(boy, event):
        if event == SPACE:
            boy.fire_ball()

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION
        boy.x += boy.x_velocity * game_framework.frame_time
        boy.y += boy.y_velocity * game_framework.frame_time

        #왼쪽, 오른쪽 라인을 일차함수로 계산!
        boy.x = clamp(5 + (boy.y / boy.bg.h) * 190, boy.x, boy.bg.w - 5 - (boy.y / boy.bg.h) * 190)
        boy.y = clamp(40, boy.y, boy.bg.h - 40)

    @staticmethod
    def draw(boy):
        # fill here
        cx, cy = boy.canvas_width//2, boy.canvas_height//2

        if boy.x_velocity > 0:
            boy.image.clip_draw(int(boy.frame) * 100, 100, 100, 100, cx, cy)
            boy.dir = 1
        elif boy.x_velocity < 0:
            boy.image.clip_draw(int(boy.frame) * 100, 0, 100, 100, cx, cy)
            boy.dir = -1
        else:
            # if boy x_velocity == 0
            if boy.y_velocity > 0 or boy.y_velocity < 0:
                if boy.dir == 1:
                    boy.image.clip_draw(int(boy.frame) * 100, 100, 100, 100, cx, cy)
                else:
                    boy.image.clip_draw(int(boy.frame) * 100, 0, 100, 100, cx, cy)
            else:
                # boy is idle
                if boy.dir == 1:
                    boy.image.clip_draw(int(boy.frame) * 100, 300, 100, 100, cx, cy)
                else:
                    boy.image.clip_draw(int(boy.frame) * 100, 200, 100, 100, cx, cy)


next_state_table = {
    WalkingState: {RIGHTKEY_UP: WalkingState, LEFTKEY_UP: WalkingState, RIGHTKEY_DOWN: WalkingState, LEFTKEY_DOWN: WalkingState,
                UPKEY_UP: WalkingState, UPKEY_DOWN: WalkingState, DOWNKEY_UP: WalkingState, DOWNKEY_DOWN: WalkingState,
                SPACE: WalkingState}
}


class Boy:

    def __init__(self):
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        # Boy is only once created, so instance image loading is fine
        self.image = load_image('animation_sheet.png')
        self.font = load_font('ENCR10B.TTF', 16)
        self.dir = 1
        self.x_velocity, self.y_velocity = 0, 0
        self.frame = 0
        self.event_que = []
        self.cur_state = WalkingState
        self.cur_state.enter(self, None)
        self.eat_sound = load_wav('pickup.wav')
        self.eat_sound.set_volume(32)
        self.count = 0;
        # fill heree

    def eat(self, ball):
        self.eat_sound.play()
        self.count += 1


    def get_bb(self):
        return 400 - 50, 300 - 50, 400 + 50, 300 + 50


    def set_background(self, bg):
        self.bg = bg
        self.x = self.bg.w / 2
        self.y = self.bg.h / 2

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
        self.font.draw(self.canvas_width // 2 - 60, self.canvas_height // 2 + 50, '(%5d, %5d)' % (self.count), (255, 255, 0))

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

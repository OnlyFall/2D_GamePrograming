from pico2d import *

class Back:
    def __init__(self):
        self.image = load_image('BG\\Stage1Map1.bmp')
        self.step = load_image('STEP\\PT_0005.png')

    def update(self):
        pass

    def draw(self):
        self.image.clip_draw(0, 0, 1600, 800, 1600 // 2, 800 // 2)
        self.step.clip_draw(100, 0, 1600, 800, 1600 // 2, 800 // 2)
        #self.image.draw(1200, 30)

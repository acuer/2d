import random
import json
import os

from pico2d import *

import game_framework
import title_state



name = "MainState"

back = None
boy = None
font = None
city = None
running = None

class Back:
    def __init__(self):
        self.image = load_image('back.png')

    def draw(self):
        self.image.draw(400, 300)

class City:
    def __init__(self):
        self.image = load_image('newMap.png')

    def draw(self):
        self.image.draw(400, 689)

class Pause:
    def __init__(self):
        self.image = load_image('hold.png')

    def draw(self):
        self.image.draw(400,300)



class Boy:
    image = None
    LEFT_RUN, RIGHT_RUN, LEFT_STAND, RIGHT_STAND, JUMP_UP, JUMP_DOWN = 0, 1, 2, 3, 4, 5

    def __init__(self):
        self.x, self.y = 20, 60
        self.frame = 0
        self.run_frames = 0
        self.stand_frames = 0
        self.dir = 1
        self.state = self.RIGHT_STAND
        if Boy.image == None:
            Boy.image = load_image('r_run.png')

    def handle_event(self, event):
        if(event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
            if self.state in (self.RIGHT_STAND, self.LEFT_STAND):
                self.state = self.LEFT_RUN

        elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
            if self.state in (self.RIGHT_STAND, self.LEFT_STAND):
                self.state = self.RIGHT_RUN

        elif(event.type, event.key) == (SDL_KEYUP, SDLK_LEFT):
            if self.state in (self.LEFT_RUN, ):
                self.state = self.LEFT_STAND

        elif(event.type, event.key) == (SDL_KEYUP, SDLK_RIGHT):
            if self.state in (self.RIGHT_RUN, ):
                self.state = self.RIGHT_STAND


    def update(self):
        
        self.frameProcess()
       
        if self.state == self.RIGHT_RUN:
            self.x = min(800, self.x + 5)
        elif self.state == self.LEFT_RUN:
            self.x = max(0, self.x - 5)
            


        # clip_draw( left, bottom,  width, height, x,y )
        # left: draw될 texture의 x position
        # bottom: draw될 texture의 y position 
        # width: draw될 texture의 가로
        # height: draw될 texture의 세로 
        # x: player position X
        # y: player position Y
    def draw(self):
        if self.state == self.RIGHT_RUN:
            self.image = load_image('r_run.png')
            self.image.clip_draw(self.frame * 100, 0, 95, 95, self.x, self.y)
        
        elif self.state == self.LEFT_RUN:
            self.image = load_image('l_run.png')
            self.image.clip_draw(self.frame * 102, 0, 90, 95, self.x, self.y)

        elif self.state == self.LEFT_STAND:
            self.image = load_image('l_stand.png')
            self.image.clip_draw(self.frame * 67, 0, 67, 108, self.x, self.y)

        elif self.state == self.RIGHT_STAND:
            self.image = load_image('r_stand.png')
            self.image.clip_draw(self.frame * 67, 0, 67, 108, self.x, self.y)
            

    def frameProcess(self):
         

         if self.state == self.LEFT_RUN or self.state == self.RIGHT_RUN:
            self.frame = (self.frame + 1) % 8
         elif self.state == self.RIGHT_STAND or self.state == self.LEFT_STAND:
            self.frame = (self.frame + 1 ) % 7

            

def enter():
    global boy, city, back
    boy = Boy()
    city = City()
    back = Back()


def exit():
    global boy, city, back
    boy = Boy()
    city = City()
    back = Back()


def pause():
    pass


def resume():
    pass


def handle_events():
    global running
    global boy
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        else:
            boy.handle_event(event)


def update():
    boy.update()


def draw():
    clear_canvas()
    back.draw()
    city.draw()
    boy.draw()
    update_canvas()
    delay(0.04)






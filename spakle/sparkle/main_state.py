import random
import json
import os

from pico2d import *

import game_framework
import title_state

from Define import *


name = "MainState"

back = None
boy = None
font = None
city = None
running = None

class Back:
    def __init__(self):
        self.image = load_image('back.png')

    def draw(self,frame_time):
        self.image.draw(400, 300)

class City:
    def __init__(self):
        self.image = load_image('newMap.png')

    def draw(self,frame_time):
        self.image.draw(400, 689)

class Pause:
    def __init__(self):
        self.image = load_image('hold.png')

    def draw(self,frame_time):
        self.image.draw(400,300)



class Boy:
    image = None
   

    def __init__(self):
        self.x, self.y = 50, 70
        self.frame = 0
        self.run_frames = 0
        self.stand_frames = 0

        self.state = STATE_STAND
        self.RightImage = load_image('Iori_Orochi_Right.png')
        self.LeftImage = load_image('Iori_Orochi_Left.png')
        self.start = 0
        self.scene = 0
        self.cx = 60
        self.cy = 100
        self.frameTime = 0
        self.last = 0
        self.textureWidth = 4500
        self.textureHeight = 3500
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.x_offset = 0
        self.y_offset = 0
        self.dir = DIR_RIGHT
        self.time = SDL_GetTicks()

    def handle_event(self, event):
        if(event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
            self.dir = DIR_LEFT
        elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
            self.dir = DIR_RIGHT

        if(event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
            if self.state in (STATE_STAND, STATE_PUNCH,STATE_PUNCH2,STATE_PUNCH3):
                self.state = STATE_WALK

        elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
            if self.state in (STATE_STAND,STATE_PUNCH,STATE_PUNCH2,STATE_PUNCH3):
                self.state = STATE_WALK

        elif(event.type, event.key) == (SDL_KEYUP, SDLK_LEFT):
            if self.state in (STATE_WALK,):
                self.state = STATE_STAND

        elif(event.type, event.key) == (SDL_KEYUP, SDLK_RIGHT):
            if self.state in (STATE_WALK,):
                self.state = STATE_STAND

        elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_DOWN):
            if self.state in (STATE_STAND, STATE_WALK ):
                self.state = STATE_SIT

        elif(event.type, event.key) == (SDL_KEYUP, SDLK_DOWN):
            if self.state in (STATE_SIT, ):
                self.state = STATE_STAND
         
        elif( event.type,event.key ) == (SDL_KEYDOWN ,SDLK_a ):
            if self.state in( STATE_STAND , STATE_WALK ):
                self.state = STATE_PUNCH
            elif self.state in( STATE_STAND, STATE_WALK):
                self.state = STATE_PUNCH

        elif( event.type,event.key ) == (SDL_KEYDOWN ,SDLK_s ):
            if self.state in( STATE_STAND , STATE_WALK ):
                self.state = STATE_PUNCH2
            elif self.state in( STATE_STAND, STATE_WALK):
                self.state = STATE_PUNCH2
        
        elif( event.type,event.key ) == (SDL_KEYDOWN ,SDLK_d ):
            if self.state in( STATE_STAND , STATE_WALK ):
                self.state = STATE_PUNCH3
            elif self.state in( STATE_STAND, STATE_WALK):
                self.state = STATE_PUNCH3

    def update(self,frame_time):
        
        self.SetMotion()
        self.FrameMove(frame_time)
       
        if self.state == STATE_WALK and self.dir == DIR_RIGHT:
            self.x = min(750, self.x + 9)
        elif self.state == STATE_WALK and self.dir == DIR_LEFT:
            self.x = max(50, self.x - 9)
            

    def SetMotion(self):
        if (self.state == STATE_STAND):
            if self.scene != RES_STAND:
                self.start = 0
            
            self.cx = 150
            self.cy = 150
            self.scene = RES_STAND
            self.frameTime = 100
            self.last = 7

        if (self.state == STATE_WALK):
            if self.scene != RES_WALK:
                self.start = 0
            
      
            self.cx = 150
            self.last = 6
            self.scene = RES_WALK
            self.frameTime = 100
            
        if (self.state == STATE_PUNCH):
            if self.scene != RES_PUNCH:
                self.start = 0
            
            self.scene = RES_PUNCH
            self.frameTime = 100
            self.last = 4

        if (self.state == STATE_PUNCH2):
            if self.scene != 6:
                self.start = 0
            
            self.scene = 6
            self.frameTime = 100
            self.last = 6

        
        if (self.state == STATE_PUNCH3):
            if self.scene != 7:
                self.start = 0
            
            self.scene = 7
            self.frameTime = 100
            self.last = 6

    def FrameMove(self,frame_time):
    
        if self.frameTime + self.time < SDL_GetTicks():
            self.time = SDL_GetTicks()
            self.start += 1

        if self.start >= self.last:
            if self.state == STATE_PUNCH or self.state == STATE_PUNCH2 or self.state == STATE_PUNCH3:
                self.state == STATE_STAND
                self.start = 0
            else:
                self.start =0

        # clip_draw( left, bottom,  width, height, x,y )
        # left: draw될 texture의 x position
        # bottom: draw될 texture의 y position 
        # width: draw될 texture의 가로
        # height: draw될 texture의 세로 
        # x: player position X
        # y: player position Y
    def draw(self,frame_time):
        if self.dir == DIR_RIGHT:
          self.RightImage.clip_draw( self.start * self.cx, self.textureHeight - ( self.cy * self.scene), 
                                 self.cx, self.cy,self.x, self.y);
        elif self.dir == DIR_LEFT:
            self.LeftImage.clip_draw( self.start * self.cx, self.textureHeight - ( self.cy * self.scene), 
                                 self.cx, self.cy,self.x, self.y);
        #if self.state == self.RIGHT_RUN:
        #    self.image = load_image('r_run.png')
        #    self.image.clip_draw(self.frame * 100, 0, 95, 95, self.x, self.y - 10)
        
        #elif self.state == self.LEFT_RUN:
        #    self.image = load_image('l_run.png')
        #    self.image.clip_draw(self.frame * 102, 0, 90, 95, self.x, self.y - 10)

        #elif self.state == self.LEFT_STAND:
        #    self.image = load_image('l_stand.png')
        #    self.image.clip_draw(self.frame * 67, 0, 67, 108, self.x, self.y)

        #elif self.state == RIGHT_STAND:
        #    self.image = load_image('r_stand.png')
        #    self.image.clip_draw(self.frame * 67, 0, 67, 108, self.x, self.y)

        #elif self.state == self.LEFT_SIT:
        #    self.image = load_image('lsit.png')
        #    self.image.clip_draw(self.frame * 53, 0, 53, 73, self.x, self.y - 15)

        #elif self.state == self.RIGHT_SIT:
        #    self.image = load_image('rsit.png')
        #    self.image.clip_draw(self.frame * 53, 0, 53, 73, self.x, self.y - 15)

       

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


def update(frame_time):
    boy.update(frame_time)


def draw(frame_time):
    clear_canvas()
    back.draw(frame_time)
    city.draw(frame_time)
    boy.draw(frame_time)
    update_canvas()
    delay(0.05)






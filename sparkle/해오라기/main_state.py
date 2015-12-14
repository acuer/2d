import random
import json
import os
import game_framework
import title_state

from pico2d import *
from hero import *
from Define import *
from background import *


name = "MainState"

back = None
hero = None
font = None
city = None
running = None

class City:
    def __init__(self):
        self.image = load_image('newMap.png')
        self.bgm = load_music('muran.mp3')
        self.bgm.set_volume(32)
        self.bgm.repeat_play()
    def draw(self, frame_time):
        self.image.draw(400,300)


class Back:
    def __init__(self):
        self.image = load_image('back.png')

    def draw(self,frame_time):
        self.image.draw(400, 300)


class Pause:
    def __init__(self):
        self.image = load_image('hold.png')

    def draw(self,frame_time):
        self.image.draw(400,300)
       

def enter():
    global hero, city, back
    hero = Hero()
    city = City()
    back = Back()


def exit():
    global hero, city, back
    hero = Hero()
    city = City()
    back = Back()


def pause():
    pass


def resume():
    pass


def handle_events():
    global running
    global hero
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        else:
            hero.handle_event(event)


def update(frame_time):
    hero.update(frame_time)


def draw(frame_time):
    clear_canvas()
    back.draw(frame_time)
    city.draw(frame_time)
    hero.draw(frame_time)
    update_canvas()
    #delay(0.05)






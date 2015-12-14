﻿from pico2d import *
import sys
import math
import time
import random
import MainFrameWork


# Player State
STATE_STAND =	1
STATE_WALK =	2
STATE_JUMP =	3
STATE_AIR =		4

STATE_PUNCH =	5
STATE_KICK =	6
STATE_SIT =		1237
STATE_STAND_GUARD = 8
STATE_SKILL_ORUGEN  =	9
STATE_SKILL_RISINGTACKLE =	10
STATE_SKILL_POWERGEYSER = 11
STATE_ROLL_DODGE = 12
STATE_HIT = 13
STATE_DIE= 7
STATE_IORI_HIT = 23


# Player Resource State
# animation + 1 ( 1 start)
RES_STAND = 1
RES_WALK = 2
RES_JUMP = 3
RES_SIT = 4
RES_GUARD = 5
RES_PUNCH = 6
RES_KICK = 7
RES_HIT = 8
RES_DIE = 19
RES_ORUGEN = 14
RES_RISINGTACKLE = 12
RES_POWERGEYSER = 123
RES_POWERGEYSER_EFFECT = 15
RES_ROLL_DODGE = 16
RES_IORI_HIT = 17

# Blanka State
STATE_BLANKA_STAND = 1
STATE_BLANKA_WALK = 2
STATE_BLANKA_KICK = 3
STATE_BLANKA_HIT = 4
STATE_BLANKA_ROLL = 12
STATE_BLANKA_DIE = 6
STATE_BLANKA_BURN_HIT = 7
STATE_BLANKA_PUNCH = 8
STATE_BLANKA_DASH = 9


# Direction
DIR_RIGHT = 1
DIR_LEFT = -1
DIR_NONE = 0

# Field Collision Check
COLL_BOTTOM = 1
COLL_ONEFLOOR_LEFT = 2
COLL_ONEFLOOR_RIGHT = 3
COLL_TWOFLOOR_CENTER = 4
COLL_THREEFLOOR_LEFT = 5
COLL_THREEFLOOR_RIGHT = 6
COLL_FORTHLOOR_CENTER = 7
COLL_FIVEFLOOR_LEFT = 8
COLL_FIVEFLOOR_RIGHT = 9

# Hit Effect State 
STATE_HIT_EF_MON = 1
STATE_HIT_EF_PLAYER = 2
STATE_HIT_EF_BOSS = 3 


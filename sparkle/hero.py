from pico2d import *
from Define import *

class Hero:

    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    RUN_SPEED_KMPH = 20.0                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8

    image = None
   

    def __init__(self): 
        self.x, self.y = 50, 70
        self.frame = 0
        self.run_frames = 0
        self.stand_frames = 0
        self.life_time = 0.0
        self.total_frames = 0.0
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
       
        elif( event.type,event.key ) == (SDL_KEYDOWN ,SDLK_s ):
            if self.state in( STATE_STAND , STATE_WALK ):
                self.state = STATE_PUNCH2
        
        elif( event.type,event.key ) == (SDL_KEYDOWN ,SDLK_d ):
            if self.state in( STATE_STAND , STATE_WALK ):
                self.state = STATE_PUNCH3
      

    def update(self,frame_time):
        
        self.SetMotion()
        self.FrameMove(frame_time)
        self.life_time += frame_time
        self.total_frames += Hero.FRAMES_PER_ACTION * Hero.ACTION_PER_TIME * frame_time
        if self.state == STATE_WALK and self.dir == DIR_RIGHT:
            self.x = min(750, self.x + 1)
        elif self.state == STATE_WALK and self.dir == DIR_LEFT:
            self.x = max(50, self.x - 1)
            

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
                self.state = STATE_STAND
                self.start = 0
            else:
                self.start =0

        # clip_draw( left, bottom,  width, height, x,y )
        # left: draw�� texture�� x position
        # bottom: draw�� texture�� y position 
        # width: draw�� texture�� ����
        # height: draw�� texture�� ���� 
        # x: player position X
        # y: player position Y

    def draw(self,frame_time):
        if self.dir == DIR_RIGHT:
          self.RightImage.clip_draw( self.start * self.cx, self.textureHeight - ( self.cy * self.scene), 
                                 self.cx, self.cy,self.x, self.y);
        elif self.dir == DIR_LEFT:
            self.LeftImage.clip_draw( self.start * self.cx, self.textureHeight - ( self.cy * self.scene), 
                                 self.cx, self.cy,self.x, self.y);

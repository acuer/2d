from Import import *
import SoundMgr

class PowerGeyser:
    def __init__(self):
        self.iEffectX, self.iEffectY = 200, 200
        self.iEffectCX, self.iEffectCY = 150, 150
        self.dFrameTime = 0.0
        self.iState = STATE_SKILL_RISINGTACKLE
        self.iScene = RES_POWERGEYSER_EFFECT
        self.iStart = 0
        self.iLast = 0
        self.iFrame = 0
        self.x_offset = 0
        self.y_offset = 0
        self.iDirX = DIR_RIGHT
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.Load_Image()
        self.Sound = SoundMgr.SoundMgr()

    def Load_Image(self):
        self.dFrameTime = SDL_GetTicks()
        self.EffectImageRight = load_image('Player_Right.png')
        self.EffectImageLeft = load_image('Player_Left.png')

    def Progress(self, frame_time):
        self.SetMotion()
        self.FrameMove(frame_time)


    def Render(self, x_offset,y_offset, iDirX ):
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.iDirX = iDirX

        if self.iDirX == DIR_LEFT   :
            self.EffectImageLeft.clip_draw( self.iStart * self.iEffectCX, 3000 - ( self.iEffectCY * self.iScene ),  
                                           self.iEffectCX, self.iEffectCY * 3,  self.canvas_width//2 + self.x_offset - 80, 
                                           self.canvas_height//2 + self.y_offset - 10);
        
        elif self.iDirX == DIR_RIGHT:
            self.EffectImageRight.clip_draw( self.iStart * self.iEffectCX, 3000 - ( self.iEffectCY * self.iScene),  
                                            self.iEffectCX, self.iEffectCY * 3, self.canvas_width//2 + self.x_offset + 80, 
                                            self.canvas_height//2 + self.y_offset - 10);

    def SetMotion(self):
        if( self.iState == STATE_SKILL_RISINGTACKLE ):
            if self.iScene != RES_POWERGEYSER_EFFECT:
                self.iStart = 0
   
            self.iScene = RES_POWERGEYSER_EFFECT
            self.iLast = 16
            self.iFrame = 30
        

    def FrameMove(self,frame_time):
         if self.dFrameTime  +  self.iFrame < SDL_GetTicks():
             self.dFrameTime = SDL_GetTicks()
             self.iStart += 1

         if self.iStart >= self.iLast:
             self.iStart = 0
             self.iState = 0
            


                          

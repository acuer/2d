from Import import *

class MonsterHitEffect:
     def __init__(self):
       self.canvas_width = get_canvas_width()
       self.canvas_height = get_canvas_height()
       self.Load_Image()

       self.bRender = False
       self.iCX = 150
       self.iCY = 150
       self.iX = 0
       self.iY = 0
       self.iStart = 7
       self.iState = STATE_HIT_EF_PLAYER
       self.iLast = 0
       self.iFrame = 0
       self.dTime = SDL_GetTicks()
       self.Monster = None
       self.bMonsterCheck = False
       self.bEffectOff = False

     def Load_Image(self):
       self.imageLeft = load_image( 'Iori_Effect_Left.png')
       self.imageRight = load_image( 'Iori_Effect_Right.png')

     def Set_Center_Object(self, Monster):
       self.Monster = Monster
       self.bMonsterCheck = True

     def Progress(self, frame_time):
         if self.iState == STATE_HIT_EF_PLAYER:
            self.SetMotion()
            self.FrameMove()
        

     def Render(self,frame_time):
        if self.Monster.iDirX == DIR_LEFT and self.iState == STATE_HIT_EF_PLAYER:
             self.imageLeft.clip_draw( self.iStart * self.iCX, 0, self.iCX, self.iCY
                                      ,self.Monster.iX - self.Monster.bg.left - self.Monster.iHitEffectX, self.Monster.iY - self.Monster.bg.top + self.Monster.iHitEffectY )
        elif self.Monster.iDirX == DIR_RIGHT and self.iState == STATE_HIT_EF_PLAYER:
             self.imageRight.clip_draw( self.iStart * self.iCX, 0, self.iCX, self.iCY
                                       ,self.Monster.iX - self.Monster.bg.left + self.Monster.iHitEffectX, self.Monster.iY - self.Monster.bg.top + self.Monster.iHitEffectY)
    
     def SetMotion(self):
         if self.iState == STATE_HIT_EF_PLAYER:
            self.iLast = 12
            self.iFrame = 30

     def FrameMove(self):
         if self.dTime + self.iFrame < SDL_GetTicks():
             self.dTime = SDL_GetTicks()
             self.iStart += 1

         if self.iStart >= self.iLast:
             self.bEffectOff = True
             self.iStart = -1
             self.iState = 0

from Import import *

class PlayerEffect:
     def __init__(self):
       self.canvas_width = get_canvas_width()
       self.canvas_height = get_canvas_height()
       self.Load_Image()

       self.bRender = False
       self.iCX = 150
       self.iCY = 150
       self.iX = 0
       self.iY = 0
       self.iStart = 0
       self.iState = STATE_HIT_EF_MON
       self.iLast = 0
       self.iFrame = 0
       self.dTime = SDL_GetTicks()
       self.Player  = None
       self.bPlayer = False
       self.bEffectOff = False

     def Load_Image(self):
       self.imageLeft = load_image( 'Player_Effect_Left.png')
       self.imageRight = load_image( 'Player_Effect_Right.png')
       self.imageDefLeft = load_image( 'Effect_Left.png')
       self.imageDefRight = load_image('Effect_Right.png')

     def Set_Center_Object(self, player):
       self.Player = player
       self.bPlayer = True

     def Progress(self, frame_time):
         if self.iState == STATE_HIT_EF_MON:
            self.SetMotion()
            self.FrameMove()
        

     def Render(self,frame_time):
        if self.Player.iDirX == DIR_LEFT and self.iState == STATE_HIT_EF_MON and self.Player.iState != STATE_STAND_GUARD:
             self.imageLeft.clip_draw( self.iStart * self.iCX, 0, self.iCX, self.iCY
                                      , self.canvas_width//2 + self.Player.x_offset, self.canvas_width//2 + self.Player.y_offset - 120)

        elif self.Player.iDirX == DIR_RIGHT and self.iState == STATE_HIT_EF_MON and self.Player.iState != STATE_STAND_GUARD:
             self.imageRight.clip_draw( self.iStart * self.iCX, 0, self.iCX, self.iCY
                                       , self.canvas_width//2 + self.Player.x_offset, self.canvas_width//2 + self.Player.y_offset - 120)

        elif self.Player.iDirX == DIR_LEFT and self.iState == STATE_HIT_EF_MON and self.Player.iState == STATE_STAND_GUARD:
             self.imageDefLeft.clip_draw( self.iStart * self.iCX, 0, self.iCX, self.iCY
                                       , self.canvas_width//2 + self.Player.x_offset + 10, self.canvas_width//2 + self.Player.y_offset - 60)

        elif self.Player.iDirX == DIR_RIGHT and self.iState == STATE_HIT_EF_MON and self.Player.iState == STATE_STAND_GUARD:
             self.imageDefRight.clip_draw( self.iStart * self.iCX, 0, self.iCX, self.iCY
                                       , self.canvas_width//2 + self.Player.x_offset - 10 , self.canvas_width//2 + self.Player.y_offset - 60)

     def SetMotion(self):
         if self.iState == STATE_HIT_EF_MON:
         #   if self.Player.iState == STATE_STAND_GUARD:
            #self.iLast = 3
            #elif self.Player.iState != STATE_STAND_GUARD: 
            self.iLast = 8

            self.iFrame = 50

     def FrameMove(self):
         if self.dTime + self.iFrame < SDL_GetTicks():
             self.dTime = SDL_GetTicks()
             self.iStart += 1

         if self.iStart >= self.iLast:
             self.bEffectOff = True
             self.iStart = 0
             self.iState = 0

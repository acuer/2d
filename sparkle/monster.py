from pico2d import *
from Define import *

class Monster:


    PIXEL_PER_METER = (12.0 / 0.3)           # 10 pixel 30 cm
    RUN_SPEED_KMPH = 5.0                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
    
    JUMP = 500
    PUNCH_SPEED = 300
    KICK_SPEED = 300
    BURNKNUCKLE_NUCKBACK = 600
    RISINGTACKLE_NUCKBACK = 700
    SKILL_RISINGTACKLE_SPEED_X = 100
    SKILL_RISINGTACKLE_SPEED_Y = 400
    SKILL_POWERGEYSER_SPEED = 200
    ROLL_DODGE_SPEED = 200

    def __init__(self):
        self.iX, self.iY = random.randint( 100, 800), random.randint( 800, 1000 )
        self.iCX, self.iCY = 110 ,150
        self.iHpCX, self.iHpCY = 0, 10
        self.left = 0
        self.top = 0
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()        
        self.iState = STATE_STAND
        self.iScene = RES_STAND
        self.iStart = 1
        self.iLast = 0
        self.dFrameTime = 0.0
        self.fTime = 0.0
        self.x_offset = 0
        self.y_offset = 0
        self.iDirX = DIR_RIGHT
        self.fGravitTime = 0
        self.iRectX = 40
        self.iRectY = 40
        self.iDirY = 0
        self.bJump = False
        self.bDown = False
        self.bAir = True
        self.bJumpColl = False
        self.bJumpMove = False
        self.bDebugMode = False
        self.bHit = False
        self.bRisingHit = False
        self.bPowerHit = False
        self.bAirColl = False
        self.iHitState = 0
        self.iHitDirX = 0 
        self.bHpCheck = False
        self.Load_Image()
        self.Left_Obstacle = False
        self.Right_Obstacle = True
        self.iHitEffectX = 0
        self.iHitEffectY = 20

    def Load_Image(self):
        self.dTime = SDL_GetTicks()
        self.imageLeft = load_image("Blanka_Left.png")
        self.imageRight = load_image("Blanka_Right.png")
        self.imageHp = load_image("Mon_Hp.png")


    def Progress(self, frame_time ):
        if self.iState != STATE_BLANKA_DIE:
            self.MonAI()
        self.Jump(frame_time)
        self.SetMotion()
        self.FrameMove(frame_time)
        self.SkillMove(frame_time)
        if self.iState != STATE_BLANKA_DIE and self.bAir == False:
            self.HitMove(frame_time)
        self.DieCheck()

    def Render( self, fram_time ):
        x_left_offset = min(0, self.iX - self.canvas_width//2)
        x_right_offset = max(0, self.iX - self.bg.w + self.canvas_width//2)
        y_top_offset = min(0, self.iY - self.canvas_height//2)
        y_bottom_offset = max(0, self.iY - self.bg.h + self.canvas_height//2)
        self.x_offset = x_left_offset + x_right_offset
        self.y_offset = y_top_offset + y_bottom_offset

        if self.iDirX == DIR_LEFT:
            self.imageLeft.clip_draw( self.iStart * self.iCX, 1500 - ( self.iCY * self.iScene), self.iCX, self.iCY,  self.iX - self.bg.left, self.iY - self.bg.top );
        elif self.iDirX == DIR_RIGHT:
            self.imageRight.clip_draw( self.iStart * self.iCX, 1500 - ( self.iCY * self.iScene), self.iCX, self.iCY, self.iX - self.bg.left, self.iY - self.bg.top );

        if self.bDebugMode == True:
            self.RenderCollRect();    
        
        self.imageHp.clip_draw( 0, 0, 80 + self.iHpCX, self.iHpCY,  self.iX - self.bg.left + self.iHpCX / 2, self.iY - self.bg.top  + 50);

    def MonAI(self):
        iDistX = math.sqrt(( self.iX - self.Player.iX ) * ( self.iX - self.Player.iX ) )
        iDistY = math.sqrt(( self.iY - self.Player.iY ) * ( self.iY - self.Player.iY ) ) 
         
        if iDistY < 30 and self.iX > self.Player.iX:
            self.iDirX = DIR_LEFT
        elif self.iX < self.Player.iX:
            self.iDirX = DIR_RIGHT
         
        if( iDistX >= 35 and iDistX < 100 and iDistY < 30 ):
            if( self.Player.bDie == False and self.iState != STATE_BLANKA_ROLL and self.iState != STATE_BLANKA_BURN_HIT
               and self.iState != STATE_BLANKA_HIT and self.iState != STATE_BLANKA_DIE ):
                #self.iDirX = self.Player.iDirX 
                self.iState = STATE_BLANKA_KICK
        elif( iDistX >= 100 and iDistX < 110  and iDistY < 30):
            if (self.Player.bDie == False and self.iState != STATE_BLANKA_ROLL and self.iState != STATE_BLANKA_BURN_HIT 
               and self.iState != STATE_BLANKA_HIT  and self.iState != STATE_BLANKA_DIE ):
                 self.iState = STATE_BLANKA_PUNCH
        elif iDistX >= 110 and iDistX < 130 and iDistY < 30:
            if( self.iState != STATE_BLANKA_ROLL and self.iState != STATE_BLANKA_BURN_HIT 
            and self.iState != STATE_BLANKA_DIE and self.iState != STATE_BLANKA_HIT  ):
                self.iState = STATE_BLANKA_WALK
        elif iDistX >= 130 and iDistX < 230 and iDistY < 30:
            if( self.iState != STATE_BLANKA_ROLL and self.iState != STATE_BLANKA_BURN_HIT 
            and self.iState != STATE_BLANKA_DIE and self.iState != STATE_BLANKA_HIT  ):
                self.iState = STATE_BLANKA_DASH
        elif iDistX >= 230 and iDistX < 300 and iDistY < 30:
            if( self.iState != STATE_BLANKA_ROLL and self.iState != STATE_BLANKA_BURN_HIT 
            and self.iState != STATE_BLANKA_DIE and self.iState != STATE_BLANKA_HIT  ):     
                self.iState = STATE_BLANKA_ROLL
        else:
            if self.Right_Obstacle == True and self.iState != STATE_BLANKA_BURN_HIT and self.iState != STATE_BLANKA_HIT:
                self.iDirX = DIR_LEFT
                self.iState = STATE_BLANKA_WALK
            elif self.Left_Obstacle == True and self.iState != STATE_BLANKA_BURN_HIT and self.iState != STATE_BLANKA_HIT:
                self.iDirX = DIR_RIGHT
                self.iState = STATE_BLANKA_WALK

        #elif iDistX < 80 and iDistY > 60 and iDistY < 90:
        #    self.iState = STATE_BLANKA_WALK
        #    self.bDown = True
        #    self.bAir = True

        


    def SetMotion(self):
        if (self.iState == STATE_BLANKA_STAND):
            if self.iScene != STATE_BLANKA_STAND:
                self.iStart = 0
            
            self.iCX = 150
            self.iScene = STATE_BLANKA_STAND
            self.dFrameTime = 100
            self.iLast = 12
        
        if (self.iState == STATE_BLANKA_WALK):
            if self.iScene != STATE_BLANKA_WALK:
                self.iStart = 0
            
            self.iCX = 150
            self.iScene = STATE_BLANKA_WALK
            if self.bDown == True: 
                self.dFrameTime = 20
            elif self.bDown == False:
                self.dFrameTime = 100
            self.iLast = 8
        
        if (self.iState == STATE_BLANKA_PUNCH):
             if self.iScene != STATE_BLANKA_PUNCH:
                self.iStart = 0

             self.iCX = 250
             self.iScene = STATE_BLANKA_PUNCH
             self.dFrameTime = 150
             self.iLast = 4

        if (self.iState == STATE_BLANKA_KICK):
             if self.iScene != STATE_BLANKA_KICK:
                self.iStart = 0

             self.iCX = 150
             self.iScene = STATE_BLANKA_KICK
             self.dFrameTime = 150
             self.iLast = 3

        if (self.iState == STATE_BLANKA_HIT):
             if self.iScene != STATE_BLANKA_HIT:
                self.iStart = 0

             self.iCX = 150
             self.iScene = STATE_BLANKA_HIT
             self.dFrameTime = 150
             self.iLast = 3

        if (self.iState == STATE_BLANKA_DASH):
             if self.iScene != STATE_BLANKA_DASH:
                self.iStart = 0

             self.iCX = 250
             self.iScene = STATE_BLANKA_DASH
             self.dFrameTime = 100
             self.iLast = 6        

        if (self.iState == STATE_BLANKA_BURN_HIT):
             if self.iScene != STATE_BLANKA_BURN_HIT:
                self.iStart = 0

             self.iCX = 200
             self.iScene = STATE_BLANKA_BURN_HIT
             self.dFrameTime = 200
             self.iLast = 12

        if (self.iState == STATE_BLANKA_DIE):
             if self.iScene != STATE_BLANKA_DIE:
                self.iStart = 0

             self.iCX = 200
             self.iScene = STATE_BLANKA_DIE
             self.dFrameTime = 100
             self.iLast = 18
        

        if ( self.iState == STATE_BLANKA_ROLL ):
            if self.iScene != STATE_BLANKA_ROLL:
                self.iStart = 0
            
            self.iCX = 150
            self.iScene = 5
            self.dFrameTime = 100
            self.iLast = 8
        
    def FrameMove(self, frame_time):

        if self.dFrameTime + self.dTime < SDL_GetTicks():
            self.dTime = SDL_GetTicks()
            self.iStart += 1
        
        distance = self.RUN_SPEED_PPS * frame_time

        if self.iState == STATE_WALK:
           self.iX += self.iDirX *  distance

        if self.iState == STATE_BLANKA_DASH:
            self.iX += self.iDirX * distance * 2
 
        if self.iState == STATE_BLANKA_ROLL:
            self.iX += self.iDirX * distance * 8

        self.iX = clamp( 80, self.iX, self.bg.w - 80 )
        self.iY = clamp( 0, self.iY, self.bg.h)

        if self.iX <= 80:
            self.Left_Obstacle = True
            self.Right_Obstacle = False
        elif self.iX >= self.bg.w - 80:
            self.Left_Obstacle = False
            self.Right_Obstacle = True

        if self.iStart >= self.iLast:
            if( (self.iState == STATE_BLANKA_KICK ) | (self.iState == STATE_BLANKA_HIT) | ( self.iState == STATE_BLANKA_PUNCH)
               | (self.iState == STATE_BLANKA_ROLL ) | (self.iState == STATE_BLANKA_DASH ) | ( self.iState == STATE_BLANKA_BURN_HIT)
               | ( self.iState == STATE_JUMP)):

                self.iStart = 0
                self.bDown = False
                self.iState = STATE_BLANKA_STAND
               
            else:
                self.iStart = 0;

    def Set_Background(self, bg ):
        self.bg = bg

        

    def Jump(self,frame_time):
         if self.bJump == True:
             self.fGravitTime += ( 3 * frame_time)
             self.iY += math.sin( 90.0 * 3.141592 / 180.0) * self.JUMP * frame_time - ( (0.98 * self.fGravitTime * self.fGravitTime) / 2.0)
             self.bAir = True
             if(  math.sin( 90.0 * 3.141592 / 180.0) * self.JUMP * frame_time <  ( (0.98 * self.fGravitTime * self.fGravitTime) / 2.0) ):
                 self.bJumpColl = True
         
         if self.bAir == True:
            if self.bJump == False:
              self.fGravitTime += ( 5 * frame_time)
              self.iY -= ( ( 0.98 * self.fGravitTime * self.fGravitTime ) / 2.0 )
         elif self.bAir == False:
              self.bJump = False
              self.bJumpColl = False
              self.fGravitTime = 0.0

    def SkillMove(self,frame_time):
        if( ( self.iState == STATE_SKILL_BURNKNUCKLE ) & (self.iStart > 6) ):
           if self.iDirX == DIR_RIGHT:
               self.iX += self.SKILL_BURNKNUCKLE_SPEED * frame_time
           elif self.iDirX == DIR_LEFT:
               self.iX -= self.SKILL_BURNKNUCKLE_SPEED * frame_time
        
        elif( (self.iState == STATE_SKILL_RISINGTACKLE) & (self.iStart > 2) ):
            if self.iDirX == DIR_RIGHT:
                self.iX += self.SKILL_RISINGTACKLE_SPEED_X * frame_time 
                self.iY += self.SKILL_RISINGTACKLE_SPEED_Y * frame_time
            elif self.iDirX == DIR_LEFT:
                self.iX -= self.SKILL_RISINGTACKLE_SPEED_X * frame_time
                self.iY += self.SKILL_RISINGTACKLE_SPEED_Y * frame_time        

    def RenderCollRect(self):
        draw_rectangle( *self.GetCollBodyRect() )

        if( (self.iState == STATE_BLANKA_PUNCH) and ( self.iStart >= 3) and (self.iDirX == DIR_LEFT ) ):
            draw_rectangle( *self.GetPunchLeft() )
        if( (self.iState == STATE_BLANKA_PUNCH) and ( self.iStart >= 3) and (self.iDirX == DIR_RIGHT ) ):
            draw_rectangle( *self.GetPunchRight() )
        if( (self.iState == STATE_BLANKA_KICK) & ( self.iStart >= 2) and (self.iDirX == DIR_LEFT) ):    
            draw_rectangle( *self.GetKickLeft() )
        if( (self.iState == STATE_BLANKA_KICK ) & ( self.iStart >= 2) and (self.iDirX == DIR_RIGHT) ):    
            draw_rectangle( *self.GetKickRight() )
                
    def HitMove(self, frame_time):
        if ( (self.bHit == True ) & (self.iHitDirX == DIR_LEFT) & ( self.iHitState == STATE_PUNCH ) ):
            self.iState = STATE_BLANKA_HIT
            self.iX -= 0.5
            if self.bHpCheck == False:
                self.iHpCX -= 10
                self.bHpCheck = True

        elif ( (self.bHit == True ) & (self.iHitDirX == DIR_RIGHT)  & ( self.iHitState == STATE_PUNCH )):
            self.iState = STATE_BLANKA_HIT
            self.iX += 0.5
            if self.bHpCheck == False:
                self.iHpCX -= 10
                self.bHpCheck = True

        elif ( (self.bHit == True ) & (self.iHitDirX == DIR_LEFT)  & ( self.iHitState == STATE_KICK )):
            self.iState = STATE_BLANKA_HIT
            self.iX -= 0.5
            if self.bHpCheck == False:
                self.iHpCX -= 20
                self.bHpCheck = True

        elif ( (self.bHit == True ) & (self.iHitDirX == DIR_RIGHT)  & ( self.iHitState == STATE_KICK )):
            self.iState = STATE_BLANKA_HIT
            self.iX += 0.5
            if self.bHpCheck == False:
                self.iHpCX -= 20
                self.bHpCheck = True

        elif( (self.bHit == True ) & ( self.iHitDirX == DIR_LEFT ) & ( self.iHitState == STATE_SKILL_BURNKNUCKLE ) ):
            self.iState = STATE_BLANKA_BURN_HIT
            if self.bHpCheck == False:
                self.iHpCX -= 10
                self.bHpCheck = True
            self.iX -= self.BURNKNUCKLE_NUCKBACK * frame_time

        elif( (self.bHit == True ) & ( self.iHitDirX == DIR_RIGHT ) & ( self.iHitState == STATE_SKILL_BURNKNUCKLE ) ):
            self.iState = STATE_BLANKA_BURN_HIT
            if self.bHpCheck == False:
                self.iHpCX -= 10
                self.bHpCheck = True
            self.iX += self.BURNKNUCKLE_NUCKBACK * frame_time

        elif( (self.bRisingHit == True ) and ( self.iHitState == STATE_SKILL_RISINGTACKLE ) and ( self.bAir == False ) ):
            self.iState = STATE_BLANKA_BURN_HIT
            self.iY += 7
            if self.bHpCheck == False:
                self.iHpCX -= 30
                self.bHpCheck = True

        elif( (self.bPowerHit == True ) and ( self.iHitState == STATE_SKILL_POWERGEYSER ) ):
            self.iState = STATE_BLANKA_BURN_HIT
            self.iY += 50
            if self.bHpCheck == False:
                self.iHpCX -= 20
                self.bHpCheck = True

        else:
            self.bHpCheck = False
    
    def DieCheck(self ):
        if self.iHpCX <= -80:
           self.iState = STATE_BLANKA_DIE
             
    def SetDebugMode( self, bDebug ):
         self.bDebugMode = bDebug

    def SetAir( self, bAirCheck ):
        self.bAir = bAirCheck
 
    def Set_Player(self, player):
        self.Player = player       
 
    def SetHit(self, bHit ):
        self.bHit = bHit 

    def SetHitDir(self, iDir ):
        self.iHitDirX = iDir
                  
    def SetPosY( self, iY ):
        self.iY = iY
    
    def SetPowerHit(self, bHit ):
        self.bPowerHit = bHit
 
    def GetPowerHit(self):
        return self.bPowerHit 

    def GetAirColl(self ):
        return self.bAirColl
     
    def SetRisingHit(self, iHit ):
         self.bRisingHit = iHit

    def SetHitState(self, iHitState ):
        self.iHitState = iHitState

    def GetPosY(self):
        return self.iY

    def SetJump( self, bJump):
        self.bJump = bJump
    
    def GetHit(self):
        return self.bHit
        
    def GetJump(self ):
        return self.bJump

    def GetJumpColl(self):
        return self.bJumpColl

    def GetRisingHit(self):
        return self.bRisingHit

    def GetAir(self):
        return self.bAir

    def GetDown(self):
        return self.bDown

    def GetDebugMode(self):
        return self.bDebugMode

    def GetMotionState(self):
        return self.iState

    def GetFrame(self):
        return self.iStart

    def GetScrollX(self):
        return self.x_offset

    def GetDirX(self):
        return self.iDirX

    def GetScrollY(self):
        return self.y_offset 
                            
    def GetCollBodyRect(self):
        return(  ( self.iX - ( self.iCX / 2 ) - self.bg.left  + self.iRectX ) , 
                   ( self.iY - ( self.iCY / 2 ) - self.bg.top + self.iRectY - 40 ) ,
                   ( self.iX + ( self.iCX / 2 ) - self.bg.left - self.iRectX  ),
                   ( self.iY + ( self.iCY / 2 ) - self.bg.top - self.iRectY    ) )
    
    def GetPunchLeft(self):
        return(  ( self.iX - ( self.iCX / 2 ) - self.bg.left  + self.iRectX - 20 ) , 
                   ( self.iY - ( self.iCY / 2 ) - self.bg.top + self.iRectY  ) ,
                   ( self.iX + ( self.iCX / 2 ) - self.bg.left - self.iRectX - 80 ),
                   ( self.iY + ( self.iCY / 2 ) - self.bg.top - self.iRectY  - 20  ) )

    def GetPunchRight(self):
        return(  ( self.iX - ( self.iCX / 2 ) - self.bg.left  + self.iRectX + 100 ) , 
                   ( self.iY - ( self.iCY / 2 ) - self.bg.top + self.iRectY - 10 ) ,
                   ( self.iX + ( self.iCX / 2 ) - self.bg.left - self.iRectX + 20 ),
                   ( self.iY + ( self.iCY / 2 ) - self.bg.top - self.iRectY  -20  ) )

    def GetKickRight(self):
        return(  ( self.iX - ( self.iCX / 2 ) - self.bg.left  + self.iRectX + 60 ) , 
                   ( self.iY - ( self.iCY / 2 ) - self.bg.top + self.iRectY - 10 ) ,
                   ( self.iX + ( self.iCX / 2 ) - self.bg.left - self.iRectX + 20 ),
                   ( self.iY + ( self.iCY / 2 ) - self.bg.top - self.iRectY  -40  ) )

    def GetKickLeft(self):
        return(  ( self.iX - ( self.iCX / 2 ) - self.bg.left  + self.iRectX - 40 ) , 
                   ( self.iY - ( self.iCY / 2 ) - self.bg.top + self.iRectY  ) ,
                   ( self.iX + ( self.iCX / 2 ) - self.bg.left - self.iRectX - 80 ),
                   ( self.iY + ( self.iCY / 2 ) - self.bg.top - self.iRectY  - 40  ) )

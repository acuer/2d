from Import import *
import SoundMgr

class Player:

    PIXEL_PER_METER = (12.0 / 0.3)           # 10 pixel 30 cm
    RUN_SPEED_KMPH = 20.0                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
    
    PUNCH_SPEED = 300
    KICK_SPEED = 300
    SKILL_ORUGEN_SPEED  = 400
    SKILL_RISINGTACKLE_SPEED_X = 300
    SKILL_RISINGTACKLE_SPEED_Y = 450
    SKILL_POWERGEYSER_SPEED = 200
    ROLL_DODGE_SPEED = 200


    def __init__(self):
        self.Load_Image()
        self.iX, self.iY = 300, 120
        self.iCX, self.iCY = 60, 150
        self.RectSizeX, self.RectSizeY = 30, 70
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
        self.Sound = SoundMgr.SoundMgr()
        self.iDirX = DIR_RIGHT
        self.fGravitTime = 0
        self.iDirY = 0
        self.bJump = False
        self.bDown = False
        self.bAir = False
        self.bJumpColl = False
        self.bRising = False
        self.bJumpMove = False
        self.bDebugMode = False
        self.bMon1Create = False
        self.bHit = False
        self.iHitDirX = 0
        self.iHitState = 0
        self.iHp = 0
        self.iSp = 0
        self.bHpCheck = False
        self.bSpCheck = False
        self.bDie = False
        self.bSoundCheck = False
        self.bSkill1Hit =False
        self.textureWidth = 4500
        self.textureHeight = 3500    
        self.range = 50
            
    def Load_Image(self):
        self.dTime = SDL_GetTicks()
        self.imageLeft = load_image('Iori_Orochi_Left.png')
        self.imageRight = load_image('Iori_Orochi_Right.png')


    def Set_Background(self, bg ):
        self.bg = bg

    def Progress(self, frame_time):
        if self.iState != STATE_STAND_GUARD and self.iState != STATE_ROLL_DODGE:
            self.HitCheck(frame_time)
        elif self.iState == STATE_STAND_GUARD:
            if self.iDirX == DIR_LEFT and self.bHit == True:
                self.iX += 0.5
                self.Sound.Guard.play()
                if self.iSp <= 0:
                    self.iSp += 2
            elif self.iDirX == DIR_RIGHT and self.bHit == True:
                self.iX -= 0.5
                self.Sound.Guard.play()
                if self.iSp <= 0:
                    self.iSp += 2


        
        self.Jump(frame_time)
        self.SetMotion()
        self.FrameMove(frame_time)
        self.SkillMove(frame_time)
        self.SoundFrame()
        
        
    def Render(self, frame_time ):
        x_left_offset = min(0, self.iX - self.canvas_width//2)
        x_right_offset = max(0, self.iX - self.bg.w + self.canvas_width//2)
        y_top_offset = min(0, self.iY - self.canvas_height//2)
        y_bottom_offset = max(0, self.iY - self.bg.h + self.canvas_height//2)
        self.x_offset = x_left_offset + x_right_offset
        self.y_offset = y_top_offset + y_bottom_offset

        if self.iDirX == DIR_LEFT:
            self.imageLeft.clip_draw( self.iStart * self.iCX, self.textureHeight - ( self.iCY * self.iScene),
                                     self.iCX, self.iCY, self.canvas_width//2 + self.x_offset, self.canvas_height//2 + self.y_offset );
        elif self.iDirX == DIR_RIGHT:
            self.imageRight.clip_draw( self.iStart * self.iCX, self.textureHeight - ( self.iCY * self.iScene),
                                      self.iCX, self.iCY, self.canvas_width//2 + self.x_offset, self.canvas_height//2 + self.y_offset );

        if self.bDebugMode == True:
            self.RenderCollRect();    

    def SoundFrame(self):
        if self.iState == STATE_PUNCH and self.bSoundCheck == False:
            self.bSoundCheck = True
            self.Sound.PlayerPunch.play()
        elif self.iState == STATE_KICK and self.bSoundCheck == False:
            self.bSoundCheck = True
            self.Sound.PlayerKick.play() 
        elif self.iState == STATE_SKILL_ORUGEN and self.bSoundCheck == False:
            self.bSoundCheck = True
            self.Sound.Charge.play()
        elif self.iState == STATE_STAND:
            self.bSoundCheck = False
        
            

    def Input(self, event,frame_time):
         if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                MainFrameWork.quit()
        
         if self.bDie == False:
             if(event.type, event.key ) == (SDL_KEYDOWN, SDLK_LEFT ):
                 if( (self.iState != STATE_SIT) & (self.iState != STATE_STAND_GUARD) & (self.iState != STATE_SKILL_POWERGEYSER) &
                      (self.iState != STATE_SKILL_ORUGEN) & (self.iState != STATE_SKILL_RISINGTACKLE) ):
                        self.iDirX = DIR_LEFT

             if(event.type, event.key ) == (SDL_KEYDOWN, SDLK_RIGHT ):
                 if( (self.iState != STATE_SIT) & (self.iState != STATE_STAND_GUARD) & (self.iState != STATE_SKILL_POWERGEYSER) &
                      (self.iState != STATE_SKILL_ORUGEN) & (self.iState != STATE_SKILL_RISINGTACKLE) ):
                        self.iDirX = DIR_RIGHT
        
             if self.bJump == True:
                 if(event.type, event.key ) == (SDL_KEYDOWN, SDLK_RIGHT ):
                    self.bJumpMove = True
                 elif(event.type, event.key ) == (SDL_KEYDOWN, SDLK_LEFT ):
                    self.bJumpMove = True
             else:
                 self.bJumpMove = False
            

             if(event.type, event.key ) == ( SDL_KEYDOWN, SDLK_LEFT ):
                 if( (self.iState != STATE_SIT) & (self.iState != STATE_JUMP) & (self.iState != STATE_STAND_GUARD) & (self.iState != STATE_SKILL_POWERGEYSER) &
                      (self.iState != STATE_SKILL_ORUGEN) & (self.iState != STATE_SKILL_RISINGTACKLE) ):
                        self.iState = STATE_WALK
                      

             if(event.type, event.key ) == (SDL_KEYUP, SDLK_LEFT ):
                 if( (self.iState != STATE_SIT) & (self.iState != STATE_STAND_GUARD) & (self.iState != STATE_SKILL_POWERGEYSER) &
                      (self.iState != STATE_SKILL_ORUGEN) & (self.iState != STATE_SKILL_RISINGTACKLE) ):
                        self.iState = STATE_STAND

             if(event.type, event.key ) == ( SDL_KEYDOWN, SDLK_RIGHT ):
                 if( (self.iState != STATE_SIT) & (self.iState != STATE_JUMP) & (self.iState != STATE_STAND_GUARD) & (self.iState != STATE_SKILL_POWERGEYSER) &
                      (self.iState != STATE_SKILL_ORUGEN) & (self.iState != STATE_SKILL_RISINGTACKLE) ):
                        self.iState = STATE_WALK
              
             if(event.type, event.key ) == (SDL_KEYUP, SDLK_RIGHT ):
                 if( (self.iState != STATE_SIT) & (self.iState != STATE_STAND_GUARD) & (self.iState != STATE_SKILL_POWERGEYSER) &
                      (self.iState != STATE_SKILL_ORUGEN) & (self.iState != STATE_SKILL_RISINGTACKLE) ):
                        self.iState = STATE_STAND
        
             if(event.type, event.key ) == (SDL_KEYDOWN,SDLK_F1 ):
                 if self.bDebugMode == True:
                     self.bDebugMode = False
                     print( " DebugMode OFF " )
                 elif self.bDebugMode == False:
                     self.bDebugMode = True
                     print( " DebugMode ON " )
          
             if( event.type ,event.key ) == (SDL_KEYDOWN, SDLK_F2 ):
                 if self.bMon1Create == False:
                     self.bMon1Create = True

             elif(event.type, event.key ) == (SDL_KEYDOWN, SDLK_DOWN ): 
                 if self.bJump == False: 
                    self.iState = STATE_SIT
               
             elif(event.type, event.key) == (SDL_KEYUP, SDLK_DOWN ):
                 if self.bJump == False:
                     self.iState = STATE_STAND
        
             elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_d ):
                 if self.bJump == False:
                     self.iState = STATE_STAND_GUARD
            
             elif(event.type, event.key) == (SDL_KEYUP, SDLK_d ):
                  if self.bJump == False:
                      self.iState = STATE_STAND
                                     
             elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_c):
                 if( (self.bJump == False) & (self.iState != STATE_SIT) & (self.iState != STATE_STAND_GUARD) 
                    & (self.iState != STATE_SKILL_POWERGEYSER) & (self.iState != STATE_SKILL_ORUGEN) 
                    & (self.iState != STATE_SKILL_RISINGTACKLE) ):
                     self.iState = STATE_JUMP
                     self.bJump = True


             elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_v):
                 if( (self.bJump == False) & (self.iState != STATE_SIT) & (self.iState != STATE_STAND_GUARD) 
                    & (self.iState != STATE_SKILL_POWERGEYSER) & (self.iState != STATE_SKILL_ORUGEN) 
                    & (self.iState != STATE_SKILL_RISINGTACKLE) & ( self.iY > 222 )):
                     self.iState = STATE_JUMP
                     self.bDown = True 
                     self.bAir = True

             elif(event.type, event.key ) == (SDL_KEYDOWN, SDLK_a):
                if( (self.iState != STATE_SIT) & (self.iState != STATE_STAND_GUARD) & (self.iState != STATE_SKILL_POWERGEYSER) &
                    (self.iState != STATE_SKILL_ORUGEN) & (self.iState != STATE_SKILL_RISINGTACKLE) ):
                    if self.bJump == False:
                        self.iState = STATE_PUNCH
                    if self.iDirX == DIR_LEFT:
                        self.iX -= self.PUNCH_SPEED * frame_time;
                    elif self.iDirX == DIR_RIGHT:
                        self.iX += self.PUNCH_SPEED * frame_time;


             elif(event.type, event.key ) == (SDL_KEYDOWN, SDLK_s):
               if( (self.iState != STATE_SIT) & (self.iState != STATE_STAND_GUARD) & (self.iState != STATE_SKILL_POWERGEYSER) &
                    (self.iState != STATE_SKILL_ORUGEN) & (self.iState != STATE_SKILL_RISINGTACKLE) ):
                    if self.bJump == False:
                        self.iState = STATE_KICK
                    if self.iDirX == DIR_LEFT:
                        self.iX -= self.KICK_SPEED * frame_time;
                    elif self.iDirX == DIR_RIGHT:
                        self.iX += self.KICK_SPEED * frame_time;
                

             elif(event.type, event.key ) == (SDL_KEYDOWN, SDLK_q ):
                 if( (self.iState != STATE_SIT) and (self.iState != STATE_STAND_GUARD) and self.iState != STATE_SKILL_RISINGTACKLE 
                    and self.iState != STATE_SKILL_POWERGEYSER ):
                     
                     if self.bJump == False:
                         if self.iSp <= -200:
                            self.iSp -= 0
                         else:
                            self.iSp -= 10   
                            self.iState = STATE_SKILL_ORUGEN
                                          
             elif(event.type, event.key ) == (SDL_KEYDOWN, SDLK_w ):
                 if( (self.iState != STATE_SIT) & (self.iState != STATE_STAND_GUARD) 
                 & ( self.iState != STATE_JUMP)  and self.iState != STATE_SKILL_ORUGEN):

                     if self.bAir == False:
                         if self.iSp <= -200:
                            self.iSp -= 0
                         else:
                            self.iSp -= 10 
                            self.iState = STATE_SKILL_RISINGTACKLE
                            self.iEffect_State = STATE_SKILL_POWERGEYSER 
                    

    def SetMotion(self):
        if (self.iState == STATE_STAND):
            if self.iScene != RES_STAND:
                self.iStart = 0
            
            self.iCX = 150
            self.iScene = RES_STAND
            self.dFrameTime = 100
            self.iLast = 7
        
        if (self.iState == STATE_WALK):
            if self.iScene != RES_WALK:
                self.iStart = 0
            
            self.iCX = 150
            self.iScene = RES_WALK
            self.dFrameTime = 100
            self.iLast = 6

        if (self.iState == STATE_JUMP):
            if self.iScene != RES_JUMP:
                self.iStart = 0
            
            if self.bDown == True:
                 self.dFrameTime = 50
            elif self.bDown == False:
                self.dFrameTime = 60

            self.iCX = 150
            self.iScene = RES_JUMP
         
            self.iLast = 12

        if (self.iState == STATE_SIT):
            if self.iScene != RES_SIT:
                self.iStart = 1

            self.iCX = 150
            self.iScene = RES_SIT
            self.dFrameTime = 100
            self.iLast = 1 
        
        if (self.iState == STATE_PUNCH):
             if self.iScene != RES_PUNCH:
                self.iStart = 0

             self.iCX = 150
             self.iScene = RES_PUNCH
             self.dFrameTime = 130
             self.iLast = 3

        if (self.iState == STATE_KICK):
             if self.iScene != RES_KICK:
                self.iStart = 0

             self.iCX = 150
             self.iScene = RES_KICK
             self.dFrameTime = 130
             self.iLast = 4

        if ( self.iState == STATE_STAND_GUARD ):
            if self.iScene != RES_GUARD:
                self.iStart = 0
            
            self.iCX = 150
            self.iScene = RES_GUARD
            self.dFrameTime = 100
            self.iLast = 1

        if ( self.iState == STATE_ROLL_DODGE ):
            if self.iScene != RES_ROLL_DODGE:
                self.iStart = 0
            
            self.iCX = 150
            self.iScene = RES_ROLL_DODGE
            self.dFrameTime = 80
            self.iLast = 7
        
        # Skill Burn Nuckle
        if( self.iState == STATE_SKILL_ORUGEN ):
            if self.iScene != RES_ORUGEN:
                self.iStart = 0
            
            self.iCX = 150
            self.iCY = 150
            self.iScene = RES_ORUGEN
            self.dFrameTime = 80
            self.iLast = 13
    
        # Skill Rising Tackle
        if( self.iState == STATE_SKILL_RISINGTACKLE ):
            if self.iScene != RES_RISINGTACKLE:
                self.iStart = 0
            
            self.iCX = 150
            self.range = 80
            self.iScene = RES_RISINGTACKLE
            self.dFrameTime = 70
            self.iLast = 23

        if( self.iState == STATE_HIT ):
            if self.iScene != RES_HIT:
                self.iStart = 0
            
            self.iCX = 150
            self.iScene = RES_HIT
            self.dFrameTime = 80
            self.iLast = 4

        if( self.iState == STATE_DIE ):
            if self.iScene != RES_DIE:
                self.iStart = 0
            
            self.iCX = 250
            self.iScene = RES_DIE
            self.dFrameTime = 200
            self.iLast = 19

        if self.iState == STATE_IORI_HIT:
            if self.iScene != RES_IORI_HIT:
                self.iStart = 0

            self.iCX = 150
            self.iCY = 150
            self.iScene = RES_IORI_HIT
            self.dFrameTime = 250
            self.iLast = 10
        
    def FrameMove(self,frame_time):
    
        if self.dFrameTime + self.dTime < SDL_GetTicks():
            self.dTime = SDL_GetTicks()
            self.iStart += 1
       
        if self.iState == STATE_SKILL_RISINGTACKLE:
            if self.iStart == 7:
                self.Sound.PowerGHit1.play()
            if self.iStart == 17:
                self.Sound.PowerGHit2.play()
            if self.iStart == 27:
                self.Sound.PowerGHit3.play()
        
        distance = self.RUN_SPEED_PPS * frame_time

        if self.iState == STATE_WALK:
           self.iX += self.iDirX *  distance
        elif ( self.iState == STATE_JUMP) & ( self.bJumpMove == True ):
            self.iX += self.iDirX *  distance    

        self.iX = clamp( 80, self.iX, self.bg.w - 80 )
        self.iY = clamp( 0, self.iY, self.bg.h)
             
        if self.iStart >= self.iLast:
            if( (self.iState == STATE_PUNCH ) |  (self.iState == STATE_KICK) | (self.iState == STATE_SKILL_ORUGEN) 
               | (self.iState == STATE_SKILL_RISINGTACKLE ) | (self.iState == STATE_SKILL_POWERGEYSER )
               | ( self.iState == STATE_JUMP) | ( self.bDown == True ) | (self.iState == STATE_HIT) 
               | (self.iState == STATE_DIE ) | (self.iState == STATE_ROLL_DODGE ) | (self.iState == STATE_IORI_HIT)):

                self.bDown = False
                self.bRising = False
                self.iStart = 0
                self.range = 50
                if self.bDie == True:
                    self.iX = 500
                    self.iY = 400 
                    self.iHp = 0
                    self.iSp = 0
                    self.bAir = True
                    self.bDie = False
                    self.range = 50

                self.iState = STATE_STAND
               
            else:


                self.iStart = 0;
                

    def Jump(self,frame_time):
         if self.bJump == True:
             self.fGravitTime += ( 3 * frame_time)
             self.iY += math.sin( 90.0 * 3.141592 / 180.0) * 400 * frame_time - ( (0.98 * self.fGravitTime * self.fGravitTime) / 2.0)
             self.bAir = True
             if(  math.sin( 90.0 * 3.141592 / 180.0) * 400 * frame_time <  ( (0.98 * self.fGravitTime * self.fGravitTime) / 2.0) ):
                 self.bJumpColl = True
         

         if self.bAir == True:
            if self.bJump == False:
              self.fGravitTime += ( 5 * frame_time)
              self.iY -= ( ( 0.98 * self.fGravitTime * self.fGravitTime ) / 2.0 )
         elif self.bAir == False:
              self.bJump = False
              self.bJumpColl = False
              self.fGravitTime = 0.0

    def SetAir( self, bAirCheck ):
        self.bAir = bAirCheck
            
    def SetPosY( self, iY ):
        self.iY = iY

    def GetPosY(self):
        return self.iY

    def SetJump( self, bJump):
        self.bJump = bJump
    
    def GetJump(self ):
        return self.bJump

    def GetJumpColl(self):
        return self.bJumpColl

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
    
    def GetRising(self):
        return self.bRising

    def GetScrollX(self):
        return self.x_offset

    def GetDirX(self):
        return self.iDirX

    def GetScrollY(self):
        return self.y_offset

    def SkillMove(self,frame_time):
        if( ( self.iState == STATE_SKILL_ORUGEN ) & (self.iStart > 5) & (self.iStart <= 8) ):
           if self.iDirX == DIR_RIGHT:
               self.iX += self.SKILL_ORUGEN_SPEED  * frame_time
           elif self.iDirX == DIR_LEFT:
               self.iX -= self.SKILL_ORUGEN_SPEED  * frame_time
        
        if( (self.iState == STATE_SKILL_RISINGTACKLE) & (self.iStart > 14)  & (self.iStart <=18)):
            if self.iDirX == DIR_RIGHT:
                self.iX += self.SKILL_RISINGTACKLE_SPEED_X * frame_time 
                self.iY += self.SKILL_RISINGTACKLE_SPEED_Y * frame_time
            elif self.iDirX == DIR_LEFT:
                self.iX -= self.SKILL_RISINGTACKLE_SPEED_X * frame_time
                self.iY += self.SKILL_RISINGTACKLE_SPEED_Y * frame_time
        elif( ( self.iState == STATE_ROLL_DODGE ) ):
                self.iX += 2 * self.iDirX 
                          
    
    def RenderCollRect(self):
        draw_rectangle( *self.GetCollBodyRect() )

        if( (self.iState == STATE_PUNCH) & ( self.iStart == 2) & (self.iDirX  == DIR_RIGHT )):
            draw_rectangle( *self.GetPunchRightRect() )

        if( (self.iState == STATE_PUNCH) & ( self.iStart == 2) & (self.iDirX  == DIR_LEFT )):
            draw_rectangle( *self.GetPunchLeftRect() )

        if( (self.iState == STATE_KICK) & ( self.iStart == 2) & (self.iDirX  == DIR_LEFT ) ):    
            draw_rectangle( *self.GetKickLeftRect() )

        if( (self.iState == STATE_KICK) & ( self.iStart == 2) & (self.iDirX  == DIR_RIGHT ) ):    
            draw_rectangle( *self.GetKickRightRect() )

        if( (self.iState == STATE_SKILL_ORUGEN) & ( self.iStart >= 8) & (self.iStart < 10) 
           & (self.iDirX  == DIR_LEFT ) ):    
            draw_rectangle( *self.GetBurnLeftRect() ) 

        if( (self.iState == STATE_SKILL_ORUGEN) and ( self.iStart >= 8) and (self.iStart < 10) 
           and (self.iDirX  == DIR_RIGHT ) ):    
            draw_rectangle( *self.GetBurnRightRect() )

        if( (self.iState == STATE_SKILL_RISINGTACKLE) ):
            if( (self.iDirX  == DIR_RIGHT )  ):
              if( ( self.iStart == 7) or (self.iStart == 17 ) 
               or ( self.iStart == 27) ):    
                  draw_rectangle( *self.GetPowerRightRect() ) 

        if( (self.iState == STATE_SKILL_RISINGTACKLE) ):
            if(  (self.iDirX  == DIR_LEFT )  ):
              if( ( self.iStart == 7) or (self.iStart == 17 ) 
               or ( self.iStart == 27) ):    
                  draw_rectangle( *self.GetPowerLeftRect() )
                  
    def HitCheck(self,frame_time):
        if self.bDie == False:
            if  self.bHit == True and self.iHitDirX == DIR_LEFT and self.iHitState == STATE_BLANKA_PUNCH:
                self.iState = STATE_HIT
                self.iX -= 0.5
                if self.bSoundCheck == False:
                    self.Sound.PlayerHit.play()
                    self.bSoundCheck = True
                if self.bHpCheck == False:
                    self.iHp -= 20
                    self.bHpCheck = True
            elif  self.bHit == True and self.iHitDirX == DIR_RIGHT and self.iHitState == STATE_BLANKA_PUNCH:
                self.iState = STATE_HIT
                self.iX += 0.5
                if self.bSoundCheck == False:
                    self.Sound.PlayerHit.play()
                    self.bSoundCheck = True

                if self.bHpCheck == False:
                    self.iHp -= 20
                    self.bHpCheck = True
            elif  self.bHit == True and self.iHitDirX == DIR_LEFT and self.iHitState == STATE_BLANKA_KICK:
                self.iState = STATE_HIT
                self.iX += 0.5
                if self.bSoundCheck == False:
                    self.Sound.PlayerHit.play()
                    self.bSoundCheck = True

                if self.bHpCheck == False:
                    self.iHp -= 10
                    self.bHpCheck = True
            elif  self.bHit == True and self.iHitDirX == DIR_RIGHT and self.iHitState == STATE_BLANKA_KICK:
                self.iState = STATE_HIT
                self.iX += 0.5
                if self.bSoundCheck == False:
                    self.Sound.PlayerHit.play()
                    self.bSoundCheck = True

                if self.bHpCheck == False:
                    self.iHp -= 10
                    self.bHpCheck = True
            elif self.bHit == True  and self.iHitDirX == DIR_RIGHT and self.iHitState == STATE_BLANKA_ROLL:
                self.iState = STATE_HIT
                self.iX += 2
                if self.bSoundCheck == False:
                    self.Sound.PlayerHit.play()
                    self.bSoundCheck = True

                if self.bHpCheck == False:
                    self.iHp -= 50
                    self.bHpCheck = True
            elif self.bHit == True  and self.iHitDirX == DIR_LEFT and self.iHitState == STATE_BLANKA_ROLL:
                self.iState = STATE_HIT
                self.iX -= 2
                if self.bSoundCheck == False:
                    self.Sound.PlayerHit.play()
                    self.bSoundCheck = True
                if self.bHpCheck == False:
                    self.iHp -= 50
                    self.bHpCheck = True
            elif self.bHit == True and self.iHitDirX == DIR_LEFT and self.iHitState == STATE_BOSS_PUNCH1:
                self.iState = STATE_HIT
                self.iX -= 0.5
                if self.bSoundCheck == False:
                    self.Sound.PlayerHit.play()
                    self.bSoundCheck = True

                if self.bHpCheck == False:
                    self.iHp -= 25
                    self.bHpCheck = True
            elif self.bHit == True and self.iHitDirX == DIR_RIGHT and self.iHitState == STATE_BOSS_PUNCH1:
                self.iState = STATE_HIT
                self.iX += 0.5
                if self.bSoundCheck == False:
                    self.Sound.PlayerHit.play()
                    self.bSoundCheck = True

                if self.bHpCheck == False:
                    self.iHp -= 25
                    self.bHpCheck = True
            elif self.bHit == True and self.iHitDirX == DIR_LEFT and self.iHitState == STATE_BOSS_PUNCH2:
                self.iState = STATE_HIT
                self.iX += 0.5
                if self.bSoundCheck == False:
                    self.Sound.PlayerHit.play()
                    self.bSoundCheck = True

                if self.bHpCheck == False:
                    self.iHp -= 25
                    self.bHpCheck = True
            elif self.bHit == True and self.iHitDirX == DIR_RIGHT and self.iHitState == STATE_BOSS_PUNCH2:
                self.iState = STATE_HIT
                self.iX += 0.5
                #if self.bSoundCheck == False:
                #    self.Sound.PlayerHit.play()
                #    self.bSoundCheck = True

                if self.bHpCheck == False:
                    self.iHp -= 25
                    self.bHpCheck = True
            elif self.bHit == True and self.iHitDirX == DIR_LEFT and self.iHitState == STATE_BOSS_PUNCH2:
                self.iState = STATE_HIT
                self.iX += 0.5
                #if self.bSoundCheck == False:
                #    self.Sound.PlayerHit.play()
                #    self.bSoundCheck = True

                if self.bHpCheck == False:
                    self.iHp -= 25
                    self.bHpCheck = True
            elif self.bHit == True and self.iHitDirX == DIR_RIGHT and self.iHitState == STATE_BOSS_PUNCH2:
                self.iState = STATE_HIT
                self.iX += 0.5
                #if self.bSoundCheck == False:
                #    self.Sound.PlayerHit.play()
                #    self.bSoundCheck = True

                if self.bHpCheck == False:
                    self.iHp -= 25
                    self.bHpCheck = True


            elif self.bSkill1Hit == True and self.iHitDirX == DIR_RIGHT:
                self.iState = STATE_IORI_HIT
                self.iX += 2
                if self.bHpCheck == False:
                        self.iHp -= 10
                        self.bHpCheck = True
                #if self.bSoundCheck == False:
                #        self.Sound.PlayerHit.play()
                #        self.bSoundCheck = True
            elif  self.bSkill1Hit == True and self.iHitDirX == DIR_LEFT:
                self.iState = STATE_IORI_HIT
                self.iX -= 2
                if self.bHpCheck == False:
                        self.iHp -= 10
                        self.bHpCheck = True
                #if self.bSoundCheck == False:
                #        self.Sound.PlayerHit.play()
                #        self.bSoundCheck = True
            else:
                # self.bSoundCheck = False
                 self.bHpCheck  = False
                        
        if self.iHp <= -360 and self.bDie == False:
            self.iState = STATE_DIE 
            self.bDie = True
            self.Sound.PlayerDie.play()
            
    def SpCheck(self):
        pass
                     
    def GetCollBodyRect(self):
        return( (self.canvas_width//2 + self.x_offset - self.RectSizeX  ),
                  (self.canvas_height//2 + self.y_offset - self.RectSizeY ),
                  (self.canvas_width//2 + self.x_offset + self.RectSizeX  ), 
                  (self.canvas_height//2 + self.y_offset + self.RectSizeY - self.range ) )

    
    def GetPunchLeftRect(self):
        return(  (self.canvas_width//2 + self.x_offset - self.RectSizeX  - 30 ),
                   (self.canvas_height//2 + self.y_offset - self.RectSizeY + 80 ),
                   (self.canvas_width//2 + self.x_offset + self.RectSizeX  - 70 ),
                   (self.canvas_height//2 + self.y_offset + self.RectSizeY - 50 ) )

    def GetPunchRightRect(self):
        return( (self.canvas_width//2 + self.x_offset - self.RectSizeX + 80  ), 
                  (self.canvas_height//2 + self.y_offset - self.RectSizeY + 80 ),
                  (self.canvas_width//2 + self.x_offset + self.RectSizeX + 35 ),
                  (self.canvas_height//2 + self.y_offset + self.RectSizeY - 50 ) )

    def GetKickRightRect(self):
        return( (self.canvas_width//2 + self.x_offset - self.RectSizeX + 80  ),
                  (self.canvas_height//2 + self.y_offset - self.RectSizeY + 60 ) ,
                  (self.canvas_width//2 + self.x_offset + self.RectSizeX + 45 ),
                  (self.canvas_height//2 + self.y_offset + self.RectSizeY - 60 ) )

    def GetKickLeftRect(self):
        return( (self.canvas_width//2 + self.x_offset - self.RectSizeX - 45  ), 
                  (self.canvas_height//2 + self.y_offset - self.RectSizeY + 60 ) ,
                  (self.canvas_width//2 + self.x_offset + self.RectSizeX - 90 ),
                  (self.canvas_height//2 + self.y_offset + self.RectSizeY - 60 ) )

    def GetBurnLeftRect(self):
        return(  (self.canvas_width//2 + self.x_offset - self.RectSizeX  - 80 ),
                   (self.canvas_height//2 + self.y_offset - self.RectSizeY + 50 ),
                   (self.canvas_width//2 + self.x_offset + self.RectSizeX  - 30 ),
                   (self.canvas_height//2 + self.y_offset + self.RectSizeY + 30 ) )

    def GetBurnRightRect(self):
        return( (self.canvas_width//2 + self.x_offset - self.RectSizeX + 10  ), 
                  (self.canvas_height//2 + self.y_offset - self.RectSizeY + 50 ),
                  (self.canvas_width//2 + self.x_offset + self.RectSizeX + 80 ),
                  (self.canvas_height//2 + self.y_offset + self.RectSizeY + 30 ) )

    def GetPowerRightRect(self):
        return( (self.canvas_width//2 + self.x_offset - self.RectSizeX + 80  ), 
                  (self.canvas_height//2 + self.y_offset - self.RectSizeY + 30 ),
                  (self.canvas_width//2 + self.x_offset + self.RectSizeX + 80 ),
                  (self.canvas_height//2 + self.y_offset + self.RectSizeY - 50 ) )

    def GetPowerLeftRect(self):
        return(  (self.canvas_width//2 + self.x_offset - self.RectSizeX  - 80 ),
                   (self.canvas_height//2 + self.y_offset - self.RectSizeY + 20 ),
                   (self.canvas_width//2 + self.x_offset + self.RectSizeX  - 70 ),
                   (self.canvas_height//2 + self.y_offset + self.RectSizeY - 50 ) )
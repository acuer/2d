from Import import *
import Stage1_State

class Stage1:
  
     def __init__(self):
       self.iX,self.iY = 500, 775
       self.iCX, self.iCY = 800, 600
       self.speed = 0
       self.left = 0
       self.top = 0
       self.bDebugMode = False
       self.canvas_width = get_canvas_width()
       self.canvas_height = get_canvas_height()
       self.iState = 0
       self.iScene = 0
       self.iFrame = 0
       self.iLast = 0
       self.iStart = 0
       self.dFrameTime = 0
       self.Load_Image()
       self.iKill = 0

     def Load_Image(self):
       self.imageFieldBack = load_image('Stage_Field_BG.png')
       self.imageField = load_image('Stage_Field.png')
       self.imageFieldReBack = load_image('Stage_Field_ReBG.png')
 


       self.w = self.imageField.w
       self.h = self.imageField.h  

     def Set_Center_Object(self, player):
       self.center_Obj = player

     def Progress(self, frame_time):
        self.left = clamp(0, int(self.center_Obj.iX) -
        self.canvas_width//2, self.w - self.canvas_width)
        self.top = clamp(0, int(self.center_Obj.iY) -
        self.canvas_height//2, self.h - self.canvas_height)
        self.SetMotion()
        self.FrameMove(frame_time)

     def Render(self,frame_time):
        if self.center_Obj.bDie == False:
            self.imageFieldBack.draw(self.iX,self.iY)
        else:
            self.imageFieldReBack.draw(self.iX,self.iY)

        if self.bDebugMode == True:
            self.RenderCollRect();
      
        self.imageField.clip_draw_to_origin(self.left,self.top, self.canvas_width,
        self.canvas_height, 0, 0)

              

     def SetMotion(self):
         if( self.iState == STATE_SKILL_RISINGTACKLE ):
             if self.iScene != 0:
                 self.iStart = 0
                 
             self.iScene = 0
             self.iLast = 10
             self.dFrameTime = 70

     def FrameMove(self,frame_time):
         if self.dFrameTime  +  self.iFrame < SDL_GetTicks():
             self.iFrame = SDL_GetTicks()
             self.iStart += 1

         if self.iStart >= self.iLast:
             self.iStart = 0
             self.iState = 0
        
    
     def RenderCollRect(self):
        draw_rectangle( *self.Bottom() ) # 1floor bottom
        draw_rectangle( *self.OneFloorLeft() )
        draw_rectangle( *self.OneFloorRight() )
        draw_rectangle( *self.TwoFloorCenter() )
        draw_rectangle( *self.ThreeFloorLeft() )
        draw_rectangle( *self.ThreeFloorRight() )
        draw_rectangle( *self.ForthFloorCenter() )
    
     def SetDebugMode( self, bDebug ):
         self.bDebugMode = bDebug

     def SetMotionState( self, iState ):
         self.iState = iState
     # Left, bottom, right. top
     def Bottom(self):
        return 50 - self.left, 140 - self.top, 950 - self.left, 150 - self.top

     def OneFloorLeft(self):
        return 50 - self.left, 344 - self.top, 395 - self.left, 345 - self.top

     def OneFloorRight(self):
        return 600 - self.left, 344 - self.top, 945 - self.left, 345 - self.top
     
     def TwoFloorCenter(self):
        return 200 - self.left, 543 - self.top, 800 - self.left, 545 - self.top

     def ThreeFloorLeft(self):
        return 50 - self.left, 743 - self.top, 395 - self.left, 745 - self.top

     def ThreeFloorRight(self):
        return 600 - self.left, 743 - self.top, 945 - self.left, 745 - self.top

     def ForthFloorCenter(self):
        return 200 - self.left, 943 - self.top, 800 - self.left, 945 - self.top

     def FiveFloorLeft(self):
        return 50 - self.left, 1143 - self.top, 395 - self.left, 1145 - self.top

     def FiveFloorRight(self):
        return 600 - self.left, 1143 - self.top, 945 - self.left, 1145 - self.top
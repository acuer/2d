from Import import *

class UI:
     def __init__(self):
       self.canvas_width = get_canvas_width()
       self.canvas_height = get_canvas_height()
       self.Load_Image()
       self.iDieCnt = 0
       self.iDieCntNumLine = 0

     def Load_Image(self):
       self.imageHpBar = load_image('Status_HpBar.png')
       self.imageSpBar = load_image('Status_SPBar.png')
       self.imageHpBack = load_image('Status_BG.png')
       self.imageKill = load_image('Player_KillScore.png')
       self.imageKillNumberOne = load_image('Player_KillScore.png')
       self.imageKillNumberTwo = load_image('Player_KillScore.png')
       self.imageKillNumberThree = load_image('Player_KillScore.png')

     def Set_Center_Object(self, player):
       self.center_Obj = player

     def Progress(self, frame_time):
       if self.iDieCnt == 10:
           self.iDieCntNumLine = 1
       elif self.iDieCnt == 20:
           self.iDieCntNumLine = 2
       elif self.iDieCnt == 30:
           self.iDieCntNumLine = 3    
       elif self.iDieCnt == 40:
           self.iDieCntNumLine = 4

     def Render(self,frame_time):
        self.imageHpBack.clip_draw( 0, 0,  360, 75, 200, 552);
        self.imageHpBar.clip_draw( 0, 0,  360 + self.center_Obj.iHp, 75, 200 + self.center_Obj.iHp / 2, 552 );
        self.imageSpBar.clip_draw( 0, 0, 310 + self.center_Obj.iSp, 75, 175 + self.center_Obj.iSp / 2, 552 );

        if self.iDieCnt >= 10 and self.iDieCnt < 20:
            self.imageKillNumberOne.clip_draw( 70 + ( (self.iDieCnt - 10) * 160 ), 0, 160, 150, 725 + ((self.iDieCnt - 10) * 10 ), 510 )
            self.imageKillNumberTwo.clip_draw( 70 + ( self.iDieCntNumLine * 160 ), 0, 160, 150, 690+ ((self.iDieCntNumLine ) * 10 ), 510 )
        elif self.iDieCnt >= 20 and self.iDieCnt < 30:
            self.imageKillNumberOne.clip_draw( 70 + ( (self.iDieCnt - 20) * 160 ), 0, 160, 150, 725 + ((self.iDieCnt - 20) * 10 ), 510 )
            self.imageKillNumberTwo.clip_draw( 70 + ( self.iDieCntNumLine * 160 ), 0, 160, 150, 690+ ((self.iDieCntNumLine ) * 10 ), 510 )
        elif self.iDieCnt >= 30 and self.iDieCnt < 40:
            self.imageKillNumberOne.clip_draw( 70 + ( (self.iDieCnt - 30) * 160 ), 0, 160, 150, 725 + ((self.iDieCnt - 30) * 10 ), 510 )
            self.imageKillNumberTwo.clip_draw( 70 + ( self.iDieCntNumLine * 160 ), 0, 160, 150, 690+ ((self.iDieCntNumLine ) * 10 ), 510 )
        elif self.iDieCnt >= 40 and self.iDieCnt < 50:
            self.imageKillNumberOne.clip_draw( 70 + ( (self.iDieCnt - 40) * 160 ), 0, 160, 150, 725 + ((self.iDieCnt - 40) * 10 ), 510 )
            self.imageKillNumberTwo.clip_draw( 70 + ( self.iDieCntNumLine * 160 ), 0, 160, 150, 690+ ((self.iDieCntNumLine ) * 10 ), 510 )
        else:
            self.imageKillNumberOne.clip_draw( 70 + ( self.iDieCnt * 160 ), 0, 160, 150, 710 + (self.iDieCnt * 10 ), 510 )

        self.imageKill.clip_draw( 1600, 0, 185, 150, 600, 510)

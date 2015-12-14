from Import import * 
class CollisonMgr:

        def __init__(self):
            self.bJumpColl = False
            self.bJump = False
             
        def SetJumpColl(self, bJumpColl ):
            self.bJumpColl = bJumpColl
        
        def SetJump(self, bJump ):
            self.bJump = bJump
        
        def CollisionFieldPlayer(self, ObjA, ObjB, iCheck ):
            self.left_A, self.bottom_A, self.right_A, self.top_A = ObjA.GetCollBodyRect()
       
            if ( (self.bJump == True) ):
                if self.bJumpColl == True:
                    if iCheck == COLL_BOTTOM:
                        self.left_B, self.bottom_B, self.right_B, self.top_B = ObjB.Bottom()
                    elif ( iCheck == COLL_ONEFLOOR_LEFT ):
                        self.left_B, self.bottom_B, self.right_B, self.top_B = ObjB.OneFloorLeft()
                        self.iCollCheckCnt = 0
                    elif iCheck == COLL_ONEFLOOR_RIGHT:
                        self.left_B, self.bottom_B, self.right_B, self.top_B = ObjB.OneFloorRight()    
                    elif iCheck == COLL_TWOFLOOR_CENTER:
                        self.left_B, self.bottom_B, self.right_B, self.top_B = ObjB.TwoFloorCenter()    
                    elif iCheck == COLL_THREEFLOOR_LEFT:
                        self.left_B, self.bottom_B, self.right_B, self.top_B = ObjB.ThreeFloorLeft()
                    elif iCheck == COLL_THREEFLOOR_RIGHT:
                        self.left_B, self.bottom_B, self.right_B, self.top_B = ObjB.ThreeFloorRight()        
                    elif iCheck == COLL_FORTHLOOR_CENTER:
                        self.left_B, self.bottom_B, self.right_B, self.top_B = ObjB.ForthFloorCenter()    
                    elif iCheck == COLL_FIVEFLOOR_LEFT:
                        self.left_B, self.bottom_B, self.right_B, self.top_B = ObjB.FiveFloorLeft()
                    elif iCheck == COLL_FIVEFLOOR_RIGHT:
                        self.left_B, self.bottom_B, self.right_B, self.top_B = ObjB.FiveFloorRight()  

                    if self.left_A > self.right_B:
                        return False
            
                    if self.right_A < self.left_B:
                        return False

                    if self.top_A < self.bottom_B:
                        return False

                    if self.bottom_A > self.top_B:
                        return False

                    return True
            else:
                if iCheck == COLL_BOTTOM:
                    self.left_B, self.bottom_B, self.right_B, self.top_B = ObjB.Bottom()
                elif ( iCheck == COLL_ONEFLOOR_LEFT ):
                    self.left_B, self.bottom_B, self.right_B, self.top_B = ObjB.OneFloorLeft()
                    self.iCollCheckCnt = 0
                elif iCheck == COLL_ONEFLOOR_RIGHT:
                    self.left_B, self.bottom_B, self.right_B, self.top_B = ObjB.OneFloorRight()    
                elif iCheck == COLL_TWOFLOOR_CENTER:
                    self.left_B, self.bottom_B, self.right_B, self.top_B = ObjB.TwoFloorCenter()    
                elif iCheck == COLL_THREEFLOOR_LEFT:
                    self.left_B, self.bottom_B, self.right_B, self.top_B = ObjB.ThreeFloorLeft()
                elif iCheck == COLL_THREEFLOOR_RIGHT:
                    self.left_B, self.bottom_B, self.right_B, self.top_B = ObjB.ThreeFloorRight()        
                elif iCheck == COLL_FORTHLOOR_CENTER:
                    self.left_B, self.bottom_B, self.right_B, self.top_B = ObjB.ForthFloorCenter()    
                elif iCheck == COLL_FIVEFLOOR_LEFT:
                    self.left_B, self.bottom_B, self.right_B, self.top_B = ObjB.FiveFloorLeft()
                elif iCheck == COLL_FIVEFLOOR_RIGHT:
                    self.left_B, self.bottom_B, self.right_B, self.top_B = ObjB.FiveFloorRight()  

                if self.left_A > self.right_B:
                    return False        
            
                if self.right_A < self.left_B:
                    return False

                if self.top_A < self.bottom_B:
                    return False

                if self.bottom_A > self.top_B:
                    return False

                return True
        
        def CollisionFieldMonster(self, ObjA, ObjB, iCheck ):
           self.left_A, self.bottom_A, self.right_A, self.top_A = ObjA.GetCollBodyRect()

           if ( (self.bJump == True) ):
               if self.bJumpColl == True:
                   if iCheck == COLL_BOTTOM:
                       self.left_B, self.bottom_B, self.right_B, self.top_B = ObjB.Bottom()
                   elif ( iCheck == COLL_ONEFLOOR_LEFT ):
                       self.left_B, self.bottom_B, self.right_B, self.top_B = ObjB.OneFloorLeft()
                       self.iCollCheckCnt = 0
                   elif iCheck == COLL_ONEFLOOR_RIGHT:
                       self.left_B, self.bottom_B, self.right_B, self.top_B = ObjB.OneFloorRight()    
                   elif iCheck == COLL_TWOFLOOR_CENTER:
                       self.left_B, self.bottom_B, self.right_B, self.top_B = ObjB.TwoFloorCenter()  
                   elif iCheck == COLL_THREEFLOOR_LEFT:
                       self.left_B, self.bottom_B, self.right_B, self.top_B = ObjB.ThreeFloorLeft()
                   elif iCheck == COLL_THREEFLOOR_RIGHT:
                       self.left_B, self.bottom_B, self.right_B, self.top_B = ObjB.ThreeFloorRight()  
                   elif iCheck == COLL_FORTHLOOR_CENTER:
                       self.left_B, self.bottom_B, self.right_B, self.top_B = ObjB.ForthFloorCenter()
                   elif iCheck == COLL_FIVEFLOOR_LEFT:
                       self.left_B, self.bottom_B, self.right_B, self.top_B = ObjB.FiveFloorLeft()
                   elif iCheck == COLL_FIVEFLOOR_RIGHT:
                       self.left_B, self.bottom_B, self.right_B, self.top_B = ObjB.FiveFloorRight()  
           
                   if self.left_A > self.right_B:
                       return False        
           
                   if self.right_A < self.left_B:
                       return False
           
                   if self.top_A < self.bottom_B:
                       return False
           
                   if self.bottom_A > self.top_B:
                       return False
           
                   return True
           else:
                   if iCheck == COLL_BOTTOM:
                       self.left_B, self.bottom_B, self.right_B, self.top_B = ObjB.Bottom()
                   elif ( iCheck == COLL_ONEFLOOR_LEFT ):
                       self.left_B, self.bottom_B, self.right_B, self.top_B = ObjB.OneFloorLeft()
                       self.iCollCheckCnt = 0
                   elif iCheck == COLL_ONEFLOOR_RIGHT:
                       self.left_B, self.bottom_B, self.right_B, self.top_B = ObjB.OneFloorRight()    
                   elif iCheck == COLL_TWOFLOOR_CENTER:
                       self.left_B, self.bottom_B, self.right_B, self.top_B = ObjB.TwoFloorCenter()  
                   elif iCheck == COLL_THREEFLOOR_LEFT:
                       self.left_B, self.bottom_B, self.right_B, self.top_B = ObjB.ThreeFloorLeft()
                   elif iCheck == COLL_THREEFLOOR_RIGHT:
                       self.left_B, self.bottom_B, self.right_B, self.top_B = ObjB.ThreeFloorRight()  
                   elif iCheck == COLL_FORTHLOOR_CENTER:
                       self.left_B, self.bottom_B, self.right_B, self.top_B = ObjB.ForthFloorCenter()
                   elif iCheck == COLL_FIVEFLOOR_LEFT:
                       self.left_B, self.bottom_B, self.right_B, self.top_B = ObjB.FiveFloorLeft()
                   elif iCheck == COLL_FIVEFLOOR_RIGHT:
                       self.left_B, self.bottom_B, self.right_B, self.top_B = ObjB.FiveFloorRight()  
           
                   if self.left_A > self.right_B:
                       return False        
           
                   if self.right_A < self.left_B:
                       return False
           
                   if self.top_A < self.bottom_B:
                       return False
           
                   if self.bottom_A > self.top_B:
                       return False
           
                   return True

        def CollisionFieldBoss(self, ObjA, ObjB, iCheck ):
           self.left_A, self.bottom_A, self.right_A, self.top_A = ObjA.GetCollBodyRect()

           if ( (self.bJump == True) ):
               if self.bJumpColl == True:
                   if iCheck == COLL_BOTTOM:
                       self.left_B, self.bottom_B, self.right_B, self.top_B = ObjB.Bottom()
                   elif ( iCheck == COLL_ONEFLOOR_LEFT ):
                       self.left_B, self.bottom_B, self.right_B, self.top_B = ObjB.OneFloorLeft()
                       self.iCollCheckCnt = 0
                   elif iCheck == COLL_ONEFLOOR_RIGHT:
                       self.left_B, self.bottom_B, self.right_B, self.top_B = ObjB.OneFloorRight()    
                   elif iCheck == COLL_TWOFLOOR_CENTER:
                       self.left_B, self.bottom_B, self.right_B, self.top_B = ObjB.TwoFloorCenter()  
                   elif iCheck == COLL_THREEFLOOR_LEFT:
                       self.left_B, self.bottom_B, self.right_B, self.top_B = ObjB.ThreeFloorLeft()
                   elif iCheck == COLL_THREEFLOOR_RIGHT:
                       self.left_B, self.bottom_B, self.right_B, self.top_B = ObjB.ThreeFloorRight()  
                   elif iCheck == COLL_FORTHLOOR_CENTER:
                       self.left_B, self.bottom_B, self.right_B, self.top_B = ObjB.ForthFloorCenter()
                   elif iCheck == COLL_FIVEFLOOR_LEFT:
                       self.left_B, self.bottom_B, self.right_B, self.top_B = ObjB.FiveFloorLeft()
                   elif iCheck == COLL_FIVEFLOOR_RIGHT:
                       self.left_B, self.bottom_B, self.right_B, self.top_B = ObjB.FiveFloorRight()  
           
                   if self.left_A > self.right_B:
                       return False        
           
                   if self.right_A < self.left_B:
                       return False
           
                   if self.top_A < self.bottom_B:
                       return False
           
                   if self.bottom_A > self.top_B:
                       return False
           
                   return True
           else:
                   if iCheck == COLL_BOTTOM:
                       self.left_B, self.bottom_B, self.right_B, self.top_B = ObjB.Bottom()
                   elif ( iCheck == COLL_ONEFLOOR_LEFT ):
                       self.left_B, self.bottom_B, self.right_B, self.top_B = ObjB.OneFloorLeft()
                       self.iCollCheckCnt = 0
                   elif iCheck == COLL_ONEFLOOR_RIGHT:
                       self.left_B, self.bottom_B, self.right_B, self.top_B = ObjB.OneFloorRight()    
                   elif iCheck == COLL_TWOFLOOR_CENTER:
                       self.left_B, self.bottom_B, self.right_B, self.top_B = ObjB.TwoFloorCenter()  
                   elif iCheck == COLL_THREEFLOOR_LEFT:
                       self.left_B, self.bottom_B, self.right_B, self.top_B = ObjB.ThreeFloorLeft()
                   elif iCheck == COLL_THREEFLOOR_RIGHT:
                       self.left_B, self.bottom_B, self.right_B, self.top_B = ObjB.ThreeFloorRight()  
                   elif iCheck == COLL_FORTHLOOR_CENTER:
                       self.left_B, self.bottom_B, self.right_B, self.top_B = ObjB.ForthFloorCenter()
                   elif iCheck == COLL_FIVEFLOOR_LEFT:
                       self.left_B, self.bottom_B, self.right_B, self.top_B = ObjB.FiveFloorLeft()
                   elif iCheck == COLL_FIVEFLOOR_RIGHT:
                       self.left_B, self.bottom_B, self.right_B, self.top_B = ObjB.FiveFloorRight()  
           
                   if self.left_A > self.right_B:
                       return False        
           
                   if self.right_A < self.left_B:
                       return False
           
                   if self.top_A < self.bottom_B:
                       return False
           
                   if self.bottom_A > self.top_B:
                       return False
           
                   return True
          
        def CollisionAttBlanka(self, ObjA, ObjB, iCheck, iState ):
            self.left_A, self.bottom_A, self.right_A, self.top_A = ObjA.GetCollBodyRect()

            if ( (iCheck == DIR_RIGHT ) & ( iState == STATE_PUNCH ) ):
                self.left_B, self.bottom_B, self.right_B, self.top_B = ObjB.GetPunchRightRect()

            elif ((iCheck == DIR_LEFT ) & ( iState == STATE_PUNCH ) ):
                self.left_B, self.bottom_B, self.right_B, self.top_B = ObjB.GetPunchLeftRect()

            elif ((iCheck == DIR_LEFT ) & ( iState == STATE_KICK ) ):
                self.left_B, self.bottom_B, self.right_B, self.top_B = ObjB.GetKickLeftRect()

            elif ((iCheck == DIR_RIGHT ) & ( iState == STATE_KICK ) ):
                self.left_B, self.bottom_B, self.right_B, self.top_B = ObjB.GetKickRightRect()

            elif ((iCheck == DIR_LEFT ) & ( iState == STATE_SKILL_ORUGEN ) ):
                self.left_B, self.bottom_B, self.right_B, self.top_B = ObjB.GetBurnLeftRect()

            elif ((iCheck == DIR_RIGHT ) & ( iState == STATE_SKILL_ORUGEN ) ):
                self.left_B, self.bottom_B, self.right_B, self.top_B = ObjB.GetBurnRightRect()
           
            elif ((iState == STATE_SKILL_RISINGTACKLE)):
                self.left_B, self.bottom_B, self.right_B, self.top_B = ObjB.GetCollBodyRect()
            
            elif ( iCheck == DIR_LEFT and iState == STATE_SKILL_POWERGEYSER):
                self.left_B, self.bottom_B, self.right_B, self.top_B = ObjB.GetPowerLeftRect()

            elif ( iCheck == DIR_RIGHT and iState == STATE_SKILL_POWERGEYSER):
                self.left_B, self.bottom_B, self.right_B, self.top_B = ObjB.GetPowerRightRect()

            elif( iCheck == DIR_LEFT and iState == STATE_BLANKA_PUNCH ):
                self.left_B, self.bottom_B, self.right_B, self.top_B = ObjB.GetPunchLeft()

            elif( iCheck == DIR_RIGHT and iState == STATE_BLANKA_PUNCH ):
                self.left_B, self.bottom_B, self.right_B, self.top_B = ObjB.GetPunchRight()

            elif( iCheck == DIR_LEFT and iState == STATE_BLANKA_KICK ):
                self.left_B, self.bottom_B, self.right_B, self.top_B = ObjB.GetKickLeft()

            elif( iCheck == DIR_RIGHT and iState == STATE_BLANKA_KICK ):
                self.left_B, self.bottom_B, self.right_B, self.top_B = ObjB.GetKickRight()

            elif( iState ==  STATE_BLANKA_ROLL ):
                self.left_B, self.bottom_B, self.right_B, self.top_B = ObjB.GetCollBodyRect()

            elif( iCheck == DIR_LEFT and iState == STATE_BOSS_PUNCH1 ):
                self.left_B, self.bottom_B, self.right_B, self.top_B = ObjB.GetPunchLeft()

            elif( iCheck == DIR_RIGHT and iState == STATE_BOSS_PUNCH1 ):
                self.left_B, self.bottom_B, self.right_B, self.top_B = ObjB.GetPunchRight()
 
            elif( iCheck == DIR_LEFT and iState == STATE_BOSS_PUNCH2 ):
                self.left_B, self.bottom_B, self.right_B, self.top_B = ObjB.GetPunchLeft()

            elif( iCheck == DIR_RIGHT and iState == STATE_BOSS_PUNCH2 ):
                self.left_B, self.bottom_B, self.right_B, self.top_B = ObjB.GetPunchRight()

            elif( iCheck == DIR_LEFT and iState == STATE_BOSS_PUNCH3 ):
                self.left_B, self.bottom_B, self.right_B, self.top_B = ObjB.GetPunchLeft()

            elif( iCheck == DIR_RIGHT and iState == STATE_BOSS_PUNCH3 ):
                self.left_B, self.bottom_B, self.right_B, self.top_B = ObjB.GetPunchRight()

            elif( iCheck == DIR_RIGHT and iState == STATE_BOSS_SKILL1 ):
                self.left_B, self.bottom_B, self.right_B, self.top_B = ObjB.GetCollBodyRect()

            elif( iCheck == DIR_LEFT and iState == STATE_BOSS_SKILL1 ):
                self.left_B, self.bottom_B, self.right_B, self.top_B = ObjB.GetCollBodyRect()

            if self.left_A > self.right_B:
                return False
            
            if self.right_A < self.left_B:
                return False

            if self.top_A < self.bottom_B:
                return False

            if self.bottom_A > self.top_B:
                return False

            return True
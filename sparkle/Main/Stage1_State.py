from Import import *

import MonsterHitEffect
import Stage1
import Player
import CollisionMgr
import PowerGeyser
import Blanka
import UI
import PlayerEffect
import SoundMgr


g_Stage1 = None
g_Player = None
g_CollMgr = None
g_PowerGeyser = None
g_Blanka = []
g_UI = None
g_PlayerEffect = []
g_MonsterEffect = []
g_iPlayerEffectCnt = 0
g_iMonsterEffectCnt = 0
g_SoundMgr = None

g_SoundCheck = False
g_JumpSoundCheck = False
g_Continue = False
g_Create = False

def Enter():
    global g_Stage1, g_Player, g_CollMgr, g_PowerGeyser, g_Blanka, g_UI, g_PlayerEffect, g_SoundMgr, g_iPlayerEffectCnt, g_iMonsterEffectCnt, g_SoundCheck
    g_Stage1 = Stage1.Stage1()
    g_Player = Player.Player()
    g_CollMgr = CollisionMgr.CollisonMgr()
    g_PowerGeyser = PowerGeyser.PowerGeyser()
    g_UI = UI.UI()
   
    g_SoundMgr = SoundMgr.SoundMgr()
    g_SoundMgr.BackGround.repeat_play()

    g_Stage1.Set_Center_Object(g_Player)
    g_UI.Set_Center_Object(g_Player)
    g_Player.Set_Background(g_Stage1)


def PlayerHitEffectCreate():
    g_PlayerEffect.append( PlayerEffect.PlayerEffect())

    for E in g_PlayerEffect:
        if E.bPlayer == False:
            E.Set_Center_Object(g_Player)

def MonsterHitEffectCreate(B):
    g_MonsterEffect.append( MonsterHitEffect.MonsterHitEffect() )
    
    for E in g_MonsterEffect:
        if E.bMonsterCheck == False: 
            E.Set_Center_Object(B)

def MonsterCreate():
    for i in range(1):
        g_Blanka.append( Blanka.Blanka() )

    for B in g_Blanka:
        B.Set_Player(g_Player)
        B.Set_Background(g_Stage1)              
       
def Release():
        del(g_Player)
        del(g_CollMgr)
        del(g_PowerGeyser)
        del(g_UI)
   

        for B in g_Blanka:
            g_Blanka.remove(B)
        for E in g_PlayerEffect:
            g_PlayerEffect.remove(E)
        for M in g_MonsterEffect:
            g_MonsterEffect.remove(M)
        

def Progress(frame_time):
    global g_iPlayerEffectCnt, g_iMonsterEffectCnt, g_SoundCheck, g_Continue, g_Create

    g_Player.Progress(frame_time)
    g_Stage1.Progress(frame_time)
    g_UI.Progress(frame_time)

    if g_Player.bDie == True:
        if g_Continue == False:
            if g_Player.iStart >= 7:
                g_SoundMgr.Continue.play()
                g_Continue = True
    else:
        g_Continue = False

    if g_Player.bHit == True:
        PlayerHitEffectCreate()

    if g_Player.bMon1Create  == True:
        MonsterCreate()
        g_Player.bMon1Create = False

    for B in g_Blanka:
        B.Progress(frame_time)
        B.SetDebugMode( g_Player.GetDebugMode() )
        if B.bHit== True or B.bRisingHit == True:
            MonsterHitEffectCreate(B)

        if ( (B.GetMotionState() == STATE_BLANKA_DIE ) & (B.GetFrame() >= 16) ):
            g_UI.iDieCnt += 1
            g_Blanka.remove(B)
   
    for E in g_PlayerEffect:
        E.Progress(frame_time)
        if E.bEffectOff == True:
            g_PlayerEffect.remove(E)
            

    for M in g_MonsterEffect:
        M.Progress(frame_time)
        if M.bEffectOff == True: 
           g_MonsterEffect.remove(M)

    g_Stage1.SetDebugMode( g_Player.GetDebugMode() )
    
    if( (g_Player.GetMotionState() == STATE_SKILL_RISINGTACKLE ) ):
        g_Stage1.SetMotionState( STATE_SKILL_RISINGTACKLE )

    if( ( g_Player.GetMotionState() == STATE_SKILL_RISINGTACKLE )
       & (g_Player.GetFrame() >= 7) ):
        g_PowerGeyser.Progress(frame_time)
 
    FieldCollision()
    AttackCollision()
         
def Render(frame_time):
    clear_canvas()

    g_Stage1.Render(frame_time)
    for B in g_Blanka:
       B.Render(frame_time)

    g_Player.Render(frame_time)
    
    PowerGeyserRender()

    for E in g_PlayerEffect:
        E.Render(frame_time)

    for M in g_MonsterEffect:
        M.Render(frame_time)

    g_UI.Render(frame_time)

    update_canvas()

def Input(frame_time):
    global g_Player
    events = get_events()
    for event in events:
       g_Player.Input(event,frame_time)
       # g_Logo.Input(event)

def Pause():
    pass
def Resume():
    pass

def FieldCollision():
    global g_JumpSoundCheck
    g_CollMgr.SetJump( g_Player.GetJump() )
    g_CollMgr.SetJumpColl( g_Player.GetJumpColl() )

    if(( g_Player.GetDown() == False ) & (g_Player.GetRising() == False ) ):
        if g_CollMgr.CollisionFieldPlayer( g_Player, g_Stage1, COLL_BOTTOM ):
            g_Player.SetPosY( 220 )
            g_Player.SetAir(False)
            if g_JumpSoundCheck == False:
                g_SoundMgr.JumpEnd.play()
                g_JumpSoundCheck = True
            
        elif g_CollMgr.CollisionFieldPlayer( g_Player, g_Stage1, COLL_ONEFLOOR_LEFT ):
             g_Player.SetPosY( 415 )
             g_Player.SetAir(False)
             g_Player.SetJump(False)
             if g_JumpSoundCheck == False:
                g_SoundMgr.JumpEnd.play()
                g_JumpSoundCheck = True
            
        elif g_CollMgr.CollisionFieldPlayer( g_Player, g_Stage1, COLL_ONEFLOOR_RIGHT ):
             g_Player.SetPosY( 415 )
             g_Player.SetAir(False)
             g_Player.SetJump(False)
             if g_JumpSoundCheck == False:
                g_SoundMgr.JumpEnd.play()
                g_JumpSoundCheck = True

        elif g_CollMgr.CollisionFieldPlayer( g_Player, g_Stage1, COLL_TWOFLOOR_CENTER ):
             g_Player.SetPosY( 615 )
             g_Player.SetAir(False)
             g_Player.SetJump(False)
             if g_JumpSoundCheck == False:
                g_SoundMgr.JumpEnd.play()
                g_JumpSoundCheck = True

        elif g_CollMgr.CollisionFieldPlayer( g_Player, g_Stage1, COLL_THREEFLOOR_LEFT ):
             g_Player.SetPosY( 815 )
             g_Player.SetAir(False)
             g_Player.SetJump(False)
             if g_JumpSoundCheck == False:
                g_SoundMgr.JumpEnd.play()
                g_JumpSoundCheck = True

        elif g_CollMgr.CollisionFieldPlayer( g_Player, g_Stage1, COLL_THREEFLOOR_RIGHT ):
             g_Player.SetPosY( 815 )
             g_Player.SetAir(False)
             g_Player.SetJump(False)
             if g_JumpSoundCheck == False:
                g_SoundMgr.JumpEnd.play()
                g_JumpSoundCheck = True

        elif g_CollMgr.CollisionFieldPlayer( g_Player, g_Stage1, COLL_FORTHLOOR_CENTER ):
             g_Player.SetPosY( 1015 )
             g_Player.SetAir(False)
             g_Player.SetJump(False)
             if g_JumpSoundCheck == False:
                g_SoundMgr.JumpEnd.play()
                g_JumpSoundCheck = True

        elif g_CollMgr.CollisionFieldPlayer( g_Player, g_Stage1, COLL_FIVEFLOOR_LEFT ):
             g_Player.SetPosY( 1215 )
             g_Player.SetAir(False)
             g_Player.SetJump(False)
             if g_JumpSoundCheck == False:
                g_SoundMgr.JumpEnd.play()
                g_JumpSoundCheck = True

        elif g_CollMgr.CollisionFieldPlayer( g_Player, g_Stage1, COLL_FIVEFLOOR_RIGHT ):
             g_Player.SetPosY( 1215 )
             g_Player.SetAir(False)
             g_Player.SetJump(False)
             if g_JumpSoundCheck == False:
                g_SoundMgr.JumpEnd.play()
                g_JumpSoundCheck = True
        else:
            g_Player.SetAir(True)
            g_JumpSoundCheck = False



        for B in g_Blanka:
            g_CollMgr.SetJump( B.GetJump() )
            g_CollMgr.SetJumpColl( B.GetJumpColl() )
            if(( B.GetDown() == False ) ):
                if g_CollMgr.CollisionFieldMonster( B, g_Stage1, COLL_BOTTOM ):
                    B.SetPosY( 220 )
                    B.SetAir(False)
                    B.SetJump(False)
                elif g_CollMgr.CollisionFieldMonster( B, g_Stage1, COLL_ONEFLOOR_LEFT ):
                     B.SetPosY( 415 )
                     B.SetAir(False)
                     B.SetJump(False)
                elif g_CollMgr.CollisionFieldMonster( B, g_Stage1, COLL_ONEFLOOR_RIGHT ):
                     B.SetPosY( 415 )
                     B.SetAir(False)
                     B.SetJump(False)
                elif g_CollMgr.CollisionFieldMonster( B, g_Stage1, COLL_TWOFLOOR_CENTER ):
                     B.SetPosY( 615 )
                     B.SetAir(False)
                     B.SetJump(False)
                elif g_CollMgr.CollisionFieldMonster( B, g_Stage1, COLL_THREEFLOOR_LEFT ):
                     B.SetPosY( 815 )
                     B.SetAir(False)
                     B.SetJump(False)
                elif g_CollMgr.CollisionFieldMonster( B, g_Stage1, COLL_THREEFLOOR_RIGHT ):
                     B.SetPosY( 815 )
                     B.SetAir(False)
                     B.SetJump(False)
                elif g_CollMgr.CollisionFieldMonster( B, g_Stage1, COLL_FORTHLOOR_CENTER ):
                     B.SetPosY( 1015 )
                     B.SetAir(False)
                     B.SetJump(False)
                elif g_CollMgr.CollisionFieldMonster( B, g_Stage1, COLL_FIVEFLOOR_LEFT ):
                     B.SetPosY( 1215 )
                     B.SetAir(False)
                     B.SetJump(False)
                elif g_CollMgr.CollisionFieldMonster( B, g_Stage1, COLL_FIVEFLOOR_RIGHT ):
                     B.SetPosY( 1215 )
                     B.SetAir(False)
                     B.SetJump(False)
                else:
                     B.SetAir(True)


def AttackCollision():
    global g_SoundMgr
    for B in g_Blanka:
            if g_Player.GetMotionState() == STATE_PUNCH:
                if( ( g_Player.GetFrame() == 1 ) and ( B.GetHit() == False) ):
                    if g_CollMgr.CollisionAttBlanka(  B, g_Player, g_Player.iDirX, STATE_PUNCH ):
                        B.SetHit( True )
                        B.SetHitState( STATE_PUNCH )
                        B.SetHitDir( g_Player.iDirX )
                        g_SoundMgr.PlayerPunchHit.play()
                        
            elif g_Player.GetMotionState() == STATE_KICK:
                if( ( g_Player.GetFrame() >= 2 ) and g_Player.GetFrame() <= 3 and ( B.GetHit() == False) ):
                    if g_CollMgr.CollisionAttBlanka(  B,g_Player ,g_Player.iDirX, STATE_KICK ):
                        B.SetHit( True )
                        B.SetHitState( STATE_KICK )
                        B.SetHitDir( g_Player.iDirX )
                        g_SoundMgr.PlayerPunchHit.play()
                
            elif g_Player.GetMotionState() == STATE_SKILL_ORUGEN:
                if( (g_Player.GetFrame() == 8 ) or ( g_Player.GetFrame() == 10)  ):
                    if(  ( B.GetHit() == False)  ):
                        if g_CollMgr.CollisionAttBlanka(  B,g_Player ,g_Player.iDirX, STATE_SKILL_ORUGEN):
                            B.SetHit( True )
                            B.SetHitState( STATE_SKILL_ORUGEN )
                            B.SetHitDir( g_Player.iDirX )
                            g_SoundMgr.PlayerPunchHit.play()

                              
            elif g_Player.GetMotionState() == STATE_SKILL_RISINGTACKLE:
                if( (g_Player.iStart == 3 ) or (g_Player.iStart == 5) or (g_Player.iStart ==  7 ) 
                       and ( B.GetRisingHit() == False)  ):
                    if g_CollMgr.CollisionAttBlanka(  B,g_Player ,g_Player.iDirX, STATE_SKILL_RISINGTACKLE):
                        B.SetRisingHit( True )
                        B.SetHitState( STATE_SKILL_RISINGTACKLE )
                        B.SetHitDir( g_Player.iDirX ) 
                        g_SoundMgr.PlayerPunchHit.play()
                                                                                                                    
            else:
               B.SetHit( False )
               B.SetRisingHit( False )
    
    for B in g_Blanka:
        if g_Player.GetMotionState() == STATE_SKILL_RISINGTACKLE:
                if( ( g_Player.iStart >= 7 and g_Player.iStart <= 9)
                   or ( g_Player.iStart >= 17 and g_Player.iStart <= 19   ) 
                   or ( g_Player.iStart >= 27 and g_Player.iStart <= 29 ) ) :
                    if  ( B.GetPowerHit() == False) :
                        if g_CollMgr.CollisionAttBlanka(  B,g_Player ,g_Player.iDirX, STATE_SKILL_RISINGTACKLE):
                            B.SetPowerHit( True )
                            B.SetHitState( STATE_SKILL_RISINGTACKLE )
                            B.SetHitDir( g_Player.iDirX )
                                        
        else:
             B.SetPowerHit(False)

    for B in g_Blanka:
        if B.iState == STATE_BLANKA_PUNCH:
            if B.iStart == 3:
                if g_Player.bHit == False:
                    if g_CollMgr.CollisionAttBlanka( g_Player, B, B.iDirX, STATE_BLANKA_PUNCH ):
                        g_Player.bHit = True
                        g_Player.iHitDirX = B.iDirX
                        g_Player.iHitState = STATE_BLANKA_PUNCH
                      

        elif B.iState == STATE_BLANKA_KICK:
            if B.iStart >= 2:
                if g_Player.bHit == False:
                    if g_CollMgr.CollisionAttBlanka( g_Player, B, B.iDirX, STATE_BLANKA_KICK ):
                        g_Player.bHit = True
                        g_Player.iHitDirX = B.iDirX
                        g_Player.iHitState = STATE_BLANKA_KICK
                  
        elif B.iState == STATE_BLANKA_ROLL:
                if g_Player.bHit == False:
                    if g_CollMgr.CollisionAttBlanka( g_Player, B, B.iDirX, STATE_BLANKA_ROLL ):
                        g_Player.bHit = True
                        g_Player.iHitDirX = B.iDirX
                        g_Player.iHitState = STATE_BLANKA_ROLL
      
        else:
            g_Player.bHit = False



def PowerGeyserRender():
    if( ( g_Player.GetMotionState() == STATE_SKILL_RISINGTACKLE ) 
       & (g_Player.GetFrame() >= 7) ):
            g_PowerGeyser.Render(g_Player.GetScrollX(), g_Player.GetScrollY(), g_Player.GetDirX())

   


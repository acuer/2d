
from Import import *



class SoundMgr:

    def __init__(self):
        self.BackGround = load_music('Sound\\muran.mp3')
        self.JumpEnd = load_wav('Sound\\JumpEnd.wav')
        self.PlayerPunch = load_wav('Sound\\Punch(Effect).wav')
        self.PlayerPunchHit = load_wav('Sound\\Punch(HitEffect).wav')
        self.PlayerHit = load_wav('Sound\\DamageCry.wav')
        self.PlayerKick = load_wav('Sound\\Kick(Effect).wav')
        self.Charge = load_wav('Sound\\IoriVoiceL.wav')
        self.PowerG = load_wav('Sound\\PowerGeyser.wav')
        self.PowerGHit1 = load_wav('Sound\\PowerGeyser(Effect).wav')
        self.PowerGHit2 = load_wav('Sound\\PowerGeyser(Effect).wav')
        self.PowerGHit3 = load_wav('Sound\\PowerGeyser(Effect).wav')
        self.Continue = load_wav('Sound\\Countinue.wav')
        self.Guard = load_wav('Sound\\HeyComeon.wav')
        self.IoriSkill = load_wav('Sound\\IoriVoiceEnd.wav')
        self.PlayerDie = load_wav('Sound\\IoriDie.wav')


        
    def set_volume(self,v):
        pass 



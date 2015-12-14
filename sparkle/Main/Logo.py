
from Import import *
import Stage1_State

class Logo:

    START_ON, START_OFF, EXIT_ON, EXIT_OFF = 0,1,1,0

    def __init__(self):
       self.startState = self.START_ON
       self.exitState = self.EXIT_OFF
       self.frame = 0
       self.iCheck = 1;
       self.running = True;
       

    def Load_Image(self):
       self.imageBack = load_image('title.png')

       
    def Render(self,frame_time):
        self.imageBack.draw(400,300)
 
    
    def Input(self,event):
        if event.type == SDL_QUIT:
            MainFrameWork.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                MainFrameWork.quit()

            elif (event.type, event.key ) == ( SDL_KEYUP, SDLK_DOWN):
                self.startState = self.START_OFF
                self.exitState = self.EXIT_ON
        
            elif (event.type, event.key ) == ( SDL_KEYUP, SDLK_UP):
                self.startState = self.START_ON
                self.exitState = self.EXIT_OFF
   
            elif(event.type, event.key ) == ( SDL_KEYUP, SDLK_RETURN):
                if self.startState == self.START_ON:
                    MainFrameWork.change_state(Stage1_State)
                elif self.exitState == self.EXIT_ON:
                    MainFrameWork.quit()
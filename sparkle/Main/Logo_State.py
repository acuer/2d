from Import import *
import Logo

g_image = None
g_Logo = None


def Enter():
    global g_Logo
    open_canvas()
    g_Logo = Logo.Logo()
    g_Logo.Load_Image()
  

def Release():
    global g_Logo
    del(g_Logo)
   

def Progress(frame_time):
    pass

def Render(frame_time):
    global g_Logo
    clear_canvas()
    g_Logo.Render(frame_time)
    update_canvas()

def Input(frame_time):
    events = get_events()
    for event in events:
        g_Logo.Input(event)

def Pause():
    pass
def Resume():
    pass
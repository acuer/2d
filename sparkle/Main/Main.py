from Import import *
import os
import platform

if platform.architecture()[0] == '32bit':
    os.environ["PYSDL2_DLL_PATH"] = "./SDL2/x86"
else:
    os.environ["PYSDL2_DLL_PATH"] = "./SDL2/x64"

import Logo_State

MainFrameWork.run(Logo_State)

#if __name__ == 'main':
#    MainFrameWork.run(Logo_State)

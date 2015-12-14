from Import import *

running = None
stack = None


def change_state(state):
    global stack
    pop_state()
    stack.append(state)
    state.Enter()



def push_state(state):
    global stack
    if (len(stack) > 0):
        stack[-1].Pause()
    stack.append(state)
    state.Enter()



def pop_state():
    global stack
    if (len(stack) > 0):
        # execute the current state's exit function
        stack[-1].Release()
        # remove the current state
        stack.pop()

    # execute resume function of the previous state
    if (len(stack) > 0):
        stack[-1].Resume()



def quit():
    global running
    running = False


def run(start_state):
    global running, stack
    running = True
    stack = [start_state]
    start_state.Enter()
    current_time = time.clock()

    while (running):
        frame_time = time.clock() - current_time
        current_time += frame_time
        stack[-1].Input(frame_time)
        stack[-1].Progress(frame_time)
        stack[-1].Render(frame_time)
    # repeatedly delete the top of the stack
    while (len(stack) > 0):
        stack[-1].Release()
        stack.pop()


def reset_time():
    global current_time
    current_time = time.clock()
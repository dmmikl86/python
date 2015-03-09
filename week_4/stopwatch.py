# template for "Stopwatch: The Game"
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
# define global variables
time_message = "0:00.0"
counter = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    return str(t)


# define event handlers for buttons; "Start", "Stop", "Reset"
def on_start():
    timer.start()


def on_stop():
    timer.stop()


def on_reset():
    global counter, time_message
    timer.stop()
    counter = 0
    time_message = format(counter)


# define event handler for timer with 0.1 sec interval
def onTimeHandler():
    global time_message, counter
    counter += 100
    time_message = format(counter)


# define draw handler
def onDraw(canvas):
    canvas.draw_text(time_message, (60, 100), 12, 'Red')

# create frame
frame = simplegui.create_frame("StopWatch", 200, 200)
timer = simplegui.create_timer(100, onTimeHandler)

# register event handlers
frame.set_draw_handler(onDraw)
button_start = frame.add_button("Start", on_start, 100)
button_start = frame.add_button("Stop", on_stop, 100)
button_start = frame.add_button("Reset", on_reset, 100)

# start frame
frame.start()


# Please remember to review the grading rubric

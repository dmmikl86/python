# template for "Stopwatch: The Game"
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
# define global variables
DEFAULT = "0:00.0"
time_message = DEFAULT
counter = 0
success = 0
attempts = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def convert(t):
    milliseconds = (t / 100) % 10
    seconds = (t / 1000) % 60
    minutes = ((t / (1000 * 60)) % 60)
    time = str(minutes) + ":" + (("0" + str(seconds)) if seconds < 10 else str(seconds)) + "." + str(milliseconds)
    return time


def format(t):
    if t == 0:
        return DEFAULT
    else:
        return convert(t)


# define event handlers for buttons; "Start", "Stop", "Reset"
def on_start():
    timer.start()


def on_stop():
    global success, attempts
    if timer.is_running():
        attempts += 1
        if ((counter / 100) % 10) == 0:
            success += 1
    timer.stop()


def on_reset():
    global counter, time_message, success, attempts
    timer.stop()
    counter = 0
    success = 0
    attempts = 0
    time_message = format(counter)


# define event handler for timer with 0.1 sec interval
def on_time_handler():
    global time_message, counter
    counter += 100
    time_message = format(counter)


# define draw handler
def on_draw_timer(canvas):
    canvas.draw_text(time_message, (60, 100), 30, 'Red')
    canvas.draw_text(str(success) + "/" + str(attempts), (140, 20), 30, 'Green')


# create frame
frame = simplegui.create_frame("StopWatch", 200, 200)
timer = simplegui.create_timer(100, on_time_handler)

# register event handlers
frame.set_draw_handler(on_draw_timer)
button_start = frame.add_button("Start", on_start, 100)
button_stop = frame.add_button("Stop", on_stop, 100)
button_reset = frame.add_button("Reset", on_reset, 100)

# start frame
frame.start()


# Please remember to review the grading rubric

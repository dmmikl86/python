__author__ = 'mdmytiaha'
# SimpleGUI program template

# Import the module
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

# Define global variables (program state)
counter = 0

# Define "helper" functions
def increment():
	global counter
	counter += 1


# Define event handler functions
def on_tick():
	increment()
	print counter


def on_button():
	global counter
	counter = 0
	print counter

# Create a frame
frame = simplegui.create_frame('SimpleGUI', 100, 100)

# Register event handlers
timer = simplegui.create_timer(1000, on_tick)
frame.add_button('click me!', on_button)

# Start frame and timers
timer.start()
frame.start()
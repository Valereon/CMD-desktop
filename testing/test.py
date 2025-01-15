import curses
import time
from pynput import mouse


mousePressed = False


def main(stdscr):
    global mousePressed
    # Initial setup
    curses.curs_set(0)  # Hide the cursor
    stdscr.nodelay(1)   # Non-blocking mode
    curses.mousemask(curses.ALL_MOUSE_EVENTS | curses.REPORT_MOUSE_POSITION)
    print('\033[?1003h')

    # Tracking mouse position and button state
    mx, my = 0, 0
    button_held = False

    while True:
        stdscr.clear()
        stdscr.addstr(0, 0, "Hold down left mouse button and move the mouse.")
        stdscr.addstr(1, 0, f"Mouse position: X={mx}, Y={my}")
        stdscr.addstr(2, 0, f"Button held: {mousePressed}")

        # Check for mouse or keyboard events
        key = stdscr.getch()

        if key == curses.KEY_MOUSE:
            _, new_mx, new_my, _, bstate = curses.getmouse() 
            mx, my = new_mx, new_my
            # Update the position only if the button is held
            if bstate & curses.BUTTON1_PRESSED:
                button_held = True
                
            elif bstate & curses.BUTTON1_RELEASED:
                button_held = False
            elif bstate & curses.BUTTON1_DOUBLE_CLICKED:
                pass

        # Exit the loop if any key is pressed other than mouse events
        if key != -1 and key != curses.KEY_MOUSE:
            break

        stdscr.refresh()
        time.sleep(0.01)  # Small delay for smoother refresh

# Start the curses application

 
 
def on_click(x, y, button, pressed):
    global mousePressed
    mousePressed = pressed
        
 
 
 
with mouse.Listener(on_click=on_click) as listener:
    curses.wrapper(main)
    
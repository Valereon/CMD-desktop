import unittest
from unittest.mock import patch, MagicMock
import curses
from test_copy import main

class TestMainFunction(unittest.TestCase):
    @patch('curses.wrapper')
    def test_mouse_press_and_release(self, mock_wrapper):
        # Mock the curses standard screen
        stdscr = MagicMock()
        mock_wrapper.side_effect = lambda func: func(stdscr)
        
        # Mock the curses functions and constants
        stdscr.getch.side_effect = [curses.KEY_MOUSE, curses.KEY_MOUSE, -1]
        curses.getmouse.side_effect = [
            (0, 10, 10, 0, curses.BUTTON1_PRESSED),
            (0, 15, 15, 0, curses.BUTTON1_RELEASED)
        ]
        
        # Run the main function
        main(stdscr)
        
        # Check if the mouse position and button state were updated correctly
        stdscr.addstr.assert_any_call(1, 0, "Mouse position: X=10, Y=10")
        stdscr.addstr.assert_any_call(2, 0, "Button held: True")
        stdscr.addstr.assert_any_call(1, 0, "Mouse position: X=15, Y=15")
        stdscr.addstr.assert_any_call(2, 0, "Button held: False")

    @patch('curses.wrapper')
    def test_mouse_double_click(self, mock_wrapper):
        # Mock the curses standard screen
        stdscr = MagicMock()
        mock_wrapper.side_effect = lambda func: func(stdscr)
        
        # Mock the curses functions and constants
        stdscr.getch.side_effect = [curses.KEY_MOUSE, -1]
        curses.getmouse.side_effect = [
            (0, 10, 10, 0, curses.BUTTON1_DOUBLE_CLICKED)
        ]
        
        # Run the main function
        main(stdscr)
        
        # Check if the double click was handled (no change in button state)
        stdscr.addstr.assert_any_call(1, 0, "Mouse position: X=10, Y=10")
        stdscr.addstr.assert_any_call(2, 0, "Button held: False")

if __name__ == '__main__':
    unittest.main()
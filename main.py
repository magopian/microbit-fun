from microbit import *


# Seems "importlib.import_module" doesn't exist on micropython. Thus this hack.
def mood():
    import mood


def rain():
    import rain


CHOICES = {
    "Mood": mood,
    "Rain": rain,
}

while True:
    if button_a.was_pressed():
        CHOICES["Mood"]()
    elif button_b.was_pressed():
        CHOICES["Rain"]()

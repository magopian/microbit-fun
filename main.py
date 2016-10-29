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

while True:  # Outer loop: keep cycling between choices.
    for choice, import_function in CHOICES.items():
        display.scroll(choice, wait=False, loop=True)
        # Inner loop: keep scrolling current choice.
        a_pressed = button_a.was_pressed()
        b_pressed = button_b.was_pressed()
        while not a_pressed and not b_pressed:
            # sleep(100)
            a_pressed = button_a.was_pressed()
            b_pressed = button_b.was_pressed()

        if a_pressed:  # Skip this demo, display the next choice.
            continue
        elif b_pressed:  # Choose this demo, run it.
            import_function()

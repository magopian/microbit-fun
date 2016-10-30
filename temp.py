from microbit import *


NUMBERS = {
    '0': ['09900',
          '90090',
          '90090',
          '90090',
          '09900',
    ],
    '1': ['00900',
          '09900',
          '00900',
          '00900',
          '09990',
    ],
    '2': ['09900',
          '90090',
          '00900',
          '09000',
          '99990',
    ],
    '3': ['99900',
          '00090',
          '09900',
          '00090',
          '99900',
    ],
    '4': ['00900',
          '09900',
          '90900',
          '99990',
          '00900',
    ],
    '5': ['99990',
          '90000',
          '99900',
          '00090',
          '99900',
    ],
    '6': ['09900',
          '90000',
          '99900',
          '90090',
          '09900',
    ],
    '7': ['99990',
          '00090',
          '09900',
          '09000',
          '90000',
    ],
    '8': ['09900',
          '90090',
          '09900',
          '90090',
          '09900',
    ],
    '9': ['09900',
          '90090',
          '09990',
          '00090',
          '09900',
    ],
}


def image_from_number(number):
    """Return an image composed of all the digits of a number."""
    # Build a list of the "pixel arrays" for each digit.
    digits_pixels = [NUMBERS[digit] for digit in number]
    # Group all the first lines, then second lines, then third...
    grouped_lines = zip(*digits_pixels)
    # Make a single line of each group of lines.
    lines = [''.join(lines) for lines in grouped_lines]
    # Join al the lines together into an image.
    return Image(':'.join(lines))


def zigzag(img):
    """Scroll a large image left then right to display all of it."""
    num_images = img.width() // 5
    # If there's two digits, we want to scroll by 5 pixels, not 10.
    pixels_to_scroll = (num_images - 1) * 5
    for i in range(pixels_to_scroll + 1):
        display.show(img.shift_left(i))
        sleep(200)
    sleep(200)
    for i in range(pixels_to_scroll, -1, -1):
        display.show(img.shift_left(i))
        sleep(200)
    sleep(200)


while True:
    temp = str(temperature())
    img = image_from_number(temp)
    zigzag(img)

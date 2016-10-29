# Having fun with the BBC micro:bit

This python code in this repository can be compiled to a .hex file using the
[mu editor](http://codewith.mu/) or the
[python microbit online editor](http://python.microbit.org/editor.html).

Connecting your [BBC micro:bit](https://www.microbit.org/) to your computer
using a USB cable will make it appear as a USB mass storage (just as a standard
USB key).

Once you have the .hex file, copy it to the "folder", the led at the back of
the board will blink rapidly while it's flashing it. Once it's done flashing,
everything is ready to enjoy ;)


## Flash from the command line

Say you have created a
[python virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/)
and installed the requirements using:

```
pip install -r requirements.txt
```

You can now flash your python script from the command line:

```
uflash <your_script_name>.py
```

It will (try to) autodetect your micro:bit. If it can't, then specify the path
to its volume (eg `/Volumes/MICROBIT/<some_file_name>.hex`):

```
uflash <your_script_name>.py /Volumes/MICROBIT/<some_file_name>.hex
```


## Use the "main.py" loader

This is a very useful trick:
[mainly main.py](https://microbit-micropython.readthedocs.io/en/latest/tutorials/storage.html#mainly-main-py).

This allows the use of "proper python modules" by uploading a `main.py` file on
the micro:bit filesystem, which will be run on each reset. The prerequisite is
to have an "empty micropython runtime" flashed on the device:

```
uflash
```

Not providing a script will flash the "empty micropython runtime", which will
allow for the use of the `main.py` file you put on the filesystem:

```
ufs put main.py
```

Using `ufs ls` should list the existing files on the filesystem (be careful,
those will all be erased whenever you re-flash your device using `uflash`!).

From now on, and until the next re-flash, whatever is in the `main.py` will be
automatically run on each device reset.

Changing the `main.py` file is MUCH faster than re-flashing the device, and
allows for a much tighter feedback loop (and we all love that).

You can now add the files you want to be run using `ufs put`, and the `main.py`
loader will allow you to choose which one you want to run:
- press the `A` (left) button to cycle through the different modules
- press the `B` (right) button to run the current module

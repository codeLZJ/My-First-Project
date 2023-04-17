"""
File: DoubleBeepers.py
Name:LZJ
-------------------------------
TODO:
"""

from karel.stanfordkarel import *


def main():
    """
    Karel will double the beepers
    """
    move()
    double_beepers()
    put_beepers_back()
    karel_goes_home()


def double_beepers():
    while on_beeper():
        # old beepers, facing East
        pick_beeper()
        move()
        put_beeper()
        put_beeper()
        # new beepers, facing West
        turn_around()
        move()
        turn_around()


def turn_around():
    turn_left()
    turn_left()


def put_beepers_back():
    while on_beeper():
        pick_beeper()
        move()
        put_beeper()
        put_beeper()


def karel_goes_home():
    turn_around()
    move()
    turn_around()


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)

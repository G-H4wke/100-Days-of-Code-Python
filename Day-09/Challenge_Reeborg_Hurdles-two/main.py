# https://www.reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json#
# The code below was to practice functions with reeborg and will not run as a stand-alone file.
# You can use this code within the link posted above!
from library import *


# Reach the Goal
while at_goal() == False:
    if wall_in_front() == True:
        jump_hurdle()
    else:
        move()


################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
def turn_around():
    turn_left()
    turn_left()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump_hurdle():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

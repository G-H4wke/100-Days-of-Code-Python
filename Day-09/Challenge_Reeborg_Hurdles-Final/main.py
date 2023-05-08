# https://www.reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json#
# The code below was to practice functions with reeborg and will not run as a stand-alone file.
# You can use this code within the link posted above!
from library import *

# Reach the Goal
while at_goal() == False:
    if wall_in_front() and is_facing_north():
        jump_hurdle()
    elif wall_in_front() and not is_facing_north():
        turn_left()
    elif not wall_in_front():
        while wall_on_right() and not wall_in_front():
            move()
            if right_is_clear():
                jump_hurdle()
            elif at_goal():
                done()


################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump_hurdle():
    turn_right()
    move()
    turn_right()
    move()

# https://www.reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json#
# The code below was to practice functions with reeborg and will not run as a stand-alone file.
# You can use this code within the link posted above!
def turn_right():
    turn_left()
    turn_left()
    turn_left()


while front_is_clear():
    move()
turn_left()

while not at_goal():
    while wall_on_right():
        if front_is_clear():
            move()
            if at_goal():
                done()
        if wall_in_front() and wall_on_right():
            turn_left()
    if wall_in_front() and wall_on_right():
        turn_right()
    elif wall_in_front() and not wall_on_right():
        turn_right()
    elif front_is_clear() and right_is_clear():
        turn_right()
    if not wall_in_front():
        move()

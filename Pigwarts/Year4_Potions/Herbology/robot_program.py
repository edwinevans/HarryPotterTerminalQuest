from robot import Robot


# |  |
# |  |
# |--|
#
# |  |
# |  |
# |--|
#
# |~~|
# |~~|
# |--|
#
# |  |
# |~~|
# |--|

robot = Robot()

# robot.pot_needs_more_water()
# robot.add_water()
# robot.move_right() # Returns False if no more pots
# robot.went_past_last_pot


# def fill_current_pot():
#     while robot.pot_needs_more_water():
#         robot.add_water()
#

# while not robot.went_past_last_pot():
#     while robot.pot_needs_more_water():
#         robot.add_water()
#     robot.move_right()

while not robot.went_past_last_pot():
    while robot.pot_needs_more_water():
        robot.add_water()
    robot.move_right()
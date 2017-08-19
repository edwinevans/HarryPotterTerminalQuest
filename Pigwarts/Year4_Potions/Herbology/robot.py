

class Robot:
    def __init__(self):
        self.pots = []
        self.max_pot_level = 2
        self.current_pot = 0
        self.pots.append({"level": 0})
        self.pots.append({"level": 0})
        self.pots.append({"level": 2})
        self.pots.append({"level": 1})
        self.show_garden()

    def show_garden(self):
        print "---"
        for pot in self.pots:
            print pot
        print "---"
        print ""

    def move_right(self):
        print "Move right"
        # if self.current_pot == len(self.pots) - 1:
        #     return False
        self.current_pot += 1
        self.show_garden()
        return True

    def add_water(self):
        print "Add water"
        self.pots[self.current_pot]["level"] += 1
        if self.pots[self.current_pot]["level"] > self.max_pot_level:
            raise Exception("Oh no! You overfilled the pot!!")
        self.show_garden()

    def pot_needs_more_water(self):
        level = self.pots[self.current_pot]["level"]
        return level != self.max_pot_level


    def went_past_last_pot(self):
        return self.current_pot == len(self.pots)

# while True:
#     while not robot.is_current_pot_full():
#         robot.add_water()
#     if not robot.move_right():
#         break

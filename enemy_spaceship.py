

class EnemySpaceships:
    def __init__(self, create_turtle):
        self.SHIP_SPEED = 1
        self.create_turtle = create_turtle
        self.xcors = [-125, -100, -75, -50, -25, 0, 25, 50, 75, 100, 125]
        self.ycors = [250, 225, 200]
        self.spaceships = self.create_spaceships()
        self.move_right = True
        self.reinforcements_arrived = False
        self.times_refreshed = 0

    def create_spaceships(self):
        ships = []
        for ycor in self.ycors:
            for xcor in self.xcors:
                ship = self.create_turtle(shape="triangle", color="purple", xy=(xcor, ycor), angle=270)
                ships.append(ship)
        return ships

    def move_spaceships(self, speed):
        for ship in self.spaceships:
            ship.setx(ship.xcor() + speed)

    def conditional_move(self, condition1, speed, condition2, should_move_right):
        if condition1:
            self.move_spaceships(speed)
            if condition2:
                self.move_right = should_move_right

    def area_is_valid(self):
        is_valid = [True if ship.xcor() > -250 else False for ship in self.spaceships]
        is_valid2 = [True if ship.xcor() < 250 else False for ship in self.spaceships]
        return [is_valid, is_valid2]

    def auto_move(self):
        try:
            self.conditional_move(self.move_right, -self.SHIP_SPEED, False in self.area_is_valid()[0], False)
            self.conditional_move(not self.move_right, self.SHIP_SPEED, False in self.area_is_valid()[1], True)
        except IndexError:
            pass

    def refresh_enemies(self):
        if len(self.spaceships) == 0:
            self.times_refreshed += 1
            self.ycors = [num - 40 for num in self.ycors]
            reinforcements = self.create_spaceships()
            self.spaceships.extend(reinforcements)
            self.reinforcements_arrived = True



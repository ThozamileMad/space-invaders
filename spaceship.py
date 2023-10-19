
class Spaceship:
    def __init__(self, create_turtle):
        self.SHIP_SPEED = 15
        self.ship = create_turtle(shape="arrow", color="green", xy=(0, -190), angle=90)

    def move_right(self):
        ship_xcor = self.ship.xcor()
        if ship_xcor < 250:
            self.ship.setx(ship_xcor + self.SHIP_SPEED)

    def move_left(self):
        ship_xcor = self.ship.xcor()
        if ship_xcor > -250:
            self.ship.setx(ship_xcor - self.SHIP_SPEED)

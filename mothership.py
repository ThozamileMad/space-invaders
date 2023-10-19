import random


class Mothership:
    def __init__(self, create_turtle):
        self.MOTHERSHIP_SPEED = 1
        self.motherships = [create_turtle(shape="square", color="purple", xy=(10000, 280), angle=0, change_size=True, size=1.2, length=3)]
        self.coordinates = (-230, 230)
        self.xcor = random.choice(self.coordinates)
        self.gone = True

    def conditional_mobility(self, xcor_value, speed, condition, create_turtle):
        ship = self.motherships[-1]
        if self.xcor == xcor_value:
            ship.setx(ship.xcor() + speed)
            if condition:
                ship.hideturtle()
                self.motherships.append(create_turtle(shape="square", color="purple", xy=(10000, 280), angle=0, change_size=True, size=1.2, length=3))
                self.gone = True

    def auto_move(self, create_turtle):
        ship = self.motherships[-1]
        if self.gone and random.randint(1, 1000) == 10:
            self.xcor = random.choice(self.coordinates)
            ship.goto(self.xcor, 280)
            self.gone = False

        self.conditional_mobility(230, -self.MOTHERSHIP_SPEED, ship.xcor() < -300, create_turtle)
        self.conditional_mobility(-230, self.MOTHERSHIP_SPEED, ship.xcor() > 300, create_turtle)





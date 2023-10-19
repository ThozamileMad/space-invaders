
class Stats:
    def __init__(self, create_turtle):
        self.create_turtle = create_turtle
        create_turtle(angle=180, size=0.1, length=26, xy=(0, -200), color="green", change_size=True, change_shape=True, shape="square")
        self.lives = [create_turtle(shape="arrow", angle=90, xy=(x, -220), color="green") for x in [-250, -220, -190]]
        self.score_text = create_turtle(shape="turtle", angle=180, xy=(205, -220), color="green", write=True, text="Score: 0", text_size=10, show_turtle=False)

    def show_game_over(self, times_refreshed):
        if len(self.lives) == 0 or times_refreshed == 4:
            self.create_turtle(shape="turtle", angle=180, xy=(-70, 0), color="white", write=True, text="Game Over", text_size=25, show_turtle=False)
            return True
        else:
            return False



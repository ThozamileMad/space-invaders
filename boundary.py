
class Cover:
    def __init__(self, create_turtle):
        self.objects = []
        self.create_objects(create_turtle)

    def create_segments(self, create_turtle, *args):
        ycors = [-num for num in range(20, 81, 20)]
        for x in args:
            objects = [create_turtle(shape="square", color="white", xy=(x, num), angle=0) for num in ycors]
            self.objects.extend(objects)

    def create_objects(self, create_turtle):
        xcors = [(-240, -220, -200), (-100, -80, -60), (40, 60, 80), (180, 200, 220)]
        for tup in xcors:
            self.create_segments(create_turtle, tup[0], tup[1], tup[2])





from turtle import *
from spaceship import Spaceship
from turrent import Missile
from time import sleep
from enemy_spaceship import EnemySpaceships
from stats import Stats
from boundary import Cover
from mothership import Mothership


def create_turtle(change_size=False, write=False, change_shape=False, show_turtle=True, **kwargs):
    if change_shape:
        turtle = Turtle(shape=kwargs["shape"])
    else:
        turtle = Turtle(shape=kwargs["shape"])

    turtle.hideturtle()
    turtle.penup()
    turtle.setheading(kwargs["angle"])
    turtle.goto(kwargs["xy"][0], kwargs["xy"][1])
    turtle.color(kwargs["color"])

    if change_size:
        turtle.shapesize(kwargs["size"], stretch_len=kwargs["length"])
    if write:
        turtle.write(kwargs["text"], font=("Impact", kwargs["text_size"], ""))
    if show_turtle:
        turtle.showturtle()

    return turtle


screen = Screen()
screen.bgcolor("black")
screen.setup(1000, 600)
screen.title("Space Invaders")
screen.tracer(0, 0)

spaceship = Spaceship(create_turtle)
ship = spaceship.ship

screen.onkey(spaceship.move_right, "s")
screen.onkey(spaceship.move_left, "a")

enemy_spaceships = EnemySpaceships(create_turtle)

stats = Stats(create_turtle)

cover = Cover(create_turtle)

mothership = Mothership(create_turtle)

missile = Missile(create_turtle, enemy_spaceships, spaceship, stats, cover, mothership)
screen.onkey(lambda: missile.create_missile(len(missile.player_missiles) < missile.PLAYER_AMMO_CAPACITY,
                                            "green",
                                            90,
                                            ship.xcor(),
                                            ship.ycor(),
                                            10,
                                            missile.player_missiles), "space")
screen.listen()

game_over = False
while not game_over:
    sleep(0.01)
    screen.update()
    if stats.show_game_over(enemy_spaceships.times_refreshed):
        game_over = True

    enemy_spaceships.auto_move()
    mothership.auto_move(create_turtle)
    missile.fire_player_missiles()
    missile.fire_enemy_missiles()
    missile.destroy_enemy()
    missile.destroy_player()
    missile.destroy_cover()
    missile.destroy_mothership()
    missile.missile_collision()
    missile.speed_up_enemy_missiles()
    enemy_spaceships.refresh_enemies()
    missile.enemies_updated()

screen.exitonclick()

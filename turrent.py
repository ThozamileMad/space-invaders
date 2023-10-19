from random import randint
from time import sleep


class Missile:
    def __init__(self, create_turtle, enemy_spaceships, player_spaceship, stats, cover, mothership):
        self.ENEMY_FIRING_RATE = 2500
        self.PLAYER_AMMO_CAPACITY = 5
        self.PLAYER_MISSILE_SPEED = 4
        self.ENEMY_MISSILE_SPEED = 4
        self.create_turtle = create_turtle
        self.enemy_ships = enemy_spaceships.spaceships
        self.player_ship = player_spaceship.ship
        self.player_missiles = []
        self.enemy_missiles = []
        self.number_of_enemy_ships = len(self.enemy_ships)
        self.player_lives = stats.lives
        self.score = 0
        self.score_text = stats.score_text
        self.enemy_spaceships_class = enemy_spaceships
        self.cover_class = cover
        self.mothership_class = mothership
        self.mothership_destroyed = False

    def create_missile(self, condition, color, angle, xcor, ycor, ycor_add_subtract, lst):
        if condition:
            missile = self.create_turtle(shape="square", color=color, xy=(xcor, ycor + ycor_add_subtract), angle=angle, change_size=True, size=0.1, length=0.6)
            lst.append(missile)

    def fire_player_missiles(self):
        for missile in self.player_missiles:
            if missile.ycor() < 300:
                missile.forward(self.PLAYER_MISSILE_SPEED)
                
                if missile.ycor() > -187:
                    missile.showturtle()
            else:
                self.move_away(missile, self.player_missiles)
        
    def fire_enemy_missiles(self):
        enemy_xycor = [(enemy.xcor(), enemy.ycor()) for enemy in self.enemy_ships]

        for coordinates in enemy_xycor:
            rand_num = randint(1, self.ENEMY_FIRING_RATE)
            if rand_num == 5:
                self.create_missile(True, "purple", 270, coordinates[0], coordinates[1], -10, self.enemy_missiles)

        for missile in self.enemy_missiles:
            if missile.ycor() > -192:
                missile.forward(self.ENEMY_MISSILE_SPEED)
                missile.showturtle()
            else:
                self.move_away(missile, self.enemy_missiles)

    def move_away(self, turtle, lst):
        turtle.hideturtle()
        turtle.goto(10000, 10000)
        if type(lst) == list:
            lst.remove(turtle)

    def destroy_enemy(self):
        for missile in self.player_missiles:
            for enemy in self.enemy_ships:
                if missile.distance(enemy) < 20:
                    self.move_away(enemy, self.enemy_ships)
                    try:
                        self.move_away(missile, self.player_missiles)
                    except ValueError:
                        pass
                    self.score += 5
                    self.score_text.clear()
                    self.score_text.write(f"Score: {self.score}", font=("Impact", 10, ""))

    def destroy_player(self):
        for missile in self.enemy_missiles:
            if self.player_ship.distance(missile) < 20:
                self.move_away(self.player_ship, None)
                self.move_away(missile, self.enemy_missiles)
                self.move_away(self.player_lives[-1], self.player_lives)
                sleep(0.5)
                if len(self.player_lives) > 0:
                    self.player_ship.goto(0, -190)
                    self.player_ship.showturtle()

    def destroy_mothership(self):
        mothership = self.mothership_class.motherships[-1]
        for missile in self.player_missiles:
            if mothership.distance(missile) < 30:
                self.move_away(mothership, self.mothership_class.motherships)
                self.move_away(missile, self.player_missiles)
                self.mothership_class.motherships.append(self.create_turtle(shape="square", color="purple", xy=(10000, 280), angle=0, change_size=True, size=1.2, length=3))
                self.mothership_class.gone = True
                self.mothership_destroyed = True
                self.ENEMY_FIRING_RATE = 2500 - 2450
                self.ENEMY_MISSILE_SPEED += 2
                self.PLAYER_MISSILE_SPEED = 50/100 * self.ENEMY_MISSILE_SPEED

    def missile_collision(self):
        for enemy_missile in self.enemy_missiles:
            for player_missile in self.player_missiles:
                if enemy_missile.distance(player_missile) < 10:
                    self.move_away(enemy_missile, self.enemy_missiles)
                    self.move_away(player_missile, self.player_missiles)

    def speed_up_enemy_missiles(self):
        current_number_of_ships = len(self.enemy_ships)
        if current_number_of_ships < self.number_of_enemy_ships and not self.mothership_destroyed:
            number_of_destroyed_ships = self.number_of_enemy_ships - current_number_of_ships
            enhance_speed_by = 0.2 * number_of_destroyed_ships
            self.ENEMY_MISSILE_SPEED += enhance_speed_by
            self.number_of_enemy_ships = current_number_of_ships
            if self.number_of_enemy_ships == 22:
                self.ENEMY_FIRING_RATE -= 2100
            elif self.number_of_enemy_ships == 11:
                self.ENEMY_FIRING_RATE -= 250
            elif self.number_of_enemy_ships == 7:
                self.ENEMY_FIRING_RATE -= 100

    def missile_cover_collision(self, lst, object):
        for missile in lst:
            if object.distance(missile) < 20:
                self.move_away(object, self.cover_class.objects)
                self.move_away(missile, lst)

    def destroy_cover(self):
        for square in self.cover_class.objects:
            self.missile_cover_collision(self.enemy_missiles, square)
            self.missile_cover_collision(self.player_missiles, square)

    def enemies_updated(self):
        if self.enemy_spaceships_class.reinforcements_arrived:
            self.ENEMY_FIRING_RATE = 2500
            self.ENEMY_MISSILE_SPEED = 2
            self.PLAYER_MISSILE_SPEED = 2.5
            self.enemy_spaceships_class.reinforcements_arrived = False
            self.number_of_enemy_ships = len(self.enemy_ships)
            self.cover_class.create_objects(self.create_turtle)
            self.mothership_destroyed = False











                        
                        
                    
                    

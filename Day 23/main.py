import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Frogger... only, with a turtle... (and you can only move forwards)")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

car_speed = 1

screen.listen()
screen.onkey(key = "Up", fun=player.go_up)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    car_manager.create_car()
    car_manager.move_cars(car_speed)

    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect successful crossing of road
    if player.is_at_finish_line():
        player.reset()
        car_manager.level_up()
        scoreboard.increase_level()




screen.exitonclick()
# Etch-A-Sketch
# from turtle import Turtle, Screen
#
# tim = Turtle()
#
# screen = Screen()
#
# def move_forwards():
#     tim.forward(10)
#
# def move_backwards():
#     tim.backward(10)
#
# def turn_left():
#     tim.left(10)
#
# def turn_right():
#     tim.right(10)
#
# def move_home():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
#
# screen.listen()
# screen.onkey(key = "w", fun=move_forwards)
# screen.onkey(key = "s", fun=move_backwards)
# screen.onkey(key = "a", fun=turn_left)
# screen.onkey(key = "d", fun=turn_right)
# screen.onkey(key = "c", fun=move_home)
# screen.exitonclick()
# End

from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="MAke your bet", prompt="Which turtle will win the race?  Enter a color: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
names = ["Raphael", "Mikey", "April", "Bob", "Leo", "Donnie"]
racers = []

y = -100
index = 0

for _ in names:
    _ = Turtle(shape = "turtle")
    _.color(colors[index])
    racers.append(_)
    _.penup()
    _.goto(-230, y)
    y += 50
    index += 1

if user_bet:
    is_race_on = True
else: is_race_on = False

while is_race_on:

    for racer in racers:

        if racer.xcor() > 230:
            is_race_on = False
            winning_color = racer.pencolor()
            if winning_color == user_bet:
                print(f"You won!  The {winning_color} turtle is the winner!")
            else: print(f"You lost!  The {winning_color} turtle is the winner!")

        random_distance = random.randint(0, 10)
        racer.forward(random_distance)
screen.exitonclick()

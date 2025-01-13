import turtle
from turtle import Turtle, Screen
tim = Turtle()
import random

turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

def crlf():
    tim.left(90)
    tim.penup()
    tim.forward(25)
    tim.left(90)
    tim.forward(500)
    tim.right(90)
    tim.forward(25)
    tim.right(90)

color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19)]

for _ in range(10):
    for _ in range(10):
        tim.color(random_color())
        tim.hideturtle()
        tim.dot(20)
        tim.penup()
        tim.forward(50)
    crlf()

screen = Screen()
screen.exitonclick()

# angle = [0, 90, 180, 270, 360]

# Kewl shape thing in lecture
# def draw(num_sides):
#     angle = 360 / num_sides
#     for _ in range(0, num_sides):
#         tim.right(angle)
#         tim.forward(100)
#
# for _ in range(3, 11):
#     tim.color(random.choice(colours))
#     draw(_)

# Random Walk from lecture
# turtle.colormode(255)
#
# tim.width(10)
# tim.speed(10)
#
# while True:
#     tim.color(random_color())
#     tim.forward(random.choice(range(20, 50)))
#     tim.right(random.choice(angle))
#     screen = Screen()
# screen.exitonclick()

# Spirograph
# tim.speed("fastest")
#
# for _ in range(72):
#     tim.color(random_color())
#     tim.circle(100)
#     current_heading = tim.heading()
#     tim.setheading(current_heading + 5)
# screen = Screen()
# screen.exitonclick()



# import heroes
# print(heroes.gen())
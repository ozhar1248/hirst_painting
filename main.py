from turtle import Turtle, Screen
import colors_picking
import random

me = Turtle()
screen = Screen()

STARTING_POINT_X = -300
STARTING_POINT_Y = -300
DOTS = 10
RADIUS = 10
GAP = 50
COLORMODE = 255

screen.colormode(COLORMODE)
me.penup()
me.speed(0)

for row in range(0, DOTS):
    me.setposition(STARTING_POINT_X, STARTING_POINT_Y+row*(RADIUS*2+GAP))
    for col in range(0, DOTS):
        color = random.choice(colors_picking.rgb_colors)
        me.fillcolor(color)
        me.pencolor(color)
        me.setheading(0)
        me.pendown()
        me.begin_fill()
        me.circle(RADIUS)
        me.end_fill()
        me.penup()
        me.forward(RADIUS*2+GAP)

screen.exitonclick()



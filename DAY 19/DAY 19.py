from turtle import Turtle, Screen
import random
tim = Turtle()
screen = Screen()

#
# def move_forward():
#     tim.forward(10)
#
# def move_backward():
#     tim.backward(10)
#
# def counter_clock():
#    tim.setheading(tim.heading()+5)
#
# def clock_wise():
#     tim.setheading(tim.heading() - 5)
#
# screen.listen()
# screen.onkey(key="w",fun = move_forward )
# screen.onkey(key="s",fun = move_backward )
# screen.onkey(key="a",fun = counter_clock )
# screen.onkey(key="d",fun = clock_wise )
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet" ,prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange" , "yellow", "green" , "blue" , "purple"]


num = []
for i in range (6):
    num.append(Turtle(shape="turtle"))
y_cord = -100
value = 0

for turtle in num:
    print(value)
    turtle.speed("fastest")
    turtle.color(colors[value])
    turtle.penup()
    y_cord +=  30
    turtle.goto(x=-230, y = y_cord)
    value += 1



screen.exitonclick()



import turtle as t
import random

tim = t.Turtle()
tim.shape("turtle")
tim.color("red")
t.colormode(255)

def random_color():
     r = random.randint(0, 255)
     g = random.randint(0, 255)
     b = random.randint(0, 255)
     random_color =(r, g, b)
     return random_color

# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# def draw_shape(num_sides):
#     angles = 360 / num_sides
#     for x in range(num_sides):
#         tim.forward(100)
#         tim.right(angles)
#
# for x in range(3,11):
#     tim.color(random.choices(colours))
#     draw_shape(x)
#
#

#randomly changing direction and moving 10 spaces
# def forward():
#     tim.forward(10)
#
# def right():
#     tim.right(90)
#     tim.forward(10)
#
# def left():
#     tim.left(90)
#     tim.forward(10)
#
# def backward():
#     tim.backward(10)
#
#
#
#
#
# # movement = [forward(),backward(),left(),right()]
#
# # action = random.choice(movement)
# tim.pensize(5)
# for x in range(100):
#     tim.color(random_color())
#     number = random.randint(1,4)
#     if number == 1:
#         forward()
#     elif number == 2:
#         backward()
#     elif number == 3:
#         left()
#     elif number ==4:
#         right()

# direction = [0, 90, 180, 270]
# tim.pensize(15)
# tim.speed("fastest")

# for _ in range (200):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(direction))

# tim.circle(50)
# tim.setheading(20)
# tim.circle(50)

tim.speed("fastest")
angle = 20
for _ in range (50):
    tim.color(random_color())
    tim.circle(50)
    angle = angle + 10
    tim.setheading(angle)



screen = t.Screen()
screen.exitonclick()

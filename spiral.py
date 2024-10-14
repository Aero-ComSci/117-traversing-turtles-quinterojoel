#   a117_traversing_turtles.py

import turtle as trtl

my_turtles = []

turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic", "arrow", "turtle", "circle", "square", "triangle", "classic", "arrow", "turtle", "circle", "square", "triangle", "classic", "arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold", "red", "blue", "green", "orange", "purple", "gold", "red", "blue", "green", "orange", "purple", "gold", "red", "blue", "green", "orange", "purple", "gold"]

for s in turtle_shapes:
    t = trtl.Turtle(shape=s)
    my_turtles.append(t)
    t.speed(0)

startx = 0
starty = 0
lastangle = 0
spiral = 30
spiralthing = 0

for t in my_turtles:
    if spiralthing == 6:
        spiral -= 5
    if spiralthing == 12:
        spiral -= 5
    if spiralthing == 18:
        spiral -= 5
    new_color = turtle_colors.pop()
    t.fillcolor(new_color)
    t.color(new_color)
    t.penup()
    t.goto(startx, starty)
    t.setheading(lastangle)
    t.pendown()
    t.forward(50)
    startx = t.xcor()
    starty = t.ycor()
    lastangle -= spiral
    spiralthing += 1

wn = trtl.Screen()
wn.mainloop()

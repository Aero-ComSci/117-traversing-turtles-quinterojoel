#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]

for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  my_turtles.append(t)

#makes all turtles start at origin
startx = 0
starty = 0
lastangle = 0

#makes all turtles move to the current coords, one by one
for t in my_turtles:
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
  lastangle -= 45


#change coords every time a turtle moves, so they don't all move to the same place

wn = trtl.Screen()
wn.mainloop()

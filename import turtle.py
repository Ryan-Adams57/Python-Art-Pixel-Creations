import turtle

# Setup screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create turtle
t = turtle.Turtle()
t.speed(0)
t.width(2)

# Rainbow colors
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

# Draw spiral rainbow
for i in range(300):
    t.pencolor(colors[i % 7])   # cycle through colors
    t.forward(i * 2)            # increase length
    t.right(59)                 # angle creates spiral effect

t.hideturtle()
turtle.done()

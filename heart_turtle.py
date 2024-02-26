import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create the turtle object
pen = turtle.Turtle()
pen.color("red")
pen.fillcolor("red")

# Start filling the heart
pen.begin_fill()

# Draw the left curve
pen.left(50)
pen.forward(100)
pen.circle(-38, 120)
pen.left(140) 

# Draw the right curve
pen.circle(-38, 120)
pen.forward(100)

# Finish filling the heart
pen.end_fill()

# Hide the turtle
pen.hideturtle()

# Keep the window open
turtle.done()

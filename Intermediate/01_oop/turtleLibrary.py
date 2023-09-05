# turtle library: https://docs.python.org/3.11/library/turtle.html


import another_module
print(another_module.another_variable)

from turtle import Turtle, Screen

# construct object
jimmy = Turtle()
print(jimmy)
jimmy.shape("turtle")
jimmy.color("coral")
jimmy.forward(100)

myScreen = Screen()
print(myScreen.canvheight)

myScreen.exitonclick()
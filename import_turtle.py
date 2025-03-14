# import turtle
#
# turtle.pendown()
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.done()

# import turtle
from turtle import *
from math import radians, cos


def square(length: int) -> None:
    """Draw a square of length"""
    inner_forward = forward
    inner_right = right
    for side in range(4):
        # turtle.forward(length)
        inner_forward(length)
        # turtle.right(90)
        inner_right(90)
        print(dir())
        print(f"Inside square function, namespace is {dir()}")


def encircled_square(length: int) -> None:
    """Draw a square of length which is enclosed then
    in a circle """
    square(length)
    angle = radians(45)
    radius = length * cos(angle)
    right(135)
    # turtle.right(135)
    circle(radius)
    # turtle.circle(radius)
    print(f"Inside encircled_square function, namespace is {dir()}")
    print(f"locals: {locals()}")


# encircled_square(300)
# turtle.speed("fast")
speed("fast")
Screen().tracer(0)  # disable turtle animation
for s in range(72):
    encircled_square(120)
    left(5)
    # turtle.left(5)
Screen().update()  # Update the Screen
done()
# turtle.done()

print(dir())
g = globals()
print(g["square"])
print(g)

print(dir(__builtins__))

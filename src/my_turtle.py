import turtle

my_turtle = turtle.Turtle()
my_turtle.speed(0)


def square(length, angle):
    my_turtle.forward(length)
    my_turtle.right(angle)
    my_turtle.forward(length)
    my_turtle.right(angle)
    my_turtle.forward(length)
    my_turtle.right(angle)
    my_turtle.forward(length)

def turn_right(length, angle):
    my_turtle.forward(length)
    my_turtle.right(angle)


def circle_of_squares(length, angle):
    for i in range(4):
        turn_right(length, angle)

for i in range(100):
    circle_of_squares(150, 90)
    my_turtle.right(11)
    
#square(150, 45)
#square(100, 30)

import turtle


def draw_diamond(some_turtle):
    for i in range(0, 2):
        some_turtle.forward(100)
        some_turtle.right(60)
        some_turtle.forward(100)
        some_turtle.right(120)


def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    brad = turtle.Turtle()
    brad.speed(20)
    brad.shape("turtle")
    for i in range(0,72):
        draw_diamond(brad)
        brad.right(5)
    brad.right(90)
    brad.forward(250)


    window.exitonclick()

draw_art()



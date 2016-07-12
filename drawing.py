import turtle


def draw_square(some_turtle):
    for i in range(0, 4):
        some_turtle.forward(100)
        some_turtle.right(90)


def draw_triangle(some_turtle):
    for u in range(0,3):
        some_turtle.forward(100)
        some_turtle.right(120)


def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    brad = turtle.Turtle()
    for i in range(0,36):
        draw_square(brad)
        brad.right(10)

    #angie = turtle.Turtle()
    #angie.shape("turtle")
    #angie.color("blue")
    #angie.speed(2)

    #angie.circle(100)

    #ammy = turtle.Turtle()
    #ammy.color("green")

    #draw_triangle(ammy)

    window.exitonclick()

draw_art()



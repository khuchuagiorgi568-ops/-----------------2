import turtle

screen = turtle.Screen()
t = turtle.Turtle()
t.speed(9)

def draw_star(size, fill):
    t.color("white")
    t.forward(-(65 - size) / 2)
    t.left(180)

    if fill == 1:
        t.color("purple")
        t.begin_fill()
    else:
        t.color("olive")

    for _ in range(5):
        t.forward(size)
        t.left(144)

    if fill == 1:
        t.end_fill()

    t.left(180)
    t.color("white")
    t.forward((65 - size) / 2)

t.color("white")
t.left(180)
t.forward(175)
t.left(180)
t.left(90)
t.forward(180)
t.left(270)

for row in range(4):
    for col in range(4):
        if row == 0 or row == 2:
            if col == 0 or col == 2:
                draw_star(28, 0)
            else:
                draw_star(65, 1)
        else:
            if col == 0 or col == 2:
                draw_star(65, 1)
            else:
                draw_star(28, 0)

        t.forward(140)

    if row != 3:
        t.left(270)
        t.forward(130)
        t.left(270)
        t.forward(560)
        t.left(180)

turtle.done()

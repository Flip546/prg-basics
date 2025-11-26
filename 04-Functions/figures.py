import turtle

# jeden wspólny żółw dla wszystkich figur
pen = turtle.Turtle()
pen.speed(4)

def draw_square(length):
    for _ in range(4):
        pen.forward(length)
        pen.right(90)

def draw_triangle(length):
    for _ in range(3):
        pen.forward(length)
        pen.left(120)

def draw_rectangle(length_a, length_b):
    for _ in range(2):
        pen.forward(length_a)
        pen.right(90)
        pen.forward(length_b)
        pen.right(90)

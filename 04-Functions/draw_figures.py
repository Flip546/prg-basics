import turtle
from figures import pen, draw_square, draw_triangle, draw_rectangle

# ekran
window = turtle.Screen()
window.bgcolor("lightgreen")

# ===== KWADRATY =====
pen.penup()
pen.goto(-200, 100)   # pierwsze miejsce
pen.pendown()
draw_square(100)

pen.penup()
pen.goto(0, 100)      # drugie miejsce
pen.pendown()
draw_square(60)

# ===== TRÓJKĄTY =====
pen.penup()
pen.goto(-200, -20)
pen.pendown()
draw_triangle(80)

pen.penup()
pen.goto(0, -20)
pen.pendown()
draw_triangle(50)

# ===== PROSTOKĄTY =====
pen.penup()
pen.goto(-200, -150)
pen.pendown()
draw_rectangle(120, 60)

pen.penup()
pen.goto(0, -150)
pen.pendown()
draw_rectangle(80, 40)

pen.hideturtle()
window.mainloop()

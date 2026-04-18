import turtle
from turtle import *
w = turtle.Screen()

tracer(0)
def soleil(n): # Цветок
    color('red', 'yellow')
    while True:
        forward(n)
        left(190)
        if abs(pos()) < 1:
            break


def fan(n):# арнамент
    color('green', 'yellow')
    for i in range(4):
        left(20)
        for j in range(4):
            forward(n)
            left(90)


def square(n):# квадрат
    for i in range(4):
        forward(n)
        left(90)


begin_fill()
soleil(100)
end_fill()
penup()

left(180)
forward(150)

pendown()
begin_fill()
square(100)
end_fill()

penup()
right(90)
forward(170)

pendown()
begin_fill()
fan(100)
end_fill()

w.mainloop()

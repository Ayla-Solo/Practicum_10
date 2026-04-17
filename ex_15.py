import turtle as t
import random

screen = t.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")

t.speed(0)
t.hideturtle()


def draw_star(x, y):
    t.penup()
    t.goto(x, y)
    size = random.randint(1, 3)
    t.dot(size, "white")

def create_sky(star_count):
    width = screen.window_width()
    height = screen.window_height()

    for _ in range(star_count):
        x = random.randint(-width // 2, width // 2)
        y = random.randint(0, height // 2)
        draw_star(x, y)

def draw_lit_window(x, y, width, height):
    if random.random() < 0.6:
        t.penup()
        t.goto(x, y)
        t.pendown()

        t.fillcolor("yellow")
        t.begin_fill()

        for _ in range(2):
            t.forward(width)
            t.left(90)
            t.forward(height)
            t.left(90)

        t.end_fill()

def draw_building(start_x, width, height):
    t.penup()
    t.goto(start_x, -300)
    t.pendown()
    t.color("#202020")
    t.begin_fill()

    t.setheading(90)
    t.forward(height)
    t.setheading(0)
    t.forward(width)
    t.setheading(270)
    t.forward(height)
    t.setheading(180)
    t.forward(width)

    t.end_fill()

    window_w = 10
    window_h = 15
    gap = 5

    curr_y = -300 + gap
    while curr_y < (-300 + height) - window_h:
        curr_x = start_x + gap
        while curr_x < (start_x + width) - window_w:
            draw_lit_window(curr_x, curr_y, window_w, window_h)
            curr_x += window_w + gap
        curr_y += window_h + gap


def draw_cityscape():
    create_sky(150)
    current_x = -400

    while current_x < 400:
        b_width = random.randint(40, 70)
        b_height = random.randint(100, 350)

        draw_building(current_x, b_width, b_height)
        current_x += b_width

draw_cityscape()
t.done()

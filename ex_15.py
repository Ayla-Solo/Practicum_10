import turtle as t
import random


screen = t.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")  # черный фон — ночное небо


t.speed(0)
t.hideturtle()   # скрыть курсор


# рисования одной "звезды"
def draw_star(x, y):
    t.penup()
    t.goto(x, y)                  # перейти в случайную точку
    size = random.randint(1, 3)   # случайный размер звезды
    t.dot(size, "white")          # нарисовать точку


# создания звездного неба
def create_sky(star_count):
    width = screen.window_width()
    height = screen.window_height()

    # Рисуем заданное количество звезд
    for _ in range(star_count):
        x = random.randint(-width // 2, width // 2)  # случайная координата X
        y = random.randint(0, height // 2)           # только верхняя половина экрана
        draw_star(x, y)


# рисование одного окна 
def draw_lit_window(x, y, width, height):
    # С вероятностью 60% окно будет светиться
    if random.random() < 0.6:
        t.penup()
        t.goto(x, y)
        t.pendown()

        t.fillcolor("yellow")  # цвет света в окне
        t.begin_fill()

        # Рисуем прямоугольник окна
        for _ in range(2):
            t.forward(width)
            t.left(90)
            t.forward(height)
            t.left(90)

        t.end_fill()


# Функция рисования одного здания
def draw_building(start_x, width, height):
    t.penup()
    t.goto(start_x, -300)  
    t.pendown()
    t.color("#202020")     
    t.begin_fill()

    # Рисуем прямоугольник здания
    t.setheading(90)
    t.forward(height)
    t.setheading(0)
    t.forward(width)
    t.setheading(270)
    t.forward(height)
    t.setheading(180)
    t.forward(width)

    t.end_fill()

    # Параметры окон
    window_w = 10
    window_h = 15
    gap = 5  # расстояние между окнами

    # Начальная позиция для окон
    curr_y = -300 + gap

    # окна по вертикали
    while curr_y < (-300 + height) - window_h:
        curr_x = start_x + gap

        # окна по горизонтали
        while curr_x < (start_x + width) - window_w:
            draw_lit_window(curr_x, curr_y, window_w, window_h)
            curr_x += window_w + gap

        curr_y += window_h + gap


# рисования городского пейзажа
def draw_cityscape():
    create_sky(150)  # создаем небо со звездами
    current_x = -400 # начинаем рисовать здания слева

    # Рисуем здания по всей ширине экрана
    while current_x < 400:
        b_width = random.randint(40, 70)   # случайная ширина 
        b_height = random.randint(100, 350)# случайная высота 

        draw_building(current_x, b_width, b_height)
        current_x += b_width  # смещаемся вправо для следующего здания


draw_cityscape()
t.done()

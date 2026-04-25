import turtle as t

screen = t.Screen()
screen.setup(width=800, height=600)
t.speed(0)
# Прячем курсор, чтобы не мешал
t.hideturtle()


# Функция для рисования квадрата
def draw_square(size, color, x, y):
    t.penup()
    # Перемещаемся в центр квадрата (x,y - центр, size/2 - половина стороны)
    t.goto(x - size / 2, y + size / 2)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(4):
        t.forward(size)  
        t.right(90)  
    t.end_fill()


# Функция для рисования круга
def draw_circle(radius, color, x, y):
    t.penup()
    # Перемещаемся в центр круга (x,y - центр, y-radius - нижняя точка)
    t.goto(x, y - radius)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()


# Функция для рисования равностороннего треугольника
def draw_triangle(size, color, x, y):
    t.penup()
    # Перемещаемся в центр треугольника (рассчитано через формулу высоты)
    # size * (3**0.5)/6 - расстояние от центра до нижней стороны
    t.goto(x - size / 2, y - size * (3 ** 0.5) / 6)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(3):
        t.forward(size)  
        t.left(120)  
    t.end_fill()


# Основная функция для создания орнамента
def ornament():
    colors_list = ["yellow", "green", "red"]
    num_colors = len(colors_list)

    # Размер одной ячейки сетки (расстояние между центрами фигур)
    grid_size = 100
    # Количество строк и столбцов в орнаменте
    rows = 4
    cols = 7

    # Вычисляем начальную позицию X (левый верхний угол орнамента)
    # (cols * grid_size)/2 - половина ширины орнамента
    # grid_size/2 - сдвиг на половину ячейки, чтобы фигуры были по центру
    start_x = - (cols * grid_size) / 2 + grid_size / 2
    # Вычисляем начальную позицию Y (левый верхний угол орнамента)
    start_y = (rows * grid_size) / 2 - grid_size / 2

    # Счётчик для определения фигуры и цвета (0,1,2,3,4,...)
    index = 0

    # Перебираем все строки (сверху вниз)
    for r in range(rows):
        # Перебираем все столбцы (слева направо)
        for c in range(cols):
            # Вычисляем координаты центра текущей ячейки
            x = start_x + c * grid_size  # по горизонтали
            y = start_y - r * grid_size  # по вертикали (минус, т.к. идём вниз)

            # Выбираем цвет по модулю индекса (циклически повторяем цвета)
            current_color = colors_list[index % num_colors]
            # Выбираем тип фигуры (0-квадрат, 1-круг, 2-треугольник) циклически
            element_type = index % 3

            # Рисуем фигуру соответствующего типа
            if element_type == 0:
                # Квадрат размером 80% от ячейки
                draw_square(grid_size * 0.8, current_color, x, y)
            elif element_type == 1:
                # Круг радиусом 40% от ячейки
                draw_circle(grid_size * 0.4, current_color, x, y)
            else:
                # Треугольник размером 80% от ячейки
                draw_triangle(grid_size * 0.8, current_color, x, y)

            # Увеличиваем счётчик для следующей фигуры
            index += 1


ornament()
t.done()

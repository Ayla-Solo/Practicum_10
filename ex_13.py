import turtle as t


screen = t.Screen()
screen.setup(width = 800, height = 800)


t.speed(0)
t.hideturtle()

C2 = "#E0F7FA"  # Светло-голубой
C3 = "#4FC3F7"  # Средний голубой
C4 = "#0288D1"  # Темно-синий

# Функция рисования треугольника по трем вершинам и цвету
def draw_triangle(p1, p2, p3, color): 
    t.penup()          
    t.goto(p1)        
    t.pendown()        
    t.fillcolor(color) # Установить цвет заливки
    t.pencolor("white")# Цвет границы (белый)
    t.pensize(2)       # Толщина линии
    t.begin_fill()     
    t.goto(p2)        
    t.goto(p3)       
    t.goto(p1)       
    t.end_fill()       

# Функция рисования одной плитки (квадрата из двух треугольников)
def draw_tile(x, y, size, color1, color2, diag_type): 
    # Координаты углов квадрата
    tl = (x, y)                 # верхний левый
    tr = (x + size, y)          # верхний правый
    bl = (x, y - size)          # нижний левый
    br = (x + size, y - size)   # нижний правый

    # В зависимости от типа диагонали рисуем два треугольника
    if diag_type == 0:  # диагональ "\" 
        draw_triangle(tl, tr, br, color1)
        draw_triangle(tl, bl, br, color2)
    else:  # диагональ "/"
        draw_triangle(tl, tr, bl, color2)
        draw_triangle(tr, br, bl, color1)


def draw_pattern():
    size = 70   # размер одной плитки
    rows = 6    # количество строк
    cols = 6    # количество столбцов

 
    start_x = - (cols * size) / 2
    start_y = (rows * size) / 2

    # Проходим по всем строкам и столбцам
    for row in range(rows):
        for col in range(cols):
            # Вычисляем координаты текущей плитки
            x = start_x + col * size
            y = start_y - row * size

            # Особые центральные плитки 
            if row == 2 and col == 2:
                draw_tile(x, y, size, C4, C3, 0)
            elif row == 2 and col == 3:
                draw_tile(x, y, size, C3, C4, 1)
            elif row == 3 and col == 2:
                 draw_tile(x, y, size, C4, C3, 1)
            elif row == 3 and col == 3:
                draw_tile(x, y, size, C3, C4, 0)

            # Остальные плитки 
            else:
                if row == 0 and col == 0:
                    draw_tile(x, y, size, C4, C3, 0)
                elif row == 0 and col == 1:
                    draw_tile(x, y, size, C3, C4, 0)
                elif row == 0 and col == 2:
                    draw_tile(x, y, size, C2, C3, 0)
                elif row == 0 and col == 3:
                    draw_tile(x, y, size, C3, C2, 1)
                elif row == 0 and col == 4:
                    draw_tile(x, y, size, C4, C3, 1)
                elif row == 0 and col == 5:
                    draw_tile(x, y, size, C3, C4, 1)
                elif row == 1 and col == 0:
                    draw_tile(x, y, size, C3, C2, 0)
                elif row == 1 and col == 1:
                    draw_tile(x, y, size, C4, C3, 0)
                elif row == 1 and col == 2:
                    draw_tile(x, y, size, C3, C4, 0)
                elif row == 1 and col == 3:
                    draw_tile(x, y, size, C4, C3, 1)
                elif row == 1 and col == 4:
                    draw_tile(x, y, size, C3, C4, 1)
                elif row == 1 and col == 5:
                    draw_tile(x, y, size, C2, C3, 1)
                elif row == 2 and col == 0:
                    draw_tile(x, y, size, C2, C3, 0)
                elif row == 2 and col == 1:
                    draw_tile(x, y, size, C3, C2, 0)
                elif row == 2 and col == 4:
                    draw_tile(x, y, size, C2, C3, 1)
                elif row == 2 and col == 5:
                    draw_tile(x, y, size, C3, C2, 1)
                elif row == 3 and col == 0:
                    draw_tile(x, y, size, C2, C3, 1)
                elif row == 3 and col == 1:
                    draw_tile(x, y, size, C3, C2, 1)
                elif row == 3 and col == 4:
                    draw_tile(x, y, size, C2, C3, 0)
                elif row == 3 and col == 5:
                    draw_tile(x, y, size, C3, C2, 0)
                elif row == 4 and col == 0:
                    draw_tile(x, y, size, C3, C2, 1)
                elif row == 4 and col == 1:
                    draw_tile(x, y, size, C4, C3, 1)
                elif row == 4 and col == 2:
                    draw_tile(x, y, size, C3, C4, 1)
                elif row == 4 and col == 3:
                    draw_tile(x, y, size, C4, C3, 0)
                elif row == 4 and col == 4:
                    draw_tile(x, y, size, C3, C4, 0)
                elif row == 4 and col == 5:
                    draw_tile(x, y, size, C2, C3, 0)
                elif row == 5 and col == 0:
                    draw_tile(x, y, size, C4, C3, 1)
                elif row == 5 and col == 1:
                    draw_tile(x, y, size, C3, C4, 1)
                elif row == 5 and col == 2:
                    draw_tile(x, y, size, C2, C3, 1)
                elif row == 5 and col == 3:
                    draw_tile(x, y, size, C3, C2, 0)
                elif row == 5 and col == 4:
                    draw_tile(x, y, size, C4, C3, 0)
                elif row == 5 and col == 5:
                    draw_tile(x, y, size, C3, C4, 0)


draw_pattern()
t.done()


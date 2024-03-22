import math
import turtle
turtle.speed(100)
turtle.pendown()
turtle.pensize(2)
turtle.pencolor('black')

center_x = float(input("Введите координату x центра окружности: "))
center_y = float(input("Введите координату y центра окружности: "))
radius = float(input("Введите радиус окружности: "))

#setposition=center_x,center_y
turtle.setpos(center_x,center_y)
turtle.circle=radius, 360
turtle.penup()
#circle = (center_x, center_y), radius

point_x = float(input("Введите координату x точки: "))
point_y = float(input("Введите координату y точки: "))
#setposition=point_x,point_y
turtle.setpos(point_x,point_y)
turtle.pendown()
turtle.dot(2)
#point = point_x, point_y

distance = math.sqrt((point_x - center_x) ** 2 + (point_y - center_y) ** 2)

if distance < radius:
    print('Точка внутри окружности')
elif distance == radius:
    print('Точка лежит на окружности')
else:
    print('Точка располагается за пределами окружности')
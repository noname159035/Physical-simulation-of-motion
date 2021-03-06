#пример ввода функции:
# Ek = M*U^2/2  формула
# def find_Ek(m, u):
#     Ek = (m*(u**2))/2
#     return Ek
#Название функции писать как find_"величина"
import math

var = {
    "circle_U": 0,
    "circle_w": 0,
    "circle_R": 0,
    "circle_t": 0,
    "circle_S": 0,
    "circle_a_o": 0,
    "circle_T": 0,
    "line_U_st": 0,
    "circle_delta_s": 0,
    "circle_delta_f": 0,
    "line_a": 0,
    "line_t": 0,
    "line_U_fin": 0,
    "line_S_mov": 0,
    "line_L": 0,
    "angle_U_st": 0,
    "angle_d": 0,
    "angle_t": 0,
    "angle_h_st": 0,
    "angle_U_fin": 0,
    "angle_H": 0,
    "angle_L": 0,
    "angle_t_fall": 0,
    "angle_U_st_x": 0,
    "angle_U_st_y": 0
}

#ДВИЖЕНИЕ ПО ОКРУЖНОСТИ

def find_circle_w (circle_U, circle_R):
    '''Функция возвращающая значение угловой скорости при движении по окружности'''
    '''circle_U - скорость вводимая с клавиатуры'''
    '''circle_R - радиус вводимый с клавиатуры'''
    circle_w = circle_U / circle_R
    return circle_w

def find_circle_U (circle_w, circle_R):
    '''Функция возвращающая значение линейной скорости при щаданных угловой скорости и радусе коружности в движении по окружности'''
    '''circle_R - радиус вводимый с клавиатуры'''
    '''circle_w - угловая скорость вводимая с клавиатуры'''
    circle_U = circle_w * circle_R
    return circle_U

def find_circle_a_o (circle_U, circle_R):
    '''Функция возвращающая значение центростремительного ускорения при движении по окружности'''
    '''circle_U - скорость вводимая с клавиатуры'''
    '''circle_R - радиус вводимый с клавиатуры'''

    circle_a_o = circle_U**2 / circle_R
    return circle_a_o

def find_circle_S (circle_U, circle_t):
    '''Функция возвращающая значение перемещения при движении по окружности'''
    '''circle_U - скорость вводимая с клавиатуры'''
    '''circle_t - время вводимое с клавиатуры'''
    circle_S = circle_U*circle_t
    return circle_S

def find_circle_T (circle_U, circle_R):
    '''Функция возвращающая значение периода при движении по окружности'''
    '''circle_U - скорость вводимая с клавиатуры'''
    '''circle_R - радиус вводимый с клавиатуры'''
    circle_T = 2 * 3.14 * circle_R / circle_U
    return circle_T

def find_circle_delta_s (circle_S, circle_U, circle_T, circle_t):
    '''Функция возвращающая значение угловой скорости при движении по окружности'''
    '''circle_U - скорость вводимая с клавиатуры'''
    '''circle_t - время вводимое с клавиатуры'''
    '''circle_T - период вводимый с клавиатуры'''
    '''circle_S - путь вводимый с клавиатуры'''
    circle_delta_s = circle_S - circle_U * circle_T * (circle_t // circle_T )
    return circle_delta_s

def find_circle_delta_f (circle_delta_s, circle_R):
    '''Функция возвращающая значение углового перемещения при движении по окружности'''
    '''circle_R - радиус вводимый с клавиатуры'''
    '''circle_delta_s - смещение относительно точки начала движения рассчитанное из функции find_circle_delta_s'''
    circle_delta_f = circle_delta_s / circle_R
    return circle_delta_f

def find_circle_U2 (circle_S, circle_t):
    '''Функция возвращающая значение линейной скорости при заданных пути и времени вдижения в движении по окружности'''
    '''circle_t - время вводимое с клавиатуры'''
    '''circle_S - путь вводимый с клавиатуры'''
    circle_U = circle_S / circle_t
    return circle_U

def find_circle_R (circle_U, circle_w):
    '''Функция возвращающая значение радиуса окружности при заданных линейной скорости и угловой скорости в движении по окружности'''
    '''circle_U - скорость вводимая с клавиатуры'''
    '''circle_w - угловая скорость вводимая с клавиатуры'''
    circle_R = circle_U / circle_w
    return circle_R

def find_circle_R2(circle_S, circle_t, circle_w):
    '''Функция возвращающая значение радиуса окружности при заднных пути, времени, и угловой скорости в движении по окружности'''
    '''circle_w - угловая скорость вводимая с клавиатуры'''
    '''circle_t - время вводимое с клавиатуры'''
    '''circle_S - путь вводимый с клавиатуры'''
    circle_R = circle_S / (circle_t * circle_w)
    return circle_R

def find_circle_U3 (circle_a_o, circle_R):
    '''Функция возвращающая значение линейной скорости при заданных центростремительном ускорении и радуисе окружности в движении по окружности'''
    '''circle_R - радиус вводимый с клавиатуры'''
    '''circle_a_o - центростремительное ускорение вводимое с клавиатуры'''
    from math import sqrt
    circle_U = math.sqrt(circle_a_o * circle_R)
    return circle_U

def find_circle_t (circle_S, circle_U):
    '''Функция возвращающая значение времени движения при движении по окружности'''
    '''circle_U - скорость вводимая с клавиатуры'''
    '''circle_S - путь вводимый с клавиатуры'''
    circle_t = circle_S / circle_U
    return circle_t


#ДВИЖЕНИЕ ПОД УГЛОМ К ГОРИЗОНТУ

def find_angle_U_st_x (angle_U_st, angle_d):
    '''Функция возвращающая значение начальной скорости по оси OX при движении типа бросок по углом к горизонту'''
    '''angle_U_st - скорость вводимая с клавиатуры или расчитываемая из функции find_angle_U_st'''
    '''angle_d - угол вводимый с клавиатуры или расчитываемый из функции find_angle_d'''
    angle_U_st_x = math.cos(math.radians(angle_d)) * angle_U_st
    return angle_U_st_x

def find_angle_U_st_y (angle_U_st, angle_d):
    '''Функция возвращающая значение начальной скорости по оси OY при движении типа бросок по углом к горизонту'''
    '''angle_U_st - скорость вводимая с клавиатуры или расчитываемая из функции find_angle_U_st'''
    '''angle_d - угол вводимый с клавиатуры или расчитываемый из функции find_angle_d'''
    angle_U_st_y = math.sin(math.radians(angle_d)) * angle_U_st
    return angle_U_st_y

def find_angle_t_fall (angle_U_st_y):
    '''Функция возвращающая значение времени падения тела при движении типа бросок по углом к горизонту'''
    '''angle_U_st_y - скорсть расчитываемая из функции find_angle_U_st_y'''
    angle_t_fall = angle_U_st_y / 9.81
    return angle_t_fall

def find_angle_H (angle_h_st, angle_U_st_y):
    '''Функция возвращающая значение максимальной высоты подъема при движении типа бросок по углом к горизонту'''
    '''angle_h_st - начальная высота вводимая с клавиатуры или расчитываемая из функции find_angle_h_st'''
    '''angle_U_st_y - скорсть расчитываемая из функции find_angle_U_st_y'''
    angle_H = angle_h_st + angle_U_st_y ** 2 / (9.81 * 2)
    return angle_H

def find_angle_L (angle_U_st_x, angle_t):
    '''Функция возвращающая значение пути пройденного телом по оси OX при движении типа бросок по углом к горизонту'''
    '''angle_U_st_x - скорсть расчитываемая из функции find_angle_U_st_x'''
    '''angle_t - время полета вводимое с клавиатуры или расчитываемое из функции find_angle_t'''
    ange_L = angle_U_st_x * angle_t
    return ange_L

def find_angle_U_fin (angle_h_st, angle_U_st):
    '''Функция возвращающая значение конечной скорости при движении типа бросок по углом к горизонту'''
    '''angle_h_st - начальная высота вводимая с клавиатуры или расчитываемая из функции find_angle_h_st'''
    '''angle_U_st - скорость вводимая с клавиатуры или расчитываемая из функции find_angle_U_st'''
    angle_U_fin = math.sqrt(2 * 9.81 * angle_h_st + angle_U_st ** 2)
    return angle_U_fin

def find_angle_U_st (angle_U_fin, angle_h_st):
    '''Функция возвращающая значение начальной скорости при движении типа бросок по углом к горизонту'''
    '''angle_U_fin - скорость вводимая с клавиатуры или расчитываемая из функции find_angle_U_fin'''
    '''angle_U_st - скорость вводимая с клавиатуры или расчитываемая из функции find_angle_U_st'''
    angle_U_st = math.sqrt(angle_U_fin ** 2 - 2 * 9.81 * angle_h_st)
    return angle_U_st

def find_angle_h_st (angle_t_fall, angle_H):
    '''Функция возвращающая значение высоты точки броска тела при движении типа бросок по углом к горизонту'''
    '''angle_t_fall - время подъема вводимое с клавиатуры или расчитываемое из функции find_angle_t_fall'''
    '''angle_h_st - начальная высота вводимая с клавиатуры или расчитываемая из функции find_angle_h_st'''
    angle_h_st = angle_H - 9.81 * angle_t_fall ** 2 / 2
    return angle_h_st

def find_angle_d (angle_U_st, angle_t_fall):
    '''Функция возвращающая значение величины угла броска к горизонту при движении типа бросок по углом к горизонту'''
    '''angle_U_st - скорость вводимая с клавиатуры или расчитываемая из функции find_angle_U_st'''
    '''angle_t_fall - время подъема вводимое с клавиатуры или расчитываемое из функции find_angle_t_fall'''
    angle_d = math.degrees(math.asin(angle_U_st / (2 * 9.81 * angle_t_fall)))
    return angle_d

def find_angle_t (angle_L, angle_U_st_x):
    '''Функция возвращающая значение всего времени движеня тела при движении типа бросок по углом к горизонту'''
    '''angle_L - длина пути вводимая с клавиатуры или расчитываемая из функции find_angle_L'''
    '''angle_U_st_x - скорость вводимая с клавиатуры или расчитываемая из функции find_angle_U_st_x'''
    angle_t = angle_L / angle_U_st_x
    return angle_t

def find_angle_x_t (angle_U_st_x, t):
    '''Функция возвращающая значение x при заданом t'''
    '''t - время полета заданого тела'''
    '''angle_U_st_x - скорость вводимая с клавиатуры или расчитываемая из функции find_angle_U_st_x'''
    angle_x_t = angle_U_st_x * t
    return angle_x_t

def find_angle_y_t (angle_U_st_y, t):
    '''Функция возвращающая значение y при заданом t'''
    '''t - время полета заданого тела'''
    '''angle_U_st_y - скорость вводимая с клавиатуры или расчитываемая из функции find_angle_U_st_y'''
    angle_y_t = var["angle_h_st"] + angle_U_st_y * t - 9.81 * t ** 2 / 2
    return angle_y_t

#ПРЯМОЛИНЕЙНОЕ ДВИЖЕНИЕ

def find_line_U_st1(line_a, line_t, line_U_fin):
    '''Функция возвращающая значение начальной скорости при заданных ускорении, времени, и конечной скорости в прямолинейном движении'''
    '''circle_a - ускорение вводимое с клавиатуры'''
    '''circle_t - время движения вводимое с клавиатуры'''
    '''circle_U_fin - конечная скорость вводимая с клавиатуры'''
    line_U_st = line_U_fin - line_a * line_t
    return line_U_st


def find_line_U_st2(line_a, line_t, line_S_mov):
    '''Функция возвращающая значение начальной скорости при заданных ускорении, времени, и пути в прямолинейном движении'''
    '''circle_a - ускорение вводимое с клавиатуры'''
    '''circle_t - время движения вводимое с клавиатуры'''
    '''circle_S_mov - путь пройденный за время движения вводимый с клавиатуры'''
    line_U_st = (2 * line_S_mov - line_a * line_t ** 2) / 2 * line_t
    return line_U_st


def find_line_U_fin1(line_a, line_t, line_U_st):
    '''Функция возвращающая значение конечной скорости при заданных ускорении, времени, и начальной скорости в прямолинейном движении'''
    '''circle_a - ускорение вводимое с клавиатуры'''
    '''circle_t - время движения вводимое с клавиатуры'''
    '''circle_U_st - начальная скорость вводимая с клавиатуры'''
    line_U_fin = line_U_st + line_a * line_t
    return line_U_fin


def find_line_U_fin2(line_a, line_t, line_S_mov):
    '''Функция возвращающая значение конечной скорости при заданных ускорении, времени, и пути в прямолинейном движении'''
    '''circle_a - ускорение вводимое с клавиатуры'''
    '''circle_t - время движения вводимое с клавиатуры'''
    '''circle_S_mov - путь пройденный за время движения вводимый с клавиатуры'''
    line_U_fin = (2 * line_S_mov + line_a * line_t ** 2) / 2 * line_t
    return line_U_fin

def find_line_S_mov1(line_U_st, line_a, line_t):
    '''Функция возвращающая значение пути при заданных ускорении, времени, и начальной скорости в прямолинейном движении'''
    '''circle_a - ускорение вводимое с клавиатуры'''
    '''circle_t - время движения вводимое с клавиатуры'''
    '''circle_U_fin - конечная скорость вводимая с клавиатуры'''
    line_S_mov = line_U_st * line_t + line_a * line_t ** 2 / 2
    return line_S_mov


def find_line_S_mov2(line_U_fin, line_a, line_t):
    '''Функция возвращающая значение пути при заданных ускорении, времени, и конечной скорости в прямолинейном движении'''
    '''circle_a - ускорение вводимое с клавиатуры'''
    '''circle_t - время движения вводимое с клавиатуры'''
    '''circle_U_fin - конечная скорость вводимая с клавиатуры'''
    line_S_mov = line_U_fin * line_t - line_a * line_t ** 2 / 2
    return line_S_mov


def find_line_L(line_S_mov, line_t, line_a):
    '''Функция возвращающая значение перемещения при заданных ускорении, времени, и пути в прямолинейном движении'''
    '''circle_a - ускорение вводимое с клавиатуры'''
    '''circle_t - время движения вводимое с клавиатуры'''
    '''circle_S_mov - путь пройденный за время движения вводимый с клавиатуры, либо рассчитанный по одной из функций def find_line_S_mov1/def find_line_S_mov1 '''
    line_L = line_S_mov ** 2 / line_t * line_a
    return line_L
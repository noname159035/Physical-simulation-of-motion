#пример ввода функции:
# Ek = M*U^2/2  формула
# def find_Ek(m, u):
#     Ek = (m*(u**2))/2
#     return Ek
#Название функции писать как find_"величина"

var = {
    "circle_U": 0,
    "circke_w": 0,
    "circke_R": 0,
    "circke_t": 0,
    "circke_S_way": 0,
    "circke_a_o": 0,
    "line_U_st": 0,
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
    "angle_t_fall": 0
}
def find_circle_w (circle_U, circle_R):
    circle_w = circle_U / circle_R
    return circle_w

def find_circle_U (circle_w, circle_R):
    circle_U = circle_w * circle_R
    return circle_U

def find_circle_a_o (circle_U, circle_R):
    circle_a_o = circle_U**2 / circle_R
    return circle_a_o

def find_circle_S (circle_U, circle_t):
    circle_S = circle_U*circle_t
    return circle_S

def find_circle_T (circle_U, circle_R):
    circle_T = 2 * pi * circle_R / circle_U
    return circle_T

def find_circle_delta_s (circle_S, circle_U, circle_T, circle_t):
    circle_delta_s = circle_S - circle_U * circle_T * (circle_t / circle_T )
    return circle_delta_s

def find_circle_f (circle_delta_s, circle_R):
    circle_f = circle_delta_s / circle_R
    return circle_f

def find_circle_U2 (circle_S, circle_t):
    circle_U = circle_S / circle_t
    return circle_U

def find_circle_R (circle_U, circle_w):
    circle_R = circle_U / circle_w
    return circle_R
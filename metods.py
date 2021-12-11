#пример ввода функции:
# Ek = M*U^2/2  формула
# def find_Ek(m, u):
#     Ek = (m*(u**2))/2
#     return Ek
#Название функции писать как find_"величина"

var = {
    "circle_U": 0,
    "circle_w": 0,
    "circle_R": 0,
    "circle_t": 0,
    "circle_S_way": 0,
    "circle_a_o": 0,
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
def find_circle_w1 (circle_U, circle_R):
    circle_W = circle_U / circle_R
    return circle_W

def find_circle_a_o (circle_U, circle_R):
    circle_a_o = circle_U**2 / circle_R
    return circle_a_o

def find_circle_t (circle_U, circle_R):
    circle_a_o = circle_U**2 / circle_R
    return circle_a_o
import metods
from metods import *

        #metods.var['circle_t'] = metods.find_angle_H(metods.var['circle_w'], ..... аналогично заполнять )
def final_count_line():
    if metods.var['line_U_st'] != 0:
        metods.var['line_U_fin'] = metods.find_line_U_fin1(metods.var['line_a'], metods.var['line_t'], metods.var['line_U_st'])
        metods.var['line_S_mov'] = metods.find_line_S_mov1(metods.var['line_U_st'], metods.var['line_a'], metods.var['line_t'])

    elif metods.var['line_S_mov'] != 0:
        metods.var['line_U_fin'] = metods.find_line_U_fin2(metods.var['line_a'], metods.var['line_t'], metods.var['line_S_mov'])
        metods.var['line_U_st'] = metods.find_line_U_st2(metods.var['line_a'], metods.var['line_t'], metods.var['line_S_mov'])

    elif metods.var['line_U_fin'] != 0:
        metods.var['line_U_st'] = metods.find_line_U_st1(metods.var['line_a'], metods.var['line_t'], metods.var['line_U_fin'])
        metods.var['line_S_mov'] = metods.find_line_S_mov2(metods.var['line_U_fin'], metods.var['line_a'],  metods.var['line_t'])

    metods.var['line_L'] = metods.find_line_L(metods.var['line_S_mov'], metods.var['line_t'], metods.var['line_a'])

def final_count_circle():

    if (metods.var['circle_w'] != 0  or metods.var['circle_U'] != 0) and metods.var['circle_R'] != 0 and metods.var['circle_t'] != 0:
            if metods.var['circle_w'] != 0 and metods.var['circle_U'] == 0 :
                metods.var['circle_w'] = metods.find_circle_w(metods.var['circle_U'], metods.var['circle_R'])
            metods.var['circle_T'] = metods.find_circle_T(metods.var['circle_U'], metods.var['circle_R'])
            metods.var['circle_a_o'] = metods.find_circle_a_o(metods.var['circle_U'], metods.var['circle_R'])
            metods.var['circle_S'] = metods.find_circle_S(metods.var['circle_U'], metods.var['circle_t'])
            metods.var['circle_delta_s'] = metods.find_circle_delta_s(metods.var['circle_S'], metods.var['circle_U'], metods.var['circle_T'], metods.var['circle_t'])
            metods.var['circle_delta_f'] = metods.find_circle_delta_f(metods.var['circle_delta_s'], metods.var['circle_R'])
            if metods.var['circle_w'] == 0 :


    elif metods.var['circle_S'] != 0 and metods.var['circle_t'] != 0 and metods.var['circle_w'] != 0:
            metods.var['circle_U'] = metods.find_circle_U2(metods.var['circle_S'], metods.var['circle_t'])
            metods.var['circle_R'] = metods.find_circle_R2(metods.var['circle_S'], metods.var['circle_t'],
                                                           metods.var['circle_w'])
            metods.var['circle_T'] = metods.find_circle_T(metods.var['circle_U'], metods.var['circle_R'])
            metods.var['circle_a_o'] = metods.find_circle_a_o(metods.var['circle_U'], metods.var['circle_R'])
            metods.var['circle_S'] = metods.find_circle_S(metods.var['circle_U'], metods.var['circle_t'])
            metods.var['circle_delta_s'] = metods.find_circle_delta_s(metods.var['circle_S'], metods.var['circle_U'], metods.var['circle_T'], metods.var['circle_t'])
            metods.var['circle_delta_f'] = metods.find_circle_delta_f(metods.var['circle_delta_s'], metods.var['circle_R'])

    elif metods.var['circle_R'] != 0 and metods.var['circle_a_o'] != 0 and metods.var['circle_S'] != 0:
            metods.var['circle_U'] = metods.find_circle_U3(metods.var['circle_a_o'], metods.var['circle_R'])
            metods.var['circle_w'] = metods.find_circle_w(metods.var['circle_U'], metods.var['circle_R'])
            metods.var['circle_T'] = metods.find_circle_T(metods.var['circle_U'], metods.var['circle_R'])
            metods.var['circle_t'] = metods.find_circle_S(metods.var['circle_S'], metods.var['circle_U'])
            metods.var['circle_delta_s'] = metods.find_circle_delta_s(metods.var['circle_S'], metods.var['circle_U'], metods.var['circle_T'], metods.var['circle_t'])
            metods.var['circle_delta_f'] = metods.find_circle_delta_f(metods.var['circle_delta_s'], metods.var['circle_R'])

def final_count_angle ():
    if metods.var['angle_U_fin'] != 0:
        metods.var['angle_U_st'] = metods.find_angle_U_st (metods.var['angle_U_fin'], metods.var['angle_h_st'])
    elif metods.var["angle_d"] == 0:
        metods.var["angle_d"] = metods.find_angle_d (metods.var['angle_U_st'], metods.var['angle_t_fall'])
    metods.var['angle_U_st_x'] = metods.find_angle_U_st_x (metods.var['angle_U_st'], metods.var["angle_d"])
    metods.var['angle_U_st_y'] = metods.find_angle_U_st_y (metods.var['angle_U_st'], metods.var["angle_d"])

    if metods.var['angle_t'] != 0 and metods.var['angle_h_st'] != 0:
        metods.var['angle_t_fall'] = metods.find_angle_t_fall(metods.var['angle_U_st_y'])
        metods.var["angle_H"] = metods.find_angle_H(metods.var['angle_h_st'], metods.var['angle_U_st_y'])
        metods.var["angle_L"] = metods.find_angle_L(metods.var['angle_U_st_x'], metods.var['angle_t'])

    elif metods.var["angle_H"] != 0 and metods.var['angle_t_fall'] != 0 and metods.var["angle_L"] !=0:
        metods.var['angle_h_st'] = metods.find_angle_h_st(metods.var['angle_t_fall'], metods.var["angle_H"])
        metods.var['angle_t'] = metods.find_angle_t(metods.var["angle_L"], metods.var['angle_U_st_x'])

    if metods.var['angle_U_fin'] == 0:
        metods.var['angle_U_fin'] = metods.find_angle_U_fin(metods.var['angle_h_st'], metods.var['angle_U_st'])



import metods
from metods import *
def final_count_circle ():
    if metods.var['circle_t'] !=0 and :

        #metods.var['circle_t'] = metods.find_angle_H(metods.var['circle_w'], ..... аналогично заполнять )
    if metods.var['line_U_st'] != 0 and metods.var['line_a'] != 0 and metods.var['line_t'] != 0:
        metods.var['line_U_fin'] = metods.find_line_U_fin1(metods.var['line_U_st'], metods.var['line_t'], metods.var['line_a'] )

    elif metods.var['line_S_mov'] != 0 and metods.var['line_a'] != 0 and metods.var['line_t'] != 0:
        metods.var['line_U_fin'] = metods.find_line_U_fin2(metods.var['line_S_mov'], metods.var['line_t'], metods.var['line_a'])

    if metods.var['line_U_fin'] != 0 and metods.var['line_a'] != 0 and metods.var['line_t'] != 0:
        metods.var['line_U_st'] = metods.find_line_U_st1(metods.var['line_U_fin'], metods.var['line_t'], metods.var['line_a'])

    elif metods.var['line_S_mov'] != 0 and metods.var['line_a'] != 0 and metods.var['line_t'] != 0:
        metods.var['line_U_st'] = metods.find_line_U_st2(metods.var['line_S_mov'], metods.var['line_t'], metods.var['line_a'])

    if metods.var['line_U_st'] != 0 and metods.var['line_a'] != 0 and metods.var['line_t'] != 0:
        metods.var['line_S_mov'] = metods.find_line_S_mov1(metods.var['line_U_st'], metods.var['line_t'], metods.var['line_a'])

    elif metods.var['line_U_fin'] != 0 and metods.var['line_a'] != 0 and metods.var['line_t'] != 0:
        metods.var['line_S_mov'] = metods.find_line_S_mov2(metods.var['line_U_fin'], metods.var['line_t'], metods.var['line_a'])





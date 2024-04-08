import math
import numpy as np
from calc_distance import vincenty_inverse
from calc_bearing import calculate_bearing
from find_coord import cal_new_coord

def matrix_calc(coord1, coord2):
    bearing_hor = calculate_bearing(coord1, coord2)
    bearing_ver = bearing_hor + 90
    distance = vincenty_inverse(coord1, coord2).m
    matrix_final = np.zeros((5, 7), dtype = object)
    matrix_final[0][0] = coord1
    matrix_final[0][1] = coord2
    
    for i in range(0, 5):
        if matrix_final[i][0] == 0:
            matrix_final[i][0] = cal_new_coord(matrix_final[i-1][0], bearing_ver, distance)
        for j in range(1, 7):
            if matrix_final[i][j] == 0:
                matrix_final[i][j] = cal_new_coord(matrix_final[i][j-1], bearing_hor, distance)
                
    return matrix_final

'''coord1 = [1, 1]
coord2 = [2, 2]
matrix1 = matrix_calc(coord1, coord2)
# print(matrix1[2][0][1])
# print(matrix1[0][2])'''
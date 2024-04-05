import math
import numpy as np
from calc_distance import vincenty_inverse
from calc_bearing import calculate_bearing
from find_coord import cal_new_coord

def matrix_lat(coord1, coord2):
    bearing_hor = calculate_bearing(coord1, coord2)
    bearing_ver = bearing_hor + 90
    distance = vincenty_inverse(coord1, coord2)
    matrix_lat = np.zeros((5, 7))
    matrix_lat[0][0] = coord1[0]
    matrix_lat[0][1] = coord2[0]
    
    for i in range(0, 5):
        if matrix_lat[i][0] == 0:
            new_coord = cal_new_coord(matrix_lat[i-1][0], bearing_ver, distance)
            matrix_lat[i][0] = new_coord[0]
        for j in range(1, 7):
            if matrix_lat[i][j] == 0:
                new_coord = cal_new_coord(matrix_lat[i][j-1], bearing_hor, distance)
                matrix_lat[i][j] = new_coord[0]

    return matrix_lat

def matrix_lon(coord1, coord2):
    bearing_hor = calculate_bearing(coord1, coord2)
    bearing_ver = bearing_hor + 90
    distance = vincenty_inverse(coord1, coord2)
    matrix_lon = np.zeros((5, 7))
    matrix_lon[0][0] = coord1[1]
    matrix_lon[0][1] = coord2[1]
    
    for i in range(0, 5):
        if matrix_lon[i][0] == 0:
            new_coord = cal_new_coord(matrix_lon[i-1][0], bearing_ver, distance)
            matrix_lon[i][0] = new_coord[1]
        for j in range(1, 7):
            if matrix_lon[i][j] == 0:
                new_coord = cal_new_coord(matrix_lon[i][j-1], bearing_hor, distance)
                matrix_lon[i][j] = new_coord[1]

coord1 = [31.2304, 121.4737]
coord2 = [31.2305, 121.47375]
matrix1_lat = matrix_lat(coord1, coord2)
matrix1_lon = matrix_lon(coord1, coord2)
print(matrix1_lat)
print(matrix1_lon)
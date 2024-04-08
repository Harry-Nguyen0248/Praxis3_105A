import math
from calc_distance import vincenty_inverse
from calc_bearing import calculate_bearing
from find_coord import cal_new_coord

def linear_function(x, slope, init_coord):
    return slope * (x - init_coord[1]) + init_coord[0]

def check_if_in_region(cur_coord, matrix):
    bearing = calculate_bearing(matrix[0][0], matrix[0][1])
    distance = vincenty_inverse(matrix[0][0], matrix[0][1]).m
    
    left_edge_coord = cal_new_coord(matrix[0][0], bearing + 180, distance/2)
    top_edge_coord = cal_new_coord(matrix[0][0], bearing - 90, distance/2)
    right_edge_coord = cal_new_coord(matrix[0][6], bearing, distance/2)
    bottom_edge_coord = cal_new_coord(matrix[4][0], bearing + 90, distance/2)
    
    left_edge_slope = math.tan(math.radians(bearing + 90))
    top_edge_slope = math.tan(math.radians(bearing))
    right_edge_slope = math.tan(math.radians(bearing + 90))
    bottom_edge_slope = math.tan(math.radians(bearing))
    
    left_edge_y_func = linear_function(cur_coord[1], left_edge_slope, left_edge_coord)
    top_edge_y_func = linear_function(cur_coord[1], top_edge_slope, top_edge_coord)
    right_edge_y_func = linear_function(cur_coord[1], right_edge_slope, right_edge_coord)
    bottom_edge_y_func = linear_function(cur_coord[1], bottom_edge_slope, bottom_edge_coord)
    
    
    if 0 < bearing < 90:
        if (left_edge_y_func <= cur_coord[0] <= right_edge_y_func) and (bottom_edge_y_func <= cur_coord[0] <= top_edge_y_func):
            return True
        else:
            return False
    elif 90 < bearing < 180:
        if (left_edge_y_func >= cur_coord[0] >= right_edge_y_func) and (bottom_edge_y_func <= cur_coord[0] <= top_edge_y_func):
            return True
        else:
            return False
    elif 180 < bearing < 270: 
        if (left_edge_y_func >= cur_coord[0] >= right_edge_y_func) and (bottom_edge_y_func >= cur_coord[0] >= top_edge_y_func):
            return True
        else:
            return False
    elif 270 < bearing < 360: 
        if (left_edge_y_func <= cur_coord[0] <= right_edge_y_func) and (bottom_edge_y_func >= cur_coord[0] >= top_edge_y_func):
            return True
        else:
            return False
   
'''coord1 = [-1, 1]
coord2 = [-2, 2]
location = [-1.5, 1.5]
matrix1 = matrix_calc(coord1, coord2)
status = check_if_in_region(location, matrix1)
if status == True:
    print("Within Region")
else:
    print("Not Within Region")'''
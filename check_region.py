import math
from final_matrix import matrix_calc
from calc_distance import vincenty_inverse
from calc_bearing import calculate_bearing
from find_coord import cal_new_coord

def linear_function(x, slope, init_coord):
    return slope * (x - init_coord[0]) + init_coord[1]

def check_if_in_region(cur_coord, matrix):
    bearing = calculate_bearing(matrix[0][0], matrix[0][1])
    distance = vincenty_inverse(matrix[0][0], matrix[0][1]).m
    
    left_edge_coord = cal_new_coord(matrix[0][0], bearing + 180, distance/2)
    top_edge_coord = cal_new_coord(matrix[0][0], 360 - 90 + bearing, distance/2)
    right_edge_coord = cal_new_coord(matrix[0][6], bearing, distance/2)
    bottom_edge_coord = cal_new_coord(matrix[4][0], bearing + 90, distance/2)
    
    left_edge_slope = math.tan(math.radians(bearing + 90))
    top_edge_slope = math.tan(math.radians(bearing))
    right_edge_slope = math.tan(math.radians(bearing + 90))
    bottom_edge_slope = math.tan(math.radians(bearing))
    
    left_edge_y_func = linear_function(cur_coord[0], left_edge_slope, left_edge_coord)
    top_edge_y_func = linear_function(cur_coord[0], top_edge_slope, top_edge_coord)
    right_edge_y_func = linear_function(cur_coord[0], right_edge_slope, right_edge_coord)
    bottom_edge_y_func = linear_function(cur_coord[0], bottom_edge_slope, bottom_edge_coord)
    
    print(bearing)
    print(distance)
    print(left_edge_coord)
    print(top_edge_coord)
    print(right_edge_coord)
    print(bottom_edge_coord)
    
    print(left_edge_y_func)
    print(top_edge_y_func)
    print(right_edge_y_func)
    print(bottom_edge_y_func)
    
    print(left_edge_slope)
    print(top_edge_slope)
    print(right_edge_slope)
    print(bottom_edge_slope)
    
    
    if cur_coord[1] >= left_edge_y_func:
        left_edge_status = True
    else:
        left_edge_status = False
        
    if cur_coord[1] <= top_edge_y_func:
        top_edge_status = True
    else:
        top_edge_status = False
        
    if cur_coord[1] <= right_edge_y_func:
        right_edge_status = True
    else:
        right_edge_status = False
        
    if cur_coord[1] >= bottom_edge_y_func:
        bottom_edge_status = True
    else:
        bottom_edge_status = False
        
    if left_edge_status and top_edge_status and right_edge_status and bottom_edge_status:
        return True
    else:
        return False
   
coord1 = [31.2304, 121.4737]
coord2 = [31.2305, 121.47375]
location = [31.2305, 121.47375]
matrix1 = matrix_calc(coord1, coord2)
status = check_if_in_region(location, matrix1)
if status == True:
    print("Within Region")
else:
    print("Not Within Region")
print(matrix1[4][0])
print(matrix1[0][6])
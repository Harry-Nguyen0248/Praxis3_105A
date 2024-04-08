import math
from final_matrix import matrix_calc
from calc_distance import vincenty_inverse
from calc_bearing import calculate_bearing
from find_coord import cal_new_coord
from check_region import check_if_in_region
from point_to_line import distance_point_to_line

def find_me(cur_coord, matrix):
    if check_if_in_region(cur_coord, matrix) == False:
        return "Not Within Region"
    
    bearing = calculate_bearing(matrix[0][0], matrix[0][1])
    distance = vincenty_inverse(matrix[0][0], matrix[0][1]).m
    cali_distance = math.sqrt((matrix[0][1][0] - matrix[0][0][0])**2 + (matrix[0][1][1] - matrix[0][0][1])**2)
    
    left_edge_coord = cal_new_coord(matrix[0][0], bearing + 180, distance/2)
    top_edge_coord = cal_new_coord(matrix[0][0], bearing - 90, distance/2)
    
    left_edge_slope = math.tan(math.radians(bearing + 90))
    top_edge_slope = math.tan(math.radians(bearing))
    
    # Below is given in [x, y]
    cali_cur_coord = [distance_point_to_line(left_edge_slope, left_edge_coord, cur_coord), distance_point_to_line(top_edge_slope, top_edge_coord, cur_coord)]
    
    LED_row = int(cali_cur_coord[1] // cali_distance)
    LED_column = int(cali_cur_coord[0] // cali_distance)
    
    return [LED_row, LED_column]

    '''coord_update = [0,0]
    min_distance = 1000
    #print("test", vincenty_inverse(matrix[5][0], current_coord).m)
    for row_i in range(len(matrix)):
        for col_i in range(len(matrix[row_i])):
            new_distance = vincenty_inverse(matrix[row_i][col_i], cur_coord).m
            print("row %d, column %d, distance %.5f" %(row_i, col_i, new_distance))
            if min_distance > new_distance:
                coord_update = [row_i, col_i]
                min_distance = new_distance
    return coord_update'''


coord1 = [1, 1]
coord2 = [2, 2]
location = [0.7, 4]
matrix1 = matrix_calc(coord1, coord2)
print(find_me(location, matrix1))
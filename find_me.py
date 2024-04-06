from final_matrix import matrix_calc
from calc_distance import vincenty_inverse

def find_me(current_coord, matrix):
    coord_update = [0,0]
    min_distance = 1000
    #print("test", vincenty_inverse(matrix[5][0], current_coord).m)
    for row_i in range(len(matrix)):
        for col_i in range(len(matrix[row_i])):
            new_distance = vincenty_inverse(matrix[row_i][col_i], current_coord).m
            print("row %d, column %d, distance %.5f" %(row_i, col_i, new_distance))
            if min_distance > new_distance:
                coord_update = [row_i, col_i]
                min_distance = new_distance
    return coord_update
            

    #find lat
    
    #return (row_i, col_i)


coord1 = [31.2304, 121.4737]
coord2 = [31.2305, 121.47375]
matrix1 = matrix_calc(coord1, coord2)

current_loc = [31.23045712351777, 121.47386659094777]
print(find_me(current_loc, matrix1))
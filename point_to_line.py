import math

def distance_point_to_line(slope, init_coord, cur_coord):
    top = abs(-1*slope*cur_coord[1] + cur_coord[0] - init_coord[0] + slope*init_coord[1])
    bottom = math.sqrt(slope**2 + 1)
    return top/bottom

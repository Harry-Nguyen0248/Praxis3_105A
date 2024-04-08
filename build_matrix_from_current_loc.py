from get_gps import get_gps
from final_matrix import matrix_calc
import machine

collect_coordinate = machine.Pin(15, machine.Pin.OUT)

def build_matrix():
    coord1 = ""
    coord2 = ""

    while coord1 == "":
        print("Ready to collect first coordinate")
        if collect_coordinate.value() == 1:
            coord1 = get_gps()
    while coord2 == "":
        print("Ready to collect second coordinate")
        if collect_coordinate.value() == 1:
            coord2 = get_gps()
    
    my_matrix = matrix_calc(coord1, coord2)
    return my_matrix
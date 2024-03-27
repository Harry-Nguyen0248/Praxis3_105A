import math

def cal_distance(lat1, lon1, lat2, lon2):
    #calculate the distance between 2 coordinates (lat1, lon1, lat2, lon2)
    earth_radius = 6371000  #in meter
    d = math.acos(math.sin(lat1)*math.sin(lat2)+math.cos(lat1)*math.cos(lat2)*math.cos(lon2-lon1))*earth_radius

    return d

print(cal_distance(43.665965, -79.392910, 43.660594, -79.390758))
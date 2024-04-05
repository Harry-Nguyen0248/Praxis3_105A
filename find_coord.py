import math
from calc_distance import vincenty_inverse
from calc_bearing import calculate_bearing

def cal_new_coord(coord1, bearing, distance):
    # Convert decimal degrees to radians
    lat1 = math.radians(coord1[0])
    lon1 = math.radians(coord1[1])
    bearing = math.radians(bearing)
    
    # Earth radius in meters
    R = 6371007.2
    
    # Calculate the destination point's latitude
    lat2 = math.asin(math.sin(lat1) * math.cos(distance / R) +
                     math.cos(lat1) * math.sin(distance / R) * math.cos(bearing))
    
    # Calculate the destination point's longitude
    lon2 = lon1 + math.atan2(math.sin(bearing) * math.sin(distance / R) * math.cos(lat1),
                             math.cos(distance / R) - math.sin(lat1) * math.sin(lat2))
    
    # Convert latitude and longitude from radians to degrees
    lat2 = math.degrees(lat2)
    lon2 = math.degrees(lon2)
    
    return lat2, lon2

taipei_coord = [25.0330, 121.5654]
beijing_coord = [39.9042, 116.4074]
alicante_coord = [38.3460, -0.4907]
shanghai_coord = [31.2304, 121.4737]
taoyuan_coord = [24.9917, 121.2990]

distance = vincenty_inverse(taipei_coord, taoyuan_coord).m
#print(distance)
bearing = calculate_bearing(taoyuan_coord, taipei_coord)
print(bearing)
print(cal_new_coord(taipei_coord, bearing, distance))
#print(cal_new_coord(43.660594, -79.390758, 180, 621.48))
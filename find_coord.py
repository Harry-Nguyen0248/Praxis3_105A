import math
from calc_distance import vincenty_inverse
from calc_bearing import calculate_bearing

def cal_new_coord(coord1, bearing, distance):

    '''brng = brng * math.pi / 180
    R = 6378137.0 #radius of earth
    lat2 = math.asin( math.sin(lat1)*math.cos(d/R) +
                      math.cos(lat1)*math.sin(d/R)*math.cos(brng) )
    lon2 = lon1 + math.atan2(math.sin(brng)*math.sin(d/R)*math.cos(lat1),
                           math.cos(d/R)-math.sin(lat1)*math.sin(lat2))
    
    return (lat2, lon2)'''
    # Convert decimal degrees to radians
    lat1 = math.radians(coord1[0])
    lon1 = math.radians(coord1[0])
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
tokyo_coord = [35.6764, 139.65]
shanghai_coord = [31.2304, 121.4737]
#distance = vincenty_inverse(taipei_coord, beijing_coord).km
#print(distance)
print(calculate_bearing(taipei_coord, shanghai_coord))
#print(cal_new_coord(43.665965, -79.392910, 180, 621.48))
#print(cal_new_coord(43.660594, -79.390758, 180, 621.48))
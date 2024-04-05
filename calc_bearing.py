import math
def calculate_bearing(coord1, coord2):
    """
    Calculate the bearing between two GPS coordinates.
    
    Arguments:
    lat1, lon1 -- Latitude and longitude of point 1 (in degrees)
    lat2, lon2 -- Latitude and longitude of point 2 (in degrees)
    
    Returns:
    bearing -- Bearing in degrees
    """
    # Convert decimal degrees to radians
    lat1 = math.radians(coord1[0])
    lon1 = math.radians(coord1[1])
    lat2 = math.radians(coord2[0])
    lon2 = math.radians(coord1[1])
    
    # Calculate the difference between longitudes
    diff_lon = lon2 - lon1
    
    # Calculate bearing using the Haversine formula
    y = math.sin(diff_lon) * math.cos(lat2)
    x = math.cos(lat1) * math.sin(lat2) - math.sin(lat1) * math.cos(lat2) * math.cos(diff_lon)
    bearing = math.atan2(y, x)
    
    # Convert bearing from radians to degrees
    bearing = math.degrees(bearing)
    print("Before normalization",bearing)
    # Normalize bearing to range [0, 360)
    bearing = (bearing + 360) % 360
    
    return bearing

#print(calculate_bearing([43.665965, -79.392910],[43.660594, -79.390758]))

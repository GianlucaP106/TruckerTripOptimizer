from math import sqrt, pi, sin, cos, atan2

def coordToDistance(lat1, long1, lat2, long2):
    R = 6371000
    φ1 = lat1 * pi/180
    φ2 = lat2 * pi/180
    Δφ = (lat2-lat1) * pi/180
    Δλ = (long2-long1) * pi/180

    a = sin(Δφ/2) * sin(Δφ/2) + cos(φ1) * \
        cos(φ2) * sin(Δλ/2) * sin(Δλ/2)
    c = 2 * atan2(sqrt(a), sqrt(1-a))

    d = R * c  # meters

    return d
import math

# 参考になったURL
# https://wiki.openstreetmap.org/wiki/Slippy_map_tilenames#Python

def deg2num(lat_deg, lon_deg, zoom):
    lat_rad = math.radians(lat_deg)
    n = 2.0 ** zoom
    xtile = int((lon_deg + 180.0) / 360.0 * n)
    ytile = int((1.0 - math.asinh(math.tan(lat_rad)) / math.pi) / 2.0 * n)
    return (xtile, ytile)


try:
    lat = float(input("Enter lat: "))
    lon = float(input("Enter lon: "))
    zoom = float(input("Enter zoom: "))
except:
    print("Error Occured, please number")

print(deg2num(lat, lon, zoom))

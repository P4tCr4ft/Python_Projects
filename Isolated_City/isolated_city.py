class city(object):

    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon


# join takes 2 city class args
def join(city1, city2):
    return sqrt((city1.lat - city2.lat)**2 + (city1.lon - city2.lon)**2)

adelaide = city(-34.927060, 138.599474)
darwin = city(-12.419566, 130.862397)
perth = city(-31.941556, 115.855623)
brisbane = city(-27.464289, 153.045604)
sydney = city(-33.891257, 151.209348)
melbourne = city(-37.805328, 144.985818)
from math import sqrt

class city(object):

    def __init__(self, name, lat, lon):
        self.name = name
        self.lat = lat
        self.lon = lon


# join takes 2 city class args
def join(city1, city2):
    return sqrt((city1.lat - city2.lat)**2 + (city1.lon - city2.lon)**2)

adelaide = city('adelaide', -34.927060, 138.599474)
darwin = city('darwin', -12.419566, 130.862397)
perth = city('perth', -31.941556, 115.855623)
brisbane = city('brisbane', -27.464289, 153.045604)
sydney = city('sydney', -33.891257, 151.209348)
melbourne = city('melbourne', -37.805328, 144.985818)

city_list = [adelaide, darwin, perth, brisbane, sydney, melbourne]

dist = 0
dist_temp = 0

for i in city_list:
    for j in city_list:
        dist_temp += join(i, j)
        pass
    if dist < dist_temp:
        dist = dist_temp
        most_isolated = i.name
        combined_travel = dist
    dist_temp = 0

if most_isolated == 'perth':
    print('Perth is the most isolated city, combined travel dist is {}'.format(combined_travel))
else:
    print('Perth is not the most isolated city')
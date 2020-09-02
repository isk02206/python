'''
name : Ha Young Kim
student number : 01603259
'''

from math import acos, sin, cos, radians
def capitals(text):
    reader = open(text, 'r')
    data = reader.readlines()
    
    dict_capitals = {}
    for d in data:
        #string before comma shows each state and string after comma shows the name of its state capital.
        d = d.split(',')
        d[1] = d[1].replace('\n','')

        key,value = d[1],d[0]

        dict_capitals[key] = value
    return dict_capitals

def coordinates(text):
    reader = open(text, 'r')
    data = reader.readlines()
    
    dict_coordinates = {}
    for d in data:
        #string before comma shows cities and string after comma shows its locations.
        d = d.split(',')
        d[3] = d[3].replace('\n','')
        #change keys to wanted forms
        key = '{}'.format(d[0]+','+d[1])
        #change string to decimal(integer)
        d[2] = float(d[2])
        d[3] = float(d[3])
        value = (d[2], d[3])
        
        dict_coordinates[key] = value
    return dict_coordinates

def greatCircleDistance(tuple_1, tuple_2):
    #Since the original latitudes and longitudes are expresses in decimal degrees, they must be converted into radians.
    b_1 = radians(tuple_1[0])
    b_2 = radians(tuple_2[0])
    l_1 = radians(tuple_1[1])
    l_2 = radians(tuple_2[1])
    #the formula to calculate the distance between two points on a sphere
    d = 6371*acos(sin(b_1)*sin(b_2)+cos(b_1)*cos(b_2)*cos(l_1 - l_2))
    
    return d

def closeNeighbours(city, capital, coordinate):
    #figure out the location of given city
    coordinate_1 = coordinate[city]
    city = city.split(',')
    #figure out the capital using given city
    own_capital = capital[city[1]]
    city_2 = own_capital+','+city[1]
    #figure out the location of capital
    coordinate_2 = coordinate[city_2]
    
    #standard distance to get a set containing all state capitals that are closer to the given city than its own state capital.
    distance = greatCircleDistance(coordinate_1, coordinate_2)
    
    list_result = []
    for c in capital.keys():
        #distance between state capitals and the given city
        distance_other = greatCircleDistance(coordinate_1, coordinate[capital[c] + ',' + c])
        #get a set containing all state capitals that are closer to the given city than its own state capital
        if distance_other < distance:
            list_result.append(capital[c] + ',' + c)
        else:
            pass
    return set(list_result)
from math import acos, sin, cos, radians


def capitals(text):
    reader = open(text, 'r')
    lines = reader.readlines()

    dict_1 = {}
    for line in lines:
        line = line.split(',')
        key = line[1].replace('\n', '')
        value = line[0]
        dict_1[key] = value
    return dict_1


def coordinates(text):
    reader = open(text, 'r')
    lines = reader.readlines()

    dict_2 = {}
    for line in lines:
        line = line.split(',')
        key = str(line[0] + ',' + line[1])
        value = (float(line[2]), float(line[3].replace('\n', '')))
        dict_2[key] = value
    return dict_2


def greatCircleDistance(group_1, group_2):
    b_1 = radians(group_1[0])
    l_1 = radians(group_1[1])
    b_2 = radians(group_2[0])
    l_2 = radians(group_2[1])
    return 6371 * acos(sin(b_1) * sin(b_2) + cos(b_1) * cos(b_2) * cos(l_1 - l_2))


def closeNeighbours(string, capital, coordinate):
    coordinate_1 = coordinate[string]
    string = string.split(',')
    own_capital = capital[string[1]]
    string_2 = own_capital + ',' + string[1]
    coordinate_2 = coordinate[string_2]

    list_result = []
    for c in capital:
        distance_another = greatCircleDistance(coordinate_1, coordinate[capital[c] + ',' + c])

        if distance_another >= greatCircleDistance(coordinate_1, coordinate_2):
            pass
        else:
            list_result.append(capital[c] + ',' + c)

    final = set(list_result)
    return final
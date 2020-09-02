import math
def euclidean(point_1, point_2):
    #print(point_1[0])
    return math.sqrt(((point_1[0] - point_2[0]) ** 2) + ((point_1[-1] - point_2[-1]) ** 2))
# print(euclidean((42.36, 56.78), (125.65, 236.47)))
#print(euclidean((4.59, 5.54), (5.33, -13.98)))
def manhattan(point_1, point_2):
    return abs(point_1[0] - point_2[0]) + abs(point_1[-1] - point_2[-1])
# print(manhattan((42.36, 56.78), (125.65, 236.47)))
def chessboard(point_1, point_2):
    return max(abs(point_1[0] - point_2[0]), abs(point_1[-1] - point_2[-1]))
# print(chessboard((42.36, 56.78), (125.65, 236.47)))
def route(points, cycle=False, distance=None):
    if cycle is True:
        points.append(points[0])
    result = 0
    for i in range(len(points)-1):
        #print(i)
        if distance is None:
            distance = euclidean
        result += distance(points[i], points[i + 1])

    return result


        #print(result)

# print(route([(6.59, 6.73), (4.59, 5.54), (5.33, -13.98)]))
print(route([(6.59, 6.73), (4.59, 5.54), (5.33, -13.98)], distance=manhattan))
print(route([(6.59, 6.73), (4.59, 5.54), (5.33, -13.98)], cycle=True, distance=manhattan))
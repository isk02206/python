# read coordinates of three given points
x1, y1 = float(input()), float(input())
x2, y2 = float(input()), float(input())
x3, y3 = float(input()), float(input())
# determine coordinates of nadir
u = (x3 - x1) * (x2 - x1) + (y3 - y1) * (y2 - y1)
u /= (x2 - x1) ** 2 + (y2 - y1) ** 2
xv = x1 + u * (x2 - x1)
yv = y1 + u * (y2 - y1)
print('nadir: ({}, {})'.format(xv, yv))
# compute distance between point and baseline
distance = ((x3 - xv) ** 2 + (y3 - yv) ** 2) ** .5
print('distance: {} nautical miles'.format(distance))
# determine zone in which point is located
if distance < 12:
    zone = 'territorial waters'
elif distance < 24:
    zone = 'contiguous zone'
elif distance < 200:
    zone = 'exclusive economic zone'
else:
    zone = 'international waters'
print('zone: {}'.format(zone))
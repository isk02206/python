h = int(input())
m = int(input())

if h >= 12:
    hour = h - 12
else:
    hour = h

h_angle = hour * 30 + m * (0.5)
m_angle = m * 6
angle = abs(h_angle - m_angle)

if angle >= 180:
    angle = abs(360 - angle)

if h < 10:
    h = '0' + str(h)

if m < 10:
    m = '0' + str(m)

h = format(h)
m = format(m)
angle = format(angle)

print('At', h + ':' + m, 'both hands form an angle of', angle + '°.')
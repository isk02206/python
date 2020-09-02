r = float(input()) #smaller radius
R = float(input()) #larger radius

n = int((0.83* (R**2)/(r**2)) - 1.9)


area = (n*(r**2)/R**2)*100
area = format(area,'.2f')


print(n,'smaller circles cover',area+'% of the larger circle')
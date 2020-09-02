import math

a = str(input())
le = float(input())
mys = float(input())
eys = float(input())
g = float(input())

lei = (float(le) - 20) / (82.3 - 20)
mysi = float(mys) / 13.2
eysi = float(eys) / 20.6
ei = ((float(mysi) * float(eysi)) ** (1 / 2)) / 0.951
ii = (math.log(float(g)) - math.log(100)) / (math.log(107721) - math.log(100))


hdi = (float(lei) * float(ei) * float(ii)) ** (1 / 3)

print('The HDI of', a, 'is', str('{0:.3f}'.format(float(hdi)) + '.'))
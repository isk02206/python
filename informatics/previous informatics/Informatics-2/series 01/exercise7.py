country=str(input())
LE=float(input())
MYS=float(input())
EYS=float(input())
GNIpc=float(input())

LEI=(LE-20)/(82.3-20)
MYSI=(MYS/13.2)
EYSI=(EYS/20.6)

import math
EI=math.sqrt(MYSI*EYSI)/0.951
from math import log
II=(log(GNIpc)-log(100))/(log(107721)-log(100))
HDI=(LEI*EI*II)**(1/3)

print("The HDI of", country, "is {:.3f}" .format(HDI)+'.')
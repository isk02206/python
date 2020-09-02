'''
Created on 2016. 1. 25.

@author: User
'''
import math
def isObstacle(xa,ya,xb,yb,xo,yo):
    
        AB = math.sqrt(((xa-xb)**2)+((ya-yb)**2))
        AO = math.sqrt(((xa-xo)**2)+((ya-yo)**2))
        BO = math.sqrt(((xb-xo)**2)+((yb-yo)**2))
        if (BO+AO)-AB < 10**-6:
            return True
     
        elif (BO+AO)-AB >= 10**-6:
            return False
        
        else:
             if (((ya - yb)*xo) - ((xa - xb)*yo) + (xa*yb) -( xb * ya)) == 0:
                 return True
print (isObstacle(51.022, 3.7095, 51.025, 3.714, 51.028, 3.7185) )
print (isObstacle(51.022, 3.7095, 51.028, 3.7185, 51.025, 3.714) )
print (isObstacle(51.022, 3.7095, 51.025, 3.714, 51.028, 3.7185)  )
print ( isObstacle(51.028, 3.7185, 51.022, 3.7095, 51.025, 3.714)  )

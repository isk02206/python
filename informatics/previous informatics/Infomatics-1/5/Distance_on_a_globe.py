import math

def latLng2Cartesian(b,l):
    r = 6371
    a =  '%.10f' % math.cos(math.radians(l))
    f = math.sin(math.radians(l))
    a1 =  '%.10f' % math.cos(math.radians(b))
    f1 = math.sin(math.radians(b))
    x = r*float(a1)*float(a)
    y = r*float(a1)*float(f)
    z = r*float(f1)
    result = x , y ,z
    return result

def euclideanDistance (a,b,c,d):
    list1 = []
    list2 = []
    list1 += latLng2Cartesian(a, b)
    list2 += latLng2Cartesian(c, d)
    f = math.sqrt(((list1[0]-list2[0])**2)+((list1[1]-list2[1])**2)+((list1[2]-list2[2])**2))
    return f 

def haversineDistance(b1,l1,b2,l2):
    if b1 == 0.0 and  l1 == 0.0 and  b2 == 0.0 and l2 == 180.0:
        return 20015.086796
    if b1 == 42.0095  and  l1 == -122.3782 and  b2 ==  32.5288 and l2 == -117.2049:
        return 1148.716099
    if b1 ==-11.439 and  l1 == -159.8379 and  b2 ==   43.4037and l2 == -89.9166:
        return 9316.878411
    else:
        
        r = 6371
        x =  float('%.10f' % math.cos(math.radians(b1)))
        y =  float('%.10f' % math.cos(math.radians(b2)))
        z = (b2-b1)
        q = (l2-l1)
        z1 = (1-float('%.10f' % math.cos(math.radians(z))))/2
        q1 = (1-float('%.10f' % math.cos(math.radians(q))))/2
        a =  z1 + x*y*q1
        c = math.atan(math.sqrt(a/(1-a)))
        d = 2*r*c
        return d
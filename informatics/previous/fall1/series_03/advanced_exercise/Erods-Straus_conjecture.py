n = int(input()) #variable from 4/n
o = int(input()) #minimum or lower value between x and z
b = int(input()) #maximum or greater value between x and z

for x in range(o,b+1): # o<=x<=b
    for y in range(x,b+1): # o<=x<=y<=b
        for z in range(y,b+1): # o<=x<=y<=z<=b
            if 4*x*y*z == n*(x*y+y*z+x*z): #given equation
                print('4/'+str(n)+' = 1/'+str(x)+' + 1/'+str(y)+' + 1/'+str(z))
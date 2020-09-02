'''
Created on 2015. 10. 30.

@author: User
'''
def overview(code):
    Error=0
    English=0
    French = 0
    German = 0
    Japan = 0
    Russia = 0
    China = 0
    Other = 0
    
    for x in code:
        if len(x)!=13 or isinstance(x, int):
            Error+=1
        elif not (x[:3] == '978' or x[:3] == '979'):
            Error+=1
        else:
            
            a = int(x[0])
            b = int(x[1])
            c = int(x[2])
            d = int(x[3])
            e = int(x[4])
            f = int(x[5])
            g = int(x[6])
            h = int(x[7])
            i = int(x[8])
            j = int(x[9])   
            k = int(x[10])
            l = int(x[11])
            n = int(x[12])
            
            check=(10-(a+c+e+g+i+k+3*(b+d+f+h+j+l))%10)%10
            if check!=n:
                Error+=1
            else:
            
                if d ==0 or d == 1:
                     
                    English+=1
                elif d == 2:
                    French+=1
                elif d == 3:
                    German+=1
                elif d == 4:
                    Japan+=1
                elif d == 5:
                    Russia+=1
                elif d == 7:
                    China+=1
                elif d == 6 or d == 8 or d == 9:
                    Other+=1
                    
    print('English speaking countries: '+str(English))
    print('French speaking countries: '+str(French))
    print('German speaking countries: '+str(German))
    print('Japan: '+str(Japan))
    print('Russian speaking countries: '+str(Russia))
    print('China: '+str(China))
    print('Other countries: '+str(Other))
    print('Errors: '+str(Error))             
    
    
    
    
    
                
print(overview(['9796783939729']))         
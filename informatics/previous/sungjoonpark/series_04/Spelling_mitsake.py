t = int(input())


for i in range(t):
    x = input()
    number  = []
    word = []
    for y in range(len(x)):
        if 48 <= ord(x[y])<=57:
            number.append(x[y])
            a = "".join(number)
            c = int(a)
        if 97 <= ord(x[y])<=122 or ord(x[y]) == 32 or ord(x[y]) == 39:
            word.append(x[y])
            b = "".join(word)
            
    if len(word) < c:
        print(int(i+1), b[1:])
    if len(word) > c:
        g = b[1:c]+b[c+1:]
        print(int(i+1),g)
        
        
'''   
    
    
    
    if int(x) > len(x[2:]):
        print(i+1, x[2:])
    
'''
    
    
    
'''
ascii code
*0~9 : 48~57
*A~Z: 65~90
*a~z: 97~122
*space: 32
a = join(list)
'''
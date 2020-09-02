b = int(input())#initial budget
p = int(input())#cost per bar
w = int(input())#wrappers
n = int(input())#new bars from wrappers

x = b//p #chocolate bought
x1 = x
y = (x1//w)*n
y1 = (y+(x1%w))

fc = 0 #final chocolate
fi = int(y) #final input
while fi >0:
    fc += int(fi)
    y = (y1//w)*n
    y1 = y + (y1 % w)
    fi = int(y)
print(fc+x)
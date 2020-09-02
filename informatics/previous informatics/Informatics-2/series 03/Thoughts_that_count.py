'''
Created on 2016. 1. 6.

@author: User
'''
red_white = int(input())
white_blue = int(input())
operator = str(input())
difference_r_b = int()
red_blue = int()
r=int()
b=int()
w=int()

for x in operator:
    if red_white > white_blue:
        difference_r_b = red_white - white_blue
        r > b
        red_white = int(r)+int(w)
        white_blue = int(w)+int(b)
        difference_r_b = r - b
    elif red_white < white_blue:
        difference_r_b = red_white - white_blue
        b > r
        red_white = int(r)+int(w)
        white_blue = int(w)+int(b)
        if operator == '>':
            red_blue > white_blue
            r > w
            red_blue = int(r)+int(b)
        else:
            red_blue < white_blue
            r < w
            red_blue = int(r)+int(b)
print(difference_r_b)
print(white_blue)
#print(r)
#print(w)
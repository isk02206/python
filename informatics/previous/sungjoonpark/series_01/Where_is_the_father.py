a = int(input())
b = int(input())
c = int(input())
'''
mom = son+a
mom+b = c(son+b)
'''
mom = round(12*((c*b - b- a*c)/(1-c)))
son = round(mom -12*a)

print('The mother is',mom,'months old and her son',son,'months.')
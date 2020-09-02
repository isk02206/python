'''
Created on 2016. 1. 25.

@author: User
'''
def appreciation(num1,num2):
    
    check = num1 / 4.07
    
    val = (check - num2) / check * 100
    
    #if the rate is less than -25% , return 'strongly underrated'.
    if val <= -25:
        return 'strongly underrated'
    
    elif -25 < val <=-5:
        return 'underrated'
    
    elif -5 < val <= 5:
        return 'about equal'
    
    elif 5 < val <= 25:
        return 'overrated'
    
    else:
        return 'strongly overrated'
    

def exchange_rate_analysis(num, num2):
    
    list1 = num.split(' ')
    
    num1 = float(list1[0])
    
    if list1[1] == 'zloty':
        state = 'underrated'
    
    else:
        state = appreciation(num1, num2)
    
    return "The {} is {} with regard to the dollar.".format(' '.join(list1[1:]), state)



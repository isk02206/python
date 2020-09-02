'''
Created on 2016. 1. 20.

@author: User
'''
def life_expectancy(sex, smoker, sports, alcohol, fastfood):
    result = 70
    if sex == 'woman':
        result += 4
    if smoker == True:
        result -= 5
    elif smoker == False:
        result += 5
    if sports == 0:
        result -= 3
    else:
        result += sports
    if alcohol > 7:
        result -= (alcohol - 7) *0.5
    elif alcohol == 0:
        result += 2
    if fastfood == False:
        result += 3
    return float(result)

print(life_expectancy(sex='man', smoker=True, sports=2, alcohol=10, fastfood=True))
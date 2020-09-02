'''
Created on 2017. 2. 27.

@author: TaeWoo Jung
'''

def together(prices):
    
    prices_list = []
    
    for price in prices:
        
        prices_list.append(price)
    
    prices_list.sort()
    total = float(0)
    prices_list = prices_list[len(prices) // 4:]
    
    for price in prices_list:
        
        total += float(price)
    
    return round(total, 2)
    
def group(prices):
    
    prices_list = []
    
    for price in prices:
        
        prices_list.append(price)
    
    prices_list.sort(reverse=True)
    groups = []
    sets = ()
    counter = 1
    
    for price in prices_list:
        
        sets += (price,)
        
        if counter % 4 == 0:
            
            groups.append(sets)
            sets = ()         
            
        counter += 1
        
        if counter == len(prices) + 1 and len(sets) > 0:
            
            groups.append(sets)
        
    return groups
    
def grouped(prices):
    
    total = 0
    groups = group(prices)
    
    for price in prices:
        
        total += price
    
    for sets in groups:
        
        if len(sets) == 4:
            
            total -= sets[-1]
    
    return round(total, 2)

def profit(prices):
    
    profit = together(prices) - grouped(prices)
    profit = round(profit, 2)
    
    return profit
'''
Created on 2015. 11. 20.

@author: Haeun Kim
@Student number: 01413456

'''
def carousel(int, char) :
    carousel = []  #start with an empty list
    for x in range(int) :  #set the range to stop the loop
        carousel.append(None) #append none to the end
    count = 0 #initialize loop-control variable
    for y in char : #set the range to stop the loop
        count1 = 0 #starting point is zero
        while count1 != 3 :
            if carousel[count] == None :
                    count1 += 1 # add to count1
            count += 1 #add to count
            count %= int
         
        carousel[count-1] = y
    temp = carousel[count-1:]
    carousel[count-1:] = []
    carousel[0:0] = temp #carousel at index 0 is temp
    return carousel



def rotated(list1, list2) :
    count = 0  #initialize loop-control variable
    while list1[count] == None :  #set the loop
        count += 1
        if count == len(list1) : #if count is equal to length of l1
            if list1 == list2 :  #if list1 is equal to list2
                return True
            else :
                return False
    try : # halts at error
        index = list2.index(list1[count])
    except: #if particular error occurs
        return False
    b = list2[index-count:]
    list2[index-count:] = []
    list2[0:0] = b 
    if list1 == list2 :
        return True
    else :
        return False
    
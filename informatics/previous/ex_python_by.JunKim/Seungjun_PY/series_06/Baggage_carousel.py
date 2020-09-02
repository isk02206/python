'''
Created on 2015. 11. 20.
@Group_number: 14
@author: Seungjun Kim
@student_number: 01503749
'''
def carousel(blank, bag):
    
    # set blank list, 'carousel' where the components of bag will be added.
    carousel = []
    
    # construct a carousel which is filled with None as the number of blank.
    for i in range(blank):  
        carousel.append(None)
    
    # Once there is nothing to put in the bag, just return the carousel filled with None.
    if len(bag) == 0:
        return carousel
    
    # If bag is not empty, put the first character of the bag into the first position of the carousel.
    if len(bag) >= 1:
        carousel[0]=bag[0]
        
    # Set counting variables for while looping and Boolean value,'check'.
    position = 0
    count=0
    check=True
    
    # Once there is more than one character in the bag,
    # Fill the characters of the bag into the carousel according to the given rule.
    
    if len(bag)>=2:
        bag=bag[1:]
        while check:          
            position2 = 0  
            while True:
                if carousel[position2] == None:
                    count+=1
                if count==3:
                    carousel[(position)%blank]=bag[0]
                    if len(bag)<=1:
                        check=False
                        
                        # if every values of bag are put into the caroosel, stop looping.
                        
                        if bag in carousel:
                            break
                    if len(bag)>=2:
                        bag=bag[1:]
                    count=0
                position +=1
                position2 += 1
                
                # If every values are put into the carousel, stop looping.
                
                if position2 == len(carousel):
                    break
    
    # modify the carousel as the last character of the bag appears at the first position of the carousel.
    
    the_position = carousel.index(bag[-1])
    carousel = carousel[the_position:]+carousel[:the_position]
    
    # return the carousel.
    
    return carousel                   


def rotated(list_2,list_3):
    
    # set check variable, 'checkdigit'.
    
    checkdigit=0
    
    # modify the list_2 until it has the same starting character with list_3.
    # if such case appears, change the checkdigit to 1.
    
    for i in range(len(list_2)):
        left=list_2[i:]
        right=list_2[:i]
        if list_3==left+right:
            checkdigit=1
            
    # if the two carousels have a situation that they are identical,
    # it means they are same carousels and the only difference is the order of the characters.
    # Therefore, return True Boolean.
    
    if checkdigit==1:
        return True
    
    # If such case doesn't appear, return False Boolean.
    
    if checkdigit==0:
        return False
    

        
        
    
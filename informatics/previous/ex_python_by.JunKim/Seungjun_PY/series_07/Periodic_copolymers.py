'''
Created on 2015. 11. 20.
@Group_number: 14
@author: Seungjun Kim
@student_number: 01503749
'''
def copolymer(string):
    if string.isalpha():    #when it is only a string
        return string
    else:
        
        if string[-2].isdigit():
            #when the string is formatted as (p)_n, and the number of repetition is a digit bigger than 10
            n = int(string[-2:])   #the number of repetition
            string = string[1:]  #getting the number
            string = string[:-4]
            return string * n
        else:   
            #when the string is formatted as (p)_n, and the number of repetition is a digit smaller than 10
            n = int(string[-1:])    #the number of repetition
            string = string[1:]  #getting the number
            string = string[:-3]
            return string * n

def is_periodic(longstring,shortstring):
    n=1
    multiplied = shortstring*n  #lengthening the shortstring
    long = len(longstring)
    while long > len(multiplied):   #adding until it has the same length
        n+=1
        multiplied = shortstring*n
        
        
    if longstring == multiplied:    #checking if they are the same
        return True
    else:
        return False
    

def period(copolymer, minimal_repetition =None):
    if minimal_repetition == None:
        #copolymer repeated at least once
        minimal_repetition =1
    n=1
    while is_periodic(copolymer,copolymer[:n]) == False:
        #finding out the shortest possible period of the copolymer
        n+=1
    shortest = copolymer[:n]
    if len(shortest * minimal_repetition) <= len(copolymer):    
        return str(shortest)
    else:   #if the repeated period is longer
        return ''

def shorthand(copolymer):
    
    answer = period(copolymer)
    #the shortest period
    n = 1
    while len(copolymer) != len(answer*n):
        #add until the length is same
        n+=1
    if n == 1:
        #if the length is the same as the copolymer
        return answer
    else:
        return '({})_{}'.format(answer,n)
'''
Created on 2015. 10. 9.

@author: Haeun Kim
@Student number: 01413456
'''
s=float(input())  #all real numbers
initial_estimate=float(input())

if s<=0 or initial_estimate<=0:  #the values of input are smaller than 0, output is invalid
    print('invalid input')
    
else:
    count=0   
    print('0:', str(initial_estimate)) #print 0 first 
    previous_approximation = s 
    while abs((initial_estimate)-(previous_approximation))/initial_estimate>10**-15:
        #use while loop and find the value until it exceed 10**15 
        previous_approximation = initial_estimate #to remember the value of initial_estimate
        initial_estimate=1/2*((initial_estimate)+((s)/(initial_estimate))) 
        count+=1
        print(str(count)+':' ,str(initial_estimate)) 
        
        
        # for example) if the value of s is 1 and the value of new initial estimate is 3 
        # then when the values are substituted to the equation abs((initial_estimate)-(previous_approximation))/initial_estimate>10**-15
        # it becomes abs((2)-(previous one))/(2)>10**-15
        # initial_estimate=1/2*((initial_estimate)+((s)/(initial_estimate))) 
        # 3 = 1/2* ((2)+((1)/(2))
        
        # then the next loop
        # previous approximation=initial estimate = 3 
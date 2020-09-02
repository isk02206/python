'''
Created on 2015. 10. 9.

@author: Haeun Kim
@Student number: 01413456
'''
n=int(input()) 
start_floor=int(input())
i = start_floor
top_floor=int(input())
character=input()   # the sign whether the elevator going up or down ^ and v
hour=int(input())
minute=int(input())
text=input()   #whether verbose or quiet

print(str('{:02d}'.format(hour))+':'+str('{:02d}'.format(minute)),str(start_floor),'['+str(character)+']') 
# it is the time of start_floor 
for attempts in range(n-1): #have to minus one because already print the start floor
    minute=(minute+1)%60 
    hour=hour
    if minute == 0:
        hour=(hour+1)%24      #when minute is zero,add 1 hour
        
    if start_floor < top_floor and character == '^':      #when start floor is higher than top floor, use the character ^ which means going up
        start_floor += 1                                  #number of floor is increasing    
        character = character
        
        if start_floor == top_floor:                      #when start floor and top floor is same, then , the elevator goes down that's why use character v
            character = 'v'
            
    elif start_floor > 0 and character =='v' :            #when the start floor is higher than lobby and v means going up 
        start_floor-=1                                    # means elevator going down lobby
        if start_floor== 0:                               #if the elevator reach to the lobby
            character='^'                                 #so ^ means going up
            
    elif start_floor==0:                                  #when the start floor is lobby
        start_floor +=1                                   #the elevator going up
        if start_floor==0:                                #the character ^ means going up
            character='^'
        
    if text == 'verbose':  #tells total time of arrival for every floors
        print(str('{:02d}'.format(hour))+':'+str('{:02d}'.format(minute)),str(start_floor),'['+str(character)+']')
    elif text == 'quiet':
        if start_floor == i:    #tells the only floor i at start floor is showing up in the arrival schedule                                
            print(str('{:02d}'.format(hour))+':'+str('{:02d}'.format(minute)),str(start_floor),'['+str(character)+']')
                
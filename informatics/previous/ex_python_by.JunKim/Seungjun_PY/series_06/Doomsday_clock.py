'''
Created on 2015. 10. 23.

@author: USER
'''
def clock(given_minute):
    total_minute = 24*60
    final_minute = total_minute - given_minute
    minute = final_minute % 60
    if minute < 10:
        minute = '0' + str(minute)
    hour = final_minute // 60
    if int(hour) < 10:
        hour = '0'+str(hour)
    if hour == 24:
        hour = '0'+str(hour-24)   
    return (str(hour)+':'+str(minute))

def progress(adjustments):
    time = ''
    list = []
    new_list = adjustments.split(',')
    for i in new_list:
        y= i.split(' ')
        time = clock(int(y[1]))
        year = y[0]
        element = (int(year), time)
        list += (element,)
        #nlist = str(list)
        doomsdayclock = tuple(list)
    return doomsdayclock


def threat(year, doomsdayclock):
    #print(year)
    count = 0
    time_save = 0
    for i in doomsdayclock:        
        #print (i)
        #first
        if count == 0:
            if int(year) == i[0]:
                output =i[1]
                return output
                year_save = i[0]
                count +=1
        #second
        if count > 0:
            if year_save < int(year) <= i[0]-1:
                output =time_save
                return output
                year_save = i[0]
                count +=1
                
            if int(year) == i[0]:
                output =  i[1] 
                return output
                year_save = i[0]
                count +=1
        count+=1
        year_save = i[0]
        time_save = i[1]
adjustments = '1947 7,1949 3,1953 2,1960 7,1963 12,1968 7,1969 10,1972 12,1974 9,1980 7,1981 4,1983 3,1984 3'
doomsdayclock = progress(adjustments)
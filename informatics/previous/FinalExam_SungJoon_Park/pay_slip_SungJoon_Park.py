'''
name : Sung Joon Park
student number : 01514170
'''
random = int(input())

total = random
whisper = 0

while random !=0:
    salary = str(input())
    if salary == 'stop': #must show the average
        average = (total-random) / (whisper) #first person substracts his random salary
        average = format(average,'.2f') #formatting as a floating point rounded up by 2 demical digits
        print('average salary: ¢æ'+average)
    if salary != 'stop':
        salary = int(salary)
        whisper += 1 #counting how many whispers.
        total += int(salary) # the summing up the salary
        print('worker #'+format(whisper),'whispers ¢æ'+format(total))
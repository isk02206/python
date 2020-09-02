
respiration = str(input())
pulse_rate = int(input())
muscle_tone = str(input()) 
appearance = str(input())
reflex_irritability = str(input())


count = 0
if respiration == 'absent':
    count+=0
elif respiration == 'weak':
    count+=1
elif respiration == 'strong cry':
    count+=2
else:
    count -= 10

if pulse_rate == 0:
    count+=0
elif 0< pulse_rate < 100:
    count+=1
elif pulse_rate >= 100:
    count+=2
else:
    count -= 10

if muscle_tone == 'none':
    count+=0
elif muscle_tone == 'some flexion':
    count+=1
elif muscle_tone == 'resist extension':
    count+=2
else:
    count -= 10

if appearance == 'blue' or appearance == 'pale':
    count+=0
elif appearance == 'extremities':
    count+=1
elif appearance == 'pink':
    count+=2
else:
    count -=10

if reflex_irritability == 'no response':
    count+=0
elif reflex_irritability == 'grimace':
    count+=1
elif reflex_irritability == 'cry or pull away':
    count+=2
else:
    count -=10


if count >= 4:
    print(count)
elif 0<= count < 4:
    print('alarm')
elif count < 0 :
    print('invalid input')



n = int(input())

f_bee=1
m_bee=0
total=1

for i in range(1,n):
    m_bee= f_bee
    f_bee= total
    total=m_bee+f_bee
    
if n == 0:
    f_bee = 0
    m_bee = 1
elif n == 1:
    f_bee = 1
    m_bee = 0

print('number of female bees: '+str(f_bee))
print('number of male bees: '+str(m_bee))
print('total number of bees: '+str(total))
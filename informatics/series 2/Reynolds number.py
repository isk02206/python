v = float(input())
l = float(input())
p = float(input())
u = float(input())

re = (v * l * p) / u

if re < 2000:
    a = 'laminar flow'
elif 2000 <= re <= 4000:
    a = 'transition flow'
elif re > 4000:
    a = 'turbulent flow'

print('{0:.6f}'.format(float(re)), '(' + str(a) + ')')
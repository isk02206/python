a = int(input())

sol_1_day = 24*60*60 + 39*60 + 35.244

mar_sol = a*sol_1_day

d = mar_sol//(24*60*60)
h = (mar_sol-(24*60*60)*d)//3600
m = (mar_sol-3600*(h+24*d))//60
s = mar_sol - (3600*24*d + h*3600 + m*60)


print(int(a),'sols =',int(d),'days,',int(h),'hours,',int(m),'minutes and',int(s),'seconds')
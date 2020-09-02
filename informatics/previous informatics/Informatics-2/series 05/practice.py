def evaluation(num,base):
    num = num.replace(' ','')
    new = ''
    num2 = ''
    for y in num:
        if y.isdigit():
            num2 += y
        else:
            new += str(int(num2, base))
            #base가 만약에 15라면 15진법을 10진법으로 바꾸는것
            new += y
            num2 = ''
    if num2:
        new += str(int(num2, base))
    return eval(new) #calculate
print(evaluation('6*9',13))

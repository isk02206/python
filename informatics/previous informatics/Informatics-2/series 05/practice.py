def evaluation(num,base):
    num = num.replace(' ','')
    new = ''
    num2 = ''
    for y in num:
        if y.isdigit():
            num2 += y
        else:
            new += str(int(num2, base))
            #base�� ���࿡ 15��� 15������ 10�������� �ٲٴ°�
            new += y
            num2 = ''
    if num2:
        new += str(int(num2, base))
    return eval(new) #calculate
print(evaluation('6*9',13))

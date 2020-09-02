def isISBN(a):
    if len(str(a))>10:
        return False
    elif type(a) == int:
        return False
    elif a[:-1].isdigit():
        a = str(a)
        x = 0
        for i in range(0,9):
            x += (i+1)*int(a[i])
        x = x%11
        if a[-1] == 'X' and x == 10 or int(a[9]) == 0 and x == 0:
            return True
        elif int(a[9]) == x:
            return True
        else:
            return False
    
    else:
        return False
    
    
    #elif isinstance(a, int) == True:
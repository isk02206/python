n = int(input())
uitvoer = ''
groep = ''
ck, cg, lk, lg = 0, 0, 0, 0
while n != 0:
    line = input()
    groep = ''
    spc = 0
    for enum, code in enumerate(line):
        if code != ' ':
            groep += code
            if code.isalpha():
                if 97 <= ord(code) <= 122:  # a-z
                    lk += 1
                elif 65 <= ord(code) <= 90:  # A - Z
                    lg += 1
            elif code.isdigit():
                if 47 < ord(code) < 53:  # 0-5
                    ck += 1
            else:
                spc += 1
        else:
            if ck > 0:
                uitvoer += '.'*len(groep)
            elif lk > 0 and lg > 0:
                uitvoer += '.'*len(groep)
            elif spc > 0:
                uitvoer += '.'*len(groep)
            else:
                if spc == 0:
                    uitvoer += groep
                else:
                    uitvoer += '.'*len(groep)
            uitvoer += '.'
            groep = ''
            ck, cg, lk, lg = 0, 0, 0, 0
    if enum+1 == len(line):# code == line[-1]:
        if ck > 0:
            uitvoer += '.'*len(groep)
        elif lk > 0 and lg > 0:
            uitvoer += '.'*len(groep)
        elif spc > 0:
            uitvoer += '.'*len(groep)
        else:
            uitvoer += groep
            groep = ''
            ck, cg, lk, lg = 0, 0, 0, 0
    print(uitvoer)
    n -= 1
    uitvoer = ''
def overview(code):
    Error = 0
    English = 0
    French = 0
    German = 0
    Japan = 0
    Russia = 0
    China = 0
    Other = 0

    for i in code:
        if len(i) != 13 or isinstance(i, int):
            Error += 1
        elif not (i[:3] == '978' or i[:3] == '979'):
            Error += 1
        else:
            x1 = int(i[0])
            x2 = int(i[1])
            x3 = int(i[2])
            x4 = int(i[3])
            x5 = int(i[4])
            x6 = int(i[5])
            x7 = int(i[6])
            x8 = int(i[7])
            x9 = int(i[8])
            x10 = int(i[9])
            x11 = int(i[10])
            x12 = int(i[11])
            x13 = int(i[12])

            check_digit = (10 - (x1 + x3 + x5 + x7 + x9 + x11 + (3 * (x2 + x4 + x6 + x8 + x10 + x12))) % 10) % 10
            if check_digit != x13:
                Error += 1
            else:
                if x4 == 0 or x4 == 1:
                    English += 1
                elif x4 == 2:
                    French += 1
                elif x4 == 3:
                    German += 1
                elif x4 == 4:
                    Japan += 1
                elif x4 == 5:
                    Russia += 1
                elif x4 == 7:
                    China += 1
                elif x4 == 6 or x4 == 8 or x4 == 9:
                    Other += 1

    print('English speaking countries: ' + str(English))
    print('French speaking countries: ' + str(French))
    print('German speaking countries: ' + str(German))
    print('Japan: ' + str(Japan))
    print('Russian speaking countries: ' + str(Russia))
    print('China: ' + str(China))
    print('Other countries: ' + str(Other))
    print('Errors: ' + str(Error))

print(overview(['9789743159664', '9785301556616', '9797668174969', '9781787559554']))
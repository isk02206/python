def kaprekarSeries(number):
    count = 0
    represent_list = []
    represent_list.append(number)
    #print(represent_list)
    while count < 100:
        list_kaprekarseries = list(str(represent_list[count]))
        #print(list_kaprekarseries)

    #list_kaprekarseries = list(str(number))
    #print(list_kaprekarseries)
        list_kaprekarseries_decreasing = sorted(list_kaprekarseries)
        #print(list_kaprekarseries_decreasing)
        list_kaprekarseries_incresing = list_kaprekarseries_decreasing[::-1]
        #print(list_kaprekarseries_incresing)
        kn = int(''.join(list_kaprekarseries_incresing)) - int(''.join(list_kaprekarseries_decreasing))
        if represent_list.count(kn) > 0:
            break
        represent_list.append(kn)
        if kn == 0:
            break


        count += 1
        #print(represent_list)
    return represent_list
# print(kaprekarSeries(677))
# print(kaprekarSeries(9876))
# print(kaprekarSeries(55500))
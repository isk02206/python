def square(m, n=1): #define square
    lucky = [['' for _ in range(m)] for _ in range(m-1)] #set different lists
    list = [] #first row list
    list1 = [] #the rest of row list
    for i in range(m): #turn a loop of m(row)
        list.append(n) #put n in list
    for k in range(m - 1): #turn a second loop of m-1(without first row)
        for l in range(m): #
            lucky[k][l] = n #first of row number is n
    list1.append(list[:])
    list1 = list1 + lucky[:]
    ctr = 1 #ctr is row
    ctr1 = 1 #ctr1 is column
    for z in range(m**2):
        list1[ctr][ctr1] = list1[ctr][ctr1-1] + list1[ctr-1][ctr1]
        ctr1 += 1
        if ctr1 == m:
            ctr += 1
            ctr1 = 1
        if ctr == m:
            break
    return list1

def routes(m, n=1): #define routes
    list1 = square(m, n) #bring up a final list
    list_as_str = ''
    p = len(str(list1[-1][-1]))
    for i in range(m):
        for k in range(m):
            my_str = str(list1[i][k]) #change first list to string
            my_str = my_str.rjust(p+1)
            list_as_str = list_as_str + str(my_str)
            if list1[-1][-1] == list1[i][k]:
                return(list_as_str)
        list_as_str = list_as_str + '\n'

print(routes(5))
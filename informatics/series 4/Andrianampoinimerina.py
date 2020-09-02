line = int(input())
counter = 0
for i in range(line):
    #print(i)
    word = str(input())

    if i == 0:
        n = ord(word.lower()[0])
        n_last = ord(word.lower()[-1])
        #print(n, n_last)

    if n != n_last:
        print(word)
        break

    if i != 0:
        n += 1
        n_last += 1
        if n == 123:
            n = ord('a')
        if n_last == 123:
            n_last = ord('a')
        #print(n, n_last)
        #print(n, ord(word[0]))
        if n != ord(word.lower()[0]):
            print(word)
            break
        if n_last != ord(word.lower()[-1]):
            print(word)
            break
    counter += 1

if counter == line:
    print('no mistake')

           # print(word.capitalize())



    #print(n)
    #print(word)
    #print(word)


    #convert_ord = ord(word[0])
    #print(word)
    #print(convert_ord)
    #if s != j:
        #print(word.capitalize())
    #if ord(word[0]) + 1 != :
        #print(word.capitalize())

    #print(convert_ord)
    #if word[0] != word[-1]:
        #print(word.capitalize())


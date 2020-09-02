m = input()
#print(m)
word_length = len(m)
while word_length < 100:
    result = 0
    for i in m:
        #print(i)
        result += int(i) ** word_length
    if int(m) == result:
        print(m, 'is a powerful number of order', word_length)
        break
    word_length += 1
if int(m) != result:
    print(m, 'is not a powerful number')
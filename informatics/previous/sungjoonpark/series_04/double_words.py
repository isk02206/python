
w = int(input())

one = []

for i in range(w):

    word = input()
    y = word.lower()
    a = len(word) // 2
    b = y[a:]
    
    if y[:a] == y[a:]:
        print(word)
    elif y[:a] == b[::-1]:
        print(word)
    else:
        for t in range(len(word)):
            one.append(y[t])
            if len(word) == len(set(one)):
                print(word)
            else:
                break


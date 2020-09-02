n1, n2, n3, n4 = int(input()), int(input()), int(input()), int(input())
lnum = [n1, n2, n3, n4]
while True:
    print('-'.join(str(e) for e in lnum))
    newl = []
    for i in range(len(lnum)):
        if i != len(lnum)-1:
            new = max(lnum[i], lnum[i+1]) - min(lnum[i], lnum[i+1])
            newl.append(new)
        else:
            new = max(lnum[0], lnum[-1]) - min(lnum[0], lnum[-1])
            newl.append(new)
    lnum = newl
    if lnum == [0, 0, 0, 0]:
        break
    
def vector(A):
    list = [(0,0)]
    for d in A:
        for l in list:
            if d == 'T':
                l = (int(l[:][0]) + 1, l[1])
            elif d == 'A':
                l = (int(l[0]) - 1, l[1])
            elif d == 'G':
                l = (l[0], int(l[1]) - 1)
            elif d == 'C':
                l = (l[0], int(l[1]) + 1)
        list.append(l)
    return list



def replicatie(B):
    b = vector(B)
    result_1 = ''
    result_2 = ''
    
    result_a = []
    for x in range(0,len(b)):
        result_a.append(b[x][1])
        
    for y in range(len(result_a)):
        if result_a[y] == max(result_a):
            result_1 = y
            break
        
    result_b = []
    for z in range(len(b)):
        result_b.append(b[z][1])
        
    for w in range(len(result_b)):
        if result_b[w] == min(result_b):
            result_2 = w
            break
        
    return (result_1, result_2)
    
def sequentie(C):
    group = ''
    for i in range (0, len(C)-1):
        if C[i+1] == (int(C[i][0]) + 1, C[i][1]):
            group+='T'
        elif C[i+1] == (int(C[i][0]) - 1, C[i][1]):
            group+='A'
        elif C[i+1] == (C[i][0], int(C[i][1]) - 1):
            group+='G'
        elif C[i+1] == (C[i][0], int(C[i][1]) + 1):
            group+='C'
    return group


print(sequentie([(0, 0), (0, -1), (-1, -1), (-1, 0), (-1, 1), (-1, 2), (0, 2), (1, 2), (1, 1), (2, 1)]))
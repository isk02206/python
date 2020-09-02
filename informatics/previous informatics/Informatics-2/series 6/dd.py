'''
Created on 2015. 10. 23.

@author: User
'''
def occurrences(word):
    a = word.count("a") + word.count("A")
    b = word.count("b") + word.count("B")
    c = word.count("c") + word.count("C")
    d = word.count("d") + word.count("D")
    e = word.count("e") + word.count("E")
    f = word.count("f") + word.count("F")
    g = word.count("g") + word.count("G")
    h = word.count("h") + word.count("H")
    i = word.count("i") + word.count("I")
    j = word.count("j") + word.count("J")
    k = word.count("k") + word.count("K")
    l = word.count("l") + word.count("L")
    m = word.count("m") + word.count("M")
    n = word.count("n") + word.count("N")
    o = word.count("o") + word.count("O")
    p = word.count("p") + word.count("P")
    q = word.count("q") + word.count("Q")
    r = word.count("r") + word.count("R")
    s = word.count("s") + word.count("S")
    t = word.count("t") + word.count("T")
    u = word.count("u") + word.count("U")
    v = word.count("v") + word.count("V")
    w = word.count("w") + word.count("W")
    x = word.count("x") + word.count("X")
    y = word.count("y") + word.count("Y")
    z = word.count("z") + word.count("Z")
    result = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z]    
    return result
    
print(occurrences('ambidextrously'))

def isogram(word):
    vari=occurrences(word)
    for i in range(26):
        find = vari[i]
        if find == 0:
            result = True
        elif find != 0:
            if find == 1:
                result = True
            else:
                result = False
                break
        
    return result

#print(isogram('DOCTORWHO'))

def anagram(w1, w2):
    vari1=occurrences(w1)
    vari2=occurrences(w2)
    if vari1==vari2:
        return True
    else:
        return False
#print(anagram('DOCTORWHO', 'Torchwood'))
#print(anagram('isogram', 'anagram'))    
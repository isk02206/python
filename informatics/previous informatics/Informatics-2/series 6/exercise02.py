'''
Created on 2015. 10. 23.

@author: User
'''
def occurrences(word):
    c_a = word.count("a") + word.count("A")
    c_b = word.count("b") + word.count("B")
    c_c = word.count("c") + word.count("C")
    c_d = word.count("d") + word.count("D")
    c_e = word.count("e") + word.count("E")
    c_f = word.count("f") + word.count("F")
    c_g = word.count("g") + word.count("G")
    c_h = word.count("h") + word.count("H")
    c_i = word.count("i") + word.count("I")
    c_j = word.count("j") + word.count("J")
    c_k = word.count("k") + word.count("K")
    c_l = word.count("l") + word.count("L")
    c_m = word.count("m") + word.count("M")
    c_n = word.count("n") + word.count("N")
    c_o = word.count("o") + word.count("O")
    c_p = word.count("p") + word.count("P")
    c_q = word.count("q") + word.count("Q")
    c_r = word.count("r") + word.count("R")
    c_s = word.count("s") + word.count("S")
    c_t = word.count("t") + word.count("T")
    c_u = word.count("u") + word.count("U")
    c_v = word.count("v") + word.count("V")
    c_w = word.count("w") + word.count("W")
    c_x = word.count("x") + word.count("X")
    c_y = word.count("y") + word.count("Y")
    c_z = word.count("z") + word.count("Z")
    
    result = [c_a, c_b, c_c, c_d, c_e, c_f, c_g, c_h, c_i, c_j, c_k, c_l, c_m, c_n, c_o, c_p, c_q, c_r, c_s, c_t, c_u, c_v, c_w, c_x, c_y, c_z]    
    return result

def isogram(word):
    c_a = word.count("a") + word.count("A")
    c_b = word.count("b") + word.count("B")
    c_c = word.count("c") + word.count("C")
    c_d = word.count("d") + word.count("D")
    c_e = word.count("e") + word.count("E")
    c_f = word.count("f") + word.count("F")
    c_g = word.count("g") + word.count("G")
    c_h = word.count("h") + word.count("H")
    c_i = word.count("i") + word.count("I")
    c_j = word.count("j") + word.count("J")
    c_k = word.count("k") + word.count("K")
    c_l = word.count("l") + word.count("L")
    c_m = word.count("m") + word.count("M")
    c_n = word.count("n") + word.count("N")
    c_o = word.count("o") + word.count("O")
    c_p = word.count("p") + word.count("P")
    c_q = word.count("q") + word.count("Q")
    c_r = word.count("r") + word.count("R")
    c_s = word.count("s") + word.count("S")
    c_t = word.count("t") + word.count("T")
    c_u = word.count("u") + word.count("U")
    c_v = word.count("v") + word.count("V")
    c_w = word.count("w") + word.count("W")
    c_x = word.count("x") + word.count("X")
    c_y = word.count("y") + word.count("Y")
    c_z = word.count("z") + word.count("Z")
    
    listing = [c_a, c_b, c_c, c_d, c_e, c_f, c_g, c_h, c_i, c_j, c_k, c_l, c_m, c_n, c_o, c_p, c_q, c_r, c_s, c_t, c_u, c_v, c_w, c_x, c_y, c_z]    
    
    for i in range(26):
        check = listing[i]
        if check == 0:
            result = True
        elif check != 0:
            if check == 1:
                result = True
            else:
                result = False
                break
        
    return result

def anagram(word1, word2):
    c_a = word1.count("a") + word1.count("A")
    c_b = word1.count("b") + word1.count("B")
    c_c = word1.count("c") + word1.count("C")
    c_d = word1.count("d") + word1.count("D")
    c_e = word1.count("e") + word1.count("E")
    c_f = word1.count("f") + word1.count("F")
    c_g = word1.count("g") + word1.count("G")
    c_h = word1.count("h") + word1.count("H")
    c_i = word1.count("i") + word1.count("I")
    c_j = word1.count("j") + word1.count("J")
    c_k = word1.count("k") + word1.count("K")
    c_l = word1.count("l") + word1.count("L")
    c_m = word1.count("m") + word1.count("M")
    c_n = word1.count("n") + word1.count("N")
    c_o = word1.count("o") + word1.count("O")
    c_p = word1.count("p") + word1.count("P")
    c_q = word1.count("q") + word1.count("Q")
    c_r = word1.count("r") + word1.count("R")
    c_s = word1.count("s") + word1.count("S")
    c_t = word1.count("t") + word1.count("T")
    c_u = word1.count("u") + word1.count("U")
    c_v = word1.count("v") + word1.count("V")
    c_w = word1.count("w") + word1.count("W")
    c_x = word1.count("x") + word1.count("X")
    c_y = word1.count("y") + word1.count("Y")
    c_z = word1.count("z") + word1.count("Z")
    
    check1 = [c_a, c_b, c_c, c_d, c_e, c_f, c_g, c_h, c_i, c_j, c_k, c_l, c_m, c_n, c_o, c_p, c_q, c_r, c_s, c_t, c_u, c_v, c_w, c_x, c_y, c_z]
    
    c_a = word2.count("a") + word2.count("A")
    c_b = word2.count("b") + word2.count("B")
    c_c = word2.count("c") + word2.count("C")
    c_d = word2.count("d") + word2.count("D")
    c_e = word2.count("e") + word2.count("E")
    c_f = word2.count("f") + word2.count("F")
    c_g = word2.count("g") + word2.count("G")
    c_h = word2.count("h") + word2.count("H")
    c_i = word2.count("i") + word2.count("I")
    c_j = word2.count("j") + word2.count("J")
    c_k = word2.count("k") + word2.count("K")
    c_l = word2.count("l") + word2.count("L")
    c_m = word2.count("m") + word2.count("M")
    c_n = word2.count("n") + word2.count("N")
    c_o = word2.count("o") + word2.count("O")
    c_p = word2.count("p") + word2.count("P")
    c_q = word2.count("q") + word2.count("Q")
    c_r = word2.count("r") + word2.count("R")
    c_s = word2.count("s") + word2.count("S")
    c_t = word2.count("t") + word2.count("T")
    c_u = word2.count("u") + word2.count("U")
    c_v = word2.count("v") + word2.count("V")
    c_w = word2.count("w") + word2.count("W")
    c_x = word2.count("x") + word2.count("X")
    c_y = word2.count("y") + word2.count("Y")
    c_z = word2.count("z") + word2.count("Z")
    
    check2 = [c_a, c_b, c_c, c_d, c_e, c_f, c_g, c_h, c_i, c_j, c_k, c_l, c_m, c_n, c_o, c_p, c_q, c_r, c_s, c_t, c_u, c_v, c_w, c_x, c_y, c_z]
    
    if check1 == check2:
        return True
    else:
        return False
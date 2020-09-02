'''
Created on 2016. 1. 26.

@author: User
'''
def sanger(seq):
    result = ''
    number_of_line = len(str(len(seq)))
    count = 1
    list2 = []
    list1 = []
    for x in range(number_of_line):
        list1 += ' ' * ((10**x)-1)
        for y in range(1,len(seq)+1):
            if y >= 10**x:
                list1 += str((y % (10**(x+1)))//(10**x))        
        list2.append(''.join(list1))
        list1 = []   
    for order in list2[::-1]:
        result += order + '\n'
    result += seq.replace('G', '-').replace('C', '-').replace('T', '-') + '\n' 
    result += seq.replace('G', '-').replace('T', '-').replace('A', '-') + '\n' 
    result += seq.replace('A', '-').replace('C', '-').replace('T', '-') + '\n' 
    result += seq.replace('G', '-').replace('A', '-').replace('C', '-') + '\n' 
    result = result + '='*len(seq) + '\n' 
    result += seq
    return result


print(sanger('ATGCTTCGGCAAGACTCAAAAAATA'))
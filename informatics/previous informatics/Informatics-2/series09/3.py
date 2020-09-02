'''
Created on 2015. 11. 4.

@author: User
'''

def birthdays(text):
    reader = open(text,'r', encoding='utf-8')
    result = dict()
    for line in reader.readlines():
        line = line.split(',')
        birthday = line[4][5:]
        result.setdefault(birthday,set()).add(line[0])
    return result



def birthdayparadox (text):
    vari = birthdays(text)
    for x in vari.values():
        if len(x)>1:
            return True
            break
    else:
        return False


def testparadox(list):
    result1 = set()
    for x in list:
        if birthdayparadox(x[1]):
            result1.add(x[0])
    return result1

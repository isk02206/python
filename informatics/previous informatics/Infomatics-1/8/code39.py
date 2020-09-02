'''
Created on 2016. 2. 13.

@author: User
'''
letter2code = {' ': 'SbBsSsBsS', '%': 'SsSbSbSbS', '$': 'SbSbSbSsS', '+': 'SbSsSbSbS', 
 '*': 'SbSsBsBsS', '-': 'SbSsSsBsB', '/': 'SbSbSsSbS', '.': 'BbSsSsBsS', 
 '1': 'BsSbSsSsB', '0': 'SsSbBsBsS', '3': 'BsBbSsSsS', '2': 'SsBbSsSsB', 
 '5': 'BsSbBsSsS', '4': 'SsSbBsSsB', '7': 'SsSbSsBsB', '6': 'SsBbBsSsS', 
 '9': 'SsBbSsBsS', '8': 'BsSbSsBsS', 'A': 'BsSsSbSsB', 'C': 'BsBsSbSsS', 
 'B': 'SsBsSbSsB', 'E': 'BsSsBbSsS', 'D': 'SsSsBbSsB', 'G': 'SsSsSbBsB', 
 'F': 'SsBsBbSsS', 'I': 'SsBsSbBsS', 'H': 'BsSsSbBsS', 'K': 'BsSsSsSbB', 
 'J': 'SsSsBbBsS', 'M': 'BsBsSsSbS', 'L': 'SsBsSsSbB', 'O': 'BsSsBsSbS', 
 'N': 'SsSsBsSbB', 'Q': 'SsSsSsBbB', 'P': 'SsBsBsSbS', 'S': 'SsBsSsBbS', 
 'R': 'BsSsSsBbS', 'U': 'BbSsSsSsB', 'T': 'SsSsBsBbS', 'W': 'BbBsSsSsS', 
 'V': 'SbBsSsSsB', 'Y': 'BbSsBsSsS', 'X': 'SbSsBsSsB', 'Z': 'SbBsBsSsS'}


#dict[key] = value
#dict[]여기에 key 를 넣으면 value가 나온다

def reverse(dict1):
    #왼쪽이 키 오른쪽이 발류 
    # 1 dict2 = {}    
    # 1 for x,y in letter2code.items():
        # 1 dict2[y] = x
    # 2 dict2 = {}    
    # 2 for x,y in letter2code.items():
        # 2 dict2.setdefault(y,x)
    dict2 = {y:x for x,y in letter2code.items()}
    # 3 번쨰 방법
    return dict2 

def code39(word,dict1):
    new = ''
    for char in word:
        if char.isalpha():
            char = char.upper()
        #given char 이 key 에 없을때
        if not char in dict1.keys():
            return None 
        new += dict[char] + 's'
        #마지막 단어 끝에s가 들어가면 안됨
    return new[:-1] 

def decode39(code,dict1):
    pos = 0
    pos2 = 9 
    word = ''
    while pos2 <= len(code):
        if code[pos:pos2] in dict1.keys():
            #dict 의  key를 합쳐 놓은것
            word += dict1[code[pos:pos2]] 
            pos += 10
            pos2 += 10
        else:
            return None
    return word  

print( decode39('BsBsSbSsSsBsBbSsSsSsSsBsBsSbSsSsSbBsBsS', code2letter))     
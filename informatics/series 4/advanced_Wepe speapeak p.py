'''
Created on 2018. 09. 25
@subject : wepe_speapeak_p
@Author : Son Jee Hun
@Student Number : 01406444
'''
sentence = str(input())
vowel = 'aeiouAEIOU' # vowel lower and upper
word = ''
left_vowel = ''
right_vowel = ''
p_count = 0
for i in sentence:
    if i not in vowel and len(left_vowel) == 0: # not vowel and last word is not vowel put word
        word += i
    elif i in vowel:
        if p_count == 1: # p next word vowel put right_vowel
            right_vowel += i
        else:
            left_vowel += i # p last word vowel put left_vowel
    elif i =='p' and p_count == 0:
        p_count += 1 # when p appear, count the number

    else:
        if left_vowel.lower() == right_vowel: # upper vowel convert lower vowel
            word += left_vowel + i
        elif left_vowel.lower() != right_vowel: # upper vowel convert lower vowel
            word += left_vowel + 'p' + right_vowel + i

        left_vowel = '' # reset left_vowel
        right_vowel = ''# reset right_vowel
        p_count = 0 # reset p_count

if i in vowel: #last value find because the loop stop
    if left_vowel.lower() == right_vowel:
        word += left_vowel
    elif left_vowel.lower() != right_vowel:
        word += left_vowel + 'p' + right_vowel
print(word)

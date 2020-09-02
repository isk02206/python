'''
vowel_count = 0
count = 0
position = 0
for i in sentence:
    #print(i)
    if i not in vowel:
        word += i

    if i in vowel:

        if word[-1] == 'p' and i in vowel:
            vowel_count = 0
            continue
        vowel_count += 1
        word += i
    position += 1
print(word)
new_word = ''
for i in word:
    if i == 'p':
        continue
    new_word += i
print(new_word)
'''

'''
sentence = str(input())
word = ''
vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I','O', 'U']
count = 0
vowel_word = ''

for i in sentence:
    if i in vowel:
        count += 1
        word += i
        #print(count)
        if i == 'p':
            continue

    if i not in vowel:
        if i == 'p':
            word += i
        word += i
print(word)
'''

'''
sentence = str(input())
vowel = 'aeiouAEIOU'
word = ''
count_1 = 0
for i in sentence:
    #print(i)
    if i not in vowel:
        if i =='p':
            continue
        word += i
        #print(word)

    if i in vowel:
        count_1 += 2

        word += i
print(word)

word1 = ''
count = 0
for j in word:
    if j not in vowel:
        word1 += j

    if j in vowel:
        count += 1
        if j == word1[-1]:
            continue
        if j in vowel and word1[-1] in vowel:
            continue
        if count == 2:
            count = 0
            continue
        word1 += j

print(word1)
'''
'''     
sentence = str(input())
length_sentence = len(sentence)
counter = 0
vowel = 'aeiouAEIOU'
sentence_string = sentence[counter:length_sentence]
print(sentence_string)
for i in sentence_string:
    print(i)
    if i == vowel:
        counter += 2
        #print(counter)
        #print(sentence_string)
    counter += 1
print(sentence_string)
'''

'''
vowel = 'aeiouAEIOU'
word = ''
for i in sentence:
    print(i)
    if i not in vowel:
        word += i
        print(word)
    if i in vowel:
'''
sentence = str(input())

vowels = ['a','e','i','o','u']
lower_sentence = ''
for i in sentence:
    if i.isalpha() == True:
         low_i = i.lower()
         lower_sentence += low_i
    else:
        lower_sentence += i
count = 0
for j in lower_sentence:
    if j
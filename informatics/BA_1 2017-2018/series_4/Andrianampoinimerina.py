n = int(input())
words = []
first_letter = []
result = []
for i in range(n):
    word = str(input())
    words.append(word)
    equ_word = []
    for j in word:
        low_j = j.lower()
        equ_word += low_j
    ini = equ_word[0]
    fin = equ_word[-1]
    first_letter.append(ord(equ_word[0]))
    if ini != fin:
        result.append(word)
        break
count = 0
for k in range(len(first_letter)-1):
    count += 1
    fir = first_letter[k]
    sec = first_letter[k+1]
    if fir == 122:
        fir = 96
    if int(int(fir) + 1) != int(sec):
        result.append(words[count])
        break
if len(result) == 0:
    print('no mistake')
else:
    print(result[-1])

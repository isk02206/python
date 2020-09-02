number=int(input())
result=''
for digit in range(1, number + 1):
    integral= input()
    digit, word =integral.split(', ',1)
    print(integral)
    word=word.lower()
    given= 0
    for character in word:
        if character.isalpha():
             given += (ord(character) - 96)
    if given < int(digit):
            result += str(digit)+'['+str(given)+'], '
#print(result[:-2])
intnum = int(input())
other = ''

for i in range(intnum):
    st = input()
    number = st[:st.index(',')]
    letter_thing =str(st[st.index(',')+2:])
    letter_thing = letter_thing.upper()
    number_letter_thing = 0
    
    
    for c in str(letter_thing):
        if c.isalpha():
            number_letter_thing = number_letter_thing + ord(c) - 64
     
    if int(number) > int(number_letter_thing):
        other +=str(number)+'['+str(number_letter_thing)+'], '
print(other[:-2])
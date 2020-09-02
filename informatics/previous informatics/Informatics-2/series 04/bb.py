'''integer = int(input())
list = ''
for character in range(integer):
    character = input(). replace(" ","")
    # 4, four
    a = character.find(',')
    number = character[:a]
    letter = character[a+1:].lower()

    count = 0
    for x in letter:
        if x.isalpha():
            
            
            count += (ord(x) - 96)
        
    if int(number) > int(count):
        list += (str(number)+'['+str(count)+'], ')

#print(list[:-2])
'''


if word.upper()==word.lower():
    a='a'.upper()*1
    b='b'.upper()*2
    c='c'.upper()*3
    d='d'.upper()*4
    e='e'.upper()*5
    f='f'.upper()*6
    g='g'.upper()*7
    h='h'.upper()*8
    i='i'.upper()*9
    j='j'.upper()*10
    k='k'.upper()*11
    l='l'.upper()*12
    m='m'.upper()*13
    n='n'.upper()*14
    o='o'.upper()*15
    p='p'.upper()*16
    q='q'.upper()*17
    r='r'.upper()*18
    s='s'.upper()*19
    t='t'.upper()*20
    u='u'.upper()*21
    v='v'.upper()*22
    w='w'.upper()*23
    x='x'.upper()*24
    y='y'.upper()*25
    z='z'.upper()*26
    print(word)
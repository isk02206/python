def mix(txt1, txt2, txt3=None):

    text_1, text_2 = open(txt1, 'r',encoding = 'utf-8').readlines(), open(txt2, 'r', encoding = 'utf-8').readlines()
    min_len = min(len(text_1), len(text_2))
    if txt3 is not None:
        text_3 = open(txt3, 'w')
        for i in range(0, min_len):
            a = text_1[i]
            b = '-->'+text_2[i][0:-1]+'<--'+'\n'
            text_3.write(a)
            text_3.write(b)
    if txt3 is None:
        for i in range(0, min_len):
            a = text_1[i].rstrip()
            b = '-->' + text_2[i][0:-1].rstrip() + '<--'
            print(a)
            print(b)
def encode(s):
    character=['-',',',' ','\'','?','.','A','E','U','I','O','a','e','u','i','o',]
    group=''
    result=''
    for i in range(len(s)):
        if s[i-1] in character and s[i] in character :
            result+=s[i] 
        
        elif s[i] in character :
            if i==0:
                result+=s[i]
            else:
                result+=group+'o'+group.lower()+s[i]
                group=''
        else:
            group+=s[i]
        if i==len(s)-1:
            if group=='':
                break
            else:
                result+=group+'o'+group.lower()
    return result
 
def decode(stri):
    characters=['-',' ','\'','?','.','A','E','U','I','O','a','e','u','i','o']
    result=''
    num=0
    i=0
    while i<len(stri):
        if stri[i]=='o' and i==num:
            result+=stri[i]
            num+=1
        elif stri[i]=='o' and stri[num:i].lower()==stri[i+1:2*i-num+1].lower():
            i+=i-num
            num=i
        elif stri[i] in characters:
            num=i+1
            result+=stri[i]
        else:
            result+=stri[i]
        i+=1
    return result
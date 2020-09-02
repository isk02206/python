'''
Created on 2016. 1. 20.

@author: User
'''
def rle(text):
   #set variables 
    pos = 1
    list1 = list()
    list2 = [text[0]] # 다른 스트링 이랑 비교 대상으로 먼저 만들어 놓기
    sub_text = ''
    result = ''
   
    # once the length of test is one
    #append it into the list without modification
    if len(text) == 1:
        
        list1.append(text[0])
    
    else:
        #compare each component of the text
        # if one component is different from the previous one,
        #it is set into a different list. 
        while pos < len(text):
           
            if text[pos] in list2:        
                list2.append(text[pos])
                
            elif not text[pos] in list2:
                list1.append(list2)
                list2 = [text[pos]]
                
            pos += 1
            # insert the rest into the list1
            if pos == len(text):
                list1.append(list2)
    # Arrange the text with following format.    
    for list3 in list1:
        
        if len(list3) > 1:
        
            if sub_text != '':
                
                sub_text = sub_text.replace('1', '11')
                
                result += '1' + sub_text + '1'
                
                sub_text = ''
            
            if len(list3) <= 9:
                
                result += str(len(list3)) + list3[0]
            
            elif len(list3) > 9:
                
                count = 0
                
                for x in list3:
                    
                    count += 1
                    
                    if count == 9:
                        
                        result += str(count) + list3[0]
                        
                        count = 0
                        
                if count != 0:
                    
                    if count == 1:
                        
                        sub_text += list3[0]
                    else:
                        
                        result += str(count) + list3[0]
                    
        elif len(list3) == 1:
            
            sub_text += str(list3[0])
    
    if sub_text != '':
        
        result += '1' + sub_text + '1'
    
           
    return result
'''
Created on 2016. 2. 13.

@author: User
'''
def isISBN(code, name=None):
    if name == True :
        if len(code) == 13 :
            check = (10-(int(code[0])+int(code[2])+int(code[4])+int(code[6])+int(code[8])+int(code[10])+3*(int(code[1])+int(code[3])+int(code[5])+int(code[7])+int(code[9])+int(code[11])))%10)%10
            
            if int(code[12]) == int(check) :
                return True
            
            else :
                return False 
            
        else :
            return False 
        
    if name == False :
        if len(code) == 10 :
            check = (int(code[0])+2*int(code[1])+3*int(code[2])+4*int(code[3])+5*int(code[4])+6*int(code[5])+7*int(code[6])+8*int(code[7])+9*int(code[8]))%11
            
            if code[9] == 'X' :
        
                if (int(code[0])+2*int(code[1])+3*int(code[2])+4*int(code[3])+5*int(code[4])+6*int(code[5])+7*int(code[6])+8*int(code[7])+9*int(code[8]))%11 ==10 :
                    return True
                        
                if (int(code[0])+2*int(code[1])+3*int(code[2])+4*int(code[3])+5*int(code[4])+6*int(code[5])+7*int(code[6])+8*int(code[7])+9*int(code[8]))%11 !=10 :
                    return False
            
            elif 0 <= int(code[9]) <= 10 :
        
                if int(code[9]) == (int(code[0])+2*int(code[1])+3*int(code[2])+4*int(code[3])+5*int(code[4])+6*int(code[5])+7*int(code[6])+8*int(code[7])+9*int(code[8]))%11 :
                    return True
                        
                if int(code[9]) != (int(code[0])+2*int(code[1])+3*int(code[2])+4*int(code[3])+5*int(code[4])+6*int(code[5])+7*int(code[6])+8*int(code[7])+9*int(code[8]))%11 :
                    return False 
                
        else :
            return False 
        
    if name == None :
        if len(code) == 13 :
            check = (10-(int(code[0])+int(code[2])+int(code[4])+int(code[6])+int(code[8])+int(code[10])+3*(int(code[1])+int(code[3])+int(code[5])+int(code[7])+int(code[9])+int(code[11])))%10)%10
            
            if int(code[12]) == int(check) :
                return True
            
            else :
                return False 
            
        else :
            return False

def areISBN(codes, name=None):
    
    if name == True :
        counter = 0
        z = []
        while counter != len(codes) :
            
            code = str(codes[counter])
            
            if len(code) == 13 :
                
                check = (10-(int(code[0])+int(code[2])+int(code[4])+int(code[6])+int(code[8])+int(code[10])+3*(int(code[1])+int(code[3])+int(code[5])+int(code[7])+int(code[9])+int(code[11])))%10)%10
            
                if int(code[12]) == int(check) :
                    z.append(True)
                
                else :
                    z.append(False) 
                
            else :
                z.append(False)
            counter +=1 
                
        return z 
    
    if name == False :
        counter = 0
        z = []
        while counter != len(codes) :
            code = str(codes[counter])
            
            if len(code) == 10 :
                check = (int(code[0])+2*int(code[1])+3*int(code[2])+4*int(code[3])+5*int(code[4])+6*int(code[5])+7*int(code[6])+8*int(code[7])+9*int(code[8]))%11
            
                if code[9] == 'X' :
            
                    if (int(code[0])+2*int(code[1])+3*int(code[2])+4*int(code[3])+5*int(code[4])+6*int(code[5])+7*int(code[6])+8*int(code[7])+9*int(code[8]))%11 ==10 :
                        z.append(True)
                            
                    if (int(code[0])+2*int(code[1])+3*int(code[2])+4*int(code[3])+5*int(code[4])+6*int(code[5])+7*int(code[6])+8*int(code[7])+9*int(code[8]))%11 !=10 :
                        z.append(False)
                
                elif 0 <= int(code[9]) <= 10 :
            
                    if int(code[9]) == (int(code[0])+2*int(code[1])+3*int(code[2])+4*int(code[3])+5*int(code[4])+6*int(code[5])+7*int(code[6])+8*int(code[7])+9*int(code[8]))%11 :
                        z.append(True)
                            
                    if int(code[9]) != (int(code[0])+2*int(code[1])+3*int(code[2])+4*int(code[3])+5*int(code[4])+6*int(code[5])+7*int(code[6])+8*int(code[7])+9*int(code[8]))%11 :
                        z.append(False) 
                    
            else :
                z.append(False)
            counter +=1
        
        return z 
    
    if name == None :
        counter = 0
        z = []
        while counter != len(codes) :
            
            code = str(codes[counter]) 
            
            if len(code) == 13 :
                check = (10-(int(code[0])+int(code[2])+int(code[4])+int(code[6])+int(code[8])+int(code[10])+3*(int(code[1])+int(code[3])+int(code[5])+int(code[7])+int(code[9])+int(code[11])))%10)%10
            
                if int(code[12]) == int(check) :
                    z.append(True)
                
                else :
                    z.append(False) 
                counter +=1
                
            if len(code) == 10 :
                check = (int(code[0])+2*int(code[1])+3*int(code[2])+4*int(code[3])+5*int(code[4])+6*int(code[5])+7*int(code[6])+8*int(code[7])+9*int(code[8]))%11
            
                if code[9] == 'X' :
            
                    if (int(code[0])+2*int(code[1])+3*int(code[2])+4*int(code[3])+5*int(code[4])+6*int(code[5])+7*int(code[6])+8*int(code[7])+9*int(code[8]))%11 ==10 :
                        z.append(True)
                            
                    if (int(code[0])+2*int(code[1])+3*int(code[2])+4*int(code[3])+5*int(code[4])+6*int(code[5])+7*int(code[6])+8*int(code[7])+9*int(code[8]))%11 !=10 :
                        z.append(False)
                
                elif 0 <= int(code[9]) <=10 :
            
                    if int(code[9]) == (int(code[0])+2*int(code[1])+3*int(code[2])+4*int(code[3])+5*int(code[4])+6*int(code[5])+7*int(code[6])+8*int(code[7])+9*int(code[8]))%11 :
                        z.append(True)
                            
                    if int(code[9]) != (int(code[0])+2*int(code[1])+3*int(code[2])+4*int(code[3])+5*int(code[4])+6*int(code[5])+7*int(code[6])+8*int(code[7])+9*int(code[8]))%11 :
                        z.append(False)
            
            else :
                z.append(False)
            counter +=1
            
        return z 
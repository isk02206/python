'''
Created on 2015. 11. 20.

@author: Haeun Kim
@Student number: 01413456

'''
def filterPeptide(letter, minlen=None, maxlen=None,contains=None,lacks=None):
    letter = letter.upper()  #upper character only
    count = 0
    while count != 1:
        
        if minlen != None and minlen > len(letter): 
            #if minimum length is not none and letter length is smaller than minimum
            return False  # return false
        
        if maxlen!= None and maxlen < len(letter):
            #if maximum length is not none and letter length is bigger than maximum
            return False  #return false
        
        if contains != None:  #if there are letters in contains
            for char in contains.upper(): #all letters become upper
                if not char in letter:    #if characters of contains not in letter
                    return False          # return false
                
        if lacks != None:  
            for char2 in lacks.upper():
                if char2 in letter:  #if characters of lack are in letter
                    return False     #return false
                
        count += 1
    else:
        return True  


def filterPeptides(file1, file2,minlen=None, maxlen=None,contains=None,lacks=None):
    
    reader = open(file1,'r') #open file and read
    writer = open(file2, 'w')
    for line in reader.readlines(): #read the text by lines
        if filterPeptide(line[:-1], minlen, maxlen, contains, lacks) == True:
            writer.writelines(line) #if true, write the letters
    writer.close() #stop writing



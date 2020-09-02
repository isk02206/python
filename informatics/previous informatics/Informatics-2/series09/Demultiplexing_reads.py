'''
Created on 2015. 11. 20.

@author: Haeun_Kim , Minki_Hong
'''
def outputFasta(des,seq,width=80,file=None):
    if file == None: #if the file is none
        print('>'+des) #print >description first
        count = 0
        range1 = width
        for x in range(len(seq)//width): #divide the length of sequence by width 
            print( seq[count:range1])   #print sequence from count to range1
            count += width
            range1 += width
        if seq[range1-width:] != '': # if written sequence from range1 minus with is nor empty string
            print(seq[range1-width:])# print sequence from range1 minus width to end
    else:  # if file is output
        file.write('>' + des + '\n')   
        count = 0
        range1 = width
        for x in range(len(seq)//width):
            file.write(seq[count:range1] + '\n') 
            count += width
            range1 += width
        if seq[range1-width:] != '':
            file.writelines(seq[range1-width:] + '\n') #\n helps to divide the lines
        
def demultiplexFasta(readfile, width = 80): 
    
    reader = open(readfile, 'r').read() #open the text file and read
    list1 = []
    num = ''
    for line in reader.split('>read'): 
        
        if line == None:
            pass
        
        else: # if line is not none
            line = line.replace('\n','').strip() 
            # Make the sequence into one line and remove the spaces at the edges
            for char in line:
                if char.isdigit(): #only digits
                    num += str(char)
            
            file_name = line[len(num):len(num) + 8] + '.fasta' #the format of file name   
            
            if file_name not in list1: 
                file = open(file_name,'w') #open file and write
                
                outputFasta('read' + num, line[len(num)+8:], width, file)
                #Write the sequence with the given format
                #into the indicated fasta file with the use of OutFasta function 
                file.close() #close file
            else: #if file is in list1
                file = open(file_name, 'a') #open file and overwrite
                outputFasta('read' + num, line[len(num) + 8:], width, file)
                
            list1.append(file_name)
            
        num = ''
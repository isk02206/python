def rorschach(text_1, text_2 = None):
    if text_2 == None:  
        reader = open(text_1, 'r')
        
        data = reader.readlines()
         
        for line in data:
            pattern = line.rstrip()+line.rstrip()[-1::-1]
            print(pattern)
        
        reader.close()
    
    else:
        reader = open(text_1, 'r')
        writer = open(text_2, 'w')
        
        data = reader.readlines()
        
        for line in data:
            line = line.rstrip()
            pattern = line.rstrip()+line.rstrip()[-1::-1]
            print(pattern, file=writer)
            
        reader.close()
        writer.close()
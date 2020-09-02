def rorschach(text, option = None):
    if option != None:
        reader = open(text, 'r')
        writer = open(option, 'w')
        data = reader.readlines()
        
        for d in data:
            d = d.rstrip()
            total = (d+d[::-1])
            print(total, file=writer)
        reader.close()
        writer.close()
    else:   
        reader = open(text, 'r')
        data = reader.readlines()
         
        for d in data:
            d = d.rstrip()
            result = (d+d[::-1])
            print(result)
        reader.close()

print(rorschach('pattern.txt'))
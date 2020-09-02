'''
name : Ha Young Kim
student number : 01603259
'''

def width(group):
    #make all different form of 'group' to list form because type 'list' is easy to handle in this assignment.
    if str(group)[1] != '(':
        group = [group]
    else:
        group = list(group)
    #find the tuple which has the maximum first value and add the first value and the second value of that tuple to get the answer.
    max_value = max(group[i][0] for i in range(len(group)))
    for j in range(len(group)):
        if group[j][0] == max_value:
            return max_value + group[j][1]


def line(gather, string = None):
    #gather all tuples('gather')
    gather = str(list(gather)).replace('[','').replace(']','').replace("'","")
    #consider two types; one is tuples that are in many different types and another is string that represents the number of boxes on the row can be passed.
    if string != None:
        gather = gather,string
    else:
        gather = gather
    gather = str(gather).replace("'","")
    #eval changes string type values which have tuple forms to tuple type values
    gather = eval(gather)
    
    #If no value is passed to the parameter, than the minimum width of the row is to be used as determined by the width function.
    if string == None:
        gather_width = width(gather)
    #the value which is passed to the parameter means the minimum width of the row
    else:
        gather_width = int(gather[-1])
        #avoid errors because of the different forms of values
        if str(gather)[1] == '(':
            gather = gather[:-1]
        else:
            gather = gather
    #set the minimum width of the row with empty string
    group_result = [' ']*gather_width
    #replace empty string to '#'; method is similar, but some value 'gather' have different different forms and have to change forms.
    if str(gather)[1] == '(':
        for g in gather:
            group_result[g[0]:g[0]+g[1]] = '#'*g[1]
            group_result = "".join(group_result)
    else:
        group_result[gather[0]:gather[0]+gather[1]] = '#'*gather[1]
        group_result = "".join(group_result)
    return group_result


def nonogram(text_1, text_2):
    #read text_1 and write changed text_1 to text_2
    reader = open(text_1, 'r')
    writer = open(text_2, 'w')
    data = reader.readlines()
    #calculate the minimum width of the row
    space_list = []
    for c in data:
        c = c.replace('\n','').replace(';',',')
        space_list.append(width(eval(c)))
    max_space = max(space_list)
    #changes text_1(tuples to strings that contains '#')
    result = ''
    for d in data:
        d = d.replace('\n','').replace(';',',')
        d = line([d])
        #make spaces after the string which passed the function 'line'.
        parse = ' '*(max_space-len(d))
        result+=d+parse+'\n'
    #write changed text_1 to text_2
    print(result, file = writer)
    
    reader.close()
    writer.close()
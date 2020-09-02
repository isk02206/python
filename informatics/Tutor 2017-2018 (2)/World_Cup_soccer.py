'''
Created on 2018. 7. 10.

@author: TaeWoo
'''

def processMatches(informations):
    
    # open given text file
    reader = open(informations, 'r')
    # save entire information as a list
    # data = reader.readlines()
    # new_data = []
    # for i in reader.readlines():
    #     if '#' not in i and i.strip() != '':
    #        new_data.append(i.strip())
    matches = [i.strip() for i in reader.readlines() if '#' not in i and i.strip() != '']
    # close text file
    reader.close()
    
    # Create empty dictionary
    Groups = dict()
    
    # Set a loop
    for match in matches:
        
        # Make it in to a list
        match = match.split(',')
        # Group
        group = match[-1]
        
        # If group is not in the dictionary add
        if group not in Groups:
            
            # Add new Group into dictionary
            Groups[group] = dict()
            Groups[group][match[0]] = [0, 0, 0, 0, 0]
            Groups[group][match[1]] = [0, 0, 0, 0, 0]
        
        # If group exist in dictionary
        elif group in Groups:
            
            # If country doesn't exist in group dictionary
            if match[0] not in Groups[group]:
                
                # Add country to a group
                Groups[group][match[0]] = [0, 0, 0, 0, 0]
                
            # If country doesn't exist in group dictionary
            if match[1] not in Groups[group]:
                
                # Add country to a group
                Groups[group][match[1]] = [0, 0, 0, 0, 0]
        
        # score of the match
        score = match[2].split('-')
        
        # record number of goals and goals conceded
        Groups[group][match[0]][3] += int(score[0])
        Groups[group][match[0]][4] += int(score[1])
        Groups[group][match[1]][3] += int(score[1])
        Groups[group][match[1]][4] += int(score[0])

        # CASE 1: if first country won
        if int(score[0]) > int(score[1]):
            Groups[group][match[0]][0] += 1
            Groups[group][match[1]][1] += 1
        
        # CASE 2: if second country won    
        elif int(score[0]) < int(score[1]):
            Groups[group][match[0]][1] += 1
            Groups[group][match[1]][0] += 1
        
        # CASE 3: if they draw
        else:
            Groups[group][match[0]][2] += 1
            Groups[group][match[1]][2] += 1
        
    return Groups

def showGroup(results, group, input=False):
    
    # prepare strings for the table construction
    title = '                            GROUP X                            '.replace('X', group)
    table_top = '''+-----------------------+-----+-------------------------+-----+
|                       |   P |   W   L   D   F   A   S | Pts |
+-----------------------+-----+-------------------------+-----+'''
    table_bottom = '+-----------------------+-----+-------------------------+-----+'
    
    score_format = '|'
    Space = ' '
    Order = []
    Countries = []
    Overall_format = dict()
    
    # Empty dictionary
    Overall_result = dict()
    
    for country in results[group]:
        
        Countries.append(country)
        Result = results[group][country]
        # Calculate pts and goal
        Pts = Result[0]*3 + Result[2]
        Goal = Result[3] - Result[4]
        
        # Record information in a list as tuple
        Order.append((Pts, Goal))
        
        # Make another dictionary
        # if pts and goal is unique
        if (Pts, Goal) not in Overall_result:
            Overall_result[(Pts, Goal)] = [country]
        
        # if pts and goal is not unique
        else:
            
            # redefine list and sort them in alphabetical order
            new = sorted(Overall_result[(Pts, Goal)] + [country])
            Overall_result[(Pts, Goal)] = new
        
        # Number of games
        Number_game = str(sum(Result[:3]))
        
        score_format += Space*(23-len(country)-1) + country + ' |'
        score_format += Space*(5-len(Number_game)-1) + Number_game + ' |'
        
        for record in Result:
            score_format += Space*(4-len(str(record))) + str(record)
        
        score_format += Space*(4-len(str(Goal))) + str(Goal) + ' |'
        score_format += Space*(4-len(str(Pts))) + str(Pts) + ' |'
        
        # Create dictionary
        if (Pts, Goal) not in Overall_format:
            Overall_format[(Pts, Goal)] = {country: score_format}
        
        else:
            old = Overall_format[(Pts, Goal)]
            new = dict()
            re_assemble = [(i, old[i]) for i in old] + [(country, score_format)]
            for i in range(len(re_assemble)):
                new[re_assemble[i][0]] = re_assemble[i][1]
                
            Overall_format[(Pts, Goal)] = new
            
        # Reset
        score_format = '|'
               
    table_middle = ''

    # Rank countries
    for score in sorted(set(Order))[::-1]:
        
        for country in Overall_result[score]:
            
            table_middle += Overall_format[score][country] + '\n'
    
    # Combine parts
    Final = title + '\n' + table_top + '\n' + table_middle + table_bottom
    
    # if there is no third parameter
    if input is False:
        
        # use print not return since answer require None type
        print(Final)
    
    else:
        file = open(input, 'w')
        file.write(Final)
        file.close()
    
stats = processMatches('worldcup2010.txt')
print(stats['F'])
print(showGroup(stats, 'F'))
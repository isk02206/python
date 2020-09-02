'''
Created on 2016. 1. 22.

@author: User
'''
def groups(motif):
    
    # Set the variables that will be used.
    protein = ''
    # by splitting a blank, it will become list form.
    group = ''.split()
    count = 0
    
    # using count and loop, set condition that will stop the loop at the given range.
    # for은 while로 바꿀수 있지만  while 은for로 바꿀수 없다
    while count < len(motif):
        
        # if a protein is not embedded with any brackets, then just add it to the group.
        # count += 1 will enables to step to next letter.
        if motif[count].isalpha():
            group += motif[count]
            count+=1
        # if character is not alphabet, this means the protein sequence is embedded with brackets.
        # Therefore, by using for loop, slice the protein.
        # Then, add it to the group.
        # At this time count value will be added by the length of the protein sequence and +2 means the brackets.
        elif not motif[count].isalpha():
            for char in motif[count+1:]:
                if char.isalpha():
                    protein += char
                else:
                    count += len(protein) +2
                    break
            group += [protein]
            # reset the protein to blank.
            protein = ''
    
    # By getting the length of group, it will state how much protein sequence is in motif.
    return len(group)

def match(protein, motif):
    
    length_protein = groups(motif)
    
    # the math definition will only possible when the number of protein and that of protein sequence are the same.
    if length_protein == len(protein):
        
        # count will indicate the position number of motif
        count = 0
        
        domain = ''
        section = ''
        
        # char1 selects the each protein of the series.
        for char1 in protein:
            
            # if the character of motif in count is alphabet and upper class,
            # Then, it means the char1 should match with it.
            if motif[count].isalpha and motif[count].isupper():
                
                # If they are not the same, it means it's wrong.
                if not char1 == motif[count]:
                    return False
                else:
                    count +=1
            
            # If the character of motif in count is x, then it will allow any protein letter.
            # Therefore, it means no possible occurrance of False statement.
            elif motif[count] == 'x':
                
                count +=1
                
            # if the character of motif in count is '[',
            # slice the protein sequence and if the char1, the protein letter, is not in the list,
            # it means False statement
        
            elif motif[count] == '[':
                domain = motif[count+1:]
                value = domain.find(']')
                section = motif[count+1:count + value+1]
                
                if not char1 in section:
                    return False
                else:
                    count += len(section)+2
                section = ''
            
            # Just like when it is '[', if it is '{', it will slice the protein sequence.
            # At this time, it is False if the char1 is in the list.
            elif motif[count] == '{':
                
                domain = motif[count+1:]
                value = domain.find('}')
                section = motif[count+1:count + value+1]
                
                if char1 in section:
                    return False
                else:
                    count += len(section) +2
                section = ''
        
        # Once the for loop is finished and any False statement is announced, then it means True statement(the protein series and the motif match)
        else:
            return True
    # If the length of protein series, protein, and that of protein sequences, motif, are different, it means False statement.
    else:
        return False
            
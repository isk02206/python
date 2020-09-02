def mutation(sequence, pattern):

    reversed = pattern[::-1]
    result = ''
    for position in range(len(sequence)):
        if sequence[position:position+len(pattern)] == pattern:
            #Gives an integer
            start_position = position+len(pattern)
            break
        
        if position == len(sequence)-1:
            return sequence
    
    end_position = None
    
    for second_pos in range(len(sequence)):
        if sequence[second_pos:second_pos+len(pattern)] == reversed:
            
            end_position = second_pos
            
    
        if second_pos == len(sequence)-1 and end_position == None:
            return sequence
    
    if end_position < start_position:
        return sequence
    
    else:
        result = sequence[:start_position] + sequence[start_position:end_position][::-1] + sequence[end_position:]
        return result
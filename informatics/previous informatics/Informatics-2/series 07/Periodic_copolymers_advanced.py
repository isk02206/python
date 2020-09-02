'''
Created on 2015. 11. 20.

@author: Haeun_Kim , Minki_Hong
'''
def copolymer (seq):
    if not '_' in seq:  #if the input do not contain the symbol ''    
        return seq      #just return the input(sequence)
    else:
        result = ''
        number = ''
        for x in seq:
            if x.isalpha():  #alphabet will be recognized for sequence
                result += x
            elif x.isdigit(): #number will be recognized for number next to sequence
                number += x
        number = int(number)
        
        return result*number 
def is_periodic(seq1,seq2):
    repetition = len(seq1)//len(seq2) #tells how many sequences are being repeated
    return seq2*repetition == seq1 #if repetition multiply second sequence is same with 
                                   # first one, return true

def period(seq, minimal_repetition = 1):
    if minimal_repetition == 1:  #if the minimal repetition is 1
        vari = ''                # return the original sequence(vari)
        for x in seq:
            vari += x
            if is_periodic(seq, vari) == True:
                return vari
                break
    else:
        vari = ''            # if the minimal repetition is bigger than 1
        for x in seq:
            vari += x
            if is_periodic(seq, vari) == True:
                break
        repetition = len(seq)//len(vari)
        
        if minimal_repetition > repetition:  #if repetition is smaller than minimal repetition
            return ''                   # return empty string
        else:                           # else return the original sequence (vari)
            return vari

    
def shorthand(seq):
    vari = ''
    for x in seq:
        vari += x
        if is_periodic(seq, vari) == True:
            break
    repetition = len(seq)//len(vari)
    if repetition == 1: # if there is only one repetition
        return seq      # just return the input sequence
    else:               # else, if there are repetition more than 1
        return '({})_{}'.format(vari,repetition) #return sequence and the number of repetition with
                                                 # this format 

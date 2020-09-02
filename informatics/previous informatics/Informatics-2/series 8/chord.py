'''
Created on 2015. 10. 30.
'
@author: User
'''
def decomposition(chord):
    chords= chord[0]
    addition=''
    for x in chord[1:]:
        if x == '#':
            chords += x
        else:
            addition += x 
    return chords, addition

def notes (chord,tone):
    list = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    list2 = []
    value = list.index(chord)
    for x in tone:
         list2.append(list[(value+x)%12])
    return list2


chordtypes = {'major':[0, 4, 7], 'minor':[0, 3, 7], 'dominant seventh':[0, 4, 7, 10], 'minor seventh':[0, 3, 7, 10], 'major seventh':[0, 4, 7, 11]}
chordsymbols = {'':'major', 'm':'minor', '7':'dominant seventh', 'm7':'minor seventh', 'M7':'major seventh'}

def chord(chord, chordtypes, chordsymbols):
    
    L , R = decomposition(chord)
    
    tone = chordtypes[chordsymbols[R]]
    
    return tuple(notes(L, tone))
    
print(chord('F#M7', chordtypes,chordsymbols))
         
    
    
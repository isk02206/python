'''
Created on 2015. 12. 3.

@author: User
'''
5.6 Protein motifs
def split(motif):
"""
Split the given motif in a tuple of groups. Each of these groups is
described in the following way by a string:
- uppercase letter -> uppercase letter
- lowercase letter x -> empty string
- uppercase letters in square brackets -> uppercase letters
- uppercase letters in curly braces -> lowercase letters
>>> split(¡¯N{P}[ST]{P}¡¯)
(¡¯N¡¯, ¡¯p¡¯, ¡¯ST¡¯, ¡¯p¡¯)
>>> split(¡¯{TCGFSM}{E}[GYD]xSx[YTA]N[AVWMYGCHD]P¡¯)
(¡¯tcgfsm¡¯, ¡¯e¡¯, ¡¯GYD¡¯, ¡¯¡¯, ¡¯S¡¯, ¡¯¡¯, ¡¯YTA¡¯, ¡¯N¡¯, ¡¯AVWMYGCHD¡¯, ¡¯P¡¯)
"""
index, groups = 0, []
while index < len(motif):
if motif[index] == ¡¯[¡¯:
start, index = index, motif.find(¡¯]¡¯, index)
groups.append(motif[start + 1:index])
elif motif[index] == ¡¯{¡¯:
start, index = index, motif.find(¡¯}¡¯, index)
groups.append(motif[start + 1:index].lower())
else:
groups.append(motif[index].replace(¡¯x¡¯, ¡¯¡¯))
index += 1
return tuple(groups)
def groups(motif):
"""
Returns the number of groups in the given motif.
>>> groups(¡¯N{P}[ST]{P}¡¯)
4
>>> groups(¡¯{TCGFSM}{E}[GYD]xSx[YTA]N[AVWMYGCHD]P¡¯)
10
"""
18
return len(split(motif))
def match(sequence, motif):
"""
Returns a Boolean value that indicates whether or not the given sequence
matches the given motif.
>>> match(¡¯NFSD¡¯, ¡¯N{P}[ST]{P}¡¯)
True
>>> match(¡¯MFSD¡¯, ¡¯N{P}[ST]{P}¡¯)
False
>>> match(¡¯NPSD¡¯, ¡¯N{P}[ST]{P}¡¯)
False
>>> match(¡¯NFAD¡¯, ¡¯N{P}[ST]{P}¡¯)
False
>>> match(¡¯NFSP¡¯, ¡¯N{P}[ST]{P}¡¯)
False
>>> match(¡¯QDNPYIEEIR¡¯, ¡¯{TCGFSM}{E}[GYD]xSx[YTA]N[AVWMYGCHD]P¡¯)
False
"""
# split the given motif into its composing groups
groups = split(motif)
# check whether or not the length of the given sequence equals the number
# groups in the given motif
if len(sequence) != len(groups):
return False
# compare each amino acid in the given protein sequence with the
# corresponding group of the given motif and return False as soon as a
# letter is found that does not matches its corresponding group
for aa, group in zip(sequence, groups):
if (
group.isupper() and aa not in group
or
group.islower() and aa in group.upper()
):
return False
# all amino acids in the given protein sequence match their group
return True
if __name__ == ¡¯__main__¡¯:
import doctest
doctest.testmod()

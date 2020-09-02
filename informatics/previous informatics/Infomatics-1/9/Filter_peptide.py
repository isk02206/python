'''
Created on 2015. 12. 3.

@author: User
'''
9.5 Filter peptides
def filterPeptide(
peptide, # given peptide
minlen=None, # minimal peptide length
maxlen=None, # maximal peptide length
contains=¡¯¡¯, # amino acids that peptides must contain
lacks=¡¯¡¯ # amino acids that peptides must not contain
):
"""
>>> filterPeptide(¡¯QEWLEMPWDNWPVYVLR¡¯, minlen=10, maxlen=20)
True
>>> filterPeptide(¡¯LICLSYGCHMMSYQWAHIVTDDCVDEGCGMYHMSHEILK¡¯, maxlen=20)
False
>>> filterPeptide(¡¯EQEETISFADLGPNGTFISK¡¯, contains=¡¯DEQ¡¯, lacks=¡¯CMHW¡¯)
True
>>> filterPeptide(¡¯QEWLEMPWDNWPVYVLR¡¯, contains=¡¯DEQ¡¯, minlen=10, maxlen=20, lacks=¡¯CMHW¡¯)
False
"""
# remove newlines and other white space at both ends of the peptide so that
# they do not influence the length of the peptide; convert peptide to upper
# case so that filters work case insensitive
pep = peptide.strip().upper()
# apply active filters
return (
(minlen is None or len(pep) >= minlen)
and
(maxlen is None or len(pep) <= maxlen)
and
set(contains.upper()).issubset(set(pep))
and
not set(lacks.upper()).intersection(set(pep))
)
def filterPeptides(
original, # file from which list of peptides can be read
filtered, # file to which filtered list of peptides must be written
minlen=None, # minimal peptide length
maxlen=None, # maximal peptide length
contains=¡¯¡¯, # amino acids that peptides must contain
lacks=¡¯¡¯ # amino acids that peptides must not contain
):
"""
>>> filterPeptides(¡¯peptides.txt¡¯, ¡¯filtered.txt¡¯, minlen=10, maxlen=20)
>>> print(open(¡¯filtered.txt¡¯, ¡¯r¡¯).read().rstrip())
EQEETISFADLGPNGTFISK
QEWLEMPWDNWPVYVLR
>>> filterPeptides(¡¯peptides.txt¡¯, ¡¯filtered.txt¡¯, maxlen=20)
>>> print(open(¡¯filtered.txt¡¯, ¡¯r¡¯).read().rstrip())
48
ISIK
GLIR
EQEETISFADLGPNGTFISK
QEWLEMPWDNWPVYVLR
>>> filterPeptides(¡¯peptides.txt¡¯, ¡¯filtered.txt¡¯, contains=¡¯DEQ¡¯, lacks=¡¯CMHW¡¯)
>>> print(open(¡¯filtered.txt¡¯, ¡¯r¡¯).read().rstrip())
EQEETISFADLGPNGTFISK
SATIDLGIYTIADLAISGGTTDNVDGTGDAPGLGDIQEVPR
>>> filterPeptides(¡¯peptides.txt¡¯, ¡¯filtered.txt¡¯, lacks=¡¯CMHW¡¯)
>>> print(open(¡¯filtered.txt¡¯, ¡¯r¡¯).read().rstrip())
ISIK
GLIR
EQEETISFADLGPNGTFISK
SATIDLGIYTIADLAISGGTTDNVDGTGDAPGLGDIQEVPR
>>> filterPeptides(¡¯peptides.txt¡¯, ¡¯filtered.txt¡¯, contains=¡¯DEQ¡¯, minlen=10, maxlen=20,
lacks=¡¯CMHW¡¯)
>>> print(open(¡¯filtered.txt¡¯, ¡¯r¡¯).read().rstrip())
EQEETISFADLGPNGTFISK
"""
# open files
original = open(original, ¡¯r¡¯) # for reading
filtered = open(filtered, ¡¯w¡¯) # for writing
# copy filtered peptides
for peptide in original:
if filterPeptide(peptide, minlen, maxlen, contains, lacks):
filtered.write(peptide)
# close files
original.close()
filtered.close()
if __name__ == ¡¯__main__¡¯:
import doctest
doctest.testmod()
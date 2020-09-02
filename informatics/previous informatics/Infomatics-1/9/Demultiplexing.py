'''
Created on 2015. 12. 3.

@author: User
'''
9.6 Demultiplexing reads
def outputFasta(header, sequence, width=80, file=None):
"""
>>> outputFasta(¡¯read1¡¯, ¡¯GGTGCGGAGGAAAGCAACACATTTGT¡¯, width=10)
>read1
GGTGCGGAGG
AAAGCAACAC
ATTTGT
>>> output = open(¡¯out.fasta¡¯, ¡¯w¡¯)
>>> outputFasta(¡¯read2¡¯, ¡¯AGTTTGTCCGCACCGACATAAATAGA¡¯, width=10, file=output)
>>> outputFasta(¡¯read3¡¯, ¡¯ACGTCAGAAACGTGAG¡¯, width=10, file=output)
>>> output.close()
>>> print(open(¡¯out.fasta¡¯, ¡¯r¡¯).read(), end=¡¯¡¯)
>read2
AGTTTGTCCG
CACCGACATA
AATAGA
>read3
ACGTCAGAAA
CGTGAG
"""
# output FASTA header; print function writes to standard output if the value
# None is passed to the parameter file, or to a file object that was opened
49
# for writing if that object is passed to the parameter file
print(¡¯>{}¡¯.format(header), file=file)
# output sequence across multiple lines, taking into account the maximal
# line width
for pos in range(0, len(sequence), width):
print(sequence[pos:pos + width], file=file)
def demultiplexFasta(filename, width=80):
"""
>>> demultiplexFasta(¡¯reads.fasta¡¯, width=60)
>>> print(open(¡¯AAAAAAAA.fasta¡¯, ¡¯r¡¯).read(), end=¡¯¡¯)
>read1
GGTGCGGAGGAAAGCAACACATTTGTTCCTCAGGACTCTTCAGCGGGAGATATCTGCAGA
ACCAAACACGCTCAAAGACCCGCGCAAATCGGCAAATTGCCTGACGTAGAACACCGACCT
AGCGTGTTTATTATGATACTCGGCACCTCTGACTTAATCAAACGTTGTCGAGGTGGAGAT
GGTATCATCTGGCGTTAGGCATAACGAGCGTGACACTAGCTTC
>read3
ACGTCAGAAACGTGAGTAGGGTTACCCACACGCATCTAAGAATGCTCGGGCAATGTGACG
GTATGAAGTTGAGAGCCTCTGTTACCCTCCACCTGATGGGGTGGCGGCCATTTACAGTAT
TGCTTAGCGCACTCAGATATACGCATGATGGGACTGATTCCCCAGGCGAGTACGTAGTCA
CCCGCGGCGACTCGACAAGGATACTATTATCAGGGTTCTCCCCGGGAGGAGGTATTAAGA
>read4
AATGTCATGACCCTAGAAGGCCCTGCATATACATGGCAGGGCAGTCTATCAGCGCCCATC
ATCATCGCTGACGTAGTTGGAGCCGTATCTGTACTGGATCTAGGGGGCATCGTGAACTAG
CGAGGTCGTGTGACGCGCTACAAAGGCTCGGCCCATCTGGAACGTCAGACGAGGCTTCTC
TACGGGGGTCCTGCCGTGGGCTATTGAGGTGCAAAGTTCGAATTCGGCACTGTCGCGTGT
AATTGAATTCGTGCCCAGT
>>> print(open(¡¯CTCTCGGA.fasta¡¯, ¡¯r¡¯).read(), end=¡¯¡¯)
>read2
AGTTTGTCCGCACCGACATAAATAGACTGATACTGATCAGGGGGACGGTACGACCCACTC
TGTCGATCGAACCAGTGACCTGTTCGCTTCGTAACTGGCCAGACGATAGATCTTAGCATA
ACCGACGCGAAGTGTGGCAGATAAGATCCCAAGGTAGTAAATAGTACATATTAGTGGTCA
ACAGGTTTTTAGCGCAGCAGCTGATCTATGCAATTGACTGCAACACCATGACGTAGGTTG
CTTCTATAAGAACAAGTTTACCGCTACGAATTCGCGTCGGTTCCGTACATA
"""
# open input file
infile = open(filename, ¡¯r¡¯)
# initialize dictionary of output files
outfiles = {}
# process FASTA file
header, sequence = ¡¯¡¯, ¡¯¡¯
for line in infile:
if line.startswith(¡¯>¡¯):
# process previous FASTA record
if header:
label = sequence[:8]
if label not in outfiles:
outfilename = ¡¯{}.fasta¡¯.format(label)
outfiles[label] = open(outfilename, ¡¯w¡¯)
outfile = outfiles[label]
outputFasta(header, sequence[8:], width=width, file=outfile)
# initialize new FASTA record
header = line.rstrip(¡¯\n¡¯)[1:]
sequence = ¡¯¡¯
else:
# extend sequence with content of current line
sequence += line.strip()
# process last FASTA record
if header:
50
label = sequence[:8]
if label not in outfiles:
outfilename = ¡¯{}.fasta¡¯.format(label)
outfiles[label] = open(outfilename, ¡¯w¡¯)
outfile = outfiles[label]
outputFasta(header, sequence[8:], width=width, file=outfile)
# close input file
infile.close()
# close output files
for outfile in outfiles.values():
outfile.close()
if __name__ == ¡¯__main__¡¯:
import doctest
doctest.testmod()

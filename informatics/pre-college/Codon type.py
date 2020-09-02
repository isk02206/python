a = str(input())

b = 'AUG'
c = 'UAG' or 'UGA' or 'UAA'

if a == b:
    print('The codon', a, 'is a start codon.')
elif a == 'UAG' or a == 'UGA' or a == 'UAA':
    print('The codon', a, 'is a stop codon.')
elif len(a) == 3:
    print('The codon', a, 'is a normal codon.')
else:
    print('The codon', a, 'is a non-valid codon.')
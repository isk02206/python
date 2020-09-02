def median(contigs):
    contigs = sorted(contigs)
    length_contigs = len(contigs)
    if length_contigs % 2 == 0 : 
        middle = length_contigs /2 
        median1 = (contigs[int(middle)] + contigs[int(middle)-1]) / 2
        return float(median1) 
    else : 
        middle2 = (length_contigs /2) - 0.5
        median2 = contigs[int(middle2)]
        return float(median2)
def extend(contigs):
    contigs = sorted(contigs)
    list1 = []
    for integer in contigs:
        for i in range(0, integer):
            list1.append(integer)
    return list1
def N50(contigs): 
    contigs = sorted(contigs)
    extend_n50 = extend(contigs)
    median_n50 = median(extend_n50)
    return median_n50

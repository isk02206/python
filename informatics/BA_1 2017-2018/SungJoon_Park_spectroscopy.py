'''
Name: Sung Joon Park
ID: 01514170
'''
def referenceSpectra(spectra):
    #dividing and converting spectra into a dictionary about symbolic name and reference spectrum
    '''
    >>> spectra = ['H 486.135,434.0472,656.279,410.1734', 'He 501.56783,667.8151,587.5621,471.31457,492.19313,504.7738,447.14802,438.79296,402.61914,412.08154', 'Li 610.354,670.791,413.259,610.365,670.776', 'Hg 404.6565,407.7837,434.74945,435.8335,535.4034,546.075,567.581,576.961,579.067,580.3782,585.9254,671.634,690.746']
    >>> referenceSpectrum = referenceSpectra(spectra)
    >>> referenceSpectrum['H']
    (410.1734, 434.0472, 486.135, 656.279)
    >>> referenceSpectrum['Li']
    (413.259, 610.354, 610.365, 670.776, 670.791)
    '''
    referenceSpectrum = {} #dictionary for the element and reference spectrum to be entered
    for i in spectra:
        element = ''
        spectrum = [] # list that would be added to
        meter = ''
        for j in i:
            if j.isdigit() == True or ord(j) == 46:
                # if j in a number or a period, the values must be added to the string meter
                meter += j
            if ord(j) == 44:
                #if j in a comma the meter string must be reset and it should be added to the spectrum list
                meter = float(meter)
                spectrum.append(meter)
                meter = ''
            if 65<= ord(j) <=90 or 97 <= ord(j) <= 122:
                # dividing the element's name by using ascii code
                element += j
        meter = float(meter) #converting the type of string meter into float
        spectrum.append(meter) #each meter value added to the total spectrum list named as spectrum
        meter = ''
        referenceSpectrum[element] = tuple(sorted(spectrum)) #sorting and converting the returning value into tuple
    return referenceSpectrum

def referenceLines(spectrum, referenceSpectrum, eps = None):
    '''
    >>> spectra = ['H 486.135,434.0472,656.279,410.1734', 'He 501.56783,667.8151,587.5621,471.31457,492.19313,504.7738,447.14802,438.79296,402.61914,412.08154', 'Li 610.354,670.791,413.259,610.365,670.776', 'Hg 404.6565,407.7837,434.74945,435.8335,535.4034,546.075,567.581,576.961,579.067,580.3782,585.9254,671.634,690.746']
    >>> referenceSpectrum = referenceSpectra(spectra)
    >>> referenceSpectrum['H']
    (410.1734, 434.0472, 486.135, 656.279)
    >>> referenceSpectrum['Li']
    (413.259, 610.354, 610.365, 670.776, 670.791)

    >>> spectrum1 = (410.1055, 434.1126, 434.1427, 486.3071, 656.224)
    >>> referenceLines(spectrum1, referenceSpectrum['H'])
    3
    >>> spectrum2 = (410.1875, 434.0906, 486.2315, 524.7571, 656.2779)
    >>> referenceLines(spectrum2, referenceSpectrum['H'], eps=0.1)
    4
    >>> referenceLines(spectrum2, referenceSpectrum['H'], eps=0.025)
    2
    '''
    count = 0
    if eps == None:#when there is no given value for eps
        for i in referenceSpectrum:
            for j in spectrum:
                if abs(float(i)-float(j)) < 0.1:
                    # finding if the given elements and the spectrometer value satisfies the given condition
                    count += 1
                    break #stopping the loop to not get any overlap values
    else: #when there is a given value for eps
        for i in referenceSpectrum:
            for j in spectrum:
                if abs(float(i)-float(j)) < eps:
                    count += 1
                    break
    return count

def decomposition(spectrum, referenceSpectrum, eps=None, minimum=None):
    '''
    >>> spectra = ['H 486.135,434.0472,656.279,410.1734', 'He 501.56783,667.8151,587.5621,471.31457,492.19313,504.7738,447.14802,438.79296,402.61914,412.08154', 'Li 610.354,670.791,413.259,610.365,670.776', 'Hg 404.6565,407.7837,434.74945,435.8335,535.4034,546.075,567.581,576.961,579.067,580.3782,585.9254,671.634,690.746']
    >>> referenceSpectrum = referenceSpectra(spectra)
    >>> referenceSpectrum['H']
    (410.1734, 434.0472, 486.135, 656.279)
    >>> referenceSpectrum['Li']
    (413.259, 610.354, 610.365, 670.776, 670.791)

    >>> spectrum1 = (410.1055, 434.1126, 434.1427, 486.3071, 656.224)
    >>> referenceLines(spectrum1, referenceSpectrum['H'])
    3
    >>> spectrum2 = (410.1875, 434.0906, 486.2315, 524.7571, 656.2779)
    >>> referenceLines(spectrum2, referenceSpectrum['H'], eps=0.1)
    4
    >>> referenceLines(spectrum2, referenceSpectrum['H'], eps=0.025)
    2

    >>> spectrum = (402.5579, 410.1914, 413.162, 434.1243, 486.0598, 504.7387, 610.157, 610.562, 656.354, 670.578, 670.991)
    >>> decomposition(spectrum, referenceSpectrum)
    ['H']
    >>> decomposition(spectrum, referenceSpectrum, eps=0.2)
    ['H', 'Li']
    >>> decomposition(spectrum, referenceSpectrum, minimum=2)
    ['H', 'He']
    >>> decomposition(spectrum, referenceSpectrum, eps=0.2, minimum=2)
    ['H', 'He', 'Li']
    '''
    if eps == None: #when there is no given value for eps
        eps = 0.1
    referenceLines_count = {} #dictionary that has the value for each element of how many referenceLines satisfies
    satisfying = [] #list for return value
    for i in referenceSpectrum:
        #finding the counting for each element
        value = referenceLines(spectrum, referenceSpectrum[i], eps)
        referenceLines_count[i] = value
    for j in referenceLines_count:
        #sorting the value by the condition of minimum
        if minimum == None: #if minimum condition is not given, then all the spectrometer must satisfy
            if referenceLines_count[j] == len(referenceSpectrum[j]):
                satisfying.append(j)
        else: #if the minimum value is given
            if referenceLines_count[j] >= minimum:
                satisfying.append(j)
    return sorted(satisfying)

if __name__ == '__main__':
    import doctest
    doctest.testmod()

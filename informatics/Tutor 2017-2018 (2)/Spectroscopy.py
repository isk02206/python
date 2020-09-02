'''
Created on 2018. 7. 15.

@author: TaeWoo
'''

def referenceSpectra(txt_file):
    
    reader = open(txt_file, 'r')
    data = reader.readlines()
    reader.close()
    
    reference = dict()
    
    # separate atom name and data and put it into dictionary
    
    for element in data:
        
        element = element.strip().split('\t')
        spectra = sorted([float(spectrum) for spectrum in element[1].split(',')])
        reference[element[0]] = tuple(spectra)
        
    return reference
    

def referenceLines(spectrum, reference, eps=0.1):
    
    # making dictionary
    
    ref_spectrum = dict()
    
    for ref_spec in reference:
        
        ref_spectrum[ref_spec] = 0
    
    # fill in dictionary
    
    for spec in spectrum:
            
        for ref_spec in ref_spectrum:
            
            if abs(ref_spec - spec) <= eps:
                
                ref_spectrum[ref_spec] += 1
    
    # Count number of valid spectral lines according to reference
    
    spectral_lines = 0
    
    for ref_spec in ref_spectrum:
        
        if ref_spectrum[ref_spec] > 0:
            
            spectral_lines += 1
    
    return spectral_lines

def decomposition(spectrum, reference, eps=0.1, minimum=None):
    
    sufficiency = dict()
    
    if minimum is None:
        
        for element in reference:
            
            sufficiency[element] = len(reference[element])
            
    else:
        
        for element in reference:
            
            sufficiency[element] = minimum
    
    sufficient = list()
    
    # compare
    for element in reference:
        
        if referenceLines(spectrum, reference[element], eps) >= sufficiency[element]:
            
            sufficient.append(element)
    
    return sorted(sufficient)

referenceSpectrum = referenceSpectra('spectra.txt')

spectrum1 = (410.1875, 434.0906, 486.2315, 524.7571, 656.2779)

print(referenceSpectrum['H'])
print(referenceLines(spectrum1, referenceSpectrum['H'], 0.025))

spectrum = (402.5579, 410.1914, 413.162, 434.1243, 486.0598, 504.7387, 610.157, 610.562, 656.354, 670.578, 670.991)


print(decomposition(spectrum, referenceSpectrum, eps=0.2, minimum=2))
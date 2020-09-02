def isObstacle(xA,yA,xB,yB,xO,yO):
    
    '''
    >>> isObstacle(51.022, 3.7095, 51.028, 3.7185, 51.025, 3.715)
    False
    >>> isObstacle(51.022, 3.7095, 51.028, 3.7185, 51.025, 3.714)
    True
    >>> isObstacle(51.022, 3.7095, 51.025, 3.714, 51.028, 3.7185)
    False
    '''
    equation = (yA-yB)*xO - (xA - xB)*yO + xA*yB - xB*yB 
    if equation == 0:
        return True
    else:
        AB = (abs(xB-xA)**2 + abs(yB-yA)**2) **0.5
        AO = (abs(xO-xA)**2 + abs(yO-yA)**2) **0.5
        BO = (abs(xO-xB)**2 + abs(yO-yB)**2) **0.5
        deviation = abs(AB - (AO + BO))
        if deviation < 10**(-6):
            return True
        else:
            return False
    

if __name__ == '__main__':
    import doctest
    doctest.testmod()

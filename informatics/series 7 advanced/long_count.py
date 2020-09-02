'''
Created on 2018. 10. 28
@Subject : long_count
@Author : Son Jee Hun
@Student Number : 01406444
'''
import re
def dmy(date):
    '''
    >>> dmy('01/01/1970')
    (1, 1, 1970)
    >>> dmy('20-7-1988')
    (20, 7, 1988)
    >>> dmy('00012+00012+02012')
    (12, 12, 2012)
    >>> dmy('21 12 2012')
    (21, 12, 2012)
    >>> dmy('26.03.2407')
    (26, 3, 2407)
    '''
    # remove without number
    remove_other_type = re.findall('\w+', date)
    list_result = []
    for i in remove_other_type:
        i = list(i)
        # first value equal 0 remove 0
        if i[0] == '0':
            i.remove(i[0])
        list_result.append(int(''.join(i))) # list change string
    return tuple(list_result)


from datetime import date
def expired(given_date):
    '''
    >>> expired('01/01/1970')
    0
    >>> expired('20-7-1988')
    6775
    >>> expired('00012+00012+02012')
    15686
    >>> expired('21 12 2012')
    15695
    >>> expired('26.03.2407')
    159695
    '''
    given_date = dmy(given_date) # use dmy function make tuple date
    gregorian_date = date(given_date[-1], given_date[-2], given_date[-3]) # change date type year, month, day
    start_day = date(1970, 1, 1)

    count_day = gregorian_date - start_day
    return count_day.days # count days

def mayadate(date='', separator=None):
    '''
    >>> mayadate('01/01/1970')
    '12/17/16/7/5'
    >>> mayadate('20-7-1988',separator='/')
    '12/18/15/4/0'
    >>> mayadate('00012+00012+02012',separator='-')
    '12-19-19-17-11'
    >>> mayadate('21 12 2012',separator='+')
    '13+0+0+0+0'
    >>> mayadate('26.03.2407')
    '14.0.0.0.0'
    '''
    # separator is none
    if separator is None:
        for i in date:
            if i.isdigit() is False:
                separator = i
                break


    day_1970 = 12 * (20 * (20 * (20 * 18))) + 17 * (20 * (20 * 18)) + 16 * (20 * 18) + (7 * 20) + 5

    total_days = expired(date) + day_1970 # total days
    baktun = total_days // (20 * (20 * (20 * 18)))
    total_days -= baktun * (20 * (20 * (20 * 18))) #total days - baktun days
    katun = total_days // (20 * (20 * 18))
    total_days -= katun * (20 * (20 * 18))#remain days(total days - baktun days) - katun days
    tun = total_days // (20 * 18)
    total_days -= tun * (20 * 18) #remain days((total days - baktun days) - katun days) - tun days
    uinal = total_days // 20
    total_days -= uinal * 20 #remain days(((total days - baktun days) - katun days) - tun days) - uinal days
    kin = total_days
    #find baktun, katun, tun ,uinal, kin
    maya_list = [str(baktun), str(katun), str(tun), str(uinal), str(kin)]
    maya_date = separator.join(maya_list) # list change string
    return maya_date

if __name__ == '__main__':
    import doctest
    doctest.testmod()
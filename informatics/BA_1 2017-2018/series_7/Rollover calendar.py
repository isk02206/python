def rolloverDate(year = None,month = None, day = None):
    '''
    >>> rolloverDate(month=4, day=31)
    datetime.date(2016, 5, 1)
    >>> rolloverDate(year=2016, month=15, day=43)
    datetime.date(2017, 4, 12)
    >>> rolloverDate(year=2016, month=3, day=16)
    datetime.date(2016, 3, 16)
    >>> rolloverDate(year=2016, month=12, day=64)
    datetime.date(2017, 2, 2)
    >>> rolloverDate(year=2016, month=19, day=99)
    datetime.date(2017, 10, 7)
    >>> rolloverDate(year=2016, month=1, day=99999)
    datetime.date(2289, 10, 14)
    >>> rolloverDate(year=2016, month=9999, day=10)
    datetime.date(2849, 3, 10)
    '''
    import datetime
    date = []
    if year is None:
        year = 2016
    if month is None:
        month = 11
    return datetime.date(year,month,day)
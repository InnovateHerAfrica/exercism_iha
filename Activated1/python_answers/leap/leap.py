def is_leap_year(x):
    if x%400 == 0:
            return True
    elif x%100 == 0:
            return False
    elif x%4 == 0:
           return True
    return False
                                                              

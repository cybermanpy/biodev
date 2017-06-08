# coding=utf-8

from django import template
from decimal import Decimal
# from datetime import datetime, timedelta
import datetime
import time
import math

register = template.Library()

@register.filter
def subDate(hire):
    if hire != None:
        today = datetime.datetime.now()
        try: 
            hiredday = hire.replace(year=today.year)
        except ValueError: # raised when birth date is February 29 and the current year is not a leap year
            hiredday = hire.replace(year=today.year, day=hire.day-1)
        if hiredday > today:
            hirey = today.year - hire.year - 1
            if hirey < 2:
                ty = str(hirey) + ' Año'
            else:
                ty = str(hirey) + ' Años'
            res = today - hire
            t = res.days - 365.25
            test = math.ceil(t / 30)
            if test < 12:
                m =  str(test) +  ' Meses'
            else:
                m = ''
            return str(ty) + '  ' + str(m)
        else:
            hirey = today.year - hire.year
            if hirey < 2:
                ty = str(hirey) + ' Año'
            else:
                ty = str(hirey) + ' Años'
            res = today - hire
            t = res.days - 365.25
            test = math.ceil(t / 30)
            if test < 12:
                m =  str(test) +  ' Meses'
            else:
                m = ''
            return str(ty) + ' ' + str(m)
    else:
        res = 'None'
        return res

    # if value != None:
    #     now = datetime.datetime.now()
    #     ny = now.year
    #     nm = now.month
    #     y = str(value.year)
    #     m = str(value.month)
    #     ty =  now - value
    #     if m > nm:
    #         tm = int(m) - nm
    #     elif mn > m :
    #         tm = nm - int(m)
    #     res = now - value
    #     ty = math.floor(res.days / 365.25)
    #     tm = res.days - 365.25
    #     tm = tm / 30
    #     tm = math.ceil(tm)
    #     res = str(ty) + ' Años ' + str(tm) + ' Meses '
    # else:
    #     res = 'none'
    # return res

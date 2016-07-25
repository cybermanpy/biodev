from django import template
from decimal import Decimal
import datetime

register = template.Library()

def valid_numeric(arg):
    if isinstance(arg, (int, float, Decimal)):
        return arg
    try:
        return int(arg)
    except ValueError:
        return float(arg)

@register.filter
def sub(value, arg):
    """Subtracts the arg from the value."""
    try:
        return valid_numeric(value) - valid_numeric(arg)
    except (ValueError, TypeError):
        try:
            return value - arg
        except Exception:
            return ''
sub.is_safe = False

@register.filter
def suma(value, arg):
    """Sum the arg from the value."""
    try:
        return valid_numeric(value) + valid_numeric(arg)
    except (ValueError, TypeError):
        try:
            return value + arg
        except Exception:
            return ''
suma.is_safe = False

@register.filter
def cutstring(value, arg):
    string = value
    cut_string = string.split(arg)
    new_string = cut_string[0]
    return new_string

@register.filter
def dateF(value, arg):
	format = ('%A %d')
	y = int(arg['y'])
	m = int(arg['m'])
	n = datetime.date(y, m, value)
	s = n.strftime(format)
	return n

@register.filter
def dateF1(value):
	format = ('%H:%M:%S')
	s = value.strftime(format)
	return s
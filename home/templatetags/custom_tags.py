from django import template
register = template.Library()

@register.filter(name = 'split')
def split(value, arg):
    return value.split(arg)

@register.filter(name = 'to_list')
def to_list(value):
    return list(value)

@register.filter(name = 'int_to_str')
def int_to_str(value):
    return str(value)
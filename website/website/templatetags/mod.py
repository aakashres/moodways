from django import template

register = template.Library()


@register.filter(name='mod')
def mod(value):
    if int(value) % 3 == 1:
        return 50
    else:
        return 0

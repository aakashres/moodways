from django import template

register = template.Library()


@register.filter(name='subtract')
def subtract(value):
    return int(value) - 1

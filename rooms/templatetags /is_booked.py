from django import template

register = template.Library()


@register.simple_tag()
def is_booked(room, day):
    return False
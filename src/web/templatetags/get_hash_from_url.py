# todo: deprecated
from django import template

register = template.Library()


@register.filter
def get_hash_from_url(value):
    # {{ request.path }}

    return value.strip().split('/')[-1]

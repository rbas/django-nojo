# coding: utf-8
from django import template

register = template.Library()

def cut(value, length=322, end_text='...'):
    """Ořízne řetězec na požadovanou délku."""
    from nojo.util.text import cut_string
    return cut_string(value, length, end_text)
register.filter('cut_string', cut)

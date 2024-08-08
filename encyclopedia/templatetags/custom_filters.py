from django import template

register = template.Library()

@register.filter
def split_sections(content):
    return content.split('~')

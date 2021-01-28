from django import template
register = template.Library()


@register.filter
def gen_iter(gen):
    try:
        return next(gen)
    except StopIteration:
        return ""


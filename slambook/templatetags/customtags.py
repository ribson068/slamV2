from django import template
from slambook.models import Contributor

register = template.Library()

@register.filter
def responded_gifts(value):
    return Contributor.objects.filter(giftchart=value,response=True).count()


@register.filter
def isread_gifts(value):
    return Contributor.objects.filter(giftchart=value,isreadgift=True).count()
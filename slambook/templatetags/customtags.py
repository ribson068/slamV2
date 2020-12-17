from django import template
from slambook.models import Contributor

register = template.Library()

@register.filter
def responded_gifts(value):
    return Contributor.objects.filter(giftchart=value,response=True).count()


@register.filter
def isread_contrib(value):
    return Contributor.objects.filter(giftchart=value,isreadcontrib=True).count()

@register.filter
def isread_receiver(value):
    return Contributor.objects.filter(giftchart=value,isreadreceiver=True).count()